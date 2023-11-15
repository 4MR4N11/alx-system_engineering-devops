# Fix nginx config for handling multiple requests
exec { 'fix-nginx':
  command => 'bash -c "sed -i \"s/ULIMIT=.*$/ULIMIT=\\\"-n 4096\\\"/\" /etc/default/nginx && service nginx restart"',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
}
