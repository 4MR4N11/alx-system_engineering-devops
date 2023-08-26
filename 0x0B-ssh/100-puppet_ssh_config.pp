#  set up client SSH configuration file
file { '/home/amrani/.ssh/config':
  ensure => present,
  content => "
  Host 34.227.89.39
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
  ",
}
