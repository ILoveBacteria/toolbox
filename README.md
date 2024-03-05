# Toolbox

[![License: MIT](https://img.shields.io/github/license/ILoveBacteria/toolbox)](https://github.com/ILoveBacteria/toolbox/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/ILoveBacteria/toolbox)](https://github.com/ILoveBacteria/toolbox/issues)
[![Last commit](https://img.shields.io/github/last-commit/ILoveBacteria/toolbox)](https://github.com/ILoveBacteria/toolbox/commits/master)
![GitHub tag](https://img.shields.io/github/v/tag/ILoveBacteria/toolbox?color=lightblue&label=last+tag)
![GitHub repo size](https://img.shields.io/github/repo-size/ILoveBacteria/toolbox)
![Docker Image Size](https://img.shields.io/docker/image-size/ilovebacteria/toolbox?logo=docker&logoColor=white&cacheSeconds=60)
![Website](https://img.shields.io/website?url=https%3A%2F%2Ftoolbox.moeinarabi.ir&label=server%20status&cacheSeconds=120&link=https%3A%2F%2Ftoolbox.moeinarabi.ir)

## Description

This repo contains a collection of tools that I have developed for my own convenience. 
They are based on the Django framework and various Python libraries.

The repo is deployed on _Liara_ platform, but it may not be always accessible because I switch it off to save costs.

The tools are made to my specific needs, so they may **not** be very useful for others. 
However, feel free to browse and give feedback.

## How to run

### Docker

Link to Docker [repository](https://hub.docker.com/r/ilovebacteria/toolbox)

```shell
docker pull ilovebacteria/toolbox:latest
docker-compose up
```

### Python

1. Make sure you have Python `3.10` installed.
2. Get the latest version of the app from [release](https://github.com/ILoveBacteria/toolbox/releases) page.
3. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```
4. Config environment variables. The `.env.sample` file contains environment variables that should
be set in your system.
This Django app uses the `celery` library, and we use **redis** as message broker for `celery`.

5. Run Django server
    ```shell
    python manage.py runserver
    ```

## Tools

- Download **Youtube** videos and playlists.
- Save and remind computer engineering course **terms**.
- My **Footprint** in different sites and articles about programming!
- **Notes** about different topics.
- Host my personal [**website**](https://moeinarabi.ir).
- ...


