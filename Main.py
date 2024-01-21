
import streamlit as st
from SupportedLanguages import DisplayLanguages
from Translate import TranslateWords
from fileUpload import uploadFile

def intro():
    import streamlit as st

    st.write("# Welcome to RTT! 👋")
    st.sidebar.success("Select an Action")

    st.markdown(
        """
        RTT is a Streamlit-based web application that provides users with an interactive chat interface to seamlessly translate text from any major world language to specific local languages in real-time.

        **Features and Functionality:**

        - **User Interface:** The app offers a chat-style interface, facilitating easy input of text messages. The chat history persists across sessions, preserving users' translation interactions.
        - **Broad Language Support:** Users can input text in any primary global language. For translation targets, a range of local languages like Luganda, Runyankole, Acholi, Lugbara, and Ateso are available via a dropdown menu.
       
        **Supported Languages:** Check out the table below to see which languages are supported for translation into local languages.

        """
    )
    data="https://youtu.be/Z1FLSofVPHA"
    st.video(data, format="video/mp4", start_time=0)

    # # Display the language support table
    # st.write(df_world_languages)

    st.markdown(
        """
        **Use Case:**
        RTT serves as an invaluable tool for individuals desiring quick translations from global languages to specific local dialects. The intuitive chat-style interface ensures user-friendly navigation, catering to both tech aficionados and newcomers.

        **👈 Select an action from the dropdown on the left** to explore the capabilities of RTT.
        """
    )



def main():
    # Mapping page names to functions
    page_names_to_funcs = {
        "—": intro,
        "ChatBot": TranslateWords,
        "Translate Docs": uploadFile,
        "Supported Languages": DisplayLanguages
    }

    # Sidebar for page selection
    demo_name = st.sidebar.selectbox("Choose an Action", page_names_to_funcs.keys())

    # Execute the selected page/function
    page_names_to_funcs[demo_name]()

if __name__ == "__main__":
    main()
