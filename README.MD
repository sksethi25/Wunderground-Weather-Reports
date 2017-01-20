Wounderground Weather Report:

  It fetches weather conditions data from wunderground and plot a bar graph
 
Project Hosted on : https://wuweather.herokuapp.com/

Setup(for hosting on local):
  1. Add data username, password, new empty created database name in settings.py if you dont want to use sqlite
  2. Add Wu key at weather_data/weather/apps.py
  

Project Details:
 1. Created a app inside project named weather which will be main app performing all required things.
 2. Added a service layer to make wunderground api http request using Request module.
 3. Created Required models like available cities, added cities and weather.
 4. Views: Total of two pages, one is to fetch weather data (index page)
 and other page is to add cities to list of cites show in fetch page.
 5. On two Views, a total of six action can be taken ,out of which 3 are api calls (check points 6,7,8 ) and other two are to switch bw views and one of api call reset is present on both pages.
 6. A Request to fetch weather data: firstly check data for which days existed in database, and for day whose data dont exist, it make request to WU Api and store in database , merge existing nd just fetched data and return back response to user.
 7. A Request to add cities: It add id of city selected from city available list to cities added db.
 8. A Request to reset data: It clear cities added and data fetched from wu and store to database.


ToDo:
1.Code Commenting.

2.More Code Reviewing.

3.Menu bar to Switch Views.

4.Change Ploting library(To heavy to load, browser slows downs).
