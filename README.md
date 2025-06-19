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

## 📌 Real Use Case Examples

| User Query                                       | Action Type           |
| ------------------------------------------------ | --------------------- |
| “List all employees who joined before 2015”      | → SQL                 |
| “What is the meaning of join\_date?”             | → Vector search (RAG) |
| “Which columns are there in this dataset?”       | → Vector search (RAG) |
| “How many people joined in HR after 2010?”       | → SQL                 |
| “What’s the definition of bonus in this schema?” | → RAG                 |

---

## Phase 1

| Area                    | Status                          | Notes                                              |
| ----------------------- | ------------------------------- | -------------------------------------------------- |
| **Model Directory**     | ✅ `llm/model/`                  | `mistral-7b-instruct-v0.3-q4_k_m.gguf` is in place |
| **Local Loading Logic** | ✅ `loader.py` + `singleton.py`  | Loads the GGUF model via llama.cpp (with Metal)    |
| **Prompt Execution**    | ✅ Works end-to-end              | Generates SQL or freeform answers                  |
| **Data**                | ✅ `data/simple_employee.csv`    | Enough for mock evaluation                         |
| **Schema**              | ✅ `schema/employee_schema.json` | Good for later RAG (Phase 2)                       |
| **Utilities**           | ✅ `utils/chroma_utils.py`       | Placeholder for Chroma DB ops                      |
| **Virtual Env**         | ✅ `ragenv/`                     | Fully isolated environment                         |

---

## Phase 2

| Task                           | File                           | Description                                                                                |
| ------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------ |
| **1. Add SQLite DB**           | `data/employees.db` or similar | Create and populate a small SQLite database with dummy employee data (if not already done) |
| **2. Create SQL executor**     | `executor.py`                  | A module to execute SQL queries safely and return results or error messages                |
| **3. Connect executor to CLI** | `cli_chat.py`                  | After LLM outputs SQL, run it and show results                                             |
| **4. Handle exceptions**       | `executor.py` + `cli_chat.py`  | Show friendly error messages if SQL is invalid                                             |
| **5. Improve UX**              | `cli_chat.py`                  | Add a loop to ask for more queries until user exits                                        |

---

## Phase 3

| Step | Task                                             | Description                                       |
| ---- | ------------------------------------------------ | ------------------------------------------------- |
| 1    | Setup & store schema/query knowledge in ChromaDB | Index schema + sample queries                     |
| 2    | Add semantic retriever (`chroma_utils.py`)       | Flexible chunk search based on user query         |
| 3    | Decide route: LLM SQL vs RAG                     | Add router logic to use LLM or fallback to Chroma |
| 4    | Print clean result in CLI                        | RAG fallback answer if no SQL                     |

---

## 👨‍🔧 Author

Built by [Kanish](https://github.com/kanish-h-h) — powered by Mistral and 🤗 Transformers.
