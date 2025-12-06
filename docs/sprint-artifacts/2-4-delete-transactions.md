# Story 2.4: Delete Transactions

Status: ready-for-dev

## Story

As a user,
I want to be able to delete a transaction,
So that I can remove accidental or incorrect entries.

## Acceptance Criteria

1.  **Given** a user is viewing their transaction history, **when** they select an option to delete a specific transaction and confirm the action, **then** the transaction is permanently removed from the database.
2.  **And** the transaction list and dashboard summary update to reflect the removal.

## Tasks / Subtasks

-   [ ] **Backend: Create API Endpoint for Deleting Transactions** (AC: #1)
    -   [ ] Implement `DELETE /api/v1/transactions/{transaction_id}` endpoint in `backend/app/api/v1/endpoints/transactions.py`.
    -   [ ] Add business logic to `backend/app/crud/transactions.py` to delete a transaction by its ID.
    -   [ ] Ensure the endpoint is protected and requires user authentication.
    -   [ ] Ensure the query is scoped to the authenticated `user_id` to prevent unauthorized access.
-   [ ] **Frontend: Add Delete Functionality to Transaction List** (AC: #1, #2)
    -   [ ] Add a "Delete" button to each row in the `TransactionList.svelte` component.
    -   [ ] Clicking the "Delete" button should trigger a confirmation modal to prevent accidental deletion.
    -   [ ] On confirmation, the component should send a `DELETE` request to `/api/v1/transactions/{transaction_id}`.
    -   [ ] After a successful deletion, the transaction list in the store should be refreshed.
-   [ ] **Frontend: Create Confirmation Modal** (AC: #1)
    -   [ ] Create a reusable `ConfirmationModal.svelte` component.
    -   [ ] The modal should display a confirmation message and provide "Confirm" and "Cancel" buttons.

## Dev Notes

-   **API Naming:** The endpoint must be `DELETE /api/v1/transactions/{transaction_id}`. [Source: `docs/architecture.md#API-Naming`]
-   **Database Naming:** The database table is `transactions` with snake_case columns. [Source: `docs/architecture.md#Database-Naming`]
-   **Error Handling:** The frontend API service should handle potential errors from the API, such as a `404 Not Found` if the transaction ID is invalid. [Source: `docs/architecture.md#Error-Handling`]
-   **Security:** All backend queries MUST be scoped to the `user_id` of the currently authenticated user to ensure data isolation. [Source: `docs/sprint-artifacts/tech-spec-epic-2.md#Security`]

### Project Structure Notes

-   The new `ConfirmationModal.svelte` component should be placed in `frontend/src/lib/components/shared/` to be reusable across the application.
-   The backend logic will modify the existing `transactions.py` endpoint file and `crud/transactions.py` file.

### Learnings from Previous Story

**From Story 2.3 (Status: done)**

-   **Testing is Mandatory**: The previous story was delayed because of skipped tests. All new components, especially shared components like the confirmation modal, **must** have corresponding `.test.ts` files with comprehensive tests.
-   **Auth Pattern**: The `deps.get_current_active_user` dependency must be used to protect the new DELETE endpoint.
-   **API Service**: Extend the shared `api.ts` service in the frontend to include a `deleteTransaction` method.
-   **State Management**: Continue using the existing Svelte stores to manage and refresh the transaction list to ensure the UI is reactive.

### References

-   [Source: docs/epics.md#Story-2.4-Delete-Transactions]
-   [Source: docs/sprint-artifacts/tech-spec-epic-2.md#APIs-and-Interfaces]
-   [Source: docs/architecture.md#Project-Structure-and-Boundaries]

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/2-4-delete-transactions.context.xml

### Agent Model Used

### Debug Log References

### Completion Notes List

### File List

## Senior Developer Review (AI)

-   **Reviewer:**
-   **Date:**
-   **Outcome:**
-   **Summary:**

### Key Findings

### Acceptance Criteria Coverage

| AC# | Description                                      | Status      | Evidence |
| --- | ------------------------------------------------ | ----------- | -------- |
| 1   | Transaction is permanently removed               | PENDING     |          |
| 2   | Transaction list and dashboard summary update    | PENDING     |          |

### Task Completion Validation

| Task                                                 | Marked As | Verified As | Evidence |
| ---------------------------------------------------- | --------- | ----------- | -------- |
| Backend: Create API Endpoint for Deleting Transactions | [ ]       | PENDING     |          |
| Frontend: Add Delete Functionality to Transaction List | [ ]       | PENDING     |          |
| Frontend: Create Confirmation Modal                  | [ ]       | PENDING     |          |

### Action Items

## Change Log
- 2025-12-06: Initial draft created.
