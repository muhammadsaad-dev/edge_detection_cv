# Edge Detection Tool

A Python project built and managed using **[uv](https://github.com/astral-sh/uv)** — a fast, reliable package and environment manager designed for modern Python workflows.

## 🚀 Features

- Fast and reproducible Python environment setup
- Dependency management using `uv`
- Lightweight and easy-to-run project structure
- **Image upload and edge detection** — Upload images and apply edge detection algorithms to identify boundaries and features

## 🧩 Setup & Installation

### Prerequisites

- Python 3.8 or higher
- pip (for installing uv)

### Installation Steps

1. **Install uv (if not already installed):**

```bash
   pip install uv
```

2. **Clone the repository:**

```bash
   git clone <your-repo-url>
   cd <project-directory>
```

3. **Create and sync the environment:**

```bash
   uv sync
```

## 🎯 Usage

Run the edge detection tool:

```bash
uv run main.py
```

The application will prompt you to upload an image, then process it to detect edges using computer vision algorithms.

## 📦 Dependencies

Dependencies are managed through `uv` and defined in `pyproject.toml`. Key libraries include:

- OpenCV or Pillow (for image processing)
- NumPy (for numerical operations)
- _(List other major dependencies)_

## 🛠️ How It Works

1. **Upload Image:** The user provides an image file (JPEG, PNG, etc.)
2. **Edge Detection:** The application applies edge detection algorithms (such as Canny, Sobel, or Laplacian)
3. **Output:** The processed image with detected edges is displayed or saved

## 📝 Project Structure

```
.
├── main.py              # Main entry point
├── pyproject.toml       # Project dependencies and configuration
├── uv.lock             # Locked dependency versions
└── README.md           # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

_(Add your license information here — e.g., MIT, Apache 2.0, etc.)_

## 🔗 Resources

- [uv Documentation](https://github.com/astral-sh/uv)
- [OpenCV Edge Detection Tutorial](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html)
