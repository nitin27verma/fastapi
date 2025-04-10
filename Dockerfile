# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port for Azure App Service
EXPOSE 8000

# Run the FastAPI app
CMD ["python", "-m", "uvicorn", "src.fast-api-app.main:app", "--host", "0.0.0.0", "--port", "8000"]
