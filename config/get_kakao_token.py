import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '0107bf036e243e3d75e066880f3b4d2f'
redirect_uri = 'https://example.com/oauth'
authorize_code = '9Nc7laIiumWgI1ASZDQwupcJKtOQlRF3dQOreb3MiVYjNlb9eqyxIAAAAAQKPXUbAAABkC3z8TjC3p98Pd5TpQ'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)