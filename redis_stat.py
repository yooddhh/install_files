import os
import subprocess
# import time

os.system('gpg2 --keyserver hkp://keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB')
os.system('yum install which -y')

os.system('yum install curl -y')
# -k option : ssl verify off
os.system('curl -k -sSL https://get.rvm.io | bash -s stable')

subprocess.Popen("source /etc/profile.d/rvm.sh", shell=True, executable="/bin/bash")

os.system('rvm reload')
os.system('rvm requirements run')
os.system('rvm install ruby-2.4.4')
os.system('ruby --version')
os.system('gem install redis-stat')
# os.system('redis-stat --server --daemon online_was_1:6379 online_was_2:6379')