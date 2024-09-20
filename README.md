# Image Encryption Tool

This is a simple image encryption and decryption tool in Python. It performs basic operations like swapping pixel values or applying mathematical transformations to each pixel to encrypt and decrypt images.

## Features
- **Encrypts images** by modifying pixel values using mathematical operations and pixel swapping.
- **Decrypts images** using the inverse of the applied encryption operation.
- Users can input their own images and provide a numerical key for encryption/decryption.
- Supports various image formats (PNG, JPEG, etc.).

## How It Works
1. **Encryption**: The program modifies each pixel in the image by performing a mathematical operation (such as addition or XOR) on the RGB values. Optionally, it also swaps the positions of pixels in a predefined manner.
2. **Decryption**: The program reverses the encryption by performing the inverse operation and swapping the pixel positions back to their original state.

## Installation
1. Install the required `Pillow` library:
   ```bash
   pip install pillow
