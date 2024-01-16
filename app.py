import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Base de datos de vehículos en Estados Unidos :sunglasses:')

st.header('Visor de datos')
st.write('Esta es una muestra de la información que se encuentra dentro de la base de datos :blue_book:') 
car_data = pd.read_csv('vehicles_us_clean.csv') # leer los datos
st.dataframe(data=car_data.sample(10) )

st.divider()

st.header('Tipo de vehículos por fabricante')
st.write('La siguiente gráfica muestra el tipo de vehículos por fabricante :car:') 

fig = px.bar(car_data, x="manufacturer", color="type")
fig.update_layout(
    xaxis_title_text = 'Fabricante', 
    yaxis_title_text = 'Número de vehículos')
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header('Estado del vehículo')
st.write('La siguiente gráfica muestra la distribución del vehículo según el año y lo clasifica según su estado :white_check_mark:' )

fig2 = px.histogram(car_data, x="model_year", color="condition")
fig2.update_layout(
    xaxis_title_text = 'Año', 
    yaxis_title_text = 'Conteo')
st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.header('Distribución de precios por marca')

option = st.selectbox(
    '¿Que marca de vehículo te gustaría ver?',
    ('bmw','hyundai','chrysler', 'toyota', 'honda', 'kia', 'chevrolet', 'ram', 'gmc',
    'jeep', 'ford', 'nissan', 'subaru', 'dodge', 'acura', 'cadillac', 'volkswagen',
    'buick'),
    index=None,
    placeholder="Selecciona el fabricante...",)
if option:
    df = car_data[car_data['manufacturer']==option]
    st.subheader(option)
    st.write('La siguiente gráfica muestra la distribución del precio de los vehículos según la marca seleccionada :money_with_wings:') 
    fig3 = px.histogram(df, x="price" )
    fig3.update_layout(
        xaxis_title_text = 'Precio', 
        yaxis_title_text = 'Conteo',)
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.header('Gráfica de dispersión interactiva')

opt1 = st.selectbox(
    'Selecciona y',
    ('price','model_year','odometer','days_listed'))
st.write('You selected:', opt1)

opt2 = st.selectbox(
    'Selecciona x',
    ('odometer','model_year','price','days_listed'))
st.write('You selected:', opt2)

if opt1 and opt2:
    st.subheader("Esta es una gráfica interactiva para analizar los datos :chart_with_upwards_trend:")
    fig4 = px.scatter(car_data, x=opt2, y=opt1)
    st.plotly_chart(fig4, use_container_width=True)
 







