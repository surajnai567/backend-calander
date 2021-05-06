import hashlib

def make_password(password):
    assert password
    hash = hashlib.md5(password).hexdigest()
    return hash

def check_password(hash, password):
    """Generates the hash for a password and compares it."""
    generated_hash = make_password(password)
    return hash == generated_hash

print(type(make_password('hi'.encode())))