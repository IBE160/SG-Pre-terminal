This workflow is designed to initialize, update, and manage the `bmm-workflow-status.md` file, providing a centralized, real-time overview of the project's status. It automates the integration of status updates from various workflow paths into a main project status document.

### Core Functionality:

- **Initialization**: Creates the `bmm-workflow-status.md` file using a predefined template, structuring it with sections for each project level (e.g., Epic, Story) and workflow stage (e.g., Analysis, Plan, Implementation).
- **Dynamic Updates**: Scans specified workflow directories to find the most recently updated `status.md` file in each.
- **Content Integration**: Reads the content of these `status.md` files and dynamically inserts them into the corresponding sections of the main `bmm-workflow-status.md`.
- **Templating**: Utilizes a template to ensure the `bmm-workflow-status.md` is always well-structured and includes the latest updates in the correct place.

### How It Works:

1.  **Configuration**: The workflow is driven by `workflow.yaml`, which defines the structure of the project, including paths to different workflow stages and the levels of project hierarchy (e.g., Epics, Stories).
2.  **Scanning**: The script traverses the directory structure defined in the configuration to locate all relevant `status.md` files.
3.  **Update Mechanism**: For each defined project level and workflow stage, it identifies the most recent `status.md` and prepares its content for injection.
4.  **Injection**: The content is injected into the main `bmm-workflow-status.md` using placeholder tags, ensuring that each section is populated with the most current information.

### Usage:

To run this workflow, simply execute the main script. It will automatically handle the detection, reading, and integration of status files. Ensure that the `workflow.yaml` is correctly configured with the paths relevant to your project structure.

### Benefits:

- **Centralized Status Tracking**: Provides a single document to view the entire project's status at a glance.
- **Automation**: Reduces manual effort in copying and pasting updates.
- **Real-time Visibility**: Ensures the status document is always up-to-date with the latest from all parts of the project.
- **Flexibility**: The YAML configuration allows for easy adaptation to different project structures and workflows.

This system is essential for maintaining clarity and alignment in complex projects, enabling teams to track progress and manage workflows effectively.