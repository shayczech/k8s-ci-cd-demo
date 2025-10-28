# --- Build Stage ---
# Use an official Python image as the base for building
FROM python:3.10-slim as builder

# Set the working directory
WORKDIR /usr/src/app

# Install build dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# --- Final Stage ---
# Use a minimal, non-root base image for security
FROM python:3.10-slim

# Create a non-root user and group
RUN addgroup --system app && adduser --system --group app

# Set the working directory
WORKDIR /home/app

# Copy the installed packages and app code from the builder stage
COPY --from=builder /usr/src/app .

# Set permissions for the non-root user
RUN chown -R app:app /home/app

# Switch to the non-root user
USER app

# Expose the port the app runs on
EXPOSE 5000

# The command to run the application
CMD [ "python", "./main.py" ]
