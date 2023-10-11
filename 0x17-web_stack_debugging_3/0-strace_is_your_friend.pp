# fix wordpress on site running apache2

exec { 'fixWordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin:/usr/bin:/usr/local/bin'
}
