from datetime import timedelta
from django.utils.timezone import now

class UpdateSessionExpiryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Reset session expiry to 30 minutes from now
            request.session.set_expiry(30 * 60)  # 30 minutes in seconds

        return response
