FROM python:3.8-slim

LABEL maintainer="Jez Smith"

RUN apt-get update

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ENV SRC_DIR /opt/api
COPY ./api ${SRC_DIR}
WORKDIR ${SRC_DIR}

EXPOSE 5000

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "server:SERVER"]
