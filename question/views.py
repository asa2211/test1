from django.http import HttpResponse


def detail(request):
    return HttpResponse("You're looking at question %s.")


def results(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)


def votes(request):
    return HttpResponse("You're voting on question %s.")
