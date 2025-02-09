def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

if __name__ == "__main__":
    while True:
        mode = input("Do you want to encrypt or decrypt? (Type 'encrypt' or 'decrypt'): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter your message: ")
        shift = int(input("Enter shift value (integer): "))
        
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
        
        another = input("Do you want to run again? (yes/no): ").strip().lower()
        if another != 'yes':
            break
