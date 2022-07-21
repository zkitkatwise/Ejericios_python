import urllib.request
from win10toast import ToastNotifier
webUrl  = urllib.request.urlopen('https://www.marca.com')
data = webUrl.read()
data=str(data)
valor = data.count("baloncesto")
toaster = ToastNotifier()
ToastNotifier().show_toast("Notificación Zkit","Se ha encontrado "+str(valor)+" veces")