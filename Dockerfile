FROM python:3.5.2-alpine
ADD requirements.txt /
RUN pip install -r requirements.txt
