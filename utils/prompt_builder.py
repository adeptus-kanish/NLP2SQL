import json

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    return schema

def format_schema(schema):
    lines = [f"Assume the table name is `{schema['table']}` and it has the following columns:"]
    for col in schema["columns"]:
        lines.append(f"- {col['name']} ({col['type']})")
    return  "\n".join(lines)


def build_prompt(user_question, schema_path="schema/employee_schema.json"):
    schema = load_schema(schema_path)
    schema_string = format_schema(schema)

    prompt = f"""
    You are an expert SQL developer, Given a user's natural language question, write only the corresponding SQL query.
    Only respond with a single SQL query in code format. Do not add explanation or examples.
    {schema_string}

    Respond with only valid SQL code and no extra explanation.

    User Question: {user_question}

    SQL:
    """.strip()
    return prompt
