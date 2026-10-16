
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Create a sample image
image = Image.new("RGB", (256, 256), "white")
draw = ImageDraw.Draw(image)
draw.rectangle((40, 40, 216, 216), fill="skyblue")
draw.ellipse((80, 80, 176, 176), fill="orange")

# Divide the image into patches
patch_size = 64
patches = []

for y in range(0, image.height, patch_size):
    for x in range(0, image.width, patch_size):
        patch = image.crop(
            (x, y, x + patch_size, y + patch_size)
        )
        patches.append(patch)

# Display the original image and its patches
fig, axes = plt.subplots(1, 2, figsize=(9, 4))

axes[0].imshow(image)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(image)
axes[1].set_title("Image Divided into Patches")

for position in range(0, 257, patch_size):
    axes[1].axhline(position - 0.5, color="red")
    axes[1].axvline(position - 0.5, color="red")

axes[1].axis("off")
plt.tight_layout()
plt.show()

print("Total number of patches:", len(patches))
print("Patch size:", patch_size, "x", patch_size)
