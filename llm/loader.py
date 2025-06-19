from llama_cpp import Llama
from utils.prompt_builder import build_prompt
import re
import os
import sys
import contextlib
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

MODEL_PATH = config["llm"]["model_path"]

# suppress verbose for Metal backend logs (llama.cpp backend)
@contextlib.contextmanager
def suppress_stderr():
    with open(os.devnull, 'w') as devnull:
        old_stderr = sys.stderr
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stderr = old_stderr

class LLMQueryEngine:
    def __init__(self, model_path=MODEL_PATH):
        with suppress_stderr():
            self.model = Llama(
                model_path=model_path,
                n_ctx=config["llm"]["n_ctx"],
                n_gpu_layers=config["llm"]["n_gpu_layers"],  # Use GPU (M2 Metal) if running out of VRAM use 20
                n_threads=config["llm"]["n_threads"],
                n_batch=config["llm"]["n_batch"],
                use_mlock=config["llm"]["use_mlock"],
                use_mmap=config["llm"]["use_mmap"],
                verbose=config["llm"]["verbose"]   # Use True for debugging
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
