# 🧠 NLP2SQL

Convert natural language questions into SQL using a local LLM (Mistral 7B) and query a CSV-based employee dataset. This is Phase 1 of a multi-phase project toward an agent-based RAG system.

---

## 📁 Directory Structure

```bash
.  
├── cli_chat.py # Interactive CLI interface  
├── main.py # Entry point for CLI  
├── llm/ # Local model loading, tokenizer, prompt handling  
│ ├── loader.py  
│ ├── singleton.py  
│ ├── model/ # Mistral .gguf file  
│ ├── tokenizer/  
│ └── prompts/ # Custom prompt templates (coming soon)  
├── data/  
│ └── simple_employee.csv # Sample data for SQL queries  
├── schema/  
│ └── employee_schema.json # JSON schema of the dataset  
├── utils/  
│ └── chroma_utils.py # ChromaDB indexing and retrieval (coming soon)  
├── config.yaml # Configuration for future agents  
└── README.md # This file
````

---

## 🚀 Quickstart

### 1. Clone & Setup Environment

```bash
git clone https://github.com/adeptus-kanish/NLP2SQL
cd NLP2SQL
python -m venv ragenv
source ragenv/bin/activate
pip install -r requirements.txt
````

---

### 2. Place Model

Download a quantized `Mistral-7B-Instruct-v0.3` model (`.gguf`) and place it in:

```
llm/model/mistral-7b-instruct-v0.3-q4_k_m.gguf
```

---

### 3. Run the CLI

```bash
python main.py
```

You should see:

```
Welcome to the NLP2SQL CLI. Type 'exit' to quit.
💬 You:
```

---

## 💬 Sample Questions to Ask

- `List all employees from IT`
    
- `Who has the highest salary?`
    
- `Employees who joined after 2015`
    
- `Average salary of Sales department`
    

> The model responds with SQL, which will be used in future phases to run actual queries.

---

## 🛠️ Phase 1 Features

- Local inference using `mistral-7b-instruct`
    
- Prompt templates for SQL generation
    
- CLI-based interaction loop
    
- Basic prompt-to-LLM wrapper
    
- Employee CSV + JSON schema for grounding
    

---

## ✅ Next Phases (Planned)

- Phase 2: Integrate SQL execution
    
- Phase 3: ChromaDB-backed RAG
    
- Phase 4: Agent Orchestration (LLM + tools)
    
- Phase 5: REST API or UI for usage
    

---

## ⚠️ Known Issues

- Metal backend prints "not supported" warnings — safe to ignore on M1/M2 Macs.
    
- Prompt formatting errors may result in malformed SQL — check `PROMPT_TEMPLATE`.
    

---

## 👨‍🔧 Author

Built by [Kanish](https://github.com/kanish-h-h) — powered by Mistral and 🤗 Transformers.
