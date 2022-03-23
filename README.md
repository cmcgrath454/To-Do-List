LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so


<VirtualHost *:80>
    ServerAdmin cmcgrath454@gmail.com
    ServerName ec2-54-159-3-235.compute-1.amazonaws.com

    ProxyRequests Off
    ProxyPreserveHost On
    ProxyPass / http://localhost:8000/
    ProxyPassReverse / http://localhost:8000/

    <Directory /home/ubuntu/django/To-Do-List/todolist/>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
</VirtualHost>