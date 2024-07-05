from django.urls import path
from auth_app import views as auth_views  # Import views from the auth_app and
#  alias them as auth_views

# Define URL patterns for the application
urlpatterns = [
    # URL pattern for the index page, which does not require authentication.
    path('', auth_views.index, name='index'),
    # URL pattern for the user registration page
    path('register/', auth_views.register, name='register'),
    # URL pattern for the user login page
    path('login/', auth_views.login_view, name='login'),
    # URL pattern for the user logout
    path('logout/', auth_views.logout_view, name='logout'),
    # URL pattern for a protected page that requires authentication
    path('protected/', auth_views.protected_view, name='protected'),
]