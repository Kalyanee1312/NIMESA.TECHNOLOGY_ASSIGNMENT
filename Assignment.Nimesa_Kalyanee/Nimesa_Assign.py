
import requests

def get_weather(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    try:
        temp = data['forecast']['forecastday'][0]['hour'][0]['temp_c']
        print(temp)
    except KeyError:
        print("Temp")   

def get_wind_speed(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    try:
        wind_speed = data['forecast']['forecastday'][0]['hour'][0]['wind_kph']
        print(wind_speed)
    except KeyError:
        print("Wind speed")   

def get_pressure(date):
    response = requests.get(f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    data = response.json()
    try:
        pressure = data['forecast']['forecastday'][0]['hour'][0]['pressure_mb']
        print(pressure)
    except KeyError:
        print("Pressure")    

def prompt_date():
    date = input("Enter the date (YYYY-MM-DD): ")
    return date

def main():
    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        option = input("Enter your choice: ")
        
        if option == "1":
            date = prompt_date()
            temp = get_weather(date)
            if temp is not None:
                print(f"The temperature on {date} is {temp}°C")
            else:
                print("No data available for the given date")

        elif option == "2":
            date = prompt_date()
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} km/h")
            else:
                print("No data available for the given date")

        elif option == "3":
            date = prompt_date()
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} mbar")
            else:
                print("No data available for the given date")
        elif option == "0":
            print("Existing the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()





























