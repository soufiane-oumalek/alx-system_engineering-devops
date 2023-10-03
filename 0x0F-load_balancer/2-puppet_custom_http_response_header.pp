# configures a brand new Ubuntu machine
class { 'nginx':
  package_manage => false,
  service_manage => false,
}

package { 'nginx':
  ensure => 'installed',
  require => Class['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('module/nginx_default.erb'),
  require => Package['nginx'],
}

file_line { 'add_custom_header':
  path    => '/etc/nginx/nginx.conf',
  line    => '    add_header X-Served-By $hostname;',
  before  => Exec['restart_nginx'],
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  refreshonly => true,
  subscribe => File_line['add_custom_header'],
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => Package['nginx'],
}

