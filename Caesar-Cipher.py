import sys

# Global configurations
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
session_history = []  # List to store history records

def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """Core cryptographic engine to process both encryption and decryption."""
    result = ""
    # Normalize input to uppercase to match the alphabet string
    text = text.upper()
    
    for letter in text:
        if letter in ALPHABET:
            position = ALPHABET.index(letter)
            if mode == "encrypt":
                new_position = (position + shift) % 26
            else:  # decrypt
                new_position = (position - shift) % 26
            result += ALPHABET[new_position]
        else:
            # Keeps spaces and punctuation exactly as they are
            result += letter
            
    return result

def run_encrypt_feature() -> None:
    """Handles the message encryption flow and records history."""
    print("\n--- ENCRYPTION FEATURE ---")
    text = input("Enter a message to encrypt: ")
    
    try:
        key = int(input("Choose a shift key (0-25): "))
        if not (0 <= key <= 25):
            print("[ERROR] Shift key must be between 0 and 25.")
            return
    except ValueError:
        print("[ERROR] Invalid input. Key must be an integer.")
        return

    encrypted_text = caesar_cipher(text, key, "encrypt")
    print(f"\nEncrypted Message: {encrypted_text}")
    
    # Save to history log
    session_history.append({
        "type": "Encryption",
        "original": text,
        "result": encrypted_text,
        "shift": key
    })

def run_decrypt_feature() -> None:
    """Handles the message decryption flow and records history."""
    print("\n--- DECRYPTION FEATURE ---")
    text = input("Enter a message to decrypt: ")
    
    try:
        key = int(input("Choose a shift key (0-25): "))
        if not (0 <= key <= 25):
            print("[ERROR] Shift key must be between 0 and 25.")
            return
    except ValueError:
        print("[ERROR] Invalid input. Key must be an integer.")
        return

    decrypted_text = caesar_cipher(text, key, "decrypt")
    print(f"\nDecrypted Message: {decrypted_text}")
    
    # Save to history log
    session_history.append({
        "type": "Decryption",
        "original": text,
        "result": decrypted_text,
        "shift": key
    })

def run_brute_force_feature() -> None:
    """Tests all possible shift configurations (1-25) to crack a message."""
    print("\n--- BRUTE-FORCE SIMULATION ---")
    text = input("Enter the encrypted message to crack: ")
    print("\nAttempting all possible shifts:")
    print("-" * 30)
    
    for shift in range(1, 26):
        attempt = caesar_cipher(text, shift, "decrypt")
        print(f"Shift {shift:02d}: {attempt}")

def run_history_feature() -> None:
    """Displays all cryptographic actions performed during the live session."""
    print("\n--- SESSION HISTORY LOG ---")
    if not session_history:
        print("No actions recorded in this session yet.")
        return
        
    for index, entry in enumerate(session_history, start=1):
        print(f"\nRecord #{index}")
        print(f"  Operation:  {entry['type']}")
        print(f"  Input Text: {entry['original']}")
        print(f"  Result:     {entry['result']}")
        print(f"  Shift Key:  {entry['shift']}")

def terminate_application() -> None:
    """Gracefully closes down the application context."""
    print("\n Thank you for using Duo 7 System. Goodbye! See you Soon!! :)")
    sys.exit(0)

def main_menu_loop() -> None:
    """Primary orchestration menu loop."""
    while True:
        print("\n" + "=" * 50)
        print("       DUO 7 CAESAR CIPHER CRYPTOGRAPHIC SYSTEM ")
        print("=" * 50)
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Simulate Brute-Force Attack (Shifts 1-25)")
        print("4. View Session Encryption History")
        print("5. Exit System")
        print("=" * 50)
        
        choice = input("Select a menu option (1-5): ").strip()
        
        if choice == "1":
            run_encrypt_feature()
        elif choice == "2":
            run_decrypt_feature()
        elif choice == "3":
            run_brute_force_feature()
        elif choice == "4":
            run_history_feature()
        elif choice == "5":
            terminate_application()
        else:
            print("[ERROR] Selection out of bounds. Please input a choice between 1 and 5.")

if __name__ == "__main__":
    try:
        main_menu_loop()
    except KeyboardInterrupt:
        print("\n\n[WARNING] Forced termination detected. Exiting system context cleanly.")
        sys.exit(0)
