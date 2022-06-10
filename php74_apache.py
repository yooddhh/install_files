import os

# SSL crt , key file copy
os.system('cp /ssh/kirbs.crt /etc/pki/tls/certs/')
os.system('cp /ssh/kirbs.key /etc/pki/tls/private/')

os.system('yum update -y')


os.system('yum update -y')
os.system('yum install wget -y')
os.system('rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm')
os.system('yum install -y epel-release')
os.system('yum install -y libnghttp2 libnghttp2-devel')


os.system('mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.back')

repo ="# CentOS-Base.repo"
repo +="\n#"
repo +="\n# The mirror system uses the connecting IP address of the client and the"
repo +="\n# update status of each mirror to pick mirrors that are updated to and"
repo +="\n# geographically close to the client.  You should use this for CentOS updates"
repo +="\n# unless you are manually picking other mirrors."
repo +="\n#"
repo +="\n# If the mirrorlist= does not work for you, as a fall back you can try the"
repo +="\n# remarked out baseurl= line instead." 
repo +="\n#"
repo +="\n#"
repo +="\n"
repo +="\n[base]"
repo +="\nname=CentOS-\$releasever - Base"
repo +="\n#mirrorlist=http://mirrorlist.centos.org/?release=\$releasever&arch=\$basearch&repo=os&infra=\$infra"
repo +="\n#baseurl=http://mirror.centos.org/centos/\$releasever/os/\$basearch/"
repo +="\nbaseurl=http://mirror.kakao.com/centos/\$releasever/os/\$basearch/"
repo +="\ngpgcheck=1"
repo +="\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7"
repo +="\n"
repo +="\n#released updates"
repo +="\n[updates]"
repo +="\nname=CentOS-\$releasever - Updates"
repo +="\n#mirrorlist=http://mirrorlist.centos.org/?release=\$releasever&arch=\$basearch&repo=updates&infra=\$infra"
repo +="\n#baseurl=http://mirror.centos.org/centos/\$releasever/updates/\$basearch/"
repo +="\nbaseurl=http://mirror.kakao.com/centos/\$releasever/updates/\$basearch"
repo +="\ngpgcheck=1"
repo +="\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7"
repo +="\n"
repo +="\n#additional packages that may be useful"
repo +="\n[extras]"
repo +="\nname=CentOS-\$releasever - Extras"
repo +="\n#mirrorlist=http://mirrorlist.centos.org/?release=\$releasever&arch=\$basearch&repo=extras&infra=\$infra"
repo +="\n#baseurl=http://mirror.centos.org/centos/\$releasever/extras/\$basearch/"
repo +="\nbaseurl=http://mirror.kakao.com/centos/\$releasever/extras/\$basearch"
repo +="\ngpgcheck=1"
repo +="\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7"
repo +="\n"
repo +="\n#additional packages that extend functionality of existing packages"
repo +="\n[centosplus]"
repo +="\nname=CentOS-\$releasever - Plus"
repo +="\n#mirrorlist=http://mirrorlist.centos.org/?release=\$releasever&arch=\$basearch&repo=centosplus&infra=\$infra"
repo +="\n#baseurl=http://mirror.centos.org/centos/\$releasever/centosplus/\$basearch/"
repo +="\nbaseurl=http://mirror.kakao.com/centos/\$releasever/centosplus/\$basearch"
repo +="\ngpgcheck=1"
repo +="\nenabled=0"
repo +="\ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7"

os.system('echo "'+repo+'" > /etc/yum.repos.d/CentOS-Base.repo')

os.system('yum install -y openssl openssl-devel')

 
os.system('yum install httpd -y')

os.system('yum install mod_ssl -y')

http_10_h2 = "LoadModule http2_module modules/mod_http2.so"
http_10_h2 += "\n\t<IfModule http2_module>"
http_10_h2 += "\n\t\t\t\t\tProtocolsHonorOrder On"
http_10_h2 += "\n\t\t\t\t\tProtocols h2 h2c http/1.1"
http_10_h2 += "\n\t</IfModule>"

os.system('echo "'+http_10_h2+'" > /etc/httpd/conf.modules.d/10-h2.conf')
os.system('systemctl start httpd')
os.system('echo "<html> a html </html>" > /var/www/html/a.html')
os.system('curl localhost/a.html')


# -----------Not required in docker environment-------------
os.system('firewall-cmd --permanent --zone=public --add-service=http')
os.system('firewall-cmd --permanent --zone=public --add-service=https')
os.system('firewall-cmd --reload')
os.system('firewall-cmd --list-all')

os.system('yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y')
os.system('yum repolist')
os.system('yum install yum-utils -y')
os.system('yum-config-manager --enable remi-php74')
os.system('yum install php -y')

os.system('systemctl restart httpd')
os.system('echo "<?php phpinfo(); ?>" > /var/www/html/info.php')
os.system('curl localhost/info.php')

# -----------Enter key -------------
os.system('make -C /etc/pki/tls/certs certreq')


os.system("sed -i 's/SSLCertificateFile\ \/etc\/pki\/tls\/certs\/localhost.crt/SSLCertificateFile\ \/etc\/pki\/tls\/certs\/kirbs.crt/g' /etc/httpd/conf.d/ssl.conf")
os.system("sed -i 's/SSLCertificateKeyFile\ \/etc\/pki\/tls\/private\/localhost.key/SSLCertificateKeyFile\ \/etc\/pki\/tls\/private\/kirbs.key/g' /etc/httpd/conf.d/ssl.conf")

os.system("sed -i 's/short_open_tag\ =\ Off/short_open_tag\ =\ On/g' /etc/php.ini")
os.system("sed -i 's/;date.timezone\ =/date.timezone\ =\ Asia\/Seoul/g' /etc/php.ini")

os.system('yum install php-mysqli -y')
os.system('yum install php-mbstring -y')
os.system('yum install php-bcmath -y')

# for codeigniter 4
# os.system('yum install php-intl -y') 

os.system('touch /var/www/html/index.html')

httpd_conf_add = "TimeOut 2000"
httpd_conf_add += "\n"
httpd_conf_add += "KeepAliveTimeout 2"
os.system('echo "'+httpd_conf_add+'" >> /etc/httpd/conf/httpd.conf')

os.system("sed -i 's/AllowOverride\ None/AllowOverride\ All/g' /etc/httpd/conf/httpd.conf")

os.system("sed -i 's/max_execution_time\ =\ 30/max_execution_time\ =\ 10000/g' /etc/php.ini")
os.system("sed -i 's/;max_input_vars\ =\ 1000/max_input_vars\ =\ 5000/g' /etc/php.ini")
os.system("sed -i 's/memory_limit\ =\ 128M/memory_limit\ =\ 1024M/g' /etc/php.ini")

os.system("systemctl restart httpd")