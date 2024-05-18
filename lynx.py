import hashlib
import os

# List of known malware hashes
malware_hashes = [
    "09c9e30cfc3d8887e715c3e1046577e9",
    "e4d909c290d0fb1ca068ffaddf22cbd0",
    "c0e817294c2a0b568b8fff8a9b81e12b",
    # Add more hashes here
]

def calculate_hash(file_path):
    """Calculate the SHA1 hash of a file."""
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def scan_file(file_path):
    """Scan a file and check if it's malicious."""
    file_hash = calculate_hash(file_path)
    if file_hash in malware_hashes:
        print(f"{file_path} is malicious!")
    else:
        print(f"{file_path} is clean.")

def scan_directory(directory_path):
    """Scan all files in a directory."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

# Example usage
scan_directory("/path/to/scan")