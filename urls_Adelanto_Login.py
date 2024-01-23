from miapp.views import login_request

urlpatterns = [
    path("login/", login_request, name="login"),
]