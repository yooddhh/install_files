import os


## PHP rdkafka install 
# os.system('yum install gcc -y');
# os.system('yum install gcc-c++ -y');
# os.system('yum install git -y');
# os.system('cd /var/www/html && git clone --depth 1 --branch v0.11.1 https://github.com/edenhill/librdkafka.git')
# os.system('cd /var/www/html/librdkafka && ./configure')
# os.system('cd /var/www/html/librdkafka && make')
# os.system('cd /var/www/html/librdkafka && make install')
# os.system('yum install php-rdkafka -y')


## kafka Server Install
# os.system('yum install java-1.8.0-openjdk -y')
# os.system('java -version')
# os.system('mkdir /kafka')
# os.system('cd /kafka && wget https://mirrors.estointernet.in/apache/kafka/2.7.0/kafka_2.13-2.7.0.tgz')
# os.system('cd /kafka && tar -xzf kafka_2.13-2.7.0.tgz')
# os.system('cd /kafka && ln -s kafka_2.13-2.7.0 kafka')
# os.system('echo "export PATH=$PATH:/root/kafka_2.13-2.7.0/bin" >> ~/.bash_profile')
# os.system('source ~/.bash_profile')
# os.system('/kafka/kafka_2.13-2.7.0/bin/zookeeper-server-start.sh -daemon /kafka/kafka_2.13-2.7.0/config/zookeeper.properties')
# os.system('/kafka/kafka_2.13-2.7.0/bin/kafka-server-start.sh -daemon /kafka/kafka_2.13-2.7.0/config/server.properties')

## test topic create 
# os.system('/kafka/kafka_2.13-2.7.0/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test')
## test topic confirm
# os.system('/kafka/kafka_2.13-2.7.0/bin/kafka-topics.sh --zookeeper localhost:2181 --list')
## test topic message confirm
# os.system('/kafka/kafka_2.13-2.7.0/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning')

