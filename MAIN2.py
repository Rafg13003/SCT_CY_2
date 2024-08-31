from PIL import Image
import matplotlib.pyplot as plt
import random

# Function to encrypt an image
def encrypt_image(image_path, output_path, key, operation="swap"):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size

    # Swapping pixels or applying a mathematical operation
    if operation == "swap":
        random.seed(key)
        for i in range(len(pixels) // 2):
            j = random.randint(0, len(pixels) - 1)
            pixels[i], pixels[j] = pixels[j], pixels[i]
    elif operation == "add":
        for i in range(len(pixels)):
            r, g, b = pixels[i]
            pixels[i] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    else:
        raise ValueError("Unsupported operation. Use 'swap' or 'add'.")

    # Save the encrypted image
    encrypted_image = Image.new(image.mode, (width, height))
    encrypted_image.putdata(pixels)
    encrypted_image.save(output_path)
    return encrypted_image

# Function to decrypt an image
def decrypt_image(image_path, output_path, key, operation="swap"):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    width, height = image.size

    # Reverse the encryption process
    if operation == "swap":
        random.seed(key)
        indices = list(range(len(pixels)))
        random.shuffle(indices)
        decrypted_pixels = [None] * len(pixels)
        for i, j in enumerate(indices):
            decrypted_pixels[j] = pixels[i]
    elif operation == "add":
        for i in range(len(pixels)):
            r, g, b = pixels[i]
            pixels[i] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
        decrypted_pixels = pixels
    else:
        raise ValueError("Unsupported operation. Use 'swap' or 'add'.")

    # Save the decrypted image
    decrypted_image = Image.new(image.mode, (width, height))
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)
    return decrypted_image

# Create a small 4x4 pixel image with random colors
original_image = Image.new("RGB", (4, 4))
original_pixels = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 255), (0, 255, 255), (128, 128, 128), (0, 0, 0),
    (255, 128, 0), (0, 128, 255), (128, 0, 255), (255, 255, 255),
    (64, 64, 64), (192, 192, 192), (0, 64, 128), (128, 64, 0)
]
original_image.putdata(original_pixels)
original_image.save("original_image.png")

# Encrypt and decrypt the image
encrypted_image = encrypt_image("original_image.png", "encrypted_image.png", key=1234, operation="swap")
decrypted_image = decrypt_image("encrypted_image.png", "decrypted_image.png", key=1234, operation="swap")

# Display the images
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(original_image)
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(encrypted_image)
axs[1].set_title("Encrypted Image")
axs[1].axis('off')

axs[2].imshow(decrypted_image)
axs[2].set_title("Decrypted Image")
axs[2].axis('off')

plt.show()
