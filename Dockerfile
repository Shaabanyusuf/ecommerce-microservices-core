
FROM python:3.9-slim
WORKDIR /app
COPY inventory-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY inventory-service/ .
EXPOSE 5001
CMD ["python", "app.py"]
