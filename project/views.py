from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User
