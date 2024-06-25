FROM python:3.12.0-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

# Create the virtualenv:
RUN python3 -m venv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies with increased timeout and retry logic:
RUN /opt/venv/bin/pip install --upgrade pip --timeout 100 && \
    /opt/venv/bin/pip install -r requirements.txt --timeout 100 --retries 5

RUN chmod +x config/scripts/entrypoint.sh

EXPOSE 8000

# Run the application:
ENTRYPOINT [ "/app/config/scripts/entrypoint.sh" ]

