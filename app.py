import streamlit as st

from chain import chain

st.set_page_config(
    page_title="Social Media Post Analyzer"
)

st.title("Social Media Post Analyzer")

st.write(
    "Analyze tone, intent, communication style, and summary."
)

user_input = st.text_area(
    "Enter Social Media Post"
)

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter a social media post.")

    else:

        try:

            result = chain.invoke({
                "post": user_input
            })

            st.subheader("Analysis Result")

            st.json(result.model_dump())

        except Exception as e:

            st.error(f"Error: {e}")