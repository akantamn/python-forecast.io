import forecastio
import time

api_key = "afe5dc26e28c297dc0336641259ee3e1"
Moab_lat = 38.5725
Moab_lng = 109.5497
Parma_lat = 44.8000
Parma_lng = 10.3333
Picabo_lat = 43.3058
Picabo_lng = 114.0678

Moab_forecast =forecastio.load_forecast(api_key,Moab_lat,Moab_lng)
Parma_forecast= forecastio.load_forecast(api_key,Parma_lat,Parma_lng)
Picabo_forecast = forecastio.load_forecast(api_key,Picabo_lat,Picabo_lng)

open("./Data/Moab_hourly.txt","a").write("time,precipIntensity,precipProbability,temperature,apparentTemperature,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")
open("./Data/Parma_hourly.txt","a").write("time,precipIntensity,precipProbability,temperature,apparentTemperature,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")
open("./Data/Picabo_hourly.txt","a").write("time,precipIntensity,precipProbability,temperature,apparentTemperature,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")



Moab_byHour = Moab_forecast.hourly()
Moab_byDay = Moab_forecast.daily()

Parma_byHour = Parma_forecast.hourly()
Parma_byDay = Parma_forecast.daily()

Picabo_byHour = Picabo_forecast.hourly()
Picabo_byDay = Picabo_forecast.daily()


for hourlyData in Moab_byHour.data:
	f1=open("./Data/Moab_hourly.txt","a").write(str(hourlyData.time)+","+str(hourlyData.precipIntensity)+","+str(hourlyData.precipProbability)+","+str(hourlyData.temperature)+","+str(hourlyData.apparentTemperature)+","+str(hourlyData.dewPoint)+","+str(hourlyData.windSpeed)+","+str(hourlyData.windBearing)+","+str(hourlyData.cloudCover)+","+str(hourlyData.humidity)+","+str(hourlyData.pressure)+","+str(hourlyData.ozone)+ "\n");

for hourlyData in Parma_byHour.data:
	f2=open("./Data/Parma_hourly.txt","a").write(str(hourlyData.time)+","+str(hourlyData.precipIntensity)+","+str(hourlyData.precipProbability)+","+str(hourlyData.temperature)+","+str(hourlyData.apparentTemperature)+","+str(hourlyData.dewPoint)+","+str(hourlyData.windSpeed)+","+str(hourlyData.windBearing)+","+str(hourlyData.cloudCover)+","+str(hourlyData.humidity)+","+str(hourlyData.pressure)+","+str(hourlyData.ozone)+ "\n");

for hourlyData in Picabo_byHour.data:
	f3=open("./Data/Picabo_hourly.txt","a").write(str(hourlyData.time)+","+str(hourlyData.precipIntensity)+","+str(hourlyData.precipProbability)+","+str(hourlyData.temperature)+","+str(hourlyData.apparentTemperature)+","+str(hourlyData.dewPoint)+","+str(hourlyData.windSpeed)+","+str(hourlyData.windBearing)+","+str(hourlyData.cloudCover)+","+str(hourlyData.humidity)+","+str(hourlyData.pressure)+","+str(hourlyData.ozone)+ "\n");
	




open("./Data/Moab_daily.txt","a").write("time,sunriseTime,sunsetTime,moonPhase,precipIntensity,precipIntensityMax,precipProbability,temperatureMin,temperatureMinTime,temperatureMax,temperatureMaxTime,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")
open("./Data/Parma_daily.txt","a").write("time,sunriseTime,sunsetTime,moonPhase,precipIntensity,precipIntensityMax,precipProbability,temperatureMin,temperatureMinTime,temperatureMax,temperatureMaxTime,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")
open("./Data/Picabo_daily.txt","a").write("time,sunriseTime,sunsetTime,moonPhase,precipIntensity,precipIntensityMax,precipProbability,temperatureMin,temperatureMinTime,temperatureMax,temperatureMaxTime,dewPoint,windSpeed,windBearing,cloudCover,humidity,pressure,ozone \n")








for dailyData in Moab_byDay.data:
	open("./Data/Moab_daily.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.moonPhase)+","+str(dailyData.precipIntensity)+","+str(dailyData.precipIntensityMax)+","+str(dailyData.precipProbability)+","+str(dailyData.temperatureMin)+","+str(dailyData.temperatureMinTime)+","+str(dailyData.temperatureMax)+","+str(dailyData.temperatureMaxTime)+","+str(dailyData.dewPoint)+","+str(dailyData.windSpeed)+","+str(dailyData.windBearing)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+","+str(dailyData.pressure)+","+str(dailyData.ozone)+ "\n");

for dailyData in Parma_byDay.data:
	open("./Data/Parma_daily.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.moonPhase)+","+str(dailyData.precipIntensity)+","+str(dailyData.precipIntensityMax)+","+str(dailyData.precipProbability)+","+str(dailyData.temperatureMin)+","+str(dailyData.temperatureMinTime)+","+str(dailyData.temperatureMax)+","+str(dailyData.temperatureMaxTime)+","+str(dailyData.dewPoint)+","+str(dailyData.windSpeed)+","+str(dailyData.windBearing)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+","+str(dailyData.pressure)+","+str(dailyData.ozone)+ "\n");

for dailyData in Picabo_byDay.data:
	open("./Data/Picabo_daily.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.moonPhase)+","+str(dailyData.precipIntensity)+","+str(dailyData.precipIntensityMax)+","+str(dailyData.precipProbability)+","+str(dailyData.temperatureMin)+","+str(dailyData.temperatureMinTime)+","+str(dailyData.temperatureMax)+","+str(dailyData.temperatureMaxTime)+","+str(dailyData.dewPoint)+","+str(dailyData.windSpeed)+","+str(dailyData.windBearing)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+","+str(dailyData.pressure)+","+str(dailyData.ozone)+ "\n");

