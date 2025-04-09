import ast
from transformers import pipeline

# Load model once
comment_generator = pipeline("text-generation", model="distilgpt2")

def generate_comment(code: str) -> str:
    prompt = f"'''Explain the following code:\n{code}\n'''"
    result = comment_generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]['generated_text']

def check_syntax(code: str) -> str:
    try:
        ast.parse(code)
        return "✅ No syntax errors found!"
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"
