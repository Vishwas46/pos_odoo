# All-in-One Odoo POS Project

This project aims to develop an enhanced Point of Sale (POS) system based on Odoo, specifically targeting the German market. The goal is to create an "all-in-one" solution integrating POS functionalities, delivery service management (Lieferando, Wolt, etc.), integrated payments, and compliance with German KassenSichV regulations.

## Key Features

*   **Odoo POS Foundation:** Leveraging the robust Odoo Point of Sale module.
*   **Delivery Service Integration:** Modules to connect with platforms like Lieferando and Wolt for order synchronization.
*   **Integrated Payments:** Streamlined payment processing within the POS using integrated payment terminals/gateways.
*   **KassenSichV Compliance (Germany):** Integration with a certified Technical Security Equipment (TSE) solution. **Note:** This requires using a specific, certified third-party hardware TSE or cloud TSE service and its corresponding Odoo integration module. Our `l10n_de_pos_kassensichv` module serves as a placeholder/wrapper for this integration.
*   **Customizable:** Built on the modular Odoo framework.

## Technology Stack

*   **Backend:** Odoo (Specify Version, e.g., 16.0 or 17.0), Python 3
*   **Frontend (POS):** Odoo Web Client (JavaScript, XML, OWL Framework, CSS)
*   **Database:** PostgreSQL (Version compatible with Odoo version)
*   **Deployment:** Docker (Recommended)

## Repository Structure

*   `custom_addons/`: Contains all custom Odoo modules developed for this project.
    *   `custom_pos_base/`: Shared POS customizations.
    *   `l10n_de_pos_kassensichv/`: KassenSichV TSE integration layer (**depends on external certified module**).
    *   `pos_delivery_base/`: Shared logic for delivery integrations.
    *   `pos_lieferando_integration/`: Lieferando specific integration.
    *   `pos_wolt_integration/`: Wolt specific integration.
    *   `pos_integrated_payment/`: Enhancements for integrated payment flows.
*   `odoo.conf`: Odoo server configuration file.
*   `requirements.txt`: Python dependencies.
*   `docker-compose.yml`: Docker setup for development and deployment.
*   `Dockerfile`: Used by Docker Compose to build the Odoo image with dependencies.
*   `PLANNING.md`: High-level project plan and milestones.
*   `README.md`: This file.

## Setup (Docker Recommended)

1.  **Prerequisites:**
    *   Docker: [Install Docker](https://docs.docker.com/engine/install/)
    *   Docker Compose: Usually included with Docker Desktop, or [Install Docker Compose](https://docs.docker.com/compose/install/)
    *   Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

2.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd your_project_name
    ```

3.  **Configure Environment:**
    *   Review and adjust `odoo.conf` (especially `admin_passwd`, `db_password`).
    *   Review and adjust `docker-compose.yml` (ports, passwords - ensure they match `odoo.conf`). You might want to use a `.env` file for sensitive data.

4.  **Build and Run:**
    ```bash
    docker-compose build # Only needed initially or when Dockerfile/requirements change
    docker-compose up -d # Start Odoo and Database in detached mode
    ```

5.  **Access Odoo:** Open your browser and navigate to `http://localhost:8069` (or the port you configured).

6.  **Install Custom Modules:**
    *   Log into Odoo (you may need to create a database first).
    *   Go to `Apps`.
    *   Click `Update Apps List` (you might need to activate developer mode first: Settings -> Activate the developer mode).
    *   Search for your custom module names (e.g., "Lieferando", "KassenSichV", "Wolt") and install them.

## Development & Contribution

*   Work is organized into separate modules within `custom_addons/`.
*   Develop features on separate branches (`git checkout -b feature/my-new-feature`).
*   Push feature branches and create Pull Requests for review.
*   Ensure code follows Odoo development guidelines.
*   Add tests where appropriate.

## Important Notes on KassenSichV

*   The `l10n_de_pos_kassensichv` module in this repository is **only a placeholder or integration layer**.
*   **Actual KassenSichV compliance requires:**
    1.  A **certified TSE device** (Hardware USB/SD card) or a **certified Cloud TSE service** (e.g., Fiskaly, Deutsche Fiskal, Swissbit Cloud).
    2.  The corresponding **certified Odoo integration module** provided by the TSE vendor or a trusted Odoo partner (e.g., `pos_fiskaly`, `l10n_de_pos_cert`).
*   You will need to **obtain and install** the certified TSE module and configure it within the `l10n_de_pos_kassensichv` module's dependencies or integrate directly. **Do not attempt to implement the core TSE signing logic yourself.**

## License

Specify your chosen license (e.g., MIT, LGPL-3). Remember that Odoo itself is LGPL-3, which has implications for derivative works.