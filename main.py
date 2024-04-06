import json
import os
from emoji import emojize as emoji
import weather


def initialise_config(path: str) -> dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialise project {e}.")
        exit(1)
    return config


if __name__ == '__main__':
    config = initialise_config("config.json")
    key = os.environ["weather_api_key"]
    city = input("Introduceti orasul: ")
    weather_dict = weather.get_current_weather(url=config['url'], key=key, city=city)

    if "rain" in str(weather_dict['current']['condition']['text']).lower():
        symbol = emoji(':cloud_with_rain:')
    elif "sunny" in str(weather_dict['current']['condition']['text']).lower():
        symbol = emoji(':sun:')
    else:
        symbol = emoji(':cloud_with_snow:')

    clock = str(weather_dict['location']['localtime'])

    print(weather_dict['location']['name'], weather_dict['location']['country'] + "\n",
          clock[10:(len(clock) - 1)] + "\n", str(weather_dict['current']['temp_c']) + " c",
          symbol)

