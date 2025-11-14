import requests

from social_core.backends.oauth import BaseOAuth2

from django.conf import settings


class Auth0(BaseOAuth2):
	"""Auth0 OAuth authentication backend."""

	name = "auth0"
	SCOPE_SEPARATOR = " "
	ACCESS_TOKEN_METHOD = "POST"
	EXTRA_DATA = [("picture", "picture")]

	def authorization_url(self):
		"""Return the authorization endpoint."""
		return "https://" + self.setting("DOMAIN") + "/authorize"

	def access_token_url(self):
		"""Return the token endpoint."""
		return "https://" + self.setting("DOMAIN") + "/oauth/token"

	def get_user_id(self, details, response):
		"""Return current user id."""
		return details.get("user_id")

	def get_user_details(self, response):
		"""Fetch userinfo from Auth0 and return a dict of user details."""
		url = "https://" + self.setting("DOMAIN") + "/userinfo"
		headers = {"authorization": "Bearer " + response.get("access_token", "")}
		resp = requests.get(url, headers=headers)
		resp.raise_for_status()
		userinfo = resp.json()

		return {
			"username": userinfo.get("nickname"),
			"first_name": userinfo.get("name"),
			"picture": userinfo.get("picture"),
			"user_id": userinfo.get("sub"),
		}

def getRole(request):
    user = request.user
    auth0user = user.social_auth.filter(provider="auth0")[0]
    accessToken = auth0user.extra_data['access_token']
    url = 'https://' + settings.SOCIAL_AUTH_AUTH0_DOMAIN + '/userinfo'
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo[f"{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/role"]
    return (role)

# def get_role(request):
# 	"""
# 	Helper to get the role claim from the Auth0 userinfo endpoint for the current user.

# 	Returns the role value or None if not available.
# 	"""
# 	user = getattr(request, "user", None)
# 	if not user or not getattr(user, "is_authenticated", False):
# 		return None

# 	try:
# 		auth0user = user.social_auth.filter(provider="auth0").first()
# 		if not auth0user:
# 			return None
# 		access_token = auth0user.extra_data.get("access_token")
# 		if not access_token:
# 			return None

# 		url = "https://" + settings.SOCIAL_AUTH_AUTH0_DOMAIN + "/userinfo"
# 		headers = {"authorization": "Bearer " + access_token}
# 		resp = requests.get(url, headers=headers)
# 		resp.raise_for_status()
# 		userinfo = resp.json()
# 		role = userinfo.get(f"{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/role")
# 		return role
# 	except Exception:
# 		return None