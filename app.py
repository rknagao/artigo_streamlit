import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import streamlit as st

#Explorando algumas modalidades de formatação de texto
st.title('Explorando o Streamlit')
st.subheader('Exercício de interatividade no Streamlit utilizando o Plotly')
st.write('O streamlit permite uma visualização **instantânea** de seu script em um formato simples e prático. Basta utilizar a caixa de seleção na barra lateral para definir seus parâmetros e pronto: o Streamlit atualizará seus resultados a partir dos novos parâmetros escolhidos.')
st.markdown('Exemplo de visualização das espécies do dataset [Iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html):')

#o dataset do plotly express é o mesmo de sua versão original do scikit-learn
df = px.data.iris()

#lista de possíveis especies
lista_especie = ('setosa','versicolor','virginica')

#caixa de seleção à esquerda
var_especie = st.selectbox(
    'Escolha a espécie a ser visualizada',
     lista_especie
)

#dicionários de cores a serem visualizadas no gráficos
dict_flor={
	lista_especie[0]:'blue',
	lista_especie[1]:'red',
	lista_especie[2]:'green'
}

#gráfico 3D gerado a partir do plotly
fig = go.Figure(data=go.Scatter3d(x=df['sepal_length'],
								  y=df['sepal_width'],
							      z=df['petal_width'],
								  mode='markers',
								  marker=dict(
								    size=4,
                   					color=np.where(
                   						df['species'] == var_especie,
                   						dict_flor[var_especie],
                   						'lightgray'
                   						)
                   					)
								  )
)
st.plotly_chart(fig)