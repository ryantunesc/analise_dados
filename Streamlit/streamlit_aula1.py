import streamlit as st
import pandas as pd
nome = "diniz"

idade = 17
st.set_page_config(page_title= "mercadinho", page_icon="H:\python\3etapa\streamlit\a.png", layout="centered")
st.title ("Meu primeiro dash")
st.subheader (nome)
st.write ("olá mundo")
st.divider()


st.write (nome, idade)

df = pd.DataFrame({
  'first column': ["Português", "Matemática", "Python","Frame"],
  'second column': [5, 9, 7, 10]
   }) 

st.write (df)
items = {
    "batata": {"price": 20 },
    "pão":  {"price": 20}
}

list = []

for a in items:
    list.append(a)

c = st.selectbox ("Mercado", list)

qtde = st.slider ("Quantidade", 0, 20)
total_preco = sum(items[c].values()) * qtde

st.metric (label = "Preço", value = f"R$ {total_preco}")

st.divider()


option = st.selectbox("Mercado2", list)
total_preco2 = sum(items[option].values())



qtde2 = st.number_input (option, step = 1)
st.metric("price", f"R$ {total_preco2  * qtde2}")


col1, col2 = st.columns(2) 
with col1:
    num1 = st.number_input  (value=0.0, step=1.0)
with col2:
    num2 = st.number_input  (value=0.0, step=1.0)

if st.button("Calcular", type="primary"):
    if operacao == "Soma (+)":
        resultado = num1 + num2
        st.success(f"Resultado: {num1} + {num2} = **{resultado}**")
        
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        st.success(f"Resultado: {num1} - {num2} = **{resultado}**")
        
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        st.success(f"Resultado: {num1} × {num2} = **{resultado}**")
        
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("Erro: Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
            st.success(f"Resultado: {num1} ÷ {num2} = **{resultado:.4f}**")
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)