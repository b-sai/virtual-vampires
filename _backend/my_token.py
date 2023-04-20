import rest_framework.authtoken.models as m

token = m.Token.objects.create(user="admin")
print(token.key)