FROM python:3.7

MAINTAINER  https://github.com/zhangshanwen

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "-k", "gevent", "-b", "0.0.0.0:5000", "app:app"]