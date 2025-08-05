import json


# Step 1: Extract the code string from JSON


def extractor(json_response):
  print(type(json_response))
  parsed_json = json.loads(json_response)

  code_block = parsed_json["manim"]

  # Step 2: Strip the triple backticks and optional "python" label
  if code_block.startswith("```python"):
    code = code_block[9:-4].strip()
  elif code_block.startswith("```"):
    code = code_block[3:-3].strip()
  else:
    code = code_block.strip()
  print(code)
  return code


