FROM python:3.6-slim-stretch

ADD requirements.txt /
RUN pip install -r /requirements.txt

ADD . /app
WORKDIR /app

EXPOSE 5000
CMD ["gunicorn", "-k", "gevent" ,"-w" ,"5" , "app:app", "-b", "0.0.0.0:5000"]
#CMD ["gunicorn", "-k", "gthread" ,"-w" ,"5" , "app:app", "-b", "0.0.0.0:5000"]
#CMD ["gunicorn", "-k", "sync" ,"-w" ,"5" , "app:app", "-b", "0.0.0.0:5000"]

