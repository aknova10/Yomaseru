set -e

# echo "Waiting for Postgres..."

# while ! nc -z $DB_HOST $DB_PORT; do
#     sleep 1
# done

# echo "Postgres is up!"

# echo "Running migrations..."
# alembic upgrade head

echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8000