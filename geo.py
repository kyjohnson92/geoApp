from geopy.geocoders import Nominatim


class GeoLocator():

    def __init__(self):
        self = self

    def GeoJson(self, input):
        geolocator = Nominatim(user_agent="default")
        location = geolocator.geocode(input)

        try:
            if location:
                self.address = location.address
                self.latitude = location.latitude
                self.longitude = location.longitude
        except ValueError:
            pass
        try:
            if geolocator.reverse(location):
                self.address = location.address
                self.latitude = location.latitude
                self.longitude = location.longitude
        except Exception as e:
            if type(e).__name__ == 'ReadTimeoutError':
                return "Must format coorindates as '0.0,0.0"
            else:
                pass

        return (self.latitude, self.longitude, self.address)


x = GeoLocator()

print(x.GeoJson("Bronx"))
