import cv2, numpy as np
import matplotlib.pyplot as plt
def display(title, img, cmap=None):
    plt.figure(figsize=(6, 6))
    plt.imshow(img if cmap is None else cv2.cvtColor(img, cmap))
    plt.title(title); plt.axis('off'); plt.show()
def edge_activity(path):
    img = cv2.imread(path)
    if img is None:
        return print("Image not found!!")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display("Original Image", img, cv2.COLOR_BGR2RGB)
    display("Grayscale Image", gray)
    def sobel():
        sx, sy = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3), cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        return cv2.bitwise_or(sx.astype(np.uint8), sy.astype(np.uint8))
    def canny():
        l, u =  map(int, [input("Lower(default 100): ") or 100, input("Upper(default 200): ") or 200])
        return cv2.Canny(gray, l, u)
    def laplacian():
        return cv2.Laplacian(gray, cv2.CV_64F).astype(np.uint8)
    def blur():
        cv2.GaussianBlur(img, (int(input("Kernel size(default 5): ") or 5) * 2,0))
    def median():
        cv2.medianBlur(img, int(input("Kernel size(default 5): ") or 5))
    actions = {
        "1":("Sobel Edge", sobel),
        "2":("Canny Edge", canny),
        "3":("Laplacian Edge", laplacian),
        "4":("Gaussian Blur", blur),
        "5":("Median Filter", median)
    }
    while True:
        print("\n1.Sobel 2. Canny 3.Laplacian 4.Gaussian Blur 5.Median Filter 6.Exit")
        choice = input("Choose input(1 - 6): ")
        if choice == "6":
            print("Bye!!")
            break
        elif choice in actions:
            title, func = actions[choice]
            result = func()
            display(title, result)
        else:
            print("Invalid choice. Please try again.")
edge_activity("gojo.jpg")