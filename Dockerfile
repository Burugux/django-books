# pull official base image
FROM python:3.8.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update && apt-get install -y \
  libpq-dev \
  gcc \
  python3-dev \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

# copy project
COPY . .