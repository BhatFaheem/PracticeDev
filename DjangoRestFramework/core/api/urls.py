from django.urls import path, include
from home import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"people", views.PeopleViewSet, basename="people")

urlpatterns = [
    path("", include(router.urls)),
    path("index/", views.index, name="index"),
    path("register/", views.RegisterAPI.as_view(), name="register"),
    path("person/", views.person, name="person"),
    path("login/", views.login, name="login"),
    path("persons/", views.PersonAPI.as_view(), name="persons"),
]
