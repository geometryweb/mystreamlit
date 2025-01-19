import streamlit as st

tab1, tab2, tab3 = st.tabs(["image01", "image02", "image03"])
with tab1:
    st.write("tab1")
    st.image("images/image01.png", width=460)
with tab2:
    st.write("tab2")
    st.image("images/image02.png", width=460)
with tab3:
    st.write("tab3")
    st.image("images/image03.png", width=460)
