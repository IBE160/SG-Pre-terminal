# Excelence: Decision Architecture Document

This document outlines the key architectural decisions for the Excelence project. It serves as the primary technical guide for AI agents to ensure consistent and high-quality implementation.

**Author:** BIP & Winston (Architect Agent)
**Date:** 2025-11-28
**Status:** Final

---

### **1. Executive Summary**

This architecture is designed for a modern, full-stack web application using a **FastAPI backend** and a **SvelteKit frontend**. It prioritizes a clean, scalable structure, rapid development, and a secure user experience. The foundation is established by a standard full-stack starter template, with application-specific decisions layered on top. The design is tailored to a beginner-friendly development process while adhering to professional standards for deployment and maintenance.

---

### **2. Project Initialization**

The first implementation story for this project is to initialize the codebase using the chosen starter template.

```bash
# Example command using a common generator
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
```

This command establishes the base architecture with the following pre-configured decisions:

-   **Language/TypeScript:** Python (FastAPI), TypeScript (SvelteKit)
-   **Styling solution:** Tailwind CSS
-   **Linting/Formatting:** Ruff, Prettier, ESLint
-   **Build tooling:** Vite, Docker
-   **Project structure:** Monorepo-style with separate frontend and backend directories.
-   **Authentication:** JWT token-based authentication.
-   **Testing Frameworks:** (Skipped as per user request).

---

### **3. Architectural Decisions**

#### **3.1. Database Schema**

**Context:** To support gamification features, the database needs to store user goals and achievements.
**Decision:** Three new tables will be created: `goals` (to store user-specific financial goals), `achievements` (a master list of all possible badges), and `user_achievements` (a linking table to track earned badges per user).
**Rationale:** This normalized structure is efficient and scalable, preventing data duplication.

#### **3.2. API Design & Communication**

**Context:** The frontend and backend need a consistent and predictable way to communicate.
**Decision:** The API will adhere to a standardized JSON response format (JSend-style).
    -   **Success:** `{ "status": "success", "data": { ... } }`
    -   **Error:** `{ "status": "error", "message": "Error description" }`
**Rationale:** This ensures that the frontend can handle all API responses with a single, unified logic, simplifying error handling and data retrieval.

#### **3.3. State Management (Frontend)**

**Context:** The SvelteKit frontend needs a way to manage application-wide data, like the logged-in user's status.
**Decision:** We will use **Svelte's built-in stores** (`writable`, `readable`).
**Rationale:** Svelte stores are lightweight, idiomatic, and perfectly sufficient for the complexity of this application. They avoid the need for external libraries, keeping the frontend lean and fast.

#### **3.4. Charting Library**

**Context:** The dashboard requires a library to render the spending breakdown graph.
**Decision:** We will use **Chart.js** with the `svelty-chartjs` wrapper.
**Rationale:** Chart.js is a powerful, popular, and highly customizable library. The `svelty-chartjs` wrapper simplifies its integration into the SvelteKit application, making it easy to create reactive and animated charts.

#### **3.5. Deployment Strategy**

**Context:** The application needs a clear plan for being hosted online.
**Decision:** The application will be containerized using **Docker**. The **SvelteKit frontend** will be deployed to **Vercel** for optimal performance and DX. The **FastAPI backend** will be deployed as a container to a service like **Fly.io or DigitalOcean App Platform**. The **Supabase** project will serve as the hosted database.
**Rationale:** This "hybrid-hosting" approach leverages the strengths of each platform: Vercel for best-in-class frontend hosting, container platforms for backend flexibility, and Supabase for a managed database solution.

#### **3.6. Environment Management**

**Context:** We need a secure way to manage configuration and secrets (like database passwords).
**Decision:** Configuration will be managed using **`.env` files**. The backend will use the `python-dotenv` library, and the frontend will use SvelteKit's built-in environment variable handling.
**Rationale:** This is a standard, secure practice that keeps sensitive information out of the codebase and allows for different configurations between development and production environments.

---

### **4. Project Structure and Boundaries**

The project will follow a monorepo structure provided by the starter, with clear separation between the frontend and backend.

```
/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py
│   │   │       │   ├── transactions.py
│   │   │       │   └── goals.py
│   │   ├── core/       # Config, security
│   │   ├── crud/       # Database interaction logic
│   │   ├── models/     # Database table models
│   │   ├── schemas/    # Pydantic data validation schemas
│   │   └── main.py
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── lib/
│   │   │   ├── components/ # Svelte components
│   │   │   │   ├── common/     # Reusable buttons, modals, etc.
│   │   │   │   └── routes/     # Components specific to a page
│   │   │   │       ├── dashboard/
│   │   │   │       └── settings/
│   │   │   ├── services/   # API interaction logic
│   │   │   └── stores/     # Svelte stores
│   │   ├── routes/       # SvelteKit pages and layouts
│   │   └── app.html
│   └── Dockerfile
└── docker-compose.yml
```

---

### **5. Epic to Architecture Mapping**

-   **Epic 1 (Foundation & Core Budgeting):** Mapped to `backend/app/api/v1/endpoints/auth.py`, `transactions.py`, and `categories.py`. Also maps to the core `frontend/src/routes` for login and spreadsheet views.
-   **Epic 2 (Dashboard & Visualizations):** Mapped to `backend/app/api/v1/endpoints/dashboard.py` and the `frontend/src/lib/components/routes/dashboard/` components, including the charting component.
-   **Epic 3 (Gamification):** Mapped to `backend/app/models/goals.py`, `achievements.py`, and corresponding API endpoints. Frontend components will be in `frontend/src/lib/components/routes/achievements/`.
-   **Epic 4 (Settings):** Mapped to the `frontend/src/routes/settings/` page and its associated components.

---

### **6. Implementation Patterns (Consistency Rules for AI Agents)**

To ensure all AI-generated code is consistent, agents **MUST** adhere to the following patterns:

-   **API Naming:**
    -   **Endpoints:** Use plural nouns and kebab-case (e.g., `/api/v1/user-achievements`).
    -   **Route Parameters:** Use `{parameter_id}` (e.g., `/transactions/{transaction_id}`).
-   **Database Naming:**
    -   **Tables:** Use plural, snake_case (e.g., `financial_goals`).
    -   **Columns:** Use snake_case (e.g., `target_amount`).
-   **Component Naming (Svelte):**
    -   **Files:** Use PascalCase (e.g., `StatCard.svelte`).
-   **Error Handling:**
    -   **Backend:** A global exception handler in FastAPI will catch all errors and return the standard JSON error response.
    -   **Frontend:** The API service module will have a central wrapper to handle API responses, distinguishing between `success` and `error` statuses.
-   **Date/Time Handling:**
    -   All dates and times will be stored in the database in **UTC** format.
    -   All dates sent via the API will be in **ISO 8601 string format**.

---

### **7. Validation and Coherence**

The architectural decisions have been reviewed for internal consistency:

-   **Compatibility:** All chosen technologies (FastAPI, SvelteKit, Chart.js, Docker) are compatible and work well together.
-   **Coverage:** All functional and non-functional requirements from the PRD are supported by this architecture.
-   **Completeness:** The implementation patterns are comprehensive enough to prevent common AI agent conflicts in naming and structure.

**Conclusion:** The architecture is sound, coherent, and ready for implementation.