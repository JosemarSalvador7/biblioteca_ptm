# codigo do mysql

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_da_sua_base',
        'USER': 'josemar',
        'PASSWORD': '1mp3rad0r',
        'HOST': 'localhost',
        'PORT': '',               # deixe vazio para usar o socket (mais rápido)
        'OPTIONS': {
            'unix_socket': '/run/mysqld/mysqld.sock',  # Confirme o caminho com SHOW VARIABLES LIKE 'socket';
        },
    }
}

## instalacao

uv add pymysql




MVT 

m - models 
v - views 
t - templates 