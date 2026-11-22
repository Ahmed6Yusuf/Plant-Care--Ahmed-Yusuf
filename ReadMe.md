# Plant Care Tracker — User Navigation Guide

Welcome to the **Plant Care Tracker**! This user manual will guide you through navigating the application, adding your plants, logging care activities, keeping track of watering schedules, and managing your plant database.

---

## Getting Started: Interface Overview

When you open the application, you will see a simple split interface:
* **Left Sidebar:** Contains the main menu controls, seasonal alerts, and data backup tools (CSV import/export).
* **Main Screen:** Displays the current active view (**Add Plant**, **Log Care**, **View Schedule**, or **Search**).

---

## Sidebar & Data Management

The sidebar on the left side of the screen is always accessible regardless of which page you are currently viewing.

### Navigation Menu
Use the **MENU** radio buttons in the sidebar to switch between views:
1. **Add Plant** — Register new plants into your tracker.
2. **Log Care** — Record watering, fertilizing, repotting, or other care activities.
3. **View Schedule** — Check which plants are due for care today, upcoming, or past due.
4. **Search** — Filter and locate plants in your collection by name or location.

### CSV Data Backup & Restore
Located directly below the navigation menu:
* **Upload existing plants CSV:** Click **Browse files** or drag and drop a `.csv` file to load your previously saved plant dataset.
* **Download Plants CSV:** Click the **Download Plants CSV** button at any time to save a copy of your current plant list and care logs locally to your computer.

---

## Step-by-Step Navigation Guide

### 1. Adding a New Plant ("Add Plant")

Use this screen when you bring home a new plant or want to add an existing plant to your tracker.

1. **Select "Add Plant"** from the sidebar menu.
2. **Fill in the Plant Details:**
   * **Plant Name:** Enter the common or scientific name (e.g., *Monstera Deliciosa*).
   * **Where is it growing?:** Enter the room or location (e.g., *Living Room Window*, *Balcony*).
   * **Date Acquired:** Select the date you brought the plant home using the date picker.
   * **Watering Frequency (days):** Choose how often the plant needs water (e.g., `7` for weekly, `14` for bi-weekly).
   * **Sunlight Needs:** Select light requirements (*Full Sun*, *Partial Shade*, *Low Light*).
3. **Upload Plant Photo:** Click **Browse files** under *Upload a photo of your plant* to select an image (`.jpg` or `.png`). A preview of the image will appear immediately.
4. **Save Plant:** Click the **Add Plant** button. A green confirmation banner will appear, and your new plant will be added to the session table below.

---

### 2. Logging Care Activities ("Log Care")

Use this screen whenever you perform maintenance on one of your plants.

1. **Select "Log Care"** from the sidebar menu.
2. **Select a Plant:** Choose the plant you cared for from the **Select a plant** drop-down list.
3. **Select Activity Type:** Choose the action you performed:
   * `Watering`
   * `Repotting`
   * `Fertilizing`
   * `Pruning`
   * `Misting`
4. **Select Care Date:** Choose the date the activity took place (defaults to today).
5. **Log Action:** Click **Log Care**. The system automatically updates the plant's `last_care_date` and resets its upcoming schedule.

---

### 3. Checking Schedules & Due Dates ("View Schedule")

Use this screen daily or weekly to monitor which plants need attention.

1. **Select "View Schedule"** from the sidebar menu.
2. **Seasonal Care Reminder:** Check the informational banner at the top of the page for seasonal care tips calibrated to the current time of year.
3. **Status Banners:**
   * ⚠️ **Past Due (Orange Warning Box):** Highlights plants that are overdue for care based on their schedule.
   * ℹ️ **Due Today / Due Tomorrow (Blue Info Box):** Displays plants that require care today or tomorrow.
4. **Schedule Table:** Scroll through the main schedule table to view all your plants along with their location, watering frequency, last care date, and calculated next due date.

---

## 4. Finding & Filtering Plants ("Search")

Use this screen when your plant collection grows large and you need to look up a specific plant quickly.

1. **Select "Search"** from the sidebar menu.
2. **Type in Search Box:** Enter a plant name (e.g., *Snake*) or location (e.g., *Bedroom*) into the text input box.
3. **View Results:** The table will update live as you type, showing only matching plants. Leave the search box empty to view all recorded plants.

---

## Quick Tips for Best Results

* **Save Your Progress:** Always click **Download Plants CSV** before closing your browser session to ensure your data is backed up.
* **Keep Dates Accurate:** Keeping `last_care_date` up-to-date in **Log Care** ensures your **View Schedule** alerts remain accurate.

Demo Video:
https://drive.google.com/file/d/1V3OTgZmxgW6pDci5J4LxKD742wXkEmbp/view?usp=sharing