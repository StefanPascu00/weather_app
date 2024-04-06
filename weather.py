import json
import requests


def get_current_weather(url: str, key: str, city: str = "Bucuresti"):
    try:
        response = requests.get(url + city, headers={"key": key})
        if response.status_code == 200:
            weather_dict = json.loads(response.text)
            if weather_dict.get('error'):
                raise Exception(f"Orasul nu exista in baza noastra de date.")
            return weather_dict
        else:
            raise Exception(f"Something wrong with the api\n"
                            f"Code: {response.status_code}\n"
                            f"Message: {response.text}")
    except Exception as e:
        print(e)



