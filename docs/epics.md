# Excelence - Epic Breakdown

**Author:** BIP
**Date:** 2025-11-06
**Project Level:** 2
**Target Scale:** Medium project - multiple epics, 10+ stories

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

## Epic 1: Foundation & User Authentication

**Expanded Goal:** To establish the core technical infrastructure for Excelence, including the SvelteKit frontend, FastAPI backend, and Supabase database, and to implement secure user registration and login functionality, ensuring a stable and accessible platform for users.

**Story Breakdown:**

**Story 1.1: Project Setup & Repository Initialization**

As a developer,
I want to initialize the SvelteKit and FastAPI projects and set up a monorepo structure,
So that the development environment is ready and version control is established.

**Acceptance Criteria:**
1. A new SvelteKit project is created.
2. A new FastAPI project is created.
3. A monorepo structure is configured (e.g., using `pnpm` workspaces or similar).
4. A `.gitignore` file is configured for both frontend and backend.
5. Basic `README.md` files are present for both projects.

**Prerequisites:** None

**Story 1.2: Supabase Project Setup & Schema Definition**

As a developer,
I want to set up a new Supabase project and define the initial database schema for users, income, expenses, and categories,
So that the application has a persistent data store and authentication services.

**Acceptance Criteria:**
1. A new Supabase project is created.
2. The `users` table is defined with appropriate columns (e.g., `id`, `email`, `created_at`).
3. The `income` table is defined with columns like `id`, `user_id`, `category_id`, `amount`, `description`, `date`.
4. The `expenses` table is defined with columns like `id`, `user_id`, `category_id`, `amount`, `description`, `date`.
5. The `categories` table is defined with columns like `id`, `user_id`, `name`, `type`.
6. Row-Level Security (RLS) is enabled and configured for all tables to ensure data privacy.

**Prerequisites:** Story 1.1

**Story 1.3: User Registration & Login (Frontend)**

As a user,
I want to be able to register for a new account and log in to the application,
So that I can access my personal budgeting features securely.

**Acceptance Criteria:**
1. A registration form is available on the frontend.
2. A login form is available on the frontend.
3. Users can successfully register with an email and password.
4. Users can successfully log in with their registered credentials.
5. Error messages are displayed for invalid registration or login attempts.
6. Upon successful login, the user is redirected to the main dashboard.

**Prerequisites:** Story 1.2

**Story 1.4: User Authentication (Backend & Supabase Integration)**

As a developer,
I want to integrate Supabase authentication into the FastAPI backend and SvelteKit frontend,
So that user sessions are managed securely and protected routes can be implemented.

**Acceptance Criteria:**
1. FastAPI backend is configured to use Supabase client for authentication.
2. SvelteKit frontend uses Supabase client for managing user sessions.
3. Protected routes are implemented in SvelteKit that require a logged-in user.
4. User session data is accessible on the frontend after login.
5. Users can log out of the application.

**Prerequisites:** Story 1.3

---

## Epic 2: Core Budgeting Functionality

**Expanded Goal:** To implement the primary features for managing a budget, including creating categories, tracking income and expenses, and viewing a summary dashboard with calculations and graphs, providing users with a clear overview of their financial situation.

**Story Breakdown:**

**Story 2.1: Category Management (CRUD)**

As a user,
I want to be able to create, edit, and delete different categories for my income and expenses,
So that I can organize my finances according to my needs.

**Acceptance Criteria:**
1. A dedicated section or modal exists for managing categories.
2. Users can add new categories with a name and type (income/expense).
3. Users can edit existing category names.
4. Users can delete categories (with a confirmation).
5. Categories are associated with the logged-in user.

**Prerequisites:** Epic 1 Completion

**Story 2.2: Income Tracking (CRUD)**

As a user,
I want to be able to add, edit, and delete my income entries, assigning them to a category,
So that I can accurately track my money coming in.

**Acceptance Criteria:**
1. A form or interface is available for adding new income entries.
2. Users can specify amount, description, and select an existing income category.
3. Users can edit existing income entries.
4. Users can delete income entries.
5. Income entries are associated with the logged-in user and selected category.

**Prerequisites:** Story 2.1

**Story 2.3: Expense Tracking (CRUD)**

As a user,
I want to be able to add, edit, and delete my expense entries, assigning them to a category,
So that I can accurately track my money going out.

**Acceptance Criteria:**
1. A form or interface is available for adding new expense entries.
2. Users can specify amount, description, and select an existing expense category.
3. Users can edit existing expense entries.
4. Users can delete expense entries.
5. Expense entries are associated with the logged-in user and selected category.

**Prerequisites:** Story 2.1

**Story 2.4: Financial Summary Dashboard**

As a user,
I want to see a dashboard that displays my total income, total expenses, and current balance,
So that I can quickly understand my overall financial status.

**Acceptance Criteria:**
1. The main dashboard displays the sum of all income entries for a selected period.
2. The main dashboard displays the sum of all expense entries for the same period.
3. The main dashboard displays the calculated balance (income - expenses).
4. The dashboard updates in real-time or upon data changes.

**Prerequisites:** Stories 2.2, 2.3

**Story 2.5: Simple Income/Expense Graphs**

As a user,
I want to see a simple visual graph of my income and expenses on the dashboard,
So that I can quickly grasp trends and proportions of my money flow.

**Acceptance Criteria:**
1. A bar chart or pie chart is displayed on the dashboard.
2. The chart visually represents income and expenses, or category-wise breakdown.
3. The chart data is dynamically updated based on user entries.

**Prerequisites:** Story 2.4

---

## Epic 3: Data Export & Gamification MVP

**Expanded Goal:** To enable users to export their budget data for external use and to introduce initial gamification elements to make budgeting more engaging and motivating.

**Story Breakdown:**

**Story 3.1: Export Budget Data to CSV/Excel**

As a user,
I want to be able to export my budget data (income, expenses, categories) to a CSV or Excel file,
So that I can have a local copy or use it in other applications.

**Acceptance Criteria:**
1. A button or option is available on the dashboard or a dedicated section to trigger data export.
2. The exported file contains all relevant income and expense entries, including category information.
3. The file format is either CSV or a compatible Excel format.
4. The export process is clear and provides feedback to the user.

**Prerequisites:** Epic 2 Completion

**Story 3.2: Gamification - "Game Mode" Toggle**

As a user,
I want to be able to toggle an optional "Game Mode" on or off,
So that I can choose whether to engage with gamified features.

**Acceptance Criteria:**
1. A clear toggle switch or setting is available in the user profile or settings.
2. Toggling "Game Mode" on/off persists across sessions.
3. When "Game Mode" is active, gamified elements become visible/active.

**Prerequisites:** Epic 1 Completion

**Story 3.3: Gamification - Financial Goal Setting**

As a user in "Game Mode",
I want to set financial goals (e.g., "Save $500 this month", "Spend less than $200 on groceries"),
So that I have clear targets to work towards and track my progress.

**Acceptance Criteria:**
1. Users can define a financial goal with a target amount and a timeframe.
2. Goals are displayed on the dashboard when "Game Mode" is active.
3. Progress towards goals is visually indicated (e.g., a progress bar).

**Prerequisites:** Story 3.2

**Story 3.4: Gamification - Achievement Pop-ups**

As a user in "Game Mode",
I want to receive achievement pop-ups when I reach a financial goal or milestone,
So that I feel motivated and rewarded for my budgeting efforts.

**Acceptance Criteria:**
1. A visual pop-up notification appears when a user successfully meets a defined financial goal.
2. The pop-up clearly states the achievement.
3. Achievements are tracked and viewable in a dedicated section.

**Prerequisites:** Story 3.3

---

## Story Guidelines Reference

**Story Format:**

```
**Story [EPIC.N]: [Story Title]**

As a [user type],
I want [goal/desire],
So that [benefit/value].

**Acceptance Criteria:**
1. [Specific testable criterion]
2. [Another specific criterion]
3. [etc.]

**Prerequisites:** [Dependencies on previous stories, if any]
```

**Story Requirements:**

- **Vertical slices** - Complete, testable functionality delivery
- **Sequential ordering** - Logical progression within epic
- **No forward dependencies** - Only depend on previous work
- **AI-agent sized** - Completable in 2-4 hour focused session
- **Value-focused** - Integrate technical enablers into value-delivering stories

---

**For implementation:** Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown.
