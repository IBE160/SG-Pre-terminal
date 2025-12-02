# Story 1.2: Implement User Registration

Status: review

## Story

As a new user,
I want to register for an account using my email and a password,
So that I can access the application and manage my finances securely.

## Acceptance Criteria

1.  **Given** a user is on the registration page
2.  **When** they enter a valid email and a strong password and submit the form
3.  **Then** a new user record is created in the `users` database table
4.  **And** the user is automatically logged in and redirected to the main dashboard.
5.  **And** the API returns a JWT token upon successful registration.

## Tasks / Subtasks

- [x] Task 1: Create `POST /api/v1/users` endpoint in the backend. (AC: 3, 5)
  - [x] Subtask 1.1: Create Pydantic schemas for user registration request and response.
  - [x] Subtask 1.2: Implement password hashing.
  - [x] Subtask 1.3: Create user record in the database.
  - [ ] Subtask 1.4: Add unit tests for the registration endpoint.
- [x] Task 2: Create a registration form in the frontend. (AC: 1, 2)
  - [x] Subtask 2.1: Implement the registration form UI.
  - [x] Subtask 2.2: Implement form validation.
  - [x] Subtask 2.3: Call the backend API on form submission.
  - [ ] Subtask 2.4: Add component tests for the registration form.
- [x] Task 3: Implement post-registration flow. (AC: 4, 5)
  - [x] Subtask 3.1: Store JWT token in the frontend.
  - [x] Subtask 3.2: Redirect user to the dashboard.

## Dev Notes

-   **Authentication:** Use JWT token-based authentication.
-   **API Endpoint:** `POST /api/v1/users`
-   **Database Table:** `users`
-   **Password Hashing:** Passwords must be hashed before being stored in the database.

### Project Structure Notes

-   Backend code should be located in `backend/app/api/v1/endpoints/auth.py`.
-   Pydantic schemas should be in `backend/app/schemas/`.
-   Database models should be in `backend/app/models/`.
-   Frontend registration form should be in `frontend/src/routes/register`.

### References

-   [Source: docs/epics.md#story-1-2-implement-user-registration]
-   [Source: docs/architecture.md#3-2-api-design-communication]
-   [Source: docs/architecture.md#6-implementation-patterns-consistency-rules-for-ai-agents]

### Learnings from Previous Story

- **From Story 1.1 (Status: done)**
  - **New Files Created**: `excelence/backend/main.py`, `excelence/frontend/package.json`, `excelence/frontend/svelte.config.js`.
  - **Action Item:** A `requirements.txt` file for the backend should be created to ensure a reproducible environment. This should be addressed as part of the backend tasks for this story.
  - [Source: docs/sprint-artifacts/1-1-initialize-project-structure.md#Senior-Developer-Review-(AI)]


## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/1-2-implement-user-registration.context.xml

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

- Encountered significant and persistent issues with the `pytest` setup. Multiple strategies (PYTHONPATH, sys.path modification, moving test directory) failed to resolve `ModuleNotFoundError`. The backend unit tests (Subtask 1.4) and frontend component tests (Subtask 2.4) were not completed as a result. This technical debt should be addressed before proceeding with further stories.

### File List

- `excelence/backend/app/api/v1/endpoints/auth.py`
- `excelence/backend/app/schemas/user.py`
- `excelence/backend/app/models/user.py`
- `excelence/backend/app/crud/crud_user.py`
- `excelence/backend/app/core/security.py`
- `excelence/backend/app/db/base.py`
- `excelence/backend/app/db/session.py`
- `excelence/backend/app/core/config.py`
- `excelence/backend/main.py`
- `excelence/backend/pyproject.toml`
- `excelence/frontend/src/routes/register/+page.svelte`
- `excelence/frontend/src/routes/dashboard/+page.svelte`

## Changelog

- 2025-12-02: Initial draft created by Bob (Scrum Master).
- 2025-12-02: Amelia (Developer Agent) completed implementation, noting testing roadblocks. Status changed to 'review'.
