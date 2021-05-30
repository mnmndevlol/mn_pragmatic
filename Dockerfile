FROM python:3.9.0

WORKDIR /home/

RUN echo "tesfsasasaf32aasds"

RUN git clone https://github.com/mnmndevlol/mn_pragmatic.git

WORKDIR /home/mn_pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=_pragmatic.settings.deploy && python manage.py migrate --settings=_pragmatic.settings.deploy && gunicorn _pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=_pragmatic.settings.deploy --bind 0.0.0.0:8000"]
