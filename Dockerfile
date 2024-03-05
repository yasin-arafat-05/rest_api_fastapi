# choose a base image:
FROM python:3.11.7

# WORKING DIRECTORY:
WORKDIR  /app

# Copy the application files
COPY ./ app


# install dependencies

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Expose the port 
EXPOSE 8000

# command for run the application: 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]


