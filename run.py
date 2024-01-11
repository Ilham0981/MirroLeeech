import subprocess

# Update package lists and install dependencies
subprocess.run(['apt-get', 'update'])
subprocess.run(['DEBIAN_FRONTEND=noninteractive', 'apt-get', 'install', '-y', 
                'python3', 'python3-pip', 'aria2', 'qbittorrent-nox', 'tzdata', 'p7zip-full', 'p7zip-rar', 'xz-utils', 'curl', 'pv', 'jq', 'ffmpeg',
                'locales', 'git', 'unzip', 'rtmpdump', 'libmagic-dev', 'libcurl4-openssl-dev', 'libssl-dev', 'libc-ares-dev', 'libsodium-dev',
                'libcrypto++-dev', 'libsqlite3-dev', 'libfreeimage-dev', 'libpq-dev', 'libffi-dev'])

# Generate locale
subprocess.run(['locale-gen', 'en_US.UTF-8'])

# Download and install megasdkrest
cpu = subprocess.check_output(['uname', '-m']).decode().strip()
arch = "amd64" if cpu == "x86_64" else "i386" if cpu == "x86" else "arm64" if cpu == "aarch64" else cpu
subprocess.run(['curl', '-L', f'https://github.com/anasty17/megasdkrest/releases/download/latest/megasdkrest-{arch}',
                '-o', '/usr/local/bin/megasdkrest'])
subprocess.run(['chmod', '+x', '/usr/local/bin/megasdkrest'])

# Set environment variables
subprocess.run(['export', 'LANG=en_US.UTF-8'])
subprocess.run(['export', 'LANGUAGE=en_US:en'])

# Install Python dependencies
subprocess.run(['pip3', 'install', '--no-cache-dir', '-r', '/usr/src/app/requirements.txt'])

# Run the Python script
subprocess.run(['python3', 'run.py'])
