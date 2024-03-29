# Password-Manager
This is a simple password manager system, built in Python using the 'cryptography' library for encryption. It allows users to securely store and manage their passwords along with their username for different applications.

## Features
<ul>
  <li><strong>Add:</strong> Add a new entry with the application name, username, and password.</li>
  <li><strong>View:</strong> View all existing entries with their details.</li>
  <li><strong>Update:</strong> Update an existing entry with new details.</li>
  <li><strong>Delete:</strong> Delete an existing entry.</li>
  <li><strong>Encryption:</strong> Passwords are encrypted using the Fernet symmetric encryption method.</li>
  <li><strong>Master Password:</strong> Users must enter a master password to access the password manager.</li>
</ul>

## How to Use
<ol>
  <li>Clone the repository: git clone https://github.com/SatishKumar1911/Password-Manager.git</li>
  <li>Select python interpreter: ./venv/bin/python</li>
  <li>Activate virtual environment: ./venv/bin/activate</li>
  <li>Install cryptography: pip install -r requirenment.txt or pip install cryptography</li>
  <li>Run generate_key.py file manually once before running the password_manage.py: python generate_key.py</li>
  <li>Now a key will be generated inside the key.key</li>
  <li>Run generate_password.py: python generate_password.py</li>
</ol>

## Dependencies
<ul>
  <li>cryptography
</li>
</ul>

## Notes
<ul>
  <li>Make sure to keep the 'key.key' file safe as it is used for encryption and decryption.</li>
  <li>Do not share your 'master password' or the 'key.key' file.</li>
</ul>

## Screenshots
### Master Password
![first](https://github.com/SatishKumar1911/Password-Manager/assets/124880943/db649c33-27a5-4520-8e80-4cbd59c9b2e2)
### Add
![image](https://github.com/SatishKumar1911/Password-Manager/assets/124880943/aeffbe09-ad5e-4f3d-84c7-93ce0609d340)
### View
![image](https://github.com/SatishKumar1911/Password-Manager/assets/124880943/77bb0414-7ebf-410b-bd30-64ac6d2504a4)
### Update
![image](https://github.com/SatishKumar1911/Password-Manager/assets/124880943/45f9858c-7565-4c0d-bc93-71a0c6abfad5)
### Delete
![image](https://github.com/SatishKumar1911/Password-Manager/assets/124880943/e8e9e386-dfb2-46de-9a8b-cc4d0795e017)
