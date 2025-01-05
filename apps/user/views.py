from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from dj_rest_auth.views import LoginView

class CustomLoginView(LoginView):
    @swagger_auto_schema(
        operation_description="Login using email and password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['email', 'password']
        ),
        responses={200: 'Token'},
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)