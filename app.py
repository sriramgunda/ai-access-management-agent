import streamlit as st
from agent import agent

st.title("🛠️ Access Issue Agent")
query = st.text_input("Describe the access issue (e.g. 'access denied for alice')")
if query:
    with st.spinner("Processing..."):
        response = agent.run(query)
    st.markdown(response)
