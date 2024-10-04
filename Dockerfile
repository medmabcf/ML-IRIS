FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./back /app/back
COPY ./ml /app/ml
COPY ./requirements_dev.txt /app/ 

RUN pip install --no-cache-dir -r requirements_dev.txt 

EXPOSE 8000

CMD ["uvicorn", "back.main:app", "--host", "0.0.0.0", "--port", "8000"]
