import cv2
import matplotlib.pyplot as plt 

img=cv2.imread("images/sample.jpg")

if img is None:
    print("Image not found! Check falie path/name.")
    exit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Sample")
plt.axis("off")
plt.show()

print("image shape(H,W,C):",img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis ("off")
plt.show()

print("Grayscale shape(H,W):",gray.shape)

resized = cv2.resize(gray,(256,256))

plt.imshow(resized, cmap="gray")
plt.title("resized grayscale (256x256)")
plt.axis("off")
plt.show()

print("resized shape:",resized.shape)

normalized = resized/256.0

print("pixel range ater normalization",normalized.min(),"to",normalized.max())

plt.imshow(normalized, cmap="gray")
plt.title("normalized image (0 to 1)")
plt.axis("off")
plt.show()

cv2.imwrite("gray.png",gray)
cv2.imwrite("resized.png",resized)

cv2.imwrite("normalized.png",(normalized*256).astype("uint8"))

print("saved gray.png,resized.png,normalized.png")