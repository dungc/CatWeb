# config_default.py

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'password',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}

await
orm.create_pool(loop=loop, user="root", password="password", db="awesome")
