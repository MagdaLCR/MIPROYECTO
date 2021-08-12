import streamlit as st 
st.title ("MI PRIMERA APLICACIÓN")
st.sidebar.title ("PARÁMETRO")
st.sidebar.header("INICIO")
st.write("APLICACIONES")
from PIL import Image
imagen1=Image.open("IMAGEN.jpg")
st.image(imagen1)
import pandas as pd
df=pd.read_excel("DATA.xlsx")
df["CALCULO"]=df.NÚMEROS*3
lista_columna=df.columns
st.write(df)
st.write(lista_columna)
estadistica=df.describe()
st.write(estadistica)
barra_desplazadora=st.slider("seleccione un valor",5,50,10,step=2)
st.write("su valor seleccionado fue",barra_desplazadora)
df["FUNCION"]=df.NÚMEROS*barra_desplazadora
st.write(df)
ingreso_numero=st.number_input("ingrese un valor:")
ingreso_texto=st.text_input("ingrese su nombre:")
caja_seleccion=st.selectbox("seleccione una opcion:",[1,2,3])
caja_seleccion=st.selectbox("seleccione una opcion:",["a","b","c"],index=2)
with st.beta_expander("Menú"):
	col1,col2=st.beta_columns(2)
	with col1:
		opciones=st.radio("seleccione una opcion:",[1,2,3])
	with col2:

		check=st.checkbox("soltera")
		if check == True:
			st.write("está seguro")
		else:
			st.write("No seleccionado el check")
lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[2,4,6,8,10,12,14,16,18,20]
lista3=[3,6,9,12,15,18,21,24,27,30]
data={"ejeX":lista1,
		"ejeY":lista2,
		"ejeZ":lista3}
ejes=pd.DataFrame(data)
st.write(ejes)
import altair as alt
grafico_altair=alt.Chart(ejes).mark_bar().encode(
	x="ejeX",
	y="ejeY",
	color="ejeZ").interactive()
st.altair_chart(grafico_altair)
import plotly.express as px
import matplotlib.pyplot as plt
figura_3d=px.line_3d(ejes,x="ejeX",y="ejeY",z="ejeZ")
st.write(figura_3d)
figura2=px.scatter(ejes,x="ejeX",y="ejeZ",animation_frame="ejeY",range_x=[0,40],range_y=[0,40])
st.write(figura2)
grafico2,ax=plt.subplots()
ax.plot(ejes["ejeY"],ejes["ejeX"],marker="x",label="x")
ax.set_xlabel("ejeX")
ax.set_ylabel("ejeY")
ax.grid()
ax.legend(loc="best")
ax.set_title("grafico")
st.pyplot(grafico2)