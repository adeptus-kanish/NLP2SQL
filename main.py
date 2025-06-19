from llm.singleton import get_llm_instance
from utils.chroma_utils import ChromaVectorStore

# 1. Load the local mistral model (GGUF)
llm = get_llm_instance()

# 2. Send a natural language instruction
# user_input = "List employees who joined after 2019"
user_input = "list all the employees"

prompt = f"""You are a SQL expert. Convert the following natural language question to SQL only.
             Do not exlain anything, just SQL query
             Question: {user_input}

             SQL:"""

# 3. Generate SQL output from LLM
sql_query = llm.generate_sql(prompt)

print("\n🧠 Input:", user_input)
print("\nGenerated SQL:\n", sql_query)

# 4. (Optional) Lookup schema-related context from Chroma
# store = ChromaVectorStore()
# results = store.query(user_input)
# print("\nRetrieved Chroma context:\n", results)


# from cli_chat import cli_loop
#
# if __name__ == "__main__":
#     cli_loop()
