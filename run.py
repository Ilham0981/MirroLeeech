import subprocess

# Install dependencies
subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

# Jalankan update.py
subprocess.run(['python3', 'update.py'])

# Jalankan python3 -m bot
subprocess.run(['python3', '-m', 'bot'])
