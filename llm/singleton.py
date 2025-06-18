# from llm.loader import LLMQueryEngine
from llm.loader import LocalLLM

_instance = None

def get_llm_instance():
    global _instance
    if _instance is None:
        # _instance = LLMQueryEngine()
        _instance = LocalLLM()
    return _instance
