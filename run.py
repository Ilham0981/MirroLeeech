import subprocess

# Install dependencies
subprocess.run(['pip3', 'install', '-r', 'requirements.txt'])

# Jalankan python3 -m bot
subprocess.run(['python3', '-m', 'bot'])
