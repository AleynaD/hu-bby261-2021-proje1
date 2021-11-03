import urllib.request
from bs4 import BeautifulSoup
f=open("Site_data.txt","w")
k=open("Site_adi.txt","w")
while(True):
  siteAdi=input("Adres giriniz : ")
  k.write(siteAdi+"\n")
  sonuc=input("Site adresi girişine devam etmek istiyor musunuz? (E/H).")
  if sonuc=="E":
    continue
  if sonuc=="H":
    k.close()
    k=open("Site_adi.txt","r")
    for i in k.readlines():
      k=open("Site_data.txt","a")
      webSite = urllib.request.urlopen(i)
      getBytes = webSite.read()
      webPage = getBytes.decode("utf8")
      webSite.close()
      soup = BeautifulSoup(webPage, 'html.parser')
      f.write(i.strip()+" | "+str(soup.title.contents)[2:-2]+"\n")   
    break
f.close()
f=open("Site_data.txt","r")
#eğer çıktımızı görmek istiyorsak bu kodu aktif etmeliyiz
#for i in f.readlines():
#  print(i)
