# build_index.py

import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter

os.environ["OPENAI_API_KEY"] = "ERSÄTT-MED-DIN-NYCKEL-VID-KÖRNING"

print("📚 Läser in boken från ./data ...")
documents = SimpleDirectoryReader("data").load_data()
print(f"   Hittade {len(documents)} dokument.")

print("🔪 Delar upp i chunks...")
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)
print(f"   Skapade {len(nodes)} chunks.")

print("🧠 Skapar index...")
index = VectorStoreIndex(nodes)

print("💾 Sparar index till ./storage ...")
index.storage_context.persist(persist_dir="./storage")

print("")
print("✅ KLART!")
