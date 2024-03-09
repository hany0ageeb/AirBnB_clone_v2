file { '/data':
  ensure => 'directory',
  path   => '/data/',
}
->file {'/data/web_static':
  ensure => 'directory',
  path   => '/data/web_static/',
}
->file {'/data/web_static/releases':
  ensure => 'directory',
  path   => '/data/web_static/releases/',
}
->file {'/data/web_static/shared/':
  ensure => 'directory',
  path   => '/data/web_static/shared/',
}
->file { '/data/web_static/releases/test':
  ensure => 'directory',
  path   => '/data/web_static/releases/test/',
}
->file {'/data/web_static/releases/test/index.html':
  ensure  => 'file',
  path    => '/data/web_static/releases/test/index.html',
  content => '<html><head><title>Title</title></head><body>Hello</body></html>'
}
->file {'/data/web_static/current':
  ensure => 'link',
  path   => '/data/web_static/current',
  target => '/data/web_static/releases/test/'
}
->exec { 'change ownership':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => ['/usr/bin', '/usr/sbin']
}
->file {'nginx config file':
  ensure  => 'file',
  path    => '/etc/nginx/sites-enabled/default',
  content => '
server {
	listen 80 default_server;
	listen [::]:80 default server;
	root /var/www/html;
	server_name _;
	location / {
		try_files $uri $uri/ =404;
	}
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
',
}
->exec{'restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin/', '/usr/sbin/'],
}
