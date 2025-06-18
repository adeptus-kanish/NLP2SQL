from llm.loader import LLMQueryEngine

_instance = None

def get_llm_instance():
    global _instance
    if _instance is None:
        _instance = LLMQueryEngine()
    return _instance
