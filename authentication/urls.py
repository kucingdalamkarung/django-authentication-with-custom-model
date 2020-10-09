from django.urls import path, include
from django.conf.urls import url

from .views import dashboard, authentication


urlpatterns = [
    path('', dashboard.home, name="home"),
    path('accounts/', include(([
        path('login/', authentication.LoginView.as_view(), name="login"),
        path('register/', authentication.RegisterView.as_view(), name="register"),
        path('logout/', authentication.user_logout, name="logout"),
    ], 'authentication'), namespace='accounts'))
]
