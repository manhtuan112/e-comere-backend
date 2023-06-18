from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from user_register.views import UserRegister, UserLogin, get_user_profile, update_user_profile, change_password, forget_password

urlpatterns = [
    path('auth/signup/', UserRegister, name="register"),
    path('auth/login/', UserLogin, name="login"),
    # path('auth/login_with_google/', UserRegisterWithGoogleAndGoogle,
    #      name="resgister_with_google_and_facebook"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/logout/', logout, name="logout"),
    path('profile/', get_user_profile, name="get_user_profile"),
    path('update/', update_user_profile, name="update_user_profile"),
    path('change_password/', change_password, name='change_pasword'),
    path('forget_password/', forget_password, name='forget_pasword')


]
