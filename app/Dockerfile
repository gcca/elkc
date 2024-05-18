FROM python:3.12.3-alpine3.19
RUN pip install --no-cache-dir Flask gunicorn python-logstash
WORKDIR /app
COPY . .
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
