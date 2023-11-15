# change limit on holberton user
exec { 'fix-limit':
  command => "bash -c \"sed -iE 's/^holberton hard nofile 5/holberton hard nofile 8192/' /etc/security/limits.conf; \
              sed -iE 's/^holberton soft nofile 4/holberton soft nofile 4096/' /etc/security/limits.conf\"",
  path    => [
    '/usr/bin',
    '/usr/sbin',
    '/bin',
  ],
}
