from llm.singleton import get_llm_instance

def cli_loop():
    llm = get_llm_instance()
    print("Welcome to the NLP2SQL CLI. Type 'exit' to quit.")
    while True:
        query = input("\n💬 You: ")
        if query.strip().lower() in ["exit", "quit"]:
            break
        sql = llm.generate_sql(query)
        print("\n🧠 SQL:\n", sql)

if __name__ == "__main__":
    cli_loop()
