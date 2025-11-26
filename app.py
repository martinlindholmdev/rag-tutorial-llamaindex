
import nest_asyncio
nest_asyncio.apply()

import streamlit as st
import os
from llama_index.core import StorageContext, load_index_from_storage

if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

SYSTEM_PROMPT = """Du är en varm och erfaren förälder som själv har barn med NPF. Du har läst boken "Pusselfamiljens verktyg för vardagshjältar" många gånger och delar gärna med dig av tipsen på ett personligt sätt.

Så här pratar du:
- Du säger "jag förstår" och "det känner jag igen" när det passar
- Du ger konkreta tips utan att låta som en manual
- Du är ärlig med att allt inte funkar för alla barn
- Du använder vardagligt språk, inte facktermer
- Du är uppmuntrande utan att vara klyschig
- Du håller dig kort och kärnfull – max 3-4 stycken

Svara ENDAST baserat på bokens innehåll. Om du inte hittar svaret i boken, säg det ärligt."""

st.set_page_config(page_title="NPF-pusslet", page_icon="🧩", layout="centered")

@st.cache_resource(show_spinner=False)
def load_index():
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    return index

# Huvudområde
st.markdown("# 🧩 NPF-pusslet")
st.markdown("")
st.markdown("""**Pusselfamiljens verktyg för vardagshjältar**  
*Om barn med ADHD och autism och pusslet som förenklar livet*""")
st.write("")
st.write("")
st.write("💬 Fråga boken:")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "OPENAI_API_KEY" in os.environ:
    try:
        index = load_index()
        query_engine = index.as_query_engine(system_prompt=SYSTEM_PROMPT, similarity_top_k=3, response_mode="compact")

        if prompt := st.chat_input("Skriv din fråga här..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Tänker..."):
                    response = query_engine.query(f"{prompt} Svara på svenska.")
                    st.markdown(response.response)
            
            st.session_state.messages.append({"role": "assistant", "content": response.response})

    except Exception as e:
        st.error(f"Ett fel inträffade: {e}")
else:
    st.error("API-nyckel saknas. Kontakta administratören.")
