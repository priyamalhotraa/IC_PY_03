import requests

def get_weather(city):
    API_KEY = "a40d296fe6ac584de276e115709441c3"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response=requests.get(url)

        if response.status_code != 200:
            print("City not found or API error")
            return

        data=response.json()

        temperature=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        wind_speed=data["wind"]["speed"]
        condition=data["weather"][0]["description"]

        print("\nWEATHER DETAILS\n")
        print(f"City: {city}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

city_name = input("Enter city name: ")
get_weather(city_name)
