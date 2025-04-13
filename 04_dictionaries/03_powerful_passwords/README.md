# Password Manager

This project implements a secure password manager using SHA-256 hashing for authentication.

## Features
- Securely hash passwords before storing them.
- Authenticate users by matching hashed passwords.

## Setup Instructions

1. Ensure you have Python installed (Python 3 recommended).
2. Run the password manager using:
   ```bash
   python app.py
   ```

## How to Use
- Enter your email and password when prompted.
- If the credentials match, access is granted; otherwise, authentication fails.

## 🔑 Example Login Process

1. Run the script:
   ```bash
   python password_manager.py
   ```
2. Enter your email:
   ```
   Enter your email: example@gmail.com
   ```
3. Enter your password:
   ```
   Enter your password: password
   ```
4. If the credentials are correct, you'll see:
   ```
   Login successful!
   ```
   Otherwise, you'll get:
   ```
   Login failed. Invalid email or password.
   ```

## Stored Logins (Hashed Passwords)
| Email                      | Plain Password | SHA-256 Hashed Password |
|----------------------------|---------------|------------------------------------------------------------------|
| example@gmail.com          | password      | `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8` |
| code_in_placer@cip.org     | Karel         | `973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc` |
| student@stanford.edu       | 123!456?789   | `882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb` |

Try logging in using one of these emails and their corresponding passwords! 🚀🔐