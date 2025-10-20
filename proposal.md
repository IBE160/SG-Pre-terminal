## Case Title
Excelence

## Background
Budgeting can be a difficult task for people not experienced in economics. We want to make a simple budgeting tool
that can help smaller organizations and individuals manage their finances.

## Purpose
Budget together, Strong 🐒

This app will contribute to gain an improved overview of the company/personal economic situation by following up budgeting with graphs and notifications for overexpending

## Target Users
People who are not familiar with excel and other spreadsheet applications. 

## Core Functionality

### Must Have (MVP)
- Feature 1: Export excel/csv file
- Feature 2: Add finance categories
- Feature 3: Add expense
- Feature 4: Add income
- Feature 5: Calculate
- Feature 6: Simple graphs to show income/loss

### Nice to Have (Optional Extensions)
- Optional Feature 1: Import excel/csv files.
- Optional Feature 2: More advanced graphs/dashboard
- Optional Feature 3: Multiple organizations
- Optional Feature 4: Transactions

## Data Requirements

- Data entity 1: [e.g., Users - id, name, email, password]
- Data entity 2: [e.g., Expenses - id, user_id, category_id, amount, description, date]
- Data entity 3: [e.g., Income - id, user_id, category_id, amount, description, date]
- Data entity 4: [e.g., Categories - id, user_id, name, type (either 'income' or 'expense')]

## User Stories (Optional)

1. As a user, I want to be able to log in to the application, so that I can access my personal budget.
2. As a user, I want to add different categories for my income and expenses, so that I can organize my finances.
3. As a user, I want to add my income and expenses, so that I can track my money flow.
4. As a user, I want to see a simple graph of my income and expenses, so that I can quickly understand my financial situation.
5. As a user, I want to export my budget to an excel/csv file, so that I can have a local copy or use it in other applications.
6. As a user, I want to view my budget on my mobile phone, so that I can check it on the go.

## Technical Constraints

- Must have simplified mobile view for graphs and displaying finished budget
- Full view only available on desktop mode (browser)
- Must support user authentication

## Tech stack

### Frontend
- Svelte

### Backend
- Python
- FastAPI
- Supabase

### Hosting
Vercel, Netlify, Heroku or similar

## Success Criteria

- Users can successfully register and log in to the application.
- Users can create, edit, and delete income and expense categories.
- Users can add, edit, and delete income and expense entries.
- The application displays a clear and easy-to-understand graph showing the user's income and expenses.
- Users can download their budget as an excel or csv file.
- The application has a responsive design that works well on mobile devices.
- The application provides a full view on desktop and a simplified view on mobile.
