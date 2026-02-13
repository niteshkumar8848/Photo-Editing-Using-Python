print("""##########################################################
Author: Nitesh Kumar Lodh
##########################################################""")
print("~~~~~~~~Hold On Importing all the Modules~~~~~~~~")
import os
from datetime import datetime
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
os.environ["U2NET_HOME"] = os.path.abspath("models")
from rembg import remove
import sys
try:
    import matplotlib.pyplot as plt
    import numpy as np
except Exception:
    plt = None
    np = None

# Background Erase MODEL_DIR
MODEL_URL = "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx"
MODEL_DIR = "models/"
MODEL_PATH = os.path.join(MODEL_DIR, "u2net.onnx")

# # Function to Ensure Model is Downloaded or Not 
# def ensure_model_downloaded():
#     if not os.path.exists(MODEL_DIR):
#         os.makedirs(MODEL_DIR)

#     if not os.path.isfile(MODEL_PATH):
#         print("Downloading AI model... (one time setup)")
#         response = requests.get(MODEL_URL, stream=True)

#         with open(MODEL_PATH, "wb") as file:
#             for chunk in response.iter_content(chunk_size=8192):
#                 file.write(chunk)

#         print("Model downloaded successfully!")
#     else:
#         print("Model already exists.")

def selection():
    global img
    global imagePath

    # Image Selection for Edit
    print("------------------Images------------------")
    folder = "1.ImageToTest/"
    files=os.listdir(folder)
    for item in files:
        if os.path.isfile(os.path.join(folder, item)):
            print(item)
    print("-------------------------------------------")
    imageName = input("Enter the image Name:")
    imagePath =os.path.join(folder,imageName)
    if not os.path.isfile(os.path.join(folder, imageName)):
        print(f"File not found: {imageName}")
        selection()

    img = Image.open(imagePath).convert("RGB")
    
    while True:
    # Calling Main Menu
        Manipulation()


# ----------- Main Menu ------------
def Manipulation():
    print("-----Image Manipulation Menu-----")
    print("0.Exit")
    print("1. View Image")
    print("2. Crop Image")
    print("3. Rotate image")
    print("4. Upscale Image")
    print("5. Downscale Image")
    print("6. Apply Filters")
    print("7. Adjust Brightness/Contrast ... etc.")
    print("8. Histogram Analyser")
    print("9.Remove Background")

    choice=int(input("Choose the options (0-9) : "))

    if choice == 0:
        print("------------- Program has been Terminated !! -------------")
        sys.exit()
    elif choice == 1:
        viewimage()
        Manipulation()
    elif choice == 2:
        cropimage()
    elif choice == 3:
        rotateimage()
    elif choice == 4:
        upscaleimage()
    elif choice == 5:
        downscaleimage()
    elif choice == 6:
        filters()
    elif choice == 7:
        adjustments()
    elif choice == 8:
        histogram_analyser()
    elif choice == 9:
        bgremove()
    else:
        print("Invalid Choice")

def bgremove():
    input_image = Image.open(imagePath)
    img1 = remove(input_image)
    print("Background removed successfully!!")
    # output_image.save("2.EditedImage/Bg_Removed_images/Bg_removed_image.png")
    filename = generate_filename("bgremoved","png")
    img1.save(os.path.join("2.EditedImage/Bg_Removed_images", filename))
    show_with_matplotlib(img1,"Background Removed Image")

# ShowImage
def viewimage():
    # print(img)
    show_with_matplotlib(img, "Original Image")

# CropImage 
def cropimage():
    x_coordinate = int(input("Enter the x-coordinate of top left point : "))
    y_coordinate = int(input("Enter the y-coordinate of top left point : "))
    width = int(input("Enter the width of the crop area : "))
    height = int(input("Enter the height of the crop area : "))
    # PIL expects box=(left, upper, right, lower)
    img1 = img.crop(box=(x_coordinate, y_coordinate, x_coordinate + width, y_coordinate + height))
    # img1.show()
    show_with_matplotlib(img1, "Cropped Image")
    # img1.save("2.EditedImage/Cropped_images/cropped_image.jpg")
    filename = generate_filename("cropped")
    img1.save(os.path.join("2.EditedImage/Cropped_images", filename))

# RotateImage 
def rotateimage():
    imageshift = int(input("Enter the degree of Rotation (E.g. 90) : " ))
    img1 = img.rotate(angle=imageshift ,expand =True, fillcolor="white", resample= Image.LANCZOS)
    # img1.show()
    show_with_matplotlib(img1, "Rotated Image")
    # img1.save("2.EditedImage/Rotated_images/rotated_image.jpg")
    filename = generate_filename("rotated")
    img1.save(os.path.join("2.EditedImage/Rotated_images", filename))

# UpscaleImage 
def upscaleimage():
    size = int(input("Enter the scale factor (E.g. 2 for 2x) : " ))
    img1 = img.resize((int(img.width * size), int(img.height * size)), resample=Image.LANCZOS)
    # img1.show()
    show_with_matplotlib(img1, "Upscaled Image")
    # img1.save("2.EditedImage/Upscaled_images/upscaled_image.jpg")
    filename = generate_filename("upscaled")
    img1.save(os.path.join("2.EditedImage/Upscaled_images", filename))

# DownscaleImage
def downscaleimage():
    size = int(input("Enter the scale factor (E.g. 0.5 for 50%): "))
    img1 = img.resize((int(img.width * size), int(img.height * size)), resample=Image.LANCZOS)
    # img1.show()
    show_with_matplotlib(img1, "Downscaled Image")
    # img1.save("2.EditedImage/Downscaled_images/downscaled_image.jpg")
    filename = generate_filename("downscaled")
    img1.save(os.path.join("2.EditedImage/Downscaled_images", filename))

# -------------------------------------------------------------------------------#
                                     # Filters

def filters():
    print("1. GUSSIAN_BLUR")
    print("2. SHARPEN")
    print("3. DETAIL")
    print("4. EDGE_ENHANCE")
    print("5. SMOOTH")
    print("6. GRAYSCALE")

    choice=int(input("Enter what filter to apply : "))

    if choice == 1:
        gussian_blur()
    elif choice == 2:
        sharpen()
    elif choice == 3:
        detail()
    elif choice == 4:
        edge_enhance()
    elif choice == 5:
        smooth()
    elif choice == 6:
        grayscale()
      
# gussian_blur
def gussian_blur():
    img1 = img.filter(ImageFilter.GaussianBlur(radius=5))
    # img1.show()
    show_with_matplotlib(img1, "Gussian Blured Image")
    # img1.save("2.EditedImage/Gussian_blur_images/gussian_blur.jpg")
    filename = generate_filename("GussianBlured")
    img1.save(os.path.join("2.EditedImage/Gussian_blur_images", filename))

# sharpen 
def sharpen():
    img1 = img.filter(ImageFilter.SHARPEN)
    # img1.show()
    show_with_matplotlib(img1, "Sharped Image")
    # img1.save("2.EditedImage/Sharped_images/sharpen.jpg")
    filename = generate_filename("sharped")
    img1.save(os.path.join("2.EditedImage/Sharped_images", filename))

# detail
def detail():
    img1 = img.filter(ImageFilter.DETAIL)
    # img1.show()
    show_with_matplotlib(img1, "Detailed Image")
    # img1.save("2.EditedImage/Detailed_images/detail.jpg")
    filename = generate_filename("detailed")
    img1.save(os.path.join("2.EditedImage/Detailed_images", filename))

# edge_enhance 
def edge_enhance():
    img1 = img.filter(ImageFilter.EDGE_ENHANCE)
    # img1.show()
    show_with_matplotlib(img1, "Edge Enhanced Image")
    # img1.save("2.EditedImage/Edge_Enhanced_images/edge_enhance.jpg")
    filename = generate_filename("edgeEnchanced")
    img1.save(os.path.join("2.EditedImage/Edge_Enhanced_images", filename))

# smooth 
def smooth():
    img1 = img.filter(ImageFilter.SMOOTH)
    # img1.show()
    show_with_matplotlib(img1, "Smooth Image")
    # img1.save("2.EditedImage/Smooth_images/smooth.jpg")
    filename = generate_filename("smooth")
    img1.save(os.path.join("2.EditedImage/Smooth_images", filename))

# grayscale 
def grayscale():
    img1 = img.convert("L")
    # img1.show()
    show_with_matplotlib(img1, "Grayscaled Image")
    # img1.save("2.EditedImage/Grayscaled_images/grayscale.jpg")
    filename = generate_filename("grayscaled")
    img1.save(os.path.join("2.EditedImage/Grayscaled_images", filename))

# Apply Enhancements 
def adjustments():
    print("1. Brightness")
    print("2. Contrast")
    print("3. Saturation")

    choice = int(input("Enter what adjustment to apply : "))

    if choice == 1:
        brightness()
    elif choice == 2:
        contrast()
    elif choice == 3:
        saturation()

# Brightness 
def brightness():
    factor = float(input("Enter the brightness factor (e.g., 1.0 for original, <1.0 for darker, >1.0 for brighter): "))
    enhancer = ImageEnhance.Brightness(img)
    img1 = enhancer.enhance(factor)
    # img1.show()
    show_with_matplotlib(img1, "Brighteen Image")
    # img1.save("2.EditedImage/Brighteen_images/brightness.jpg")
    filename = generate_filename("brighteen")
    img1.save(os.path.join("2.EditedImage/Brighteen_images", filename))

# Contrast 
def contrast():
    factor = float(input("Enter the contrast factor (e.g., 1.0 for original, <1.0 for less contrast, >1.0 for more contrast): "))
    enhancer = ImageEnhance.Contrast(img)
    img1 = enhancer.enhance(factor)
    # img1.show()
    show_with_matplotlib(img1, "Contrasted Image")
    # img1.save("2.EditedImage/Contrasted_images/contrast.jpg")
    filename = generate_filename("contrasted")
    img1.save(os.path.join("2.EditedImage/Contrasted_images", filename))

# Saturation 
def saturation():
    factor = float(input("Enter the saturation factor (e.g., 1.0 for original, <1.0 for less saturation, >1.0 for more saturation): "))
    enhancer = ImageEnhance.Color(img)
    img1 = enhancer.enhance(factor)
    # img1.show()
    show_with_matplotlib(img1, "Saturated Image")
    # img1.save("2.EditedImage/Saturated_images/saturation.jpg")
    filename = generate_filename("saturated")
    img1.save(os.path.join("2.EditedImage/Saturated_images", filename))

#------------------------------------------------------------------------#
                
                 # Histogram Analyser 

def histogram_analyser():
    if plt is None or np is None:
        print("matplotlib and numpy are required for histogram plotting and adjustments.\nInstall them with: pip install matplotlib numpy")
        return

    print("Histogram Analyzer")
    print("1. View histogram (R,G,B and Grayscale)")
    print("2. Adjust histogram")
    choice = int(input("Choose option: "))

    arr = np.array(img)
    r = arr[:, :, 0].ravel()
    g = arr[:, :, 1].ravel()
    b = arr[:, :, 2].ravel()

    def show_histograms():
        hr, _ = np.histogram(r, bins=256, range=(0, 255))
        hg, _ = np.histogram(g, bins=256, range=(0, 255))
        hb, _ = np.histogram(b, bins=256, range=(0, 255))
        gray = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
        hgray, _ = np.histogram(gray.ravel(), bins=256, range=(0, 255))

        plt.figure(figsize=(10, 6))
        plt.subplot(2, 1, 1)
        x = np.arange(256)
        plt.plot(x, hr, color='r', label='Red')
        plt.plot(x, hg, color='g', label='Green')
        plt.plot(x, hb, color='b', label='Blue')
        plt.legend()
        plt.title('Per-channel histograms')

        plt.subplot(2, 1, 2)
        plt.bar(x, hgray, color='gray')
        plt.title('Grayscale histogram')
        plt.tight_layout()
        plt.show()

    def adjust_menu():
        print('Adjust Histogram')
        print('1. Equalize (grayscale)')
        print('2. Stretch channels (linear contrast stretch)')
        sub = int(input('Choose adjustment: '))

        if sub == 1:
            # Equalize grayscale
            gray = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
            hist, bins = np.histogram(gray.flatten(), 256, [0, 256])
            cdf = hist.cumsum()
            # avoid division by zero
            cdf_masked = np.ma.masked_equal(cdf, 0)
            if cdf_masked.max() == cdf_masked.min():
                print('Image has flat histogram; equalization skipped.')
                return
            cdf_m = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
            cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')
            img_eq = cdf_final[gray]
            pil = Image.fromarray(img_eq, mode='L')
            pil.show()

        elif sub == 2:
            # Stretch each channel independently to [0,255]
            def stretch_channel(chan):
                cmin = chan.min()
                cmax = chan.max()
                if cmax == cmin:
                    return np.clip(chan, 0, 255).astype(np.uint8)
                stretched = (chan - cmin) * (255.0 / (cmax - cmin))
                return stretched.astype(np.uint8)

            r2 = stretch_channel(arr[:, :, 0])
            g2 = stretch_channel(arr[:, :, 1])
            b2 = stretch_channel(arr[:, :, 2])
            arr2 = np.stack([r2, g2, b2], axis=2)
            pil = Image.fromarray(arr2.astype(np.uint8), mode='RGB')
            pil.show()

        else:
            print('Invalid adjustment choice')

    if choice == 1:
        show_histograms()
    elif choice == 2:
        adjust_menu()
    else:
        print('Invalid choice')


def show_with_matplotlib(image, title="Preview"):
    if plt is None:
        print("matplotlib not installed")
        return

    plt.figure(figsize=(8, 6))
    plt.imshow(image)

    # If grayscale image
    if image.mode == "L":
        plt.imshow(image, cmap="gray")

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def generate_filename(prefix, extension="jpg"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{extension}"

selection()