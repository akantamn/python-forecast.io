import forecastio
import time
from datetime import date

api_key = "afe5dc26e28c297dc0336641259ee3e1"
Moab_lat = 38.5725
Moab_lng = 109.5497
Parma_lat = 44.8000
Parma_lng = 10.3333
Picabo_lat = 43.3058
Picabo_lng = 114.0678

open("./Data/Moab_daily_2001.txt","a").write("time,sunriseTime,sunsetTime,cloudCover,humidity \n")
open("./Data/Parma_daily_2001.txt","a").write("time,sunriseTime,sunsetTime,cloudCover,humidity \n")
open("./Data/Picabo_daily_2001.txt","a").write("time,sunriseTime,sunsetTime,cloudCover,humidity \n")



#1036152000
for i in range(978350400,1036152000,86400):
	Moab_forecast =forecastio.load_forecast(api_key,Moab_lat,Moab_lng,date.fromtimestamp(i))
	Parma_forecast= forecastio.load_forecast(api_key,Parma_lat,Parma_lng,date.fromtimestamp(i))
	Picabo_forecast = forecastio.load_forecast(api_key,Picabo_lat,Picabo_lng,date.fromtimestamp(i))
	#Moab_byHour = Moab_forecast.hourly()
	Moab_byDay = Moab_forecast.daily()
	#Parma_byHour = Parma_forecast.hourly()
	Parma_byDay = Parma_forecast.daily()
	#Picabo_byHour = Picabo_forecast.hourly()
	Picabo_byDay = Picabo_forecast.daily()
	for dailyData in Moab_byDay.data:
		open("./Data/Moab_daily_2001.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+ "\n");
	for dailyData in Parma_byDay.data:
		open("./Data/Parma_daily_2001.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+ "\n");
	for dailyData in Picabo_byDay.data:
		open("./Data/Picabo_daily_2001.txt","a").write(str(dailyData.time)+","+str(dailyData.sunriseTime)+","+str(dailyData.sunsetTime)+","+str(dailyData.cloudCover)+","+str(dailyData.humidity)+ "\n");



















