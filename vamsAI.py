import streamlit as st
import openai
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
import os
from dotenv import load_dotenv

# Load the API keys from the .env file
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

if not google_api_key:
    st.error("Google API key not found. Please check your .env file.")
if not openai_api_key:
    st.error("OpenAI API key not found. Please check your .env file.")
else:
    # Set the API keys in the environment
    os.environ["GOOGLE_API_KEY"] = google_api_key
    openai.api_key = openai_api_key

    # Initialize the Google Generative AI model with specified safety settings
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            convert_system_message_to_human=True,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            },
        )
    except Exception as e:
        st.error(f"Failed to initialize the Google Generative AI model: {e}")
    else:
        st.set_page_config(
            page_title="Value Addition Management System",
            page_icon="📘"
        )

        # Apply custom CSS for the background color and layout
        st.markdown(
            """
            <style>
            .stApp {
                background-color: lime;
                padding:1px;
                margin:1px;
            }
            .text-response {
                background-color: white;
                padding: 1px;
                margin-bottom: 10px;
                border-radius: 5px;
            }
            .input-form {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
            }
            .input-field {
                width: 600px; /* Adjust the width as needed */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Streamlit app
        st.title("value addition management system")

        # Form for user input and submit button
        with st.form(key='search_form'):
            st.markdown('<div class="input-form">', unsafe_allow_html=True)
            search_prompt = st.text_area("Enter your prompt:", "given coffee, milk and bananas, suggest ways of combining them to end up with atleast six new product in increase their sales in a company.For each product suggested give a very clear procedure of preparing it and describe the best packaging image on each package product", key='search_input', height=150)
            submit_button = st.form_submit_button(label='Submit')
            st.markdown('</div>', unsafe_allow_html=True)

        # Apply custom CSS class to the search input
        st.markdown(
            """
            <style>
            #search_input {
                width: 600px; /* Adjust the width as needed */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # If the submit button is clicked
        if submit_button:
            # Check if the prompt is asking about the developer
            if "developer" in search_prompt.lower():
                st.markdown('<div class="text-response">value addition management members</div>', unsafe_allow_html=True)
            else:
                # Prompting the LLM
                try:
                    result = llm.invoke(search_prompt)
                    # Display the result in Streamlit
                    if result and hasattr(result, 'content'):
                        st.markdown(f'<div class="text-response">{result.content}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown('<div class="text-response">No result available or an error occurred.</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"An error occurred while invoking the LLM: {e}")

        # Form for image generation input and submit button
        with st.form(key='image_form'):
            st.markdown('<div class="input-form">', unsafe_allow_html=True)
            image_prompt = st.text_area("Enter a prompt to generate an image:", key='image_input')
            image_button = st.form_submit_button(label='Generate Image')
            st.markdown('</div>', unsafe_allow_html=True)

        # Apply custom CSS class to the image input
        st.markdown(
            """
            <style>
            #image_input {
                width: 400px; /* Adjust the width as needed */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # If the image button is clicked
        if image_button:
            try:
                response = openai.Completion.create(
                    model="image-davinci-002",
                    prompt=image_prompt,
                    n=1,
                    max_tokens=50
                )
                image_url = response['choices'][0]['text']
                st.image(image_url, caption='Generated Image', use_column_width=True)
            except Exception as e:
                st.error(f"An error occurred while generating the image: {e}")
