import requests
from pathlib import Path

import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')
env = environ.Env()

headers = {
    'Authorization': f'token {env("GITHUB_TOKEN")}',
    'X-GitHub-Api-Version': '2022-11-28'
}
try:
    response = requests.get('https://api.github.com/repos/ILoveBacteria/toolbox/tags', headers=headers)
    VERSION = response.json()[0]['name']
except:
    VERSION = 'latest'
