# Image Encryption with AES Block Cipher Modes 🖼️🔐=>

This project is a Python script that demonstrates the principles of symmetric-key encryption by applying the Advanced Encryption Standard (AES) algorithm to images.It showcases the key differences between various block cipher modes of operation, specifically ECB, CBC, CFB, OFB, and CTR.

### 💡 Key Features =>

1. Multi-Mode Encryption: Encrypts an image using five different AES modes.
2. AES-256: Implements the robust AES algorithm with a 256-bit key.
3. Image Handling: Utilizes the Pillow library to handle image data, converting it to a byte array for encryption and then back to an image for output.
4. Padding: Correctly applies PKCS#7 padding for block cipher modes like ECB and CBC to ensure data integrity.
5. Visual Comparison: The generated output files provide a powerful visual comparison of how different modes affect the ciphertext, revealing which modes are more secure against pattern analysis.

### 🎯 Why This Project Matters

For a cybersecurity student, this project is an excellent way to demonstrate a deep understanding of core cryptographic concepts. The visual outputs are especially revealing:

+ ECB (Electronic Codebook) Mode: This mode encrypts each block independently. As a result, identical plaintext blocks (e.g., areas of uniform color in an image) will produce identical ciphertext blocks, revealing patterns in the encrypted image. This visually proves why ECB is considered insecure for most applications.

* Chaining and Stream Modes (CBC, CFB, OFB, CTR): These modes introduce randomness by linking the encryption of each block to the previous one (or to a nonce), resulting in a visually indistinguishable, noise-like output. This demonstrates the critical role of Initialization Vectors (IVs) and nonces in providing confidentiality and making the ciphertext robust against pattern analysis.

### 🛠️ Prerequisites
This project requires a few Python libraries. You can install them using pip:

    pip install pillow cryptography numpy

### 🚀 Usage

1. Clone the repository to your local machine.

2. Place an image file (e.g., original.png) in the root directory of the project.

3. Update the input_image variable in the Python script to point to your image file.

4. Run the script from your terminal
   
        python enc.py

The script will automatically generate five new encrypted images in your directory:

    ecb_encrypted.png

    cbc_encrypted.png

    cfb_encrypted.png

    ofb_encrypted.png

    ctr_encrypted.png

### ⚠️ Security Notes
This project focuses on the confidentiality provided by different block cipher modes. In a real-world application, it is crucial to also ensure data integrity and authenticity. For this, you would typically use an authenticated encryption mode like AES-GCM or combine a confidentiality mode with a message authentication code like HMAC. This ensures that the data has not been tampered with.
