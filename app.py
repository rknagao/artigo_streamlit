import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from random import randint

###############
#CASO PRÁTICO #
###############

#Explorando algumas modalidades de formatação de texto
st.title('Explorando o Streamlit')
st.write('O streamlit permite uma visualização **instantânea** de seu script em um formato simples e prático. Basta utilizar a caixa de seleção na barra lateral para definir seus parâmetros e pronto: o Streamlit atualizará seus resultados a partir dos novos parâmetros escolhidos.')
st.markdown('Exemplo de visualização das espécies do dataset [Iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html):')

#o dataset do plotly express é o mesmo de sua versão original do scikit-learn
df = px.data.iris()

#lista de possíveis especies
lista_especie = ('setosa','versicolor','virginica')

#caixa de seleção à esquerda
var_especie = st.sidebar.selectbox('Escolha a espécie a ser visualizada',lista_especie)

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
#comando necessário para chamar o gráfico do plotly
st.plotly_chart(fig)



st.title('Elementos Básicos')
st.write('O Stream oferece uma diversidade de estruturas diferentes para criar o melhor aplicativo web para seu projeto. Dentre as diferentes estruturas, é possível listar algumas principais, como os objetos interativos, gráficos e imagens.')
st.write('A partir de agora é recomendado que você acompanhe este Streamlit lado-a-lado com o artigo, no capítulo "Streamlit".')

#############
#1 - TEXTOS #
#############
st.header('1. Textos')

code = '''
st.title('Isso é um título')
st.header('Isso é um cabeçalho')
st.subheader('Isso é um subcabeçalho')
st.text('Isso é um texto normal')
st.markdown('Texto em **negrito** ou _itálico_')
st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)',False)
'''

st.code(code, language='python')

#Diferentes tamanhos de texto
st.title('Isso é um título')
st.header('Isso é um cabeçalho')
st.subheader('Isso é um subcabeçalho')
st.text('Isso é um texto normal')

#formatação
st.markdown('Texto em **negrito** ou _itálico_')

#Utilização para guardar html
st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)',False)
st.text('')
st.text('')
st.text('')

##############
#2 - TABELAS #
##############
st.header('2. Tabelas')

st.subheader('Exemplo de Tabela interativa')
code = '''
df = pd.DataFrame(
	np.random.randn(5,10),
	columns=('col_%d' % i for i in range(10))
	)
st.dataframe(df)
'''
st.code(code, language='python')

df = pd.DataFrame(
	np.random.randn(5,10),
	columns=('col_%d' % i for i in range(10))
	)
st.dataframe(df)

st.text('')
st.text('')
st.text('')

#tabelas estática
st.subheader('Exemplo de Tabela estática')

code = '''
st.table(df)
'''
st.code(code, language='python')

st.table(df)


############################
#3 - ELEMENTOS INTERATIVOS #
############################
st.header('3. Elementos Interativos')

#Botão
st.subheader('Exemplo de botão')
code='''
if st.button('BOTÃO'):
   st.write(randint(0, 1000000))
else:
   st.write('Clique no botão acima')
'''
st.code(code, language='python')

if st.button('BOTÃO'):
   st.write(randint(0, 1000000))
else:
   st.write('Clique no botão acima')



#Radio
st.subheader('4. Exemplo de radio')
code='''
chute = st.radio(
    "Por que essa função se chama radio?",
    ('Opção 1: rádio é um osso muito bonito', 'Opção 2: homenagem à Marie Curie', 'Opção 3: as opções lembram botões de rádio'))

if chute == 'Opção 3: as opções lembram botões de rádio':
    st.write('Correto!')
else:
    st.write("Errado, tente novamente.")
'''
st.code(code, language='python')

chute = st.radio(
    "Por que essa função se chama radio?",
    ('Opção 1: rádio é um osso muito bonito', 'Opção 2: homenagem à Marie Curie', 'Opção 3: as opções lembram botões de rádio'))

if chute == 'Opção 3: as opções lembram botões de rádio':
    st.write('Correto!')
else:
    st.write("Errado, tente novamente.")


#Barra de arraste
st.subheader('Exemplo de barra de arraste')
code='''
bar = st.slider('Isso é um slider',
				min_value=0,
				max_value=10,
				value=5,
				step=1)
st.write("você selecionou: ",bar)
'''
st.code(code, language='python')


bar = st.slider('Isso é um slider',
				min_value=0,
				max_value=10,
				value=5,
				step=1)
st.write("você selecionou: ",bar)



#caixa de multiseleção
st.subheader('Exemplo de caixa de multiseleção')
code='''
cx_mult = st.multiselect(
	'Selecione as colunas abaixos',
	df.columns
)
st.dataframe(df[cx_mult])
'''
st.code(code, language='python')


cx_mult = st.multiselect(
	'Selecione as colunas abaixos',
	df.columns
)
st.dataframe(df[cx_mult])


#input de informação
st.subheader('Exemplos de input número')
code='''
input_num = st.number_input('Escreva um número entre 0 e 10',
							min_value = 0,
							max_value = 10,
							value = 0,
							step = 1)
st.write('O número inputado foi: ', input_num)
'''
st.code(code, language='python')


input_num = st.number_input('Escreva um número entre 0 e 10',
							min_value = 0,
							max_value = 10,
							value = 0,
							step = 1)
st.write('O número inputado foi: ', input_num)

st.subheader('Exemplos de input texto')
code='''
input_txt = st.text_input('Escreva uma palavra com até 5 letras',
						  value = 'juiz',
						  max_chars = 5)
st.write('A palavra inputada foi: ', input_txt)
'''
st.code(code, language='python')

input_txt = st.text_input('Escreva uma palavra com até 5 letras',
						  value = 'juiz',
						  max_chars = 5)
st.write('A palavra inputada foi: ', input_txt)


##############
#4 - GRAFICO #
##############

#gráfico
st.subheader('Exemplo de gráfico')
code='''
#vamos aproveitar o dataframe criado anteriormente
df2 = pd.DataFrame(df, columns=['col_0','col_1','col_2'])
#exemplo de gráfico 
st.area_chart(df2)
'''
st.code(code, language='python')

#vamos aproveitar o dataframe criado anteriormente
df2 = pd.DataFrame(df, columns=['col_0','col_1','col_2'])
#exemplo de gráfico 
st.area_chart(df2)

#############
#5 - MIDIAS #
#############

st.subheader('Exemplo de mídia')

code='''
from PIL import Image
foto = Image.open('foto.png')

st.image(foto,
         caption='Imagem desalinhada do logo',
         use_column_width=False)
'''
st.code(code, language='python')

from PIL import Image
foto = Image.open('foto.png')

st.image(foto,
         caption='Imagem desalinhada do logo',
         use_column_width=False)


#criando 3 colunas 
col1, col2, col3 = st.beta_columns(3)
code='''
col1, col2, col3 = st.beta_columns(3)

foto = Image.open('foto.png')
#inserindo na coluna 2
col2.image(foto,
		   caption='Imagem centralizada do logo',
		   use_column_width=False)
'''
col2.code(code, language='python')

foto = Image.open('foto.png')
#inserindo na coluna 2
col2.image(foto,
		   caption='Imagem centralizada do logo',
		   use_column_width=False)


st.subheader('Exemplo do streamlit.write()')
code='''
st.write('hola!')
st.write(df)
st.write(fig)
'''
st.code(code, language='python')

#precisa escrever o texto? Beleza
st.write('hola!')
#quer mostrar a tabela? Não tem problema
st.write(df)
#aguenta gráficos? Tranquilo
st.write(fig)
#e muito mais...