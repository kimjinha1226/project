#!/bin/sh

echo "컨테이너 시작"
python /app/update.py
cron -f