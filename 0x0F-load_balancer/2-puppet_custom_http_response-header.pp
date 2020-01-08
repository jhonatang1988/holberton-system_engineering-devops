# updates and install nginx, then creates a index.html
exec { 'installnginxwithcustomheader':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx; sudo ufw allow 'Nginx HTTP'; echo "Holberton School" | sudo tee /var/www/html/index.html; new_string="server_name _;\n\trewrite ^\/redirect_me http:\/\/104.196.170.235\/some_page.html permanent;"; sudo sed -i "s/server_name _;/${new_string/" /etc/nginx/sites-available/default; echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html; string_404="server_name _;\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}"; sudo sed -i "s/server_name _;/${string_404/" /etc/nginx/sites-enabled/default; sudo nginx -t; sudo service nginx restart; xservedby_string="sendfile on;\n\tadd_header X-Served-By ${HOSTNAME;"; sudo sed -i "s/sendfile on;/${xservedby_string/" /etc/nginx/nginx.conf; sudo service nginx restart',
  provider => shell,
}
