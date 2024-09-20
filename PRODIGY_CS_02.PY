from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Get the image pixels
    pixels = list(img.getdata())
    
    # Encrypt each pixel using XOR with the key
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]
    
    # Create a new encrypted image and put the encrypted pixels into it
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    
    # Get the image pixels
    pixels = list(img.getdata())
    
    # Decrypt each pixel using XOR with the key (same as encryption)
    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]
    
    # Create a new decrypted image and put the decrypted pixels into it
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    print("Image Encryption Tool")
    
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    image_path = input("Enter the image file path: ")
    key = int(input("Enter the encryption/decryption key (0-255): "))
    
    if choice == 'e':
        encrypt_image(image_path, key)
    elif choice == 'd':
        decrypt_image(image_path, key)
    else:
        print("Invalid option. Please choose 'e' for encryption or 'd' for decryption.")
