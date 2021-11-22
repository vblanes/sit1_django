from django.shortcuts import render
from django.http import HttpResponse
import requests


def data_input(request):
    #  This will be the first screen to load
    # At first, this will only have a button to submit the case
    return render(request, 'base/simple_data_input.html')


def send_test_job(request):
    # TODO send the predefined JSON to the service
    # Use the response to call results and render the result page
    return HttpResponse("Aquí haréis cosas y luego mostraréis los resultados :)")


def results(request):
    pass
