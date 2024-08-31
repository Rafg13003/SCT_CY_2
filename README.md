Encrypting the Image:

Swap Operation: Randomly swaps pixel positions using a seed (key). This makes the image look garbled and encrypted.
Add Operation: Adds a value (key) to each color channel (R, G, B) of every pixel, modulo 256 to keep the values in the valid range.


Decrypting the Image:
Swap Operation: The random pixel swapping is reversed using the same seed (key) to restore the original order of pixels.
Add Operation: Subtracts the same value (key) from each color channel, modulo 256, to revert the image to its original state.
