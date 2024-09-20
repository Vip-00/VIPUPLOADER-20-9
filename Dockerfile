FROM python:3.9.6-alpine3.14

WORKDIR /app

COPY . .

# Update package index and install dependencies
RUN apk update \
    && apk add --no-cache gcc libffi-dev musl-dev ffmpeg \
    # Add the community repository for aria2c
    && apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community aria2 \
    && pip install --no-cache-dir -r requirements.txt

# Run both Gunicorn and the Python script
CMD gunicorn app:app & python3 main.py
