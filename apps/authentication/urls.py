# -*- encoding: utf-8 -*-

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from monkoo_calendar.views import loggedUser, recomendacionJapon, recomendacionParis, recomendacionVietnam, send_events

urlpatterns = [
    path('login', login_view, name="login"),
    path('register', register_user, name="register"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('calendar', send_events, name='calendar'),
    path('recomendacionParis', recomendacionParis, name='recomendacionParis'),
    path('recomendacionJapon', recomendacionJapon, name='recomendacionJapon'),
    path('recomendacionVietnam', recomendacionVietnam, name='recomendacionVietnam'),
    path('navigation', loggedUser),
]
