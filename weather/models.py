from django.db import migrations,models

class Cities_available(models.Model):
    # city nd its lat long
    city = models.CharField(max_length=30)
    lat_long = models.CharField(max_length=50)

class Cities(models.Model):
    # city
    city = models.ForeignKey(Cities_available, null=True)

class Weather(models.Model):
	# temperature
    mintempm = models.FloatField()
    maxtempm = models.FloatField()

    # dew
    mindewptm = models.FloatField()
    maxdewptm = models.FloatField()

    # humidity
    minhumidity = models.FloatField()
    maxhumidity = models.FloatField()

    # wind speed
    minwspdm = models.FloatField()
    maxwspdm = models.FloatField()

    # visibility
    minvism = models.FloatField()
    maxvism = models.FloatField()

    # pressure
    minpressurem = models.FloatField()
    maxpressurem = models.FloatField()

    #which date_weather
    weather_date = models.DateField()
    city = models.ForeignKey(Cities_available, null=True)

    def get_values(self, args):
    	data = {}
    	for arg in args:
    		data[arg] = getattr(self, arg)
    	return data