from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class LoginUsingEmailAsUsernameBackend(object):

  supports_object_permissions = False
  supports_anonymous_user = False
  supports_inactive_user = False

  def authenticate(self, email=None, password=None):
    try:
      # Check if the user exists in Django's database
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      return None

    # Check password of the user we found
    if check_password(password, user.password):
      return user
    return None

  # Required for the backend to work properly - unchanged in most scenarios
  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
