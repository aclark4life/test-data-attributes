from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.core import serializers



class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User

    # https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/#adding-extra-context
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        fields = self.object._meta.get_fields()
        context["fields"] = fields
        
        return context
