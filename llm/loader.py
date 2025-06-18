from llama_cpp import Llama
from utils.prompt_builder import build_prompt
import re

MODEL_PATH = "llm/model/mistral-7b-instruct-v0.3-q4_k_m.gguf"

class LLMQueryEngine:
    def __init__(self, model_path=MODEL_PATH):
        self.model = Llama(
            model_path=model_path,
            n_ctx=512,
            n_gpu_layers=-1,  # Use GPU (M2 Metal) if running out of VRAM use 20
            n_threads=6,
            n_batch=64,
            use_mlock=True,
            use_mmap=True,
            verbose=False   # Use True for debugging
        )

    def clean_sql(self, raw_output):
        match = re.search(r"(?i)(select|insert|update|delete).*?;", raw_output, re.DOTALL)
        return match.group(0).strip() if match else raw_output.strip()


    def generate_sql(self, user_question, max_tokens=200):
        prompt = build_prompt(user_question)
        output = self.model(
            prompt,
            max_tokens=max_tokens,
            stop=["SQL:", "\n\n", "<|end|>", "</s>"],
            echo=False,
            temperature=0.3,
        )
        sql_text = output['choices'][0]['text'].strip()
        return self.clean_sql(sql_text)
