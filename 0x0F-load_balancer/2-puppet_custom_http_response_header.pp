# configures a brand new Ubuntu machine
class { 'nginx':
  package_manage => true,
  service_manage => true,
}

file { '/etc/nginx/sites-available/default':
  ensure => 'file',
  content => template('module/nginx_default.erb'),
  require => Package['nginx'],
}

file_line { 'add_custom_header':
  path    => '/etc/nginx/nginx.conf',
  line    => '    add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File_line['add_custom_header']],
}

