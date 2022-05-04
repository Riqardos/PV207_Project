FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /backend/

# Install pipenv dependencies
COPY rest_service/Pipfile .
COPY rest_service/Pipfile.lock .

RUN pip install pipenv
RUN pipenv install --system
RUN pipenv run pip list
