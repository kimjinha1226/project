FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y cron

COPY update.py /app/update.py
COPY crontab /etc/cron.d/mycron

RUN pip install requests
RUN chmod 0644 /etc/cron.d/mycron
RUN crontab /etc/cron.d/mycron

CMD ["sh", "-c", "python /app/update.py && cron -f"]