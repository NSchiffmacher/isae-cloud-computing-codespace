import streamlit as st

st.title('Example')

st.header('Header 1')
st.subheader('Subheader 1')
st.markdown('Texte en gras: **Gras** ')

st.code('''a = 12
b = 19
print(a+b+10)''', language='python')