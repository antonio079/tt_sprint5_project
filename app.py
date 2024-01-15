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
st.write('La siguiente gráfica muestra el tipo de vehiculos por fabricante :car:') 

fig = px.bar(car_data, x="manufacturer", color="type")
fig.update_layout(
    xaxis_title_text = 'Fabricante', 
    yaxis_title_text = 'Número de vehículos')
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header('Estado del vehículo')
st.write('La siguiente gráfica muestra la distrubucion del vehículo segun el año y lo clasifica segun su estado :white_check_mark:' ) 

fig2 = px.histogram(car_data, x="model_year", color="condition")
fig2.update_layout(
    xaxis_title_text = 'Año', 
    yaxis_title_text = 'Conteo')
st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.header('Distrubución de precios segun la marca de vehículos')

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
    st.write('La siguiente gráfica muestra la distrubucion del precio de los vehículos segun marca :money_with_wings:' ) 
    fig3 = px.histogram(df, x="price" )
    fig.update_layout(
        xaxis_title_text = 'Fabricante', 
        yaxis_title_text = 'Número de vehículos',
        template='plotly_dark')
    st.plotly_chart(fig3, use_container_width=True)












