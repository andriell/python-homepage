import datetime


def date_now(request):
    return {'now': datetime.datetime.now()}
