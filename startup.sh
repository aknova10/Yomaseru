#!/bin/bash
docker compose -f docker/docker-compose.yml down
docker compose -f docker/docker-compose.yml up --build -d

NETWORK=$(docker network ls --format '{{.Name}}' | grep _default)

docker network connect $NETWORK yomaseru_ollama 2>/dev/null || true