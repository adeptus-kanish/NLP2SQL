from llama_cpp import Llama

class LocalLLM:
    def __init__(self, model_path="llm/model/mistral-7b-instruct-v0.3-q4_k_m.gguf"):
        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_gpu_layers=20,  # Use GPU (M2 Metal)
            n_threads=4,
            use_mlock=True,
            use_mmap=True
        )

    def generate(self, prompt, max_tokens=200):
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=["<|end|>", "</s>"],
            echo=False,
            temperature=0.7,
        )
        return output['choices'][0]['text'].strip()


# import os
# from llama_cpp import Llama
#
# MODEL_PATH = "llm/model/mistral-7b-instruct-v0.3-q4_k_m.gguf"
#
# with open('llm/prompts/sql_prompt.txt', 'r') as f:
#     PROMPT_TEMPLATE = f.read()
#
# class LLMQueryEngine:
#     def __init__(self, model_path=MODEL_PATH, max_tokens=256):
#         self.llm = Llama(
#             model_path=model_path,
#             n_ctx=2048,
#             n_gpu_layers=20,  # Use GPU (M2 Metal)
#             n_threads=4,
#             use_mlock=True,
#             use_mmap=True
#
#             # use_mmap=True
#             # model_path=model_path,
#             # n_ctx=2048,
#             # n_threads=4,
#             # use_mlock=True,
#             # n_gpu_layers=-1,
#             # n_batch=64,
#             # use_mmap=True,
#             # verbose=False
#         )
#         self.max_tokens = max_tokens
#
#     # def load_prompt(self, nl_query):
#     #     with open("llm/prompts/sql_prompt.txt", "r") as f:
#     #         prompt_template = f.read()
#     #     return prompt_template.replace("{{query}}", nl_query)
#
#     def generate_sql(self, nl_query):
#         # full_prompt = self.load_prompt(nl_query)
#         # full_prompt = PROMPT_TEMPLATE.format(question=nl_query)
#         # output = self.llm(
#         #     full_prompt,
#         #     max_tokens=self.max_tokens,
#         #     stop=["\n\n", "\nSQL"],
#         #     echo=False
#         # )
#         response = self.llm(full_prompt)
#         return response['choices'][0]['text'].strip()
