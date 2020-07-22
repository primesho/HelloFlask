#systemd の用意
//config.pyの実行でiniファイルの生成
```ini
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = myproject.sock#ここは<自分のサービス>.sockになるように
chmod-socket = 660
vacuum = true

die-on-term = true
```

//:/etc/systemd/system/myproject.service
※etc/systemd/system/<自分のサービス>.service
```ini
[Unit]
Description=uWSGI instance to serve myproject
After=network.target

[Service]
User=uchida
Group=www-data
WorkingDirectory=/home/ubuntu/myproject
Environment="PATH=/home/ubuntu/myproject/myprojectenv/bin"
ExecStart=/home/ubuntu/myproject/myprojectenv/bin/uwsgi --ini config.ini

[Install]
WantedBy=multi-user.target
```

#サービス起動
```commandline
sudo systemctl start myproject
sudo systemctl enable myproject
```

#Nginxの設定
```metadata json
server {
    listen 80;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/uchida/myproject/myproject.sock;
    }
}
```
移動と削除
```commandline
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo rm -f /etc/nginx/sites-enabled/default
```
Nginxがただしいのかチェック
```commandline
sudo nginx -t
```
Nginxの再起動
```commandline
sudo systemctl restart nginx
```

