from django.http import JsonResponse

FRONTEND_TOKEN_HEADER = 'HTTP_X_FRONTEND_TOKEN'
EXPECTED_FRONTEND_TOKEN = 'develop'

class FrontendAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        frontend_token = request.META.get(FRONTEND_TOKEN_HEADER)
        print(frontend_token)
        if request.path in ['/api/sesion/login', '/api/sesion/register']:
            if frontend_token != EXPECTED_FRONTEND_TOKEN:
                return JsonResponse({'error': 'Unauthorized frontend'}, status=403)

        response = self.get_response(request)
        return response