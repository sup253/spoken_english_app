import streamlit as st
from gtts import gTTS
import os
import tempfile
import openai

# Uncomment if you're using OpenAI's GPT for conversation
# openai.api_key = "your-openai-api-key"

st.set_page_config(page_title="Spoken English Learning", layout="wide")

st.title("🗣️ SpeakEasy: Your Spoken English Mentor")
st.write("Practice vocabulary, pronunciation, conversation, and more!")

# ----------------------------
# Vocabulary Section
# ----------------------------
st.header("📚 Vocabulary Builder")
vocab_list = {
    "Aberration": "A departure from what is normal or expected",
    "Benevolent": "Well-meaning and kindly",
    "Candid": "Truthful and straightforward",
    "Diligent": "Having or showing care in one’s work or duties"
}
selected_word = st.selectbox("Pick a word to learn:", list(vocab_list.keys()))
st.write(f"**Meaning**: {vocab_list[selected_word]}")

if st.button("🔊 Listen to pronunciation"):
    tts = gTTS(selected_word)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")

# ----------------------------
# Sentence Practice
# ----------------------------
st.header("✍️ Sentence Formation Practice")
user_sentence = st.text_input("Try using the selected word in a sentence:")
if user_sentence:
    st.success(f"Great! You wrote: '{user_sentence}'")

# ----------------------------
# AI-based Conversation (Optional)
# ----------------------------
st.header("🤖 Practice Conversation with AI")
prompt = st.text_area("Ask me anything or say something you'd like to translate or improve in English:")

if st.button("💬 Get AI Response"):
    if prompt.strip():
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You are an English speaking tutor helping learners improve their spoken English."},
                    {"role": "user", "content": prompt}
                ]
            )
            ai_reply = response['choices'][0]['message']['content']
            st.markdown(f"**AI:** {ai_reply}")
    else:
        st.warning("Please type something to start the conversation.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("👩‍🏫 Developed with ❤️ for Spoken English Learners")

