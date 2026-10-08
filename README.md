# CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 

A lightweight, terminal-based Python application that implements the classic **Caesar Cipher** encryption and decryption techniques. This system allows users to secure text messages, decode cipher text, perform brute-force analysis, and maintain a runtime log of session history.

---

## 🚀 Features

* **Secure Encryption:** Converts plaintext messages into ciphertext using custom shift keys (0–10).
* **Precise Decryption:** Reverses encrypted ciphertext back into readable plaintext with the corresponding key.
* **Brute-Force Simulation:** Cycles through all 25 possible alphabetic shifts to crack intercepted or unknown ciphers.
* **Live Session History:** Temporarily logs all active operations, maintaining record counts, original inputs, results, and shift configurations.
* **Robust Text Processing:** Automatically preserves spaces, numbers, and special punctuation marks during operations.

---

## 🛠️ Installation & Setup

### Prerequisites
* Ensure you have **Python 3.6 or higher** installed on your system or any online compiler.

### Running the Application
1. Download or copy the script file (e.g., `caesar_cipher.py`).
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file and execute:

```bash
python caesar_cipher.py
```
4. open Online-python.com in any browser and run the codes
---

## 📖 How To Use

When launched, the system presents an interactive command-line interface menu:

```text
==================================================
  CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5): 
```

### 1. Encryption
* Select Option `1`.
* Enter the message you want to encrypt.
* Input a numeric key shift between `0` and `10`.
* *Example:* `HELLO` with a shift of `3` becomes `KHOOR`.

```text
==================================================
 CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5):

Select a menu option (1-5): 1

--- ENCRYPTION FEATURE ---
Enter a message to encrypt: HELLO
Choose a shift key (0-10): 3

Encrypted Message: KHOOR
```

### 2. Decryption
* Select Option `2`.
* Input your ciphertext.
* Input the exact numeric key shift used to encrypt it.
* *Example:* `KHOOR` with a shift of `3` yields `HELLO`.

```text
==================================================
 CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5):

Select a menu option (1-5): 2

--- DECRYPTION FEATURE ---
Enter a message to decrypt: KHOOR
Choose a shift key (0-10): 3

Decrypted Message: HELLO
```
### 3. Brute Force
* Select Option `3`.
* Input an unknown ciphertext.
* The system will print all 11 shift permutations sequentially so you can scan for the readable, original message.

```text
==================================================
 CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5):

Select a menu option (1-5): 3

--- BRUTE-FORCE SIMULATION ---
Enter the encrypted message to crack: KHOOR

Attempting all possible shifts:
------------------------------
Shift 01: JGNNQ
Shift 02: IFMMP
Shift 03: HELLO
Shift 04: GDKKN
Shift 05: FCJJM
Shift 06: EBIIL
Shift 07: DAHHK
Shift 08: CZGGJ
Shift 09: BYFFI
Shift 10: AXEEH
```
### 4. Session History
* Select Option `4`.
* View an indexed list of every cryptographic conversion handled since the script was launched. *(Note: History resets when the script terminates).*


```text
==================================================
 CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5):

Select a menu option (1-5): 4

--- SESSION HISTORY LOG ---

Record #1
  Operation:  Encryption
  Input Text: HELLO
  Result:     KHOOR
  Shift Key:  3

Record #2
  Operation:  Decryption
  Input Text: KHOOR
  Result:     HELLO
  Shift Key:  3

```
---

### 5. Exit System

```text
==================================================
 CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM 
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5):

Select a menu option (1-5): 5

 Thank you for using CODE COBRAS CAESAR CIPHER SYSTEM. Goodbye! See you Soon!! :)


** Process exited - Return Code: 0 **

```
## 🔒 Error Handling & Safety

```text
==================================================
  CODE COBRAS CAESAR CIPHER CRYPTOGRAPHIC SYSTEM       
==================================================
1. Encrypt a Message
2. Decrypt a Message
3. Simulate Brute-Force Attack (Shifts 1-10)
4. View Session Encryption History
5. Exit System
==================================================
Select a menu option (1-5): r
[ERROR] Selection out of bounds. Please input a choice between 1 and 5.
```

* **Input Validation:** Prevents application crashes from empty commands, decimal shift inputs, or entries exceeding the 0–11 bounds.
* **Graceful Termination:** Includes built-in support for `Ctrl + C` (KeyboardInterrupt), shutting down cleanly without raising unhandled Python system tracebacks.
