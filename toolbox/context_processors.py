from .settings.base import VERSION


def server_version(request):
    return {'version': VERSION}
