from django.urls import path
from userapp.api import event
from userapp.api import user
from django.views.decorators.csrf import csrf_exempt
from userapp.api.user import UserRegistrationView
from userapp.api.user import UserLoginView
from userapp.api.event import EventDetails
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/v1/events/', event.events, name='events'),

    path('api/v1/users/', user.register, name='register'),

    path('events/<str:userId>/', EventDetails.as_view()),

    path('api/v1/signup', UserRegistrationView.as_view()),

    path('api/v1/signin', UserLoginView.as_view()),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),

]