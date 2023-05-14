import streamlit as st

st.title("Stremlit APP")
st.markdown("Streamlit is **_really_cool**.")
st.header("Cabeçalho")
st.subheader("Subcabeçalho")
st.caption("Texto")
st.code("a = 1234")
st.text("Hello World")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule