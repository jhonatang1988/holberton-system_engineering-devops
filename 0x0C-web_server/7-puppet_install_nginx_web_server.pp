# updates and install nginx, then creates a index.html
exec { 'installnginx':
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; echo "Holberton School" | sudo tee /var/www/html/index.html; new_string="server_name _;\n\trewrite ^\/redirect_me http:\/\/104.196.19.203\/some_page.html permanent;"; sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default; sudo nginx -t; sudo service nginx restart',
  provider => shell,
}
