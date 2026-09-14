import hashlib
from pyodide.http import open_url

def check_password_strength(password):
    # 1. Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # 2. Split the hash into prefix (first 5 chars) and suffix
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]
    
    # 3. Fetch data via browser's built-in fetch API (Pyodide compatible)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        data = open_url(url).read()
    except Exception as e:
        print("Error connecting to the API:", e)
        return 0
        
    # 4. Safely parse lines
    for line in data.splitlines():
        if ':' in line:
            h, count = line.split(':', 1)
            if h == suffix:
                return int(count)
    return 0

# Interactive Menu
print("--- Password Security Checker ---")
user_password = input("Enter a password to check: ")
count = check_password_strength(user_password)

if count:
    print(f"\n⚠️ DANGER: This password was found {count} times in data breaches!")
else:
    print("\n✅ SAFE: This password has not been found in known data breaches.")
