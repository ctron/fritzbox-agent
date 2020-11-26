
FROM docker.io/library/python:slim

RUN pip install fritzconnection
COPY main.py /

CMD [ "python", "main.py" ]