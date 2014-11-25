import forecastio
import csv

api_key = "afe5dc26e28c297dc0336641259ee3e1"
lat = 38.5725
lng = 109.5497
forecast =forecastio.load_forecast(api_key,lat,lng)


byHour = forecast.hourly()
print byHour.summary
print byHour.icon

fo = open("hourly.txt", "wb")

fo.write("time,temperature,cloud cover\n");

for hourlyData in byHour.data:
	fo.write(str(hourlyData.time)+",")
	fo.write(str(hourlyData.temperature)+",")
	fo.write(str(hourlyData.cloudCover) + "\n");
	

fo.close()

byDay = forecast.daily()
print byDay.summary
print byDay.icon


fi = open("Daily.txt", "wb")
fi.write("MinTemp, cloud cover\n");


for dailyData in byDay.data:
	fi.write( str(dailyData.temperatureMin)+",")
	fi.write(str(dailyData.cloudCover) + ", \n");
fi.close()