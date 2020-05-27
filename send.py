import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkwNTE4NTQ5LCJqdGkiOiIwMzEzM2Q0ZWQwZjg0NDljODkwZjlkNGViMDhjYzlhNyIsInVzZXJfaWQiOjJ9.zk7RNCfE1eFaXKB95-4gOf1kr1SVTshSfXGB3SzQo_8'

r = requests.get('http://127.0.0.1:8000/api/paradigm/', headers=headers)

print(r.text)
