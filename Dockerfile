FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r /app/my_env/server/requirements.txt

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "my_env.server.app:app", "--host", "0.0.0.0", "--port", "8000"]
