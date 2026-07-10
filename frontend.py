import streamlit as st
import requests

# -------------------------------
# Railway Backend URL
# -------------------------------

API_URL = "https://intelligent-document-query-system-production.up.railway.app"

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Intelligent Document Query System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Intelligent Document Query System")
st.write("Upload a PDF and ask questions using AI.")

# -------------------------------
# Session State
# -------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

# -------------------------------
# Upload PDF
# -------------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Upload"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        with st.spinner("📤 Uploading PDF..."):

            try:

                response = requests.post(
                    f"{API_URL}/upload",
                    files=files,
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    st.success("✅ PDF uploaded successfully!")

                    st.write(f"**Filename:** {data['filename']}")
                    st.write(f"**Chunks Created:** {data['total_chunks']}")

                    st.session_state.uploaded = True

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(f"Upload failed:\n\n{e}")

st.divider()

# -------------------------------
# Ask Question
# -------------------------------

question = st.text_input("Ask a question")

if st.button("Ask AI"):

    if not st.session_state.uploaded:

        st.warning("⚠ Please upload a PDF first.")

    elif question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("🤖 Thinking..."):

            try:

                response = requests.post(
                    f"{API_URL}/query",
                    json={
                        "question": question
                    },
                    timeout=300
                )

                if response.status_code == 200:

                    data = response.json()

                    answer = data["answer"]
                    chunks = data["chunks"]

                    st.session_state.messages.append(
                        {
                            "role": "user",
                            "content": question
                        }
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "chunks": chunks
                        }
                    )

                else:

                    st.error(response.text)

            except Exception as e:

                st.error(f"Query failed:\n\n{e}")

# -------------------------------
# Conversation
# -------------------------------

if st.session_state.messages:

    st.subheader("💬 Conversation")

    for message in st.session_state.messages:

        if message["role"] == "user":

            with st.chat_message("user"):

                st.write(message["content"])

        else:

            with st.chat_message("assistant"):

                st.write(message["content"])

                if "chunks" in message:

                    with st.expander("📄 Retrieved Context"):

                        for i, chunk in enumerate(message["chunks"], start=1):

                            st.markdown(f"### Chunk {i}")

                            st.caption(
                                f"Similarity Score: {chunk['similarity']:.2f}%"
                            )

                            st.write(chunk["text"])

                            st.divider()
