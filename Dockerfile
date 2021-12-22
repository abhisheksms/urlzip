FROM python:3.9-slim

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY src /src
WORKDIR /src