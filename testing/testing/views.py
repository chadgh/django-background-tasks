from django.http import HttpResponse
from .tasks import test


def main(request):
    test()
    return HttpResponse("it's finished")
