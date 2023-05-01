import requests
import json
from twilio.rest import Client


with open("twilio.json")  as f:
  twilio = json.load(f)
#accond_sid ve auth_token'u mycrendentials.json dosyasından çekiyoruz 
account_sid = twilio["account_sid"]
auth_token = twilio["auth_token"]
client = Client(account_sid, auth_token)
api = twilio["weather_api"]


sehir = "ankara"
adres = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=tr".format(sehir,api)
baglan = requests.get(adres)
sorgu = baglan.json()


hava_durumu = sorgu["weather"][0]["description"]
main = sorgu["main"]
sicaklik = main["temp"]
hissedilen_sicaklik = main["feels_like"]
min_sicaklik = main["temp_min"]
max_sicaklik = main["temp_max"]
basinc = main["pressure"]
nem = main["humidity"]


whatsapp_mesaj = f"{sehir} için hava durumu: {hava_durumu}\nsıcaklık:{sicaklik} °\nhissedilen sıcaklık:{hissedilen_sicaklik} °\nmin sıcaklık: {min_sicaklik} °\nmax sıcaklık: {max_sicaklik} °\nnem oranı:{nem}\nbasınç:{basinc}"

print(whatsapp_mesaj)

message = client.messages.create(
from_='whatsapp:+14155238886',
body=whatsapp_mesaj,
to='whatsapp:'+twilio["numara"]
)

    