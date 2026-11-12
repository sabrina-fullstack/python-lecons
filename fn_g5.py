def connect(host,* , port=80, secure=False):
    return f"{host}:{port} secure={secure}"

print(connect("site.com"))
print(connect("site.com", port=443, secure=True))
try:
    connect("site.com", 443)
except TypeError as e:
    print("Erreur :", e)