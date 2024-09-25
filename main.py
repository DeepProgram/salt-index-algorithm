import base64

def encode_with_salt(payload: str, salt_key: str, salt_index: int) -> str:
    if salt_index < 0 or salt_index > len(payload):
        raise ValueError("Salt index is out of bounds")
    salted_payload = payload[:salt_index] + salt_key + payload[salt_index:]
    base64_encoded = base64.b64encode(salted_payload.encode('utf-8')).decode('utf-8')
    return base64_encoded

def decode_with_salt(encoded_payload: str, salt_key: str, salt_index: int) -> str:
    decoded_payload = base64.b64decode(encoded_payload).decode('utf-8')
    if decoded_payload[salt_index:salt_index + len(salt_key)] != salt_key:
        raise ValueError("Invalid salt key or index, decoding failed")
    original_payload = decoded_payload[:salt_index] + decoded_payload[salt_index + len(salt_key):]
    return original_payload
