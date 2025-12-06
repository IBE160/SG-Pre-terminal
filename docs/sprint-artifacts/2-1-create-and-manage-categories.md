# Story 2.1: Create and Manage Categories

Status: drafted

## Story

As a user,
I want to create, view, update, and delete custom categories,
So that I can organize my financial entries in a way that is meaningful to me.

## Acceptance Criteria

1.  **Given** a user is on the category management page
2.  **When** they create a new category with a unique name
3.  **Then** the new category is saved to the database and appears in their list of categories.
4.  **When** they edit an existing category's name
5.  **Then** the change is reflected in the database and the UI.
6.  **When** they delete a category
7.  **Then** it is removed from the database and the UI.
8.  **And** if the category is in use by a transaction, the deletion is blocked and an error message is displayed.

## Tasks / Subtasks

- [ ] Task 1: Implement Backend API for Categories (AC: 3, 5, 7, 8)
    - [ ] Subtask 1.1: Create `categories` table model in `excelence/backend/app/models/category.py`.
    - [ ] Subtask 1.2: Create Pydantic schemas for category data in `excelence/backend/app/schemas/category.py`.
    - [ ] Subtask 1.3: Implement CRUD functions for categories in `excelence/backend/app/crud/crud_category.py`.
    - [ ] Subtask 1.4: Create API endpoints (`GET`, `POST`, `PUT`, `DELETE`) in `excelence/backend/app/api/v1/endpoints/categories.py`.
    - [ ] Subtask 1.5: Implement logic to block deletion of categories in use.
    - [ ] Subtask 1.6: Add unit tests for all category endpoints, including security checks.
- [ ] Task 2: Implement Frontend UI for Category Management (AC: 1, 2, 4, 6)
    - [ ] Subtask 2.1: Create a new page for category management at `excelence/frontend/src/routes/settings/categories/+page.svelte`.
    - [ ] Subtask 2.2: Implement a component to display the list of categories.
    - [ ] Subtask 2.3: Implement a form to create and edit categories.
    - [ ] Subtask 2.4: Implement a confirmation modal for deleting categories.
    - [ ] Subtask 2.5: Integrate the UI with the backend API using the existing API service.
    - [ ] Subtask 2.6: Add component tests for the category management page.

## Dev Notes

-   **Security:** All API endpoints must be protected and all database queries must be scoped to the authenticated user's ID to ensure data isolation.
-   **Error Handling:** The backend should return a user-friendly error message when attempting to delete a category that is in use. The frontend should display this message to the user.
-   **Testing:** Following the learnings from the previous story, ensure that both backend and frontend tests are implemented and passing before marking the story as complete.

### Project Structure Notes

-   Backend logic for categories should be placed in a new file: `excelence/backend/app/api/v1/endpoints/categories.py`.
-   Frontend UI for category management will be located at `excelence/frontend/src/routes/settings/categories/+page.svelte`.
-   A new Svelte store in `excelence/frontend/src/lib/stores/data.ts` should be created to manage the list of categories.

### References

-   [Source: docs/epics.md#story-2-1-create-and-manage-categories]
-   [Source: docs/sprint-artifacts/tech-spec-epic-2.md#apis-and-interfaces]
-   [Source: docs/sprint-artifacts/tech-spec-epic-2.md#data-models-and-contracts]
-   [Source: docs/architecture.md#4-project-structure-and-boundaries]

### Learnings from Previous Story

- **From Story 1.3 (Status: done)**
  - **Testing is Mandatory**: Ensure that all required tests, especially component tests, are implemented and passing.
  - **Code Reuse**: Leverage the existing authentication and security patterns from the `auth.py` endpoint.
  - **Attention to Detail**: Pay close attention to details like HTTP status codes and specific error handling.

## Dev Agent Record

### Context Reference

<!-- Path(s) to story context XML will be added here by context workflow -->

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

### Completion Notes List

### File List
