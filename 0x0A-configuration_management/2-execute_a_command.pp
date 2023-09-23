# create a manifest that kills a process
exec {
  'pkill':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/sbin', '/bin']
}
