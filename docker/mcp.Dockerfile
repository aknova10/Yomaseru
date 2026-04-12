# docker/mcp.Dockerfile

FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_server/ ./mcp_server/

WORKDIR /app/mcp_server

# CMD ["python", "server.py"]
CMD ["fastmcp", "run", "server.py:mcp", "--transport", "http", "--host", "0.0.0.0", "--port", "9000"]