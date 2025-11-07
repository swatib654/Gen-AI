import streamlit as st
import google.generativeai as genai

# -------------------- SETUP --------------------
st.set_page_config(page_title="Gen AI App", page_icon="🤖", layout="wide")
st.title("🤖 Generative AI App")
st.markdown("This app connects to **Google Gemini** for text generation!")

# Sidebar for API Key
st.sidebar.header("🔑 API Configuration")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("⚠️ Please enter your Gemini API Key in the sidebar to continue.")

# -------------------- USER INPUT --------------------
st.subheader("Enter your prompt or text:")
user_input = st.text_area("Prompt", placeholder="Type something like: 'Write a poem about AI'")

st.sidebar.header("⚙️ Settings")
temperature = st.sidebar.slider("Creativity (Temperature)", 0.0, 1.0, 0.7, 0.1)
max_output_tokens = st.sidebar.slider("Max output tokens", 50, 1000, 300, 50)

# -------------------- GENERATION --------------------
if st.button("Generate Response"):
    if not api_key:
        st.error("❌ Please enter your Gemini API key before generating.")
    elif not user_input.strip():
        st.warning("Please enter a prompt first.")
    else:
        with st.spinner("✨ Generating response..."):
            try:
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(
                    user_input,
                    generation_config=genai.types.GenerationConfig(
                        temperature=temperature,
                        max_output_tokens=max_output_tokens,
                    ),
                )

                st.success("✅ Response generated!")
                st.text_area("Output", response.text, height=300)
            except Exception as e:
                st.error(f"Error: {str(e)}")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Google Gemini API")
