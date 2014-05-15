from django.shortcuts import render_to_response

# Create your views here.
def hello_world(request):
  return render_to_response("hello_world.html", {"username": "Monty Python"})
