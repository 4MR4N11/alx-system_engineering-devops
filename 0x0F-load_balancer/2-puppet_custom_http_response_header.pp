# This puppet manifest installs nginx and adds a custom header to the nginx.conf file
package { 'update':
  name   => 'update',
  ensure => 'latest',
}

package { 'nginx':
  ensure => 'installed',
  require => Package['update'],
}

$headername = "X-Served-By"
$headervalue = $trusted['hostname']

$line = "\\\tadd_header $headername \\\"$headervalue\\\";"

exec { 'add_header':
  command => "/bin/sed -i \"49i $line\" /etc/nginx/nginx.conf",
  unless  => "/bin/grep -q \"$line\" /etc/nginx/nginx.conf",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
