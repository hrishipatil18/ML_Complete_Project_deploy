# Uses Python 3.8 as the base image. slim-buster → A minimal Debian-based image, reducing image size.
FROM python:3.8-slim-buster  

# Install Required Dependencies. apt update -y → Updates package lists. apt install awscli -y → Installs AWS CLI (useful for S3, Lambda, etc.).
# Set the Working Directory
RUN apt update -y && apt install awscli -y
WORKDIR /app
# Sets /app as the working directory inside the container. All subsequent commands will be executed inside /app.

#Copy Project Files. Copies all files from the host system into the container at /app. Includes requirements.txt, app.py, and any other necessary files.
COPY . /app

# Installs all Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Defines the command that runs when the container starts.
CMD ["python3", "app.py"]