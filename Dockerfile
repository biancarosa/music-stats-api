FROM python:3.6-alpine
ADD . /
RUN pip install -r requirements.txt
WORKDIR /
CMD ["python -m", "app.run"]
