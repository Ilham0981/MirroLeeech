import subprocess

# Update and install dependencies
subprocess.run(['apt-get', '-y', 'update'])
subprocess.run(['DEBIAN_FRONTEND=noninteractive', 'apt-get', 'install', '-y', 'python3', 'python3-pip', 'aria2', 'qbittorrent-nox', 'tzdata', 'p7zip-full', 'p7zip-rar', 'xz-utils', 'curl', 'pv', 'jq', 'ffmpeg', 'locales', 'git', 'unzip', 'rtmpdump', 'libmagic-dev', 'libcurl4-openssl-dev', 'libssl-dev', 'libc-ares-dev', 'libsodium-dev', 'libcrypto++-dev', 'libsqlite3-dev', 'libfreeimage-dev', 'libpq-dev', 'libffi-dev'])

# Generate locale
subprocess.run(['locale-gen', 'en_US.UTF-8'])

# Download and install megasdkrest
cpu = subprocess.check_output(['uname', '-m']).decode().strip()
arch = ''
if cpu == 'x86_64':
    arch = 'amd64'
elif cpu == 'x86':
    arch = 'i386'
elif cpu == 'aarch64':
    arch = 'arm64'
else:
    arch = cpu

url = f'https://github.com/anasty17/megasdkrest/releases/download/latest/megasdkrest-{arch}'
subprocess.run(['curl', '-L', url, '-o', '/usr/local/bin/megasdkrest'])
subprocess.run(['chmod', '+x', '/usr/local/bin/megasdkrest'])
