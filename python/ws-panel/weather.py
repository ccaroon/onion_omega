from lib.adafruit_io import AdafruitIO

aio = AdafruitIO("weather-station")

data = aio.get_data("temperature")
print(data["results"][0]["value"])


data = aio.get_data("temperature-high")
print(data["results"][0]["value"])

data = aio.get_data("temperature-low")
print(data["results"][0]["value"])
