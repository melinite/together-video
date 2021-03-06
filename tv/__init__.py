from flask import Flask
from redis import Redis

app = Flask(__name__)
app.config.update(
    CSRF_ENABLED = True,
    DEBUG = True,
    SECRET_KEY = 'development key',
    REQUIRE_AUTH = False,
    BACKEND = 'redis',
    REDIS = {
        'host': 'localhost',
        'port': 6379,
        'password': None,
        'db': 0
    },
    AUTH_BACKEND = 'openid',
    OPENID_FORCED_PROVIDER = 'https://www.google.com/accounts/o8/id',
    OPENID_PROVIDERS = {
        'google': 'https://www.google.com/accounts/o8/id'
    },
)
app.config.from_envvar('TV_SETTINGS', silent=True)

# Needed for the models and will hopefully be usable for
# the factory below later.
redis = Redis(**app.config['REDIS'])

import tv.auth
import tv.routes

if __name__ == '__main__':
    app.run()
