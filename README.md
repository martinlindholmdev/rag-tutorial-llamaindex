
# 🧩 NPF-pusslet - RAG-applikation

En AI-driven kunskapsassistent byggd med **Retrieval-Augmented Generation (RAG)** som svarar på frågor om boken "Pusselfamiljens verktyg för vardagshjältar" - om barn med ADHD, autism och pusslet som förenklar livet.

## 🎯 Om projektet

Detta projekt startade som en övning från min mentor **Mats**, där jag fick lära mig grunderna i RAG med en enkel Jupyter Notebook. Jag utvecklade sedan konceptet till en fullfjädrad webbapplikation med Streamlit.

**Vad är RAG?**
- **Retrieval:** Hämtar relevant information från dokumentet
- **Augmented:** Förstärker AI:n med specifik kunskap
- **Generation:** Genererar exakta svar baserade på källan

## 📁 Projektstruktur

```
rag-tutorial-llamaindex/
├── simple_rag_notebook-checkpoint.ipynb  # Original övning från Mats
├── app.py                                 # Streamlit webbapp
├── build_index.py                         # Script för att bygga index
├── data/                                  # PDF/TXT/DOCX källor
├── storage/                               # Vektorindex (genereras automatiskt)
├── requirements.txt                       # Python-beroenden
├── .gitignore                             # Git-undantag
└── README.md                              # Denna fil
```

## 🚀 Två sätt att använda projektet

### **1. Jupyter Notebook (Original övning)**

**Krav:**
- Anaconda Navigator installerad
- OpenAI API-nyckel ([skaffa här](https://platform.openai.com/launch))
- Några dollar på OpenAI-kontot för tokens
- Din kunskapskälla (PDF, TXT eller DOCX)

**Steg:**
1. Installera **Anaconda Navigator** från [anaconda.com](https://www.anaconda.com/products/navigator)
2. Skapa mapp `data/` och lägg din fil där
3. Öppna Anaconda Navigator → Installera **Jupyter Labs**
4. Starta Jupyter Labs
5. Öppna `simple_rag_notebook-checkpoint.ipynb`
6. Lägg till din OpenAI API-nyckel i cell [2]
7. Kör cellerna steg för steg

**⚠️ Notering:** Vektordatabasen byggs om vid varje körning (använder tokens). För produktion, använd persistent storage.

---

### **2. Streamlit Webbapp (Deployment-klar)**

**Krav:**
- Python 3.8+
- OpenAI API-nyckel

**Installation:**
```bash
# Klona repot
git clone [ditt-repo-url]
cd rag-tutorial-llamaindex

# Installera dependencies
pip install -r requirements.txt

# Lägg till API-nyckel
# Skapa .streamlit/secrets.toml:
# OPENAI_API_KEY = "din-nyckel-här"

# Kör lokalt
streamlit run app.py
```

**Deploy till Streamlit Cloud:**
1. Pusha till GitHub
2. Gå till [share.streamlit.io](https://share.streamlit.io)
3. Anslut repot
4. Lägg till `OPENAI_API_KEY` i Secrets
5. Deployas automatiskt! 🎉

## 🛠️ Teknisk Stack

| Komponent | Teknologi |
|-----------|-----------|
| **RAG Framework** | LlamaIndex |
| **LLM** | OpenAI GPT-3.5-turbo |
| **Frontend** | Streamlit |
| **Vektorlagring** | Local Disk (SimplePersistStorage) |
| **Deployment** | Streamlit Cloud |

## 📖 Hur det fungerar

1. **Indexering:** Dokumentet läses in och delas upp i "chunks"
2. **Embeddings:** Varje chunk omvandlas till vektorer
3. **Lagring:** Vektorindex sparas lokalt i `storage/`
4. **Query:** Användarfråga matchas semantiskt mot index
5. **Retrieval:** Relevanta chunks hämtas
6. **Generation:** GPT genererar svar baserat på hämtad kontext

## 🎓 Lärdomar

- **RAG eliminerar AI-hallucinationer** genom att förankra svar i källor
- **LlamaIndex förenklar RAG-utveckling** enormt (jämfört med att bygga från scratch)
- **Persistent storage** är kritiskt för produktion (undvik onödiga token-kostnader)
- **Streamlit** gör det extremt enkelt att deploya Python-appar

## 🙏 Tack till

**Mats** - för den perfekta introduktionen till RAG och LlamaIndex!

## 📚 Resurser

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Vector Stores Guide](https://developers.llamaindex.ai/python/framework/module_guides/storing/vector_stores/)
- [OpenAI API Reference](https://platform.openai.com/docs)

## 📝 Licens

Detta är ett utbildningsprojekt. Använd och modifiera fritt!

---

**Byggt med ❤️ och AI-magi 🤖**
