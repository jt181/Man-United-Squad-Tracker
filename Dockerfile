# Use a minimal Python runtime as a parent image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# At build time, create and seed the SQLite database
RUN python create_db.py && python seed_db.py

# Tell Cloud Run which port to listen on
ENV PORT=8080
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]
