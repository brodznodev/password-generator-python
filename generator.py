import secrets
import string

def generate_password(length: int = 12) -> str:
    """
    Generate a secure random password.

    Rules:
    - Minimum length: 12 characters
    - Must contain at least one uppercase, one lowercase, one digit, and one special character
    - Avoids common weak words and obvious sequences
    """
    
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lowercase + uppercase + digits + special
    common_patterns = [
        "password", "123456", "qwerty", "abc123", "letmein", "iloveyou", "admin", "welcome", "monkey", "dragon"
    ]

    def has_sequence(s, min_len=4):
        # Detecta secuencias alfabéticas y numéricas ascendentes
        for i in range(len(s) - min_len + 1):
            sub = s[i:i+min_len]
            # Alfabéticas
            if sub.isalpha():
                ords = [ord(c) for c in sub]
                if all(ords[j] == ords[j-1] + 1 for j in range(1, min_len)):
                    return True
            # Numéricas
            if sub.isdigit():
                nums = [int(c) for c in sub]
                if all(nums[j] == nums[j-1] + 1 for j in range(1, min_len)):
                    return True
        return False

    def has_repetition(s, min_len=4):
        # Detecta repeticiones simples
        for i in range(len(s) - min_len + 1):
            sub = s[i:i+min_len]
            if len(set(sub)) == 1:
                return True
        return False

    while True:
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(special)
        ]
        password += [secrets.choice(all_characters) for _ in range(length - 4)]
        secrets.SystemRandom().shuffle(password)
        password_str = ''.join(password)

        password_str_lower = password_str.lower()
        patterns_lower = [pattern.lower() for pattern in common_patterns]

        # Validaciones
        if any(word in password_str_lower for word in patterns_lower):
            continue
        if has_sequence(password_str_lower):
            continue
        if has_repetition(password_str_lower):
            continue
        # Si pasa todas las validaciones, retorna
        return password_str

# Example usage
if __name__ == "__main__":
    try:
        print(generate_password(16))
    except ValueError as e:
        print(f"Error: {e}")