# updates and install nginx, then creates a index.html
exec { 'installnginxwithcustomheader':
  environment => ["ahostname=${hostname}"]
  command     => 'sudo apt update ; sudo apt -y install nginx ; echo "Holberton School" | sudo tee /var/www/html/index.html; sudo sed -i "s/sendfile on;/sendfile on;\n\tadd_header X-Served-By $ahostname;/" /etc/nginx/nginx.conf'; sudo service nginx restart',
  provider    => shell,
}
