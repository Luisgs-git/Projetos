import urllib
import urllib.request
try:
    site=urllib.request.urlopen('https://www.google.com')
except:
    print("Deu erro.")
else:
    print("Okay")
    print(site.read()) 