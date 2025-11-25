import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# --- SYSTEM PROMPT: Den Raka Rösten ---
SYSTEM_PROMPT = """
Du är Bokens Röst och agerar som en rak, handlingsorienterad NPF-expert. Ditt enda mål är att leverera omedelbara, konkreta strategier och tips för vardagssituationer kopplade till NPF, baserat EXKLUSIVT på bokens innehåll. Använd ett stärkande, direkt tilltal (du/ni). Svara med tydliga, punktade steg eller korta stycken. Avsluta alltid med en kort uppmuntrande punchline.
"""

# 3. Load Data & Create Index (Cached for Speed)
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner("Läser in boken och skapar index... (Detta sker bara en gång)"):
        # Läs dokumenten från mappen 'data'
        documents = SimpleDirectoryReader("data").load_data()
        # Skapa det sökbara indexet
        index = VectorStoreIndex.from_documents(documents)
        return index

# 4. Main Chat Logic
# OBS: Denna logik använder den SYSTEM_PROMPT du definierade högst upp i filen.
if "OPENAI_API_KEY" in os.environ:
    try:
        # Ladda indexet (använder cache om det redan är klart)
        index = load_data() 
        
        # Skapa sökmotorn och injicera den stärkande personligheten
        query_engine = index.as_query_engine(
            system_prompt=SYSTEM_PROMPT
        )

        # User Input (Uppdaterad till den action-orienterade prompten)
        question = st.text_input(
            "Vad behöver du hjälp med just nu?", 
            placeholder="T.ex. Hur fixar jag läggningspusslet? Eller: Vilka är de 3 viktigaste verktygen?"
        )

        # Generate Answer
        if question:
            with st.spinner("AI:n tänker..."):
                # Force Swedish response
                response = query_engine.query(f"{question} Svara på svenska.")
                
                # Display Result
                st.markdown("### 🤖 Svar:")
                st.write(response.response)

    except Exception as e:
        st.error(f"Ett fel inträffade: {e}")