# 🖼️ CLI Photo Editing Tool

A powerful command-line image editor built with Python using the Pillow library. Perform various image manipulation operations directly from your terminal, including AI-powered background removal!

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pillow](https://img.shields.io/badge/Pillow-latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![AI Background Removal](https://img.shields.io/badge/AI-Background%20Removal-purple.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Setting Up Virtual Environment](#setting-up-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Running the Program](#running-the-program)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Available Operations](#available-operations)
  - [Basic Operations](#basic-operations)
  - [Filters](#filters)
  - [Adjustments](#adjustments)
  - [Histogram Analysis](#histogram-analysis)
  - [AI Background Removal](#ai-background-removal)
- [Output Directory](#output-directory)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## ✨ Features

### � Basic Operations
- 📷 **View Image** - Display images in your terminal with graphical preview
- ✂️ **Crop Image** - Crop images by specifying coordinates and dimensions
- 🔄 **Rotate Image** - Rotate images by any degree angle
- 🔍 **Upscale Image** - Increase image resolution by a scale factor
- 📉 **Downscale Image** - Decrease image resolution by a scale factor

### 🎨 Filters
- 🌫️ **Gaussian Blur** - Apply Gaussian blur effect
- 🔪 **Sharpen** - Sharpen the image
- 🎨 **Detail** - Enhance detail in the image
- 📐 **Edge Enhance** - Enhance edges in the image
- 🌊 **Smooth** - Smooth the image
- ⬛ **Grayscale** - Convert to grayscale/black & white

### ☀️ Adjustments
- ☀️ **Brightness** - Adjust image brightness
- 🌓 **Contrast** - Adjust image contrast
- 🎭 **Saturation** - Adjust color saturation

### 📊 Histogram Analysis
- 📊 **View Histogram** - Display RGB and grayscale histograms
- 📈 **Adjust Histogram** - Equalize or stretch histogram for better image quality

### 🤖 AI Features
- 🧠 **Background Removal** - Remove background from images using AI (U2Net model)

---

## 🔧 Prerequisites

Before running the application, ensure you have:

| Requirement | Minimum Version | Description |
|-------------|-----------------|-------------|
| Python | 3.8+ | Programming language |
| pip | Latest | Python package installer |
| Operating System | Windows/macOS/Linux | Cross-platform support |

### Verify Python Installation

```bash
# Check Python version
python --version

# Or for macOS/Linux
python3 --version

# Check pip is installed
pip --version
```

---

## 📦 Installation

### Setting Up Virtual Environment

Using a virtual environment is **highly recommended** to avoid conflicts with other Python projects. Follow these steps:

#### Windows

```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate

# You should see (venv) prefix in your terminal
```

#### macOS / Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# You should see (venv) prefix in your terminal
```

#### Deactivating the Virtual Environment

```bash
# When you're done, deactivate the environment
deactivate
```

> **💡 Pro Tip:** Always activate the virtual environment before installing dependencies or running the program!

### Installing Dependencies

Once your virtual environment is activated, install all required packages:

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

#### What Gets Installed:

| Package | Purpose |
|---------|---------|
| Pillow | Core image processing library |
| rembg | AI-powered background removal |
| numpy | Numerical computing for histograms |
| matplotlib | Image preview and histogram visualization |
| onnxruntime | AI model inference (CPU) |

---

## 🚀 Running the Program

### Step 1: Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 2: Run the Application

```bash
python imageManipulation.py
```

### Step 3: Using the Application

1. The program will display available images in the `1.ImageToTest/` directory
2. Enter the image name you want to edit
3. Select an operation from the menu (0-9)
4. Follow on-screen instructions for each operation
5. Processed images are automatically saved to `2.EditedImage/`

### Quick Start with Sample Image

The repository includes a sample image for testing:
- Location: `1.ImageToTest/nkl.jpg`

```bash
# After running the program, enter: nkl.jpg
# Then select any operation from the menu!
```

---

## 📂 Project Structure

```
Photo-Editing-Using-Python/
├── imageManipulation.py      # Main application script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── venv/                     # Virtual environment (created by you)
│
├── 1.ImageToTest/          # Input images directory
│   └── nkl.jpg              # Sample test image
│
├── 2.EditedImage/           # Output directory
│   ├── Bg_Removed_images/   # AI background removed images
│   ├── Brighteen_images/    # Brightness adjusted images
│   ├── Contrasted_images/   # Contrast adjusted images
│   ├── Cropped_images/      # Cropped images
│   ├── Detailed_images/     # Detail enhanced images
│   ├── Downscaled_images/   # Downscaled images
│   ├── Edge_Enhanced_images/# Edge enhanced images
│   ├── Grayscaled_images/   # Grayscale images
│   ├── Gussian_blur_images/ # Blurred images
│   ├── Rotated_images/      # Rotated images
│   ├── Saturated_images/   # Saturation adjusted images
│   ├── Sharped_images/      # Sharpened images
│   ├── Smooth_images/       # Smoothed images
│   └── Upscaled_images/     # Upscaled images
│
└── models/                  # AI models directory
    └── u2net.onnx           # Pre-trained background removal model
```

---

## 🎯 Usage

### Main Menu Options

Run `python imageManipulation.py` and you'll see:

```
-----Image Manipulation Menu-----
0.Exit
1. View Image
2. Crop Image
3. Rotate image
4. Upscale Image
5. Downscale Image
6. Apply Filters
7. Adjust Brightness/Contrast ... etc.
8. Histogram Analyser
9.Remove Background
```

### Example Workflow

```
# 1. Run the program
python imageManipulation.py

# 2. Program shows available images:
# ------------------Images------------------
# nkl.jpg
# ------------------------------------------

# 3. Enter image name: nkl.jpg

# 4. Select operation (e.g., 9 for background removal)
# Choose the options (0-9) : 9

# 5. Background removed! Image saved and displayed.
```

---

## 📋 Available Operations

### Basic Operations

| Option | Operation | Description | Example Input |
|--------|-----------|-------------|---------------|
| 1 | View Image | Display image in graphical window | - |
| 2 | Crop Image | Crop by coordinates | x: 100, y: 100, width: 200, height: 200 |
| 3 | Rotate Image | Rotate by degrees | 90, 180, 270 |
| 4 | Upscale Image | Increase size | 2 (for 2x) |
| 5 | Downscale Image | Decrease size | 0.5 (for 50%) |

### Filters (Option 6)

| Sub-option | Filter | Description |
|------------|--------|-------------|
| 6 → 1 | Gaussian Blur | Apply smooth blur effect |
| 6 → 2 | Sharpen | Enhance image sharpness |
| 6 → 3 | Detail | Enhance fine details |
| 6 → 4 | Edge Enhance | Emphasize image edges |
| 6 → 5 | Smooth | Apply smoothening filter |
| 6 → 6 | Grayscale | Convert to black & white |

### Adjustments (Option 7)

| Sub-option | Adjustment | Factor Guide |
|------------|------------|--------------|
| 7 → 1 | Brightness | > 1.0 = brighter, < 1.0 = darker |
| 7 → 2 | Contrast | > 1.0 = more contrast, < 1.0 = less |
| 7 → 3 | Saturation | > 1.0 = more saturated, < 1.0 = less |

### Histogram Analysis (Option 8)

| Sub-option | Operation | Description |
|------------|-----------|-------------|
| 8 → 1 | View Histogram | Display RGB and grayscale histograms |
| 8 → 2 → 1 | Equalize | Apply histogram equalization |
| 8 → 2 → 2 | Stretch | Apply linear contrast stretching |

### AI Background Removal (Option 9)

| Option | Operation | Description |
|--------|-----------|-------------|
| 9 | Remove Background | Uses AI (U2Net) to remove background from images |

> **⚠️ Note:** The first time you use background removal, the AI model will be downloaded automatically (~170MB).

---

## 📁 Output Directory

All processed images are automatically saved with timestamps:

```
2.EditedImage/
├── Bg_Removed_images/bgremoved_20260213_161040.png
├── Brighteen_images/brighteen_20260213_161045.jpg
├── Contrasted_images/contrasted_20260213_161050.jpg
├── Cropped_images/cropped_20260213_161030.jpg
├── Detailed_images/detailed_20260213_161035.jpg
├── Downscaled_images/downscaled_20260213_161025.jpg
├── Edge_Enhanced_images/edgeEnhanced_20260213_161040.jpg
├── Grayscaled_images/grayscaled_20260213_161040.jpg
├── Gussian_blur_images/gussianBlured_20260213_161040.jpg
├── Rotated_images/rotated_20260213_161020.jpg
├── Saturated_images/saturated_20260213_161055.jpg
├── Sharped_images/sharped_20260213_161040.jpg
├── Smooth_images/smooth_20260213_161040.jpg
└── Upscaled_images/upscaled_20260213_161015.jpg
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'Pillow'"

**Solution:** Activate your virtual environment and reinstall dependencies:

```bash
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. "matplotlib not installed" warning

**Solution:** Install matplotlib:

```bash
pip install matplotlib
```

#### 3. Background removal is slow on first run

**Solution:** This is normal! The AI model (~170MB) is downloaded on first use. Subsequent runs will be faster.

#### 4. "No module named 'rembg'" error

**Solution:** Install rembg:

```bash
pip install rembg
```

#### 5. Image file not found

**Solution:** Make sure your image is in the `1.ImageToTest/` directory. The program only searches in that folder.

### Getting Help

If you encounter any other issues:

1. Check the [Issues](https://github.com/niteshkumar-lodh/Photo-Editing-Using-Python/issues) page
2. Create a new issue with:
   - Error message
   - Your operating system
   - Python version (`python --version`)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/niteshkumar8848/Photo-Editing-Using-Python.git
   ```
3. **Create** your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
4. **Commit** your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
5. **Push** to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
6. **Open** a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- [Pillow (PIL)](https://python-pillow.org/) - Python Imaging Library
- [rembg](https://github.com/danielgatis/rembg) - AI background removal
- [U2Net](https://github.com/xuanbinh-nguyen27/U2Net) - Deep learning model for salient object detection
- [NumPy](https://numpy.org/) - Numerical computing library
- [Matplotlib](https://matplotlib.org/) - Plotting library for histograms

---

**Made with ❤️ by [Nitesh Kumar Lodh](https://github.com/niteshkumar8848)**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/niteshkumar-lodh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/niteshkumar-lodh)

