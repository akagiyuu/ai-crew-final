def required_input(prompt: str) -> str:
    result = ""
    while result == "":
        result = input(prompt)

    return result
