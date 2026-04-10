import os

# ensure output folder exists
os.makedirs("output", exist_ok=True)

def create_file(filename):
    path = f"output/{filename}"
    with open(path, "w") as f:
        f.write("File created successfully")
    return f"Created {path}"


def write_code(filename, code):
    path = f"output/{filename}"
    with open(path, "w") as f:
        f.write(code)
    return f"Code written to {path}"


def summarize(text):
    return "Summary: " + text[:50]


def chat(text):
    return "Chat response: " + text