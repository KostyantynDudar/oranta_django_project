#!/bin/bash
echo "Stopping Gunicorn service..."
sudo systemctl stop oranta_django.service

echo "Killing all Gunicorn processes..."
sudo pkill -f gunicorn

echo "Checking for remaining Gunicorn processes..."
REMAINING=$(ps aux | grep gunicorn | grep -v grep | wc -l)
if [ "$REMAINING" -gt 0 ]; then
    echo "Found remaining processes, killing forcefully..."
    sudo pkill -9 -f gunicorn
fi

echo "Restarting Gunicorn service..."
sudo systemctl start oranta_django.service

echo "Reload complete. Checking service status..."
sudo systemctl status oranta_django.service
