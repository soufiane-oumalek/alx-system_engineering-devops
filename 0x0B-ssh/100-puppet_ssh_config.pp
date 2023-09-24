#changes to our configuration file
file_line { 'Change the main private key':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/school',
}

file_line { 'No Authenticate with passowrd':
  ensure => present,
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}
