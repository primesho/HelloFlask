import configparser

cfg = configparser.ConfigParser()
cfg['uwsgi'] = {
    'module': "wsgi:app",
    "master": "true",
    "processes": "5",
    "socket": "myproject.sock",
    "chmod-socket": "600",
    "vacuum": "true",
    "die-on-term": "true"
}
with open('config.ini', 'w') as config_file:
    cfg.write(config_file)