# Step 1: Start with a base image
# We'll use an official Python 3.9 image.
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
# This is where our app will live.
WORKDIR /app

# Step 3: Copy our project files into the container
# First, copy the requirements file.
COPY requirements.txt .

# Step 4: Install the Python libraries
# This runs 'pip install' inside the container.
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of our application code
# This copies the app.py file and the models folder.
COPY . .

# Step 6: Tell Docker what command to run when the container starts
# This will execute 'python app.py'.
CMD ["python", "app.py"]
