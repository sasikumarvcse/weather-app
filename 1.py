import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class WeatherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        bg_image = Image(source='12.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg_image)
        self.city_input = TextInput(hint_text='Enter city name', multiline=False, halign="center", font_size=80)
        self.result_label = Label()

        layout.add_widget(self.city_input)
        layout.add_widget(self.result_label)

        self.city_input.bind(on_text_validate=self.get_weather)

        return layout

    def get_weather(self, instance):
        city = self.city_input.text
        api_key = '8718d08a6ac5e0bb4ee0045eac0c83c4'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            data = response.json()

            if data['cod'] == 200:
                weather_info = data['weather'][0]['main']
                temperature = (data['main']['temp'] -273,2)
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']

                result_text = f'Weather: {weather_info}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'
            else:
                result_text = f'Error: {data["message"]}'

        except requests.exceptions.RequestException as e:
            result_text = f'Error: {str(e)}'

        self.result_label.text = result_text

if __name__ == '__main__':
    WeatherApp().run()