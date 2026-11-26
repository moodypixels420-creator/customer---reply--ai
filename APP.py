
import streamlit as st
import google.generativeai as genai

# This tells the app to look for the key in Streamlit's secret settings
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# Streamlit page settings
st.set_page_config(
    page_title="Customer Review Reply Generator",
    page_icon="💬",
    layout="centered"
)

# Application heading
st.title("💬 Customer Review Reply Generator")

st.write(
    "Paste a customer review below and let AI "
    "generate a polite and professional response."
)

st.divider()

# Customer review input
review = st.text_area(
    "Enter Customer Review:",
    placeholder="Paste the customer's review here...",
    height=180
)

# Generate reply button
if st.button("Generate Reply", type="primary"):


    if not review.strip():
        st.warning("Please enter a customer review first.")

    else:
        try:
            with st.spinner("Generating your reply..."):

                # Select Gemini model
                model = genai.GenerativeModel(
                    "gemini-1.5-flash"
                )

                # Create prompt
                prompt = f"""
                You are a professional customer service representative.

                Read the following customer review and write
                a polite, friendly, and professional reply.

                Instructions:
                1. Thank the customer for their feedback.
                2. Address their experience appropriately.
                3. Keep the reply natural and concise.
                4. If the review is negative, show empathy.
                5. Do not make promises that the business
                   has not authorized.

                Customer Review:
                {review}

                Write only the reply.
                """

                # Generate response using Gemini
                response = model.generate_content(prompt)

                # Display generated reply
                st.success("Reply generated successfully!")

                st.subheader("Generated Customer Reply")

                st.write(response.text)

                # Download reply
                st.download_button(
                    label="Download Reply",
                    data=response.text,
                    file_name="customer_reply.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

st.caption("Powered by Streamlit and Google Gemini AI")
