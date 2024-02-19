from toolbox.settings import VERSION


def server_version(request):
    return {'version': VERSION}
