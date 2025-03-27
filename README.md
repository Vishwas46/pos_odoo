# pos_odoo

This repository provides a minimal Docker Compose setup for running Odoo 18 with a PostgreSQL 13 database.

## Files Included

- **docker-compose.yaml**:  
  Defines two services:
  - **db**: Runs a PostgreSQL 13 container.
  - **odoo**: Runs an Odoo 18 container that depends on the `db` service.

- **odoo.conf**:  
  Contains configuration options for the Odoo service including database connection details.

## How to Use

1. **Ensure you have Docker and Docker Compose installed.**

2. **Start the Services:**
   ```bash
   docker-compose up

