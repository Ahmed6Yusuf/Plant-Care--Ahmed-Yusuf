import datetime
import os
import pandas as pd
import streamlit as st

CSV_FILE = "plants.csv"
COLUMNS = [
    "plant_name",
    "location",
    "date_acquired",
    "watering_freq_days",
    "sunlight_needs",
    "last_activity",
    "last_care_date",
    "photo_name",
]


def load_initial_df() -> pd.DataFrame:
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=COLUMNS)


if "plants_df" not in st.session_state:
    st.session_state.plants_df = load_initial_df()


def save_df(df: pd.DataFrame):
    st.session_state.plants_df = df
    df.to_csv(CSV_FILE, index=False)


def get_care_status(row: pd.Series, today: datetime.date) -> tuple[str, str]:
    freq = int(row["watering_freq_days"])

    # Use last_care_date if available, otherwise date_acquired
    ref_str = row["last_care_date"] if pd.notna(row["last_care_date"]) and str(row["last_care_date"]).strip() != "" else row["date_acquired"]
    if pd.isna(ref_str) or str(ref_str).strip() == "":
        return "Unknown", "Missing date info"

    ref_date = pd.to_datetime(ref_str).date()
    next_due = ref_date + datetime.timedelta(days=freq)
    diff_days = (next_due - today).days

    if diff_days < 0:
        return "Past Due", f"Overdue by {abs(diff_days)} day(s) (was due {next_due})"
    elif diff_days == 0:
        return "Due Today", f"Due today ({next_due})"
    elif diff_days == 1:
        return "Due Tomorrow", f"Due tomorrow ({next_due})"
    else:
        return "Upcoming", f"Due in {diff_days} days ({next_due})"


def show_seasonal_reminder(today: datetime.date):
    month = today.month
    if month in (6, 7, 8):
        st.warning("Summer Care Reminder: High heat increases evaporation—check soil moisture more frequently and shield delicate leaves from harsh afternoon sun.")
    elif month in (12, 1, 2):
        st.info("Winter Care Reminder: Growth slows down and indoor air can be dry—avoid overwatering and watch for cold drafts near windows.")
    else:
        st.info("Seasonal Tip: Spring/Autumn transition is a great time for light fertilizing, pruning, or repotting root-bound plants.")


# --- Sidebar Navigation & CSV Loop ---
with st.sidebar:
    page_chosen = st.radio(
        "MENU",
        ("Add Plant", "Log Care", "View Schedule", "Search"),
    )

    st.divider()
    st.subheader("Pre-loaded Plants Data")

    uploaded_csv = st.file_uploader("Upload existing plants CSV", type=["csv"])
    if uploaded_csv is not None:
        loaded = pd.read_csv(uploaded_csv)
        save_df(loaded)
        st.success("Loaded CSV into session!", icon="✅")

    current_csv = st.session_state.plants_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Plants CSV",
        data=current_csv,
        file_name="plants_export.csv",
        mime="text/csv",
    )


today = datetime.date.today()
df = st.session_state.plants_df


# --- 1. Add Plant ---
if page_chosen == "Add Plant":
    st.title("New Plant!")
    show_seasonal_reminder(today)

    # Distinct variable names so nothing overwrites
    plant_name = st.text_input("Plant Name", "")
    location = st.text_input("Where is it growing? (Location)", "")
    date_acquired = st.date_input("Date Acquired", value=today)

    watering_freq = st.selectbox(
        "Watering Frequency (days)",
        [1, 2, 3, 4, 7, 10, 14],
        index=4,
        accept_new_options=True,
    )

    sunlight_needs = st.selectbox(
        "Sunlight Needs",
        ["Full Sun", "Partial Shade", "Low Light", "Yes", "No"],
    )

    uploaded_photo = st.file_uploader("Upload a photo of your plant", type=["jpg", "jpeg", "png"])
    photo_name = ""
    if uploaded_photo is not None:
        st.image(uploaded_photo, caption=plant_name or "Plant Preview", use_container_width=True)
        photo_name = uploaded_photo.name

    if st.button("Add Plant"):
        if plant_name.strip() == "":
            st.error("Please enter a plant name.")
        else:
            new_row = pd.DataFrame([{
                "plant_name": plant_name.strip(),
                "location": location.strip(),
                "date_acquired": str(date_acquired),
                "watering_freq_days": int(watering_freq),
                "sunlight_needs": sunlight_needs,
                "last_activity": "Acquired",
                "last_care_date": str(date_acquired),
                "photo_name": photo_name,
            }])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            save_df(updated_df)
            st.success(f"Added '{plant_name}'!")
            st.dataframe(updated_df, use_container_width=True)


# --- 2. Log Care ---
elif page_chosen == "Log Care":
    st.title("Cultivate Your Plant")

    if df.empty:
        st.info("No plants found yet. Add a plant first.")
    else:
        selected_plant = st.selectbox("Select a plant", df["plant_name"].tolist())
        activity = st.selectbox("Care Activity", ["Watering", "Repotting", "Fertilizing", "Pruning", "Misting"])
        care_date = st.date_input("Care Date", value=today)

        if st.button("Log Care"):
            mask = df["plant_name"] == selected_plant
            df.loc[mask, "last_activity"] = activity
            df.loc[mask, "last_care_date"] = str(care_date)
            save_df(df)
            st.success(f"Logged {activity} for {selected_plant} on {care_date}.")
            st.dataframe(df, use_container_width=True)


# --- 3. View Schedule ---
elif page_chosen == "View Schedule":
    st.title("Scheduled Care")
    show_seasonal_reminder(today)

    if df.empty:
        st.info("No plants in your tracker yet.")
    else:
        schedule_df = df.copy()
        statuses = schedule_df.apply(lambda r: get_care_status(r, today), axis=1)
        schedule_df["status"] = [s[0] for s in statuses]
        schedule_df["details"] = [s[1] for s in statuses]

        for _, row in schedule_df.iterrows():
            if row["status"] == "Past Due":
                st.warning(f"**{row['plant_name']}** ({row['location']}) — {row['details']}")
            elif row["status"] in ("Due Today", "Due Tomorrow"):
                st.info(f"**{row['plant_name']}** ({row['location']}) — {row['details']}")

        st.dataframe(
            schedule_df[["plant_name", "location", "watering_freq_days", "last_activity", "last_care_date", "status", "details"]],
            use_container_width=True,
        )


# --- 4. Search ---
elif page_chosen == "Search":
    st.title("Find an Existing Plant")

    if df.empty:
        st.info("No plants available to search.")
    else:
        query = st.text_input("Search by plant name or location", "").strip().lower()
        if query:
            filtered = df[
                df["plant_name"].astype(str).str.lower().str.contains(query, na=False)
                | df["location"].astype(str).str.lower().str.contains(query, na=False)
            ]
        else:
            filtered = df

        st.write(f"Showing {len(filtered)} plant(s)")
        st.dataframe(filtered, use_container_width=True)