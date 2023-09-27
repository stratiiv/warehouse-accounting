FROM python:3.11

WORKDIR /home/warehouse-accounting

ENV PYTHONUNBUFFERED 1
# Disables generation of pyc files
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /home/warehouse-accounting

RUN pip install --no-cache-dir -r requirements.txt

