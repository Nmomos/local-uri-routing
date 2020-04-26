FROM python:3.8.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/
WORKDIR /usr/src/app

RUN apk update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

RUN python3 manage.py collectstatic --no-input

#EXPOSE 8000
#CMD [ "gunicorn", "a-api.wsgi:application --bind 0.0.0.0:8000 --workers 3" ]
#CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]
