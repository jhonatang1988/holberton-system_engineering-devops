# use exec to terminate a process using pkill and puppet
exec { 'killmenow':
  command  => '/usr/bin/pkill -f killmenow',
}
