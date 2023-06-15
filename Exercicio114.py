import urllib
import urllib.request

try:
    sit = urllib.request.urlopen('http://google.com')
except urllib.error.URLError:
    print('Inacessivel')
else:
    print('Consegui acessar')