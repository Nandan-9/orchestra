def validate_python_code(code_str: str) -> bool:
    try:
        compile(code_str, "<string>", "exec")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax Error: {e}")
        return False


