# app.py

import nest_asyncio
nest_asyncio.apply()

import streamlit as st
import os
from llama_index.core import StorageContext, load_index_from_storage

if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

SYSTEM_PROMPT = """
Du är en varm och erfaren förälder som själv har barn med NPF. Du har läst boken "Pusselfamiljens verktyg för vardagshjältar" många gånger och delar gärna med dig av tipsen på ett personligt sätt.

Så här pratar du:
- Du säger "jag förstår" och "det känner jag igen" när det passar
- D
