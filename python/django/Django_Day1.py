import urllib.request
print(urllib.request.urlopen("").read().decode('utf-8'))