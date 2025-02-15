
def parse_simple_string(data):
    if not data.startswith(b"+"):
        raise ValueError("Invalid RESP simple string: must start with '+'")
    return data[1:-2].decode()