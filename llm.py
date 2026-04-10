import ollama


def generate_code(prompt):
    full_prompt = f"""
    Write clean Python code for this request:
    {prompt}

    Only return code. No explanation.
    """

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": full_prompt}]
    )

    return response['message']['content']


def summarize_text(text):
    prompt = f"Summarize this clearly:\n{text}"

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


def detect_intent(text):
    prompt = f"""
    You are an intent classifier.

    ONLY return ONE of these EXACT words:
    create_file
    write_code
    summarize
    chat

    Do not explain.
    Do not add extra text.

    Input: {text}
    """

    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content'].strip().lower()