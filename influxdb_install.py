import os
os.system('wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.0.4-linux-amd64.tar.gz')
os.system('tar xvzf influxdb2-2.0.4-linux-amd64.tar.gz')
os.system('cd influxdb2-2.0.4-linux-amd64 && ./influxd')