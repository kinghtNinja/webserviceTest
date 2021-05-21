import requests


class WebServiceData:

    def __init__(self):
        self.api_key="4d36e583c21e085757a0b18ed1d06d52"

    def getByCity(self,city):
        url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+self.api_key+"&units=metric"
        request = requests.get(url)
        json = request.json()
        return  json.get("name")

    def getCordinates(self, latitude, longitude):
        url="http://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&appid="+self.api_key
        request = requests.get(url)
        json = request.json()
        mylatitude=int(json.get("coord").get("lat"))
        mylongitude=int(json.get("coord").get("lon"))
        return (mylatitude, mylongitude)

    def getCityNameByZipCode(self, zipCode):
        url="http://api.openweathermap.org/data/2.5/weather?zip="+zipCode+"&appid="+self.api_key
        request = requests.get(url)
        json = request.json()
        return json.get("name")

