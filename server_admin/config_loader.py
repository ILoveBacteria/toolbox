import tomli
import os


FILE1 = 'config.toml'
FILE2 = '/etc/django-server.toml'
config = None
if os.path.exists(FILE1):
    with open(FILE1, 'rb') as f:
        config = tomli.load(f)
elif os.path.exists(FILE2):
    with open(FILE2, 'rb') as f:
        config = tomli.load(f)