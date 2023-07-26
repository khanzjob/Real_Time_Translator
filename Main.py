
import streamlit as st
from Translate import TranslateWords

def intro():
    import streamlit as st

    st.write("# Welcome to Macro! 👋")
    st.sidebar.success("Select a Action")

    st.markdown(
        """
        Marco is a comprehensive event management platform designed primarily for travelers. It serves as a one-stop database for discovering, booking, and even hosting events. Whether you're a tourist exploring a new city or a local looking to uncover hidden gems, Marco has you covered. Our platform offers a list of diverse events and provides reservation and booking services. Additionally, event organizers can take advantage of Marco's 
        promotional services to boost their event's visibility, regardless of its location.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Marco can do!

       
    """
    )


page_names_to_funcs = {
    "—": intro,
    "ChatBot": TranslateWords,
    
}

demo_name = st.sidebar.selectbox("Choose a Action", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()