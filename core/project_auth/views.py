from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    return HttpResponse("home page permissions")


class CustomUserCreateView(CreateView):
    model = CustomUser
    fields = '__all__'
    success_url = reverse_lazy('my_app:home')


# def register(request):    # causing problems
#     if request.method == "POST":
#         form = RegisterForm()
#         if form.is_valid():
#             print("form is valid ")
#             form.save()
#     else:
#         form = RegisterForm()
#     return render(request, "project_auth/register.html", {'form': form})


# @api_view(['POST'])
# def create_teacher(request):
#     # 'id', 'name', 'subject', 'email', 'password'
#     user_name = request.data['name']
#     subject = request.data['subject']
#     email = request.data['email']
#     password = request.data['password']
#     teacher = Teacher(name=user_name, subject=subject, email=email, password=password)
#     teacher.save()
#     return Response({"success": "teacher created successfully"})
