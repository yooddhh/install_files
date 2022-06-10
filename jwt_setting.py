# yum install git -y
import os
os.system('curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer;')
os.system('mkdir /var/www/html/jwt_lib')
os.system('cd /var/www/html/jwt_lib && composer require firebase/php-jwt')

# jwt_php = "include_once('./vendor/autoload.php');"
# jwt_php += "\nuse Firebase\JWT\JWT;"
# jwt_php += "\nclass Jwt_session{"
# jwt_php += "\n\tprivate $SECRET_KEY = 'kirbsKIRBS1968';"
# jwt_php += "\n\tpublic function getJwtToken($data){"
# jwt_php += "\n\t\treturn JWT::encode($data , $this->SECRET_KEY);"
# jwt_php += "\n\t}"
# jwt_php += "\n\tpublic function getDecodeData($token){"
# jwt_php += "\n\t\t$return_data = NULL;"
# jwt_php += "\n\t\ttry{"
# jwt_php += "\n\t\t\t$return_data = JWT::decode($token , $this->SECRET_KEY , array('HS256'));"
# jwt_php += "\n\t\t}catch(Exception $e){"
# jwt_php += "\n\t\t\t$return_data = FALSE;"
# jwt_php += "\n\t\t}"