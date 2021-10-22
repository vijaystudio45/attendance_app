from django.shortcuts import redirect
from django.conf import settings

def auth_middleware(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        if not request.session.get('user_id'):
            return redirect(settings.SITE_URL)
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
    return  middleware
