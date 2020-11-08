import streamlit as st
from streamlit_drawable_canvas import st_canvas


st.set_page_config(
    page_title="Handwritten Letters Classifier",
    page_icon=":pencil:",
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Handwritten Letters Classifier")

stroke_width = st.sidebar.slider("Stroke width: ", 1, 100, 25)

canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color="#fff",
    background_color="#000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)
