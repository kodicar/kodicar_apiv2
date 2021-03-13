# import jwt
# from django.conf import settings
# from rest_framework import authentication
# from users.models import Profile


# class JWTAuthentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         try:
#             token = request.META.get("HTTP_AUTHORIZATION")
#             if token is None:
#                 return None
#             xjwt, jwt_token = token.split(" ")
#             decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
#             pk = decoded.get("pk")
#             profile = Profile.objects.get(pk=pk)
#             return (profile, None)
#         except (ValueError, jwt.exceptions.DecodeError, Profile.DoesNotExist):
#             return None
