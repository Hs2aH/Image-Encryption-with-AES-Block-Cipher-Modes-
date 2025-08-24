from PIL import Image
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def encrypt_image(input_path, mode, output_path, key, iv=None, nonce=None):
    """Encrypts an image using AES in specified mode"""
    # Load image and convert to bytes
    img = Image.open(input_path)
    img_bytes = np.array(img).tobytes()
    orig_size = img.size
    orig_mode = img.mode

    # Initialize cipher based on mode
    if mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    elif mode == 'CFB':
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    elif mode == 'OFB':
        cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend=default_backend())
    elif mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    else:
        raise ValueError("Invalid mode specified")

    # Encrypt the data
    encryptor = cipher.encryptor()

    # Pad data only for block modes (ECB/CBC)
    if mode in ['ECB', 'CBC']:
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(img_bytes) + padder.finalize()
        encrypted_bytes = encryptor.update(padded_data) + encryptor.finalize()
    else:  # Stream modes (no padding needed)
        encrypted_bytes = encryptor.update(img_bytes) + encryptor.finalize()

    # Convert encrypted bytes to image
    encrypted_img = Image.frombytes(
        orig_mode,
        orig_size,
        encrypted_bytes[:len(img_bytes)]  # Trim to original size
    )
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")

# Configuration
input_image = "/media/husam/567E-8746/UniFolder/FYP 2/4th Task Block_Encryption/s-l1200.jpg"
key = os.urandom(32)  # AES-256 key
iv = os.urandom(16)   # Initialization vector
nonce = os.urandom(16) # CTR nonce

# Encrypt using different modes
encrypt_image(input_image, 'ECB', 'ecb_encrypted.png', key)
encrypt_image(input_image, 'CBC', 'cbc_encrypted.png', key, iv)
encrypt_image(input_image, 'CFB', 'cfb_encrypted.png', key, iv)
encrypt_image(input_image, 'OFB', 'ofb_encrypted.png', key, iv)
encrypt_image(input_image, 'CTR', 'ctr_encrypted.png', key, nonce=nonce)
