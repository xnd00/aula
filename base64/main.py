# Importando biblioteca para decodificaçãod e base64
from base64 import b64decode, b64encode

# Código codificado em base 64
b64 = 'JVBERi0xLjQKJdP0zOEKJSBQREZzaGFycCBWZXJzaW9uIDEuMzIuMjYwOC4wICh2ZXJib3NlIG1vZGUpCiUgQ3JlYXRpb24gZGF0ZTogMjUvMDgvMjAyMyAyMDo0NjoyNCAgICAgICAgICAgICAKJSBDcmVhdGlvbiB0aW1lOiAwLjAwMCBzZWNvbmRzICAgICAgICAgICAgICAgICAgIAolIEZpbGUgc2l6ZTogNDQ5NiBieXRlcyAgICAgICAgICAgICAgICAgICAgICAgICAgCiUgUGFnZXM6IDEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKJSBPYmplY3RzOiA3ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAolLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KMSAwIG9iaiAgICUgUGRmU2hhcnAuUGRmLlBkZkRvY3VtZW50SW5mb3JtYXRpb24KPDwKICAvQ3JlYXRpb25EYXRlIChEOjIwMjMwODI1MjA0NjI0KzAwJzAwJykKICAvQ3JlYXRvciAoUERGc2hhcnAgMS4zMi4yNjA4LWcgXCh3d3cucGRmc2hhcnAubmV0XCkpCiAgL1Byb2R1Y2VyIChQREZzaGFycCAxLjMyLjI2MDgtZyBcKHd3dy5wZGZzaGFycC5uZXRcKSkKPj4KZW5kb2JqCiUtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoyIDAgb2JqICAgJSBQZGZTaGFycC5QZGYuQWR2YW5jZWQuUGRmQ2F0YWxvZwo8PAogIC9QYWdlcyAzIDAgUgogIC9UeXBlIC9DYXRhbG9nCj4+CmVuZG9iagolLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t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W93D3XtYRcUeN+Bpvl+9y99XJH8CdryTLwplbmRzdHJlYW0KZW5kb2JqCiUtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQo3IDAgb2JqICAgJSBQZGZTaGFycC5QZGYuUGRmUGFnZQo8PAogIC9Db250ZW50cyA2IDAgUgogIC9Hcm91cAogIDw8CiAgICAvQ1MgL0RldmljZVJHQgogICAgL0kgZmFsc2UKICAgIC9LIGZhbHNlCiAgICAvUyAvVHJhbnNwYXJlbmN5CiAgPj4KICAvTWVkaWFCb3ggWzAgMCA1OTUgODQyXQogIC9QYXJlbnQgMyAwIFIKICAvUmVzb3VyY2VzCiAgPDwKICAgIC9Gb250CiAgICA8PAogICAgICAvRjEgNSAwIFIKICAgICAgL0YyIDQgMCBSCiAgICA+PgogICAgL1Byb2NTZXQgWy9QREYgL1RleHQgL0ltYWdlQiAvSW1hZ2VDIC9JbWFnZUldCiAgPj4KICAvVHlwZSAvUGFnZQo+PgplbmRvYmoKJS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCnhyZWYKMCA4CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDQxMSAwMDAwMCBuIAowMDAwMDAwNzI1IDAwMDAwIG4gCjAwMDAwMDA5MTUgMDAwMDAgbiAKMDAwMDAwMTEwNCAwMDAwMCBuIAowMDAwMDAxMzQ1IDAwMDAwIG4gCjAwMDAwMDE1ODEgMDAwMDAgbiAKMDAwMDAwMzc0MyAwMDAwMCBuIAp0cmFpbGVyCjw8CiAgL0lEIFs8Mzc3RERDRDM3QkYwNTA0RkI3OTFBRkJGNjU2OEEzQzk+PDM3N0REQ0QzN0JGMDUwNEZCNzkxQUZCRjY1NjhBM0M5Pl0KICAvSW5mbyAxIDAgUgogIC9Sb290IDIgMCBSCiAgL1NpemUgOAo+PgpzdGFydHhyZWYKNDE3NwolJUVPRgo='

# Decodificando base 64
bytes = b64decode(b64, validate=True)

# Verificando se o resultado é um arquivo PDF
if bytes[0:4] != b'%PDF':
  raise ValueError('O resultado não é um arquivo PDF, operação abortada!')

# Criar arquivo
f = open('./aula/base64/file.pdf', 'wb')
f.write(bytes)
f.close()


teste = b"Criptografando em base 64"
rcod = b64encode(teste)
print(f'REsultado: {rcod}')

print(b64decode(rcod))
