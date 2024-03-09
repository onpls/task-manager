# Task-manager

## Running the Application
To start the application with the PostgreSQL database, use the following command:
`./start.sh`

## Database Migration
To migrate the database to the required state, execute:
`alembic upgrade head`

## Removing Database Volumes
To delete the database volumes, run:
`docker compose down --volumes`
