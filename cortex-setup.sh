#!/bin/bash
git clone https://github.com/jrabinovitz-ideal/cortex.git /opt/
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-9.0.0-x86_64.rpm
sudo rpm -vi filebeat-9.0.0-x86_64.rpm
mv /opt/filebeat.yml /etc/filebeat/
(crontab -l 2>/dev/null || true; echo "5 * * * * /usr/bin/python3 /opt/fetch-cortex-alerts.py") | crontab -
systemctl enable filebeat
systemctl start filebeat
