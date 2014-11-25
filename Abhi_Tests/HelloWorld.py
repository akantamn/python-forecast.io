import forecastio
import csv

api_key = "afe5dc26e28c297dc0336641259ee3e1"
lat = 38.5725
lng = 109.5497
forecast =forecastio.load_forecast(api_key,lat,lng)


byHour = forecast.hourly()
print byHour.summary
print byHour.icon

fo = open("foo.txt", "wb")

for hourlyData in byHour.data:
	print hourlyData.temperature
	print hourlyData.cloudCover
	fo.write("Python is a great language." + str(hourlyData.cloudCover) + "\n Yeah its great!!\n");

fo.close()