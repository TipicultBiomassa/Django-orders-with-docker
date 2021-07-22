# pull official base image
FROM python:3.8
# set work directory
WORKDIR /usr/src/itorum
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./manage.py .
RUN pip install -r requirements.txt
# copy project
COPY . .