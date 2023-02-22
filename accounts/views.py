from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):

    def post(self, request, *args, **kwargs):
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        return super().post(request, *args, **kwargs)

            