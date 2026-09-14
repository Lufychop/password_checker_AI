# Gemini 3.6
# 🛡️ Password Security Checker

A lightweight, privacy-focused Python utility that checks if a password has been compromised in known data breaches. Built to demonstrate API integration, hashing algorithms, and privacy-preserving protocols.

## 🚀 Key Features
* **Zero-Knowledge Architecture:** Never transmits plaintext passwords over the internet.
* **k-Anonymity Privacy:** Employs the *Have I Been Pwned* API model—only sending the first 5 characters of the password hash to ensure complete confidentiality.
* **Instant Breach Detection:** Queries a database of billions of leaked credentials in real-time.

## ⚙️ How It Works (k-Anonymity)
1. The script hashes the user's password using **SHA-1**.
2. The hash is split: the first 5 characters (**prefix**) are sent to the HIBP API.
3. The API returns a list of all leaked password hashes sharing that same prefix.
4. The local script checks if the remaining hash characters (**suffix**) exist in the API response.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** `hashlib`, `pyodide.http` (WebAssembly compatible)
* **API:** [Have I Been Pwned Passwords API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange)

## 📌 Usage
Run the script in any Python environment (including Pyodide / browser-based Python runners):

```python
python passcheck.py
