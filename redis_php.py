import os


# PHP Redis install 
os.system('yum install php-redis -y')
os.system('systemctl restart httpd')

# Redis Server Install
os.system('yum install redis -y')
os.system('systemctl start redis')
os.system('systemctl enable redis')

#return : PONG
os.system('redis-cli ping')
