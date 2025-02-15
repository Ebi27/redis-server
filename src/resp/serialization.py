

def serialize_simple_string(message):
    if not isinstance(message, str):
        raise TypeError("Input must be a string.")
    return f"+{message}\r\n".encode()