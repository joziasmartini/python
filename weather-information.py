import requests

# Get the city from the user
city = input("\nEnter a city: ")

# Set the API Key
api_key = 'cb771e45ac79a4e8e2205c0ce66ff633'

# Get the weather information from the API
response = requests.get('http://api.openweathermap.org/data/2.5/weather?appid='+api_key+'&q='+city)

# Convert the JSON data to a Python dictionary
data = response.json()

# Print the weather description
print('\nWheather:', (data['weather'][0]['description']).title())

# Print the temperature in degrees Celsius
print('Temperature:', int(data['main']['temp'] - 273.15), '°C')

# Print the wind speed in km/h
print('Wind Speed:', data['wind']['speed'] * 3.6)

# Print the humidity in percentage
print('Humidity:', data['main']['humidity'])

# Print the pressure in hPa
print('Pressure:', data['main']['pressure'], '\n')