# UX Design Specification: Excelence (Excelence)

## 1. Introduction

This document outlines the User Experience (UX) and User Interface (UI) design for **Excelence**, a personal finance web application. The design, created with Google Stitch, prioritizes a clean, intuitive, and engaging user experience to help users manage their finances effectively.

**Note on Branding:** A minor inconsistency was noted in the designs. The login/registration page uses the name "Excelence," while the main application uses "Excelence." This document will proceed assuming the brand name is **Excelence**, and the login page should be updated to reflect this.

## 2. User Flow

The application follows a logical and straightforward user flow, designed to guide users from authentication to their financial dashboard and subsequent management tasks.

1.  **Authentication:**
    *   New users **Sign Up** for an account using their email and password or by connecting their Google account.
    *   Existing users **Log In**.
    *   A "Forgot Password" flow allows users to reset their credentials.

2.  **Dashboard:**
    *   Upon successful login, the user lands on the **Main Dashboard**.
    *   The dashboard provides a high-level "Financial Snapshot" for the current month.
    *   A persistent sidebar on the left provides primary navigation to all key sections of the application.

3.  **Core Tasks:** From the dashboard, the user can navigate to perform core financial management tasks:
    *   **View Transactions:** Access a detailed **Spreadsheet** view of all income and expenses.
    *   **Manage Data:** Add, edit, or delete transactions from the spreadsheet.
    *   **Gamification:**
        *   Toggle "Game Mode" on or off.
        *   View earned and in-progress **Achievements**.
    *   **Customize:**
        *   Create custom spending **Categories**.
        *   Set financial **Goals**.
    *   **Configure:** Access and update account **Settings**.

## 3. Page-by-Page Specification

This section details the purpose, features, and user interactions for each page of the application.

### 3.1. Login & Registration

*   **File:** `login_/_registration/code.html`
*   **Purpose:** To provide a secure entry point for new and existing users.
*   **Key Features:**
    *   Tabbed interface to switch between "Sign Up" and "Log In" forms.
    *   Email and password fields for standard authentication.
    *   Password visibility toggle.
    *   "Continue with Google" button for OAuth authentication.
    *   "Forgot Password?" link.
*   **User Interactions:**
    *   Users can seamlessly switch between login and registration without a page reload.
    *   Input fields have clear labels and icons.
    *   Primary call-to-action (CTA) is prominent ("Create My Account" or "Log In").

### 3.2. Main Dashboard (Default)

*   **File:** `main_dashboard_default/code.html`
*   **Purpose:** To provide a comprehensive, at-a-glance summary of the user's financial health and act as the central navigation hub.
*   **Key Features:**
    *   **Financial Snapshot:** Summary cards for Total Income, Total Expenses, and Net Savings.
    *   **Spending Breakdown:** A donut chart visualizing spending by category.
    *   **Goals Overview:** Progress bars for active savings goals.
    *   **Recent Transactions:** A list of the most recent financial activities.
    *   **Quick Actions:** Buttons to quickly "Add Income" or "Add Expense".
    *   **Navigation Sidebar:** Links to Dashboard, Spreadsheet, Achievements, and Settings. Includes a toggle for "Game Mode".
*   **User Interactions:**
    *   Users can filter the snapshot view (e.g., "This Month," "Last 30 Days").
    *   Hovering over the spending chart segments reveals more details.
    *   Clicking "View All" on the Goals or Transactions sections navigates to the respective detailed pages.

### 3.3. Spreadsheet

*   **File:** `main_dashboard_spreadsheet/code.html`
*   **Purpose:** To provide a detailed, tabular view of all transactions for in-depth analysis and management.
*   **Key Features:**
    *   A familiar spreadsheet-like interface with rows and columns.
    *   Columns for Amount, Category, Description, and Date.
    *   Color-coded amounts (green for income, red for expenses).
    *   Category tags for easy identification.
    *   A prominent "New Transaction" button.
*   **User Interactions:**
    *   On hover, action buttons (Edit, Delete) appear for each transaction row, minimizing visual clutter.
    *   The table is sortable and filterable (functionality to be implemented).
    *   Users can add a new transaction via a modal or a dedicated page.

### 3.4. Achievements

*   **File:** `main_dashboard_achievements/code.html`
*   **Purpose:** To gamify the budgeting experience, motivating users to achieve their financial goals through a system of badges and rewards.
*   **Key Features:**
    *   A grid of achievement badges.
    *   **Unlocked Achievements:** Displayed in full color with a checkmark.
    *   **In-Progress Achievements:** Are partially opaque and show a progress bar (e.g., "7-Day Streak - 4/7 days").
    *   **Locked Achievements:** Are grayed out with a question mark icon.
*   **User Interactions:**
    *   Users can quickly see their progress and what they need to do to unlock the next badge.

### 3.5. Game Mode Dashboard

*   **File:** `main_dashboard_game_mode/code.html`
*   **Purpose:** This appears to be a variant of the main dashboard, likely activated when "Game Mode" is toggled on. It presents the same financial data but possibly with a more visually engaging, game-like interface.
*   **Key Features:**
    *   Structurally identical to the default dashboard. The primary difference is the enabled state of the "Game Mode" toggle in the sidebar. The UI might change dynamically when this is active (e.g., different animations, colors, or component styles).

### 3.6. Settings

*   **File:** `main_dashboard_settings/code.html`
*   **Purpose:** To allow users to manage their profile, preferences, and security settings.
*   **Key Features:**
    *   **Profile:** Update Full Name, Email, and Avatar.
    *   **Preferences:** Set preferred currency (USD, GBP, EUR) and toggle email notifications.
    *   **Security:** A button to initiate a "Change Password" flow.
    *   **Theme:** Select between Light, Dark, and System theme preferences.
*   **User Interactions:**
    *   Users can edit their information in clearly defined sections.
    *   A "Save Changes" button persists all modifications made on the page.

### 3.7. Create New Category

*   **File:** `create_category/code.html`
*   **Purpose:** To allow users to create custom categories for organizing their expenses. This is presented as a modal overlay.
*   **Key Features:**
    *   Input field for the category name.
    *   Optional input field for selecting an emoji to represent the category.
    *   A progress bar indicating the form is complete.
    *   A clear "Create Category" CTA.
*   **User Interactions:**
    *   The modal appears over the current page, with the background dimmed.
    *   Users can close the modal using an 'X' button.

### 3.8. Create New Goal

*   **File:** `create_goal/code.html`
*   **Purpose:** To enable users to set specific, measurable savings goals. This is presented as a modal overlay.
*   **Key Features:**
    *   Input field for the goal's name (e.g., "Dream Vacation Fund").
    *   Input field for the target amount.
    *   A date picker to set the target date.
    *   A progress bar indicating the form is complete.
    *   A "Set My Goal" CTA.
*   **User Interactions:**
    *   The modal guides the user through the necessary steps to define a new goal.
    *   Users can close the modal using an 'X' button.