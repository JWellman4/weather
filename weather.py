import requests
import streamlit as st

st.set_page_config(
    layout='wide',
    page_title='Wellman Weather App',
    page_icon='cloud',
)

st.title('Wellman Weather App :mostly_sunny:')
api_key = '79b962a1124522a8d5a249642ae69e69'

with st.sidebar:
    user_input = st.text_input("Enter City, State Code/Country Code:", value='Raleigh, NC')
    state_code = "Enter State Code:"

try :
     loc_data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={user_input},{state_code}&appid={api_key}')
except IndexError:
    st.write('Invalid Location')
try:
    lat = loc_data.json()[0]['lat']
    lon = loc_data.json()[0]['lon']
    weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={api_key}')

    description = weather_data.json()['weather'][0]['description']
    temp = round(weather_data.json()['main']['temp'])
    degree_sign = u'\N{DEGREE SIGN}'

    row1 = st.columns(1)
    for col in row1:
         st.write('')
            
    col1, col2 = st.columns(2)
    with col1:
            st.metric(label='Location', value=user_input)
            st.metric(label='Temperature', value=f'{temp}{degree_sign}')
            st.metric(label='Description', value=description)
    with col2:
        if 'rain' in description:
            st.image('https://as2.ftcdn.net/v2/jpg/03/66/90/39/1000_F_366903907_RzCXMYTOdWnfEmm8wZ3fKnfEOLE2Qhmh.jpg', use_column_width=True)
        elif description == 'clear sky':
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlM15MON_NUU5wG9xwwxCIojU3JvdXt6b8Z6QkssCpLg&s', use_column_width=True)
        elif 'cloud' in description:
            st.image('data:image/jpeg;base64,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', use_column_width=True)

except IndexError:
    st.write('Invalid Location')
