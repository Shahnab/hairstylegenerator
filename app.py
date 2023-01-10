import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://img.freepik.com/premium-vector/woman-hair-salon-logo-design-luxury-vector_487414-1667.jpg", width=100)
st.sidebar.subheader("About HairClip Engine")
st.sidebar.markdown("###### Hair editing is an interesting and challenging problem in computer vision and graphics")
st.sidebar.markdown("###### Many existing methods require well-drawn sketches or masks as conditional inputs for editing, however these interactions are neither straightforward nor efficient")
st.sidebar.markdown("###### Uses a unified hair editing framework by leveraging the powerful image text representation capability of the Contrastive Language-Image Pre-Training (CLIP) model")

st.sidebar.caption("Streamlit App by </Shahnab>")

st.subheader("Interface")
# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://gradio-blocks-hairclip.hf.space", width=1100, height=650, scrolling=True)
