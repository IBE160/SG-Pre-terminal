# Excelence - Epic Breakdown

**Author:** BIP
**Date:** 2025-11-07
**Project Level:** 2

---

## Overview

This document provides the detailed epic breakdown for Excelence, expanding on the high-level epic list in the [PRD](./PRD.md).

Each epic includes:

- Expanded goal and value proposition
- Complete story breakdown with user stories
- Acceptance criteria for each story
- Story sequencing and dependencies

**Epic Sequencing Principles:**

- Epic 1 establishes foundational infrastructure and initial functionality
- Subsequent epics build progressively, each delivering significant end-to-end value
- Stories within epics are vertically sliced and sequentially ordered
- No forward dependencies - each story builds only on previous work

---

**Epic 1: Project Foundation & Core Budgeting**

**Goal:** Establish the project's technical foundation, implement user authentication, and deliver the core functionalities for tracking income, expenses, and categories.

---

**Story 1.1: Backend and Database Setup**

**Covers:** Foundational Setup

As a developer,
I want to set up the FastAPI backend and connect it to a Supabase project,
So that we have a foundational server and database to build upon.

**Acceptance Criteria:**
1.  A new Supabase project is created.
2.  A new FastAPI project is initialized.
3.  Database connection between FastAPI and Supabase is established and verified.
4.  Initial database schema for users, categories, income, and expenses is defined and created in Supabase.

---

**Story 1.2: User Authentication Endpoints**

**Covers:** FR001, FR002

As a developer,
I want to create API endpoints for user registration and login,
So that users can securely create accounts and sign in.

**Acceptance Criteria:**
1.  An endpoint for user registration (`/register`) is created that securely hashes passwords.
2.  An endpoint for user login (`/login`) is created that returns a JWT token upon success.
3.  Supabase Auth is integrated for handling user management.
4.  API endpoints are tested and functional.

---

**Story 1.3: Frontend Project Setup & Authentication UI**

**Covers:** FR001, FR002, FR008

As a user,
I want to see a registration and login page,
So that I can access the application.

**Acceptance Criteria:**
1.  A new SvelteKit project is initialized.
2.  Basic UI components for registration and login forms are created.
3.  The UI is connected to the backend authentication endpoints.
4.  Users can successfully register and log in, and the app stores the auth token.
5.  A basic route protection mechanism is in place to prevent access to protected areas.

---

**Story 1.4: Category Management API**

**Covers:** FR004

As a developer,
I want to build CRUD API endpoints for managing categories,
So that the frontend can interact with user-defined categories.

**Acceptance Criteria:**
1.  API endpoints for creating, reading, updating, and deleting categories are created.
2.  Endpoints are protected and only accessible by authenticated users.
3.  Each category is associated with the correct user.
4.  API endpoints are tested and functional.

---

**Story 1.5: Income/Expense Management API**

**Covers:** FR003

As a developer,
I want to build CRUD API endpoints for managing income and expense entries,
So that the frontend can manage financial records.

**Acceptance Criteria:**
1.  API endpoints for creating, reading, updating, and deleting income/expense entries are created.
2.  Endpoints are protected and only accessible by authenticated users.
3.  Each entry is associated with the correct user and a category.
4.  API endpoints are tested and functional.

---

**Story 1.6: Basic Frontend for Budget Management**

**Covers:** FR003, FR004, FR008

As a user,
I want to create, view, edit, and delete my income, expenses, and categories,
So that I can manage my budget.

**Acceptance Criteria:**
1.  A UI is created for managing categories (create, view, edit, delete).
2.  A UI is created for adding, editing, and deleting income and expense entries.
3.  The UI is connected to the corresponding backend APIs.
4.  The application displays a simple, real-time list of income and expenses.

---

**Epic 2: Dashboard, Visualizations, and Data Export**

**Goal:** Develop the main dashboard, integrate charting libraries for visual representation of financial data, and implement the data export feature.

---

**Story 2.1: Dashboard Data API Endpoint**

**Covers:** FR005, FR006

As a developer,
I want to create an API endpoint that provides aggregated financial summary data,
So that the frontend has a single source for dashboard information.

**Acceptance Criteria:**
1.  A protected API endpoint (e.g., `/dashboard/summary`) is created.
2.  The endpoint returns the current user's total income, total expenses, and net balance for a default period (e.g., current month).
3.  The endpoint also returns data structured for use in a charting library (e.g., expenses grouped by category).
4.  The endpoint is tested for performance and accuracy.

---

**Story 2.2: Frontend Dashboard Layout**

**Covers:** FR005, FR008

As a user,
I want to see a central dashboard page when I log in,
So that I can get an immediate overview of my financial situation.

**Acceptance Criteria:**
1.  A new, protected route for the dashboard is created in the SvelteKit application.
2.  The dashboard page has clear placeholders for a financial summary, a main graph, and a list of recent transactions.
3.  The dashboard UI is connected to the `/dashboard/summary` endpoint and displays the total income, expenses, and balance.

---

**Story 2.3: Integrate Charting Library and Display Graph**

**Covers:** FR006, FR008

As a user,
I want to see a simple graph of my finances,
So that I can visually understand where my money is going.

**Acceptance Criteria:**
1.  A charting library (e.g., Chart.js) is integrated into the SvelteKit project.
2.  The graph component on the dashboard is connected to the summary API endpoint.
3.  A simple pie or bar chart is displayed, showing the breakdown of expenses by category.
4.  The chart is visually clear and easy to understand.

---

**Story 2.4: Data Export API Endpoint**

**Covers:** FR007

As a developer,
I want to create an API endpoint that generates a CSV file of the user's budget data,
So that users can download their financial records.

**Acceptance Criteria:**
1.  A protected API endpoint (e.g., `/export/csv`) is created.
2.  The endpoint retrieves all income and expense entries for the authenticated user.
3.  The endpoint formats the data into a valid CSV format with appropriate headers (Date, Category, Description, Income, Expense).
4.  The endpoint returns the data as a downloadable file.

---

**Story 2.5: Frontend Export Button**

**Covers:** FR007, FR008

As a user,
I want to be able to download my budget data as a file,
So that I can keep a local copy or use it in other applications.

**Acceptance Criteria:**
1.  An "Export to CSV" button is added to the dashboard UI.
2.  Clicking the button calls the `/export/csv` API endpoint.
3.  The browser prompts the user to download the generated CSV file.
4.  The downloaded file is correctly formatted and contains the user's data.

---

**Epic 3 (Optional): Gamification and Enhanced User Experience**

**Goal:** Implement the optional "Game Mode," including features like drag-and-drop, animations, and progress tracking.

---

**Story 3.1: "Game Mode" Toggle**

**Covers:** N/A (Optional Gamification)

As a user,
I want to be able to turn "Game Mode" on or off,
So that I can choose the experience that best suits me.

**Acceptance Criteria:**
1.  A user setting for "Game Mode" is added to the user profile in the database.
2.  A toggle switch is available in the application's settings UI.
3.  The application's UI conditionally renders gamified features based on this setting.

---

**Story 3.2: Drag-and-Drop Entry**

**Covers:** N/A (Optional Gamification)

As a user in "Game Mode",
I want to drag an icon to a drop zone to start adding an expense or income,
So that data entry is faster and more interactive.

**Acceptance Criteria:**
1.  A library like `svelte-dnd-action` is integrated into the project.
2.  A selection of common category icons is displayed on the dashboard.
3.  Dragging an icon to a designated drop zone opens the entry form with the category pre-selected.
4.  This feature is only available when "Game Mode" is enabled.

---

**Story 3.3: Add UI Animations**

**Covers:** N/A (Optional Gamification)

As a user in "Game Mode",
I want to see simple animations when I complete actions,
So that the application feels more alive and provides satisfying feedback.

**Acceptance criteria:**
1.  Svelte's built-in animation modules are utilized.
2.  A subtle animation is triggered when a new item is added to the income/expense list.
3.  A confirmation animation (e.g., a brief flash or a checkmark) appears when an entry is successfully saved.
4.  These animations are only present when "Game Mode" is enabled.

---

**Story 3.4: Financial Goal Setting**

**Covers:** N/A (Optional Gamification)

As a user in "Game Mode",
I want to set a simple financial goal, like a monthly savings target,
So that I can track my progress and stay motivated.

**Acceptance Criteria:**
1.  The database is updated to store user-defined goals.
2.  A UI is created for the user to set or update their primary financial goal.
3.  A simple progress bar or visual indicator is added to the dashboard, showing progress towards the active goal.
4.  This feature is only available when "Game Mode" is enabled.

---

**Story 3.5: Achievements and Badges**

**Covers:** N/A (Optional Gamification)

As a user in "Game Mode",
I want to earn badges for reaching financial milestones,
So that I feel a sense of accomplishment and recognition.

**Acceptance Criteria:**
1.  A system for defining and awarding badges is created (e.g., "First Week Done!", "Savings Goal Met!").
2.  Backend logic is implemented to award badges when criteria are met.
3.  A non-intrusive notification appears when a user earns a badge.
4.  A section in the user's profile displays their collection of earned badges.
5.  This feature is only available when "Game Mode" is enabled.

---

## Story Guidelines Reference

**Story Format:**

`'
**Story [EPIC.N]: [Story Title]**

As a [user type],
I want [goal/desire],
So that [benefit/value].

**Acceptance Criteria:**
1. [Specific testable criterion]
2. [Another specific criterion]
3. [etc.]

**Prerequisites:** [Dependencies on previous stories, if any]
`'

**Story Requirements:**

- **Vertical slices** - Complete, testable functionality delivery
- **Sequential ordering** - Logical progression within epic
- **No forward dependencies** - Only depend on previous work
- **AI-agent sized** - Completable in 2-4 hour focused session
- **Value-focused** - Integrate technical enablers into value-delivering stories

---

**For implementation:** Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown.
