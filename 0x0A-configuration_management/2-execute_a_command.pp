# killing a process named `killmenow`
exec { 'kill_killmenow':
  command => '/bin/pkill killmenow',
}
