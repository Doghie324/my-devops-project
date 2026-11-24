FROM python:3.13-slim-bookworm
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
