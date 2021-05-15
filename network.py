import requests
import urllib.request

class Data():

    #api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

    API = "40365a48657d127816602e1b92b59a58"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    IMG_URL = 'https://openweathermap.org/img/w/'

    def checkInternet(self):
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False

    def getData(self, city):
        if self.checkInternet(self):
            params = {'APPID': self.API, 'q': city, 'units': 'metric'}
            response = requests.get(self.URL, params=params)
            weather = response.json()
            try:
                name = weather['name']
                desc = weather['weather'][0]['main']
                temp = weather['main']['temp']
                icon = weather['weather'][0]['icon']
                return(['City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp), icon])
            except:
                return(["There was an error","error"])
        else:
            return(["Please Check Your \nInternet Connection","error"])


