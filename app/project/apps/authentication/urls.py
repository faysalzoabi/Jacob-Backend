from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # get a new GWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  # get a new GWT with refresh Token
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),

]
