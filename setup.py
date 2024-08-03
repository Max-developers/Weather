import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # для получения температуры в градусах Цельсия
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
        else:
            return None

class WeatherApp:
    def __init__(self, api_key):
        self.weather = Weather(api_key)

    def run(self):
        print("Добро пожаловать в приложение прогноза погоды!")
        city = input("Введите название города: ")
        weather_data = self.weather.get_weather(city)

        if weather_data:
            print(f"\\nПогода в городе {weather_data['city']}:")
            print(f"Температура: {weather_data['temperature']}°C")
            print(f"Описание: {weather_data['description']}")
            print(f"Влажность: {weather_data['humidity']}%")
            print(f"Скорость ветра: {weather_data['wind_speed']} м/с")
        else:
            print("Не удалось получить данные о погоде. Проверьте название города.")

if __name__ == '__main__':
    API_KEY = 'ваш_api_key'  # Замените своим API ключом
    app = WeatherApp(API_KEY)
    app.run()

