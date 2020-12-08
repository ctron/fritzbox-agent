
FROM docker.io/library/python:slim

LABEL org.opencontainers.image.source="https://github.com/ctron/fritzbox-agent"

RUN pip install fritzconnection
COPY main.py /

CMD [ "python", "main.py" ]
