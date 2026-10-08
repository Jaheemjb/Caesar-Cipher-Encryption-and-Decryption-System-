import sys

# =====================================================================
#             GLOBAL CONFIGURATIONS & INITIALIZATION
# =====================================================================
# The standard uppercase English alphabet used for the cipher mechanics
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# List acting as a historical log to store data dictionary records for each operation
session_history = []

# =====================================================================
#              PRIMARY ORCHESTRATION MENU LOOP
# =====================================================================
# Runs an infinite loop to handle user menu choices until an explicit exit is triggered
while True:
    print("\n" + "=" * 50)
    print("  CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM       ")
    print("=" * 50)
    print("1. Encrypt a Message")
    print("2. Decrypt a Message")
    print("3. Simulate Brute-Force Attack (Shifts 1-10)")
    print("4. View Session Encryption History")
    print("5. Exit System")
    print("=" * 50)
    
    # Catching manual script interrupts safely during standard menu choices
    try:
        choice = input("Select a menu option (1-5): ").strip()
    except KeyboardInterrupt:
        print("\n\n[WARNING] Forced termination detected. Exiting system context cleanly.")
        sys.exit(0)

    # -----------------------------------------------------------------
    # MENU OPTION 1: ENCRYPTION FEATURE
    # -----------------------------------------------------------------
    if choice == "1":
        print("\n--- ENCRYPTION FEATURE ---")
        text = input("Enter a message to encrypt: ")
        
        # Validating user input to ensure the shift key is an integer within range
        try:
            key = int(input("Choose a shift key (0-10): "))
            if not (0 <= key <= 10):
                print("[ERROR] Shift key must be between 0 and 10.")
                continue
        except ValueError:
            print("[ERROR] Invalid input. Key must be an integer.")
            continue

        # Core cryptographic engine execution logic for encryption
        encrypted_text = ""
        normalized_text = text.upper()
        for letter in normalized_text:
            if letter in ALPHABET:
                position = ALPHABET.index(letter)
                new_position = (position + key) % 26
                encrypted_text += ALPHABET[new_position]
            else:
                # Keeps spaces and punctuation exactly as they are
                encrypted_text += letter
                
        print(f"\nEncrypted Message: {encrypted_text}")
        
        # Save operation telemetry to history log
        session_history.append({
            "type": "Encryption",
            "original": text,
            "result": encrypted_text,
            "shift": key
        })

    # -----------------------------------------------------------------
    # MENU OPTION 2: DECRYPTION FEATURE
    # -----------------------------------------------------------------
    elif choice == "2":
        print("\n--- DECRYPTION FEATURE ---")
        text = input("Enter a message to decrypt: ")
        
        # Validating user input to ensure the shift key is an integer within range
        try:
            key = int(input("Choose a shift key (0-10): "))
            if not (0 <= key <= 10):
                print("[ERROR] Shift key must be between 0 and 10.")
                continue
        except ValueError:
            print("[ERROR] Invalid input. Key must be an integer.")
            continue

        # Core cryptographic engine execution logic for decryption
        decrypted_text = ""
        normalized_text = text.upper()
        for letter in normalized_text:
            if letter in ALPHABET:
                position = ALPHABET.index(letter)
                new_position = (position - key) % 26
                decrypted_text += ALPHABET[new_position]
            else:
                # Keeps spaces and punctuation exactly as they are
                decrypted_text += letter
                
        print(f"\nDecrypted Message: {decrypted_text}")
        
        # Save operation telemetry to history log
        session_history.append({
            "type": "Decryption",
            "original": text,
            "result": decrypted_text,
            "shift": key
        })

    # -----------------------------------------------------------------
    # MENU OPTION 3: BRUTE-FORCE SIMULATION
    # -----------------------------------------------------------------
    elif choice == "3":
        print("\n--- BRUTE-FORCE SIMULATION ---")
        text = input("Enter the encrypted message to crack: ")
        print("\nAttempting all possible shifts:")
        print("-" * 30)
        
        # Automatically loop and evaluate all potential shift key combinations (1 to 10)
        for shift in range(1, 11):
            attempt = ""
            normalized_text = text.upper()
            for letter in normalized_text:
                if letter in ALPHABET:
                    position = ALPHABET.index(letter)
                    new_position = (position - shift) % 26
                    attempt += ALPHABET[new_position]
                else:
                    attempt += letter
            print(f"Shift {shift:02d}: {attempt}")

    # -----------------------------------------------------------------
    # MENU OPTION 4: SESSION HISTORY LOG
    # -----------------------------------------------------------------
    elif choice == "4":
        print("\n--- SESSION HISTORY LOG ---")
        # Guard clause condition checks if any past computations exist
        if not session_history:
            print("No actions recorded in this session yet.")
            continue
            
        # Parse out and display telemetry blocks to the user interface
        for index, entry in enumerate(session_history, start=1):
            print(f"\nRecord #{index}")
            print(f"  Operation:  {entry['type']}")
            print(f"  Input Text: {entry['original']}")
            print(f"  Result:     {entry['result']}")
            print(f"  Shift Key:  {entry['shift']}")

    # -----------------------------------------------------------------
    # MENU OPTION 5: TERMINATE APPLICATION
    # -----------------------------------------------------------------
    elif choice == "5":
        print("\n Thank you for using CODE COBRAS CAESAR CIPHER SYSTEM. Goodbye! See you Soon!! :)")
        sys.exit(0)

    # -----------------------------------------------------------------
    # ERROR HANDLING: INVALID SELECTION
    # -----------------------------------------------------------------
    else:
        print("[ERROR] Selection out of bounds. Please input a choice between 1 and 5.")
