FROM python:3.7-slim-buster

COPY application.py requirements.txt /

RUN pip3 install -r requirements.txt

ENV FLASK_APP=application.py \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

EXPOSE 5000

CMD ["/bin/sh", "-c", "flask run --host 0.0.0.0"]