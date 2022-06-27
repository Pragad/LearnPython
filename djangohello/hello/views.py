from django.http import HttpResponse

from hello.clients.github_client import GithubClient


# RUN THE SERVICE USING 
#       python manage.py runserver
# RUN TESTS USING
#       ./manage.py test
# Create your views here.
def home(request):
    print("Hello from Django")

    github_client = GithubClient()
    url = github_client.get_git_url("pragad")
    print("URL: ", url)

    return HttpResponse("Hello Django!")
