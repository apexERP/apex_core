from django.urls import path


from .views import landing_page

app_name = 'apps.landing'



urlpatterns = [
    path("", landing_page, name="landing_page"),
]

