#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
DOCKER_COMPOSE_FILENAME=docker-compose.yaml
docker compose -f "${DIR}/${DOCKER_COMPOSE_FILENAME}" up --build --remove-orphans
