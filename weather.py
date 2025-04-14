import streamlit as stl
import requests


API_KEY = "642990c2d40c3ee377703304e1a359e8"



def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin -273.15


def find_current_weather(city):
    base_rul = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data = requests.get(base_rul).json()
    
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(convert_to_celcius(weather_data['main']['temp']))
        country = weather_data['sys']['country']
        icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        stl.error("City is not found.")
        stl.stop()
    return general,temperature,icon,country
        

def main():
    #stl.header("Find the World Weather")
    stl.set_page_config(page_title="Weather App 🌦️", layout="centered")
    
     # 🌍 Rotating Earth Header with Hover Effect
    stl.markdown("""
        <style>
        .custom-header {
            font-size: 36px;
            color: #1f77b4;
            transition: color 0.2s ease;
            text-align: center;
            font-weight: bold;
        }

        .custom-header:hover {
            color: #e91e63;
        }

        .rotate-earth {
            display: inline-block;
            animation: spin 6s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>

        <h1 class="custom-header">
            <span class="rotate-earth">🌍</span> Find the World Weather
        </h1>
    """, unsafe_allow_html=True)
    city = stl.text_input("Enter the city name").lower()
    if stl.button("Click"):
        general,temperature,icon,country = find_current_weather(city)
        stl.subheader(f"{city.title()}, {country}")
        col_1,col_2 = stl.columns(2)
        with col_1:
            stl.metric(label="Temperature",value=f"{temperature}°C")
        with col_2:
            stl.write(general)
            stl.image(icon)
    
    
       

if __name__=='__main__':
    main()
    