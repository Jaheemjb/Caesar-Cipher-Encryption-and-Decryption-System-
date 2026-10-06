# Caesar-Cipher-Encryption-and-Decryption-System-
# Duo 7 Caesar Cipher System

A lightweight, terminal-based Python application that implements the classic **Caesar Cipher** encryption and decryption techniques. This system allows users to secure text messages, decode cipher text, perform brute-force analysis, and maintain a runtime log of session history.

---

## 🚀 Features

* **Secure Encryption:** Converts plaintext messages into ciphertext using custom shift keys (0–25).
* **Precise Decryption:** Reverses encrypted ciphertext back into readable plaintext with the corresponding key.
* **Brute-Force Simulation:** Cycles through all 25 possible alphabetic shifts to crack intercepted or unknown ciphers.
* **Live Session History:** Temporarily logs all active operations, maintaining record counts, original inputs, results, and shift configurations.
* **Robust Text Processing:** Automatically preserves spaces, numbers, and special punctuation marks during operations.

---

## 🛠️ Installation & Setup

### Prerequisites
* Ensure you have **Python 3.6 or higher** installed on your system.

### Running the Application
1. Download or copy the script file (e.g., `caesar_cipher.py`).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file and execute:

```bash
python caesar_cipher.py
```

---

## 📖 How To Use

When launched, the system presents an interactive command-line interface menu:

```text
==================================================
       DUO 7 CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-25)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5): 
```

### 1. Encryption
* Select Option `1`.
* Enter the message you want to encrypt.
* Input a numeric key shift between `0` and `25`.
* *Example:* `HELLO` with a shift of `3` becomes `KHOOR`.

### 2. Decryption
* Select Option `2`.
* Input your ciphertext.
* Input the exact numeric key shift used to encrypt it.
* *Example:* `KHOOR` with a shift of `3` yields `HELLO`.

### 3. Brute Force
* Select Option `3`.
* Input an unknown ciphertext.
* The system will print all 25 shift permutations sequentially so you can scan for the readable, original message.

### 4. Session History
* Select Option `4`.
* View an indexed list of every cryptographic conversion handled since the script was launched. *(Note: History resets when the script terminates).*

---

## 🔒 Error Handling & Safety
* **Input Validation:** Prevents application crashes from empty commands, decimal shift inputs, or entries exceeding the 0–25 bounds.
* **Graceful Termination:** Includes built-in support for `Ctrl + C` (KeyboardInterrupt), shutting down cleanly without raising unhandled Python system tracebacks.
