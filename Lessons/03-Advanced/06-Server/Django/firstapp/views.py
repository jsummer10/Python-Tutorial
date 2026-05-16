from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import UserData


# def user_view(request):
#     """ First "Hello World" view to view. 
#         testLaunch via http://127.0.0.1:8000/home/ 
#     """
#     return HttpResponse("Hello world!")


def main(request):
    """ Landing page for the application """
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def user_view(request):
    """ View to display all users in the database """

    userdata = UserData.objects.all().values()
    template = loader.get_template('users.html')

    context = {
        'userdata': userdata,
    }

    return HttpResponse(template.render(context, request))


def detailed_user_view(request, id):
    """ View to display a single user's details """

    userdata = UserData.objects.get(id=id)
    template = loader.get_template('userdetails.html')

    context = {
        'userdata': userdata,
    }

    return HttpResponse(template.render(context, request))
