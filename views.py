from django.shortcuts import render_to_response

def home(request):
    parameters = []
    return render_to_response('index.html', {'parameters': parameters,})
