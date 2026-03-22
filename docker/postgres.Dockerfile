# docker/postgres.Dockerfile

FROM postgres:16

# Install pgvector
RUN apt-get update && apt-get install -y \
    postgresql-16-pgvector \
    && rm -rf /var/lib/apt/lists/*

# Optional: init scripts
COPY docker/postgres/init/ /docker-entrypoint-initdb.d/