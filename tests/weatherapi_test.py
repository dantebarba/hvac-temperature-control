import unittest
import os
import requests
from dotenv import load_dotenv


class WeatherApiTest(unittest.TestCase):

    def setUp(self):
        load_dotenv()

    def test_weather_api(self):
        print(os.getenv("WEATHER_API_KEY"))
        print(os.getenv("WEATHER_API_URL"))

        response = requests.get(os.getenv("WEATHER_API_URL").format(api_key=os.getenv("WEATHER_API_KEY")))

        print(response.json())