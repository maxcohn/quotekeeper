FROM python:3

COPY quotekeeper/ /app/quotekeeper/
COPY requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip3 install gunicorn

RUN pip3 install -r requirements.txt

CMD gunicorn -w 4 -b 0.0.0.0:8001 "quotekeeper:create_app()"
