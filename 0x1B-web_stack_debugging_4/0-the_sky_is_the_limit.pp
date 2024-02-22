# Increase the request's limit

# Increase ulimit value
exec { 'fix-config-nginx':
  # Check if the Nginx configuration file exists before proceeding
  onlyif  => 'test -e /etc/default/nginx',
  # Use sed to replace the value at line 5 with the current ulimit value
  command => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx',
  # Set the command search path to include necessary directories
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

# Restart Nginx service
exec { 'nginx-restart':
  # Command to restart the Nginx service
  command => 'nginx restart',
  # Set the command search path to include the directory where the Nginx service script is located
  path    => '/etc/init.d/'
}
