# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "portfolio_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#fastapi
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
