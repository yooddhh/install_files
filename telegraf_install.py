import os
os.system('wget https://dl.influxdata.com/telegraf/releases/telegraf-1.20.4-1.x86_64.rpm')
os.system('yum localinstall telegraf-1.20.4-1.x86_64.rpm -y')
os.system('systemctl start telegraf')