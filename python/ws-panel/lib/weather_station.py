from lib.adafruit_io import AdafruitIO

class WeatherStation:
    def __init__(self, is_dev = False):
        group_name = "weather-station%s" % ("-dev" if is_dev else "")
        self.__aio = AdafruitIO(group_name)

    def get_temp(self):
        data = self.__aio.get_data("temperature")
        return int(data["results"][0]["value"])

    def get_high_temp(self):
        data = self.__aio.get_data("temperature-high")
        return int(data["results"][0]["value"])

    def get_low_temp(self):
        data = self.__aio.get_data("temperature-low")
        return int(data["results"][0]["value"])

    def get_humidity(self):
        data = self.__aio.get_data("humidity")
        return int(data["results"][0]["value"])

    def get_temp_info(self):
        info = (
            self.get_low_temp(),
            self.get_high_temp(),
            self.get_temp(),
        )
        return info
