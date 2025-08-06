import json

def extractor(json_response: str) -> str:
    print("🔍 Raw LLM response (repr):", repr(json_response))

    # Step 1: Strip outer triple backticks and optional "json"
    if json_response.startswith("```json"):
        json_response = json_response[7:-3].strip()
    elif json_response.startswith("```"):
        json_response = json_response[3:-3].strip()

    print("🧼 Cleaned JSON string (repr):", repr(json_response))

    # Step 2: Parse JSON
    try:
        parsed_json = json.loads(json_response)
    except json.JSONDecodeError as e:
        print("❌ Failed to parse JSON:", e)
        raise

    # Step 3: Extract the Manim code block
    code_block = parsed_json.get("manim", "")
    if not code_block:
        raise ValueError("❌ 'manim' key not found or empty.")

    # Step 4: Strip inner ```python or ``` wrapper
    if code_block.startswith("```python"):
        code = code_block[9:-3].strip()
    elif code_block.startswith("```"):
        code = code_block[3:-3].strip()
    else:
        code = code_block.strip()

    print("✅ Extracted Manim Code:\n", code)
    return code
