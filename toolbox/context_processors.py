from . import version


def server_version(request):
    return {'version': version}
