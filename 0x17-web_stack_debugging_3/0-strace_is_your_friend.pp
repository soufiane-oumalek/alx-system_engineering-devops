#find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet

exec {'replace_the_line':
  provider => shell,
  command  => 'sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
