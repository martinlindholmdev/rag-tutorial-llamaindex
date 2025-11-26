
# 🧩 NPF-pusslet - RAG Application

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![LlamaIndex](https://img.shields.io/badge/llamaindex-latest-orange.svg)

An AI-powered knowledge assistant built with **Retrieval-Augmented Generation (RAG)** that answers questions about the book "Pusselfamiljens verktyg för vardagshjältar" - about children with ADHD, autism, and the puzzle that simplifies life.

## 🚀 Live Demo

Try it here: **[npf-pusslet.streamlit.app](https://npf-pusslet.streamlit.app/)**

## 🎯 About the Project

This project demonstrates the power of RAG (Retrieval-Augmented Generation) by building a knowledge assistant that can answer questions about a specific book with accuracy and source citations.

**What is RAG?**
- **Retrieval:** Fetches relevant information from the document
- **Augmented:** Enhances the AI with specific knowledge
- **Generation:** Generates accurate answers based on the source

## 📁 Project Structure

```
rag-tutorial-llamaindex/
├── simple_rag_notebook.ipynb             # Jupyter notebook implementation
├── app.py                                 # Streamlit web app
├── build_index.py                         # Script to build index
├── data/                                  # PDF/TXT/DOCX sources
├── storage/                               # Vector index (auto-generated)
├── requirements.txt                       # Python dependencies
├── .gitignore                             # Git exclusions
└── README.md                              # This file
```

## 🚀 Two Ways to Use the Project

### **1. Jupyter Notebook (Learning & Experimentation)**

**Requirements:**
- Anaconda Navigator installed
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- A few dollars in your OpenAI account for tokens
- Your knowledge source (PDF, TXT, or DOCX)

**Steps:**
1. Install **Anaconda Navigator** from [anaconda.com](https://www.anaconda.com/products/navigator)
2. Create a `data/` folder and place your file there
3. Open Anaconda Navigator → Install **Jupyter Labs**
4. Launch Jupyter Labs
5. Open `simple_rag_notebook.ipynb`
6. Add your OpenAI API key in cell [2]
7. Run the cells step by step

**⚠️ Note:** The vector database is rebuilt on every run (uses tokens). For production, use persistent storage.

---

### **2. Streamlit Web App (Production-Ready)**

**Requirements:**
- Python 3.8+
- OpenAI API key

**Installation:**
```bash
# Clone the repo
git clone https://github.com/martinlindholmdev/rag-tutorial-llamaindex.git
cd rag-tutorial-llamaindex

# Install dependencies
pip install -r requirements.txt

# Add API key - Create .streamlit/secrets.toml:
mkdir -p .streamlit
echo 'OPENAI_API_KEY = "sk-your-key-here"' > .streamlit/secrets.toml

# Run locally
streamlit run app.py
```

**Deploy to Streamlit Cloud:**
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect the repo
4. Add `OPENAI_API_KEY` in Secrets
5. Deploys automatically! 🎉

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **RAG Framework** | LlamaIndex |
| **LLM** | OpenAI GPT-3.5-turbo |
| **Frontend** | Streamlit |
| **Vector Storage** | Local Disk (SimplePersistStorage) |
| **Deployment** | Streamlit Cloud |

## 📖 How It Works

1. **Indexing:** The document is loaded and split into "chunks"
2. **Embeddings:** Each chunk is converted to vectors using OpenAI's embedding model
3. **Storage:** Vector index is saved locally in `storage/`
4. **Query:** User question is semantically matched against the index
5. **Retrieval:** Most relevant chunks are fetched
6. **Generation:** GPT generates an answer based on retrieved context with source citations

## 🎓 Key Features

- ✅ **Accurate answers** grounded in source material
- ✅ **Source citations** for transparency
- ✅ **Persistent storage** to avoid rebuilding index
- ✅ **Simple deployment** with Streamlit Cloud
- ✅ **Cost-efficient** token usage

## 🎓 Lessons Learned

- **RAG eliminates AI hallucinations** by grounding answers in sources
- **LlamaIndex simplifies RAG development** enormously (compared to building from scratch)
- **Persistent storage** is critical for production (avoid unnecessary token costs)
- **Streamlit** makes it extremely easy to deploy Python apps

## 📚 Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Vector Stores Guide](https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores.html)
- [OpenAI API Reference](https://platform.openai.com/docs)

## 📬 Contact

- **GitHub:** [@martinlindholmdev](https://github.com/martinlindholmdev)
- **Email:** martin.lindholm.dev@gmail.com
- **Live Demo:** [npf-pusslet.streamlit.app](https://npf-pusslet.streamlit.app/)

## 📝 License

This is an educational project. Feel free to use and modify!

---

**Built with ❤️ and AI magic 🤖**
