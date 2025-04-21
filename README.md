---

```markdown
# 👁️ Eye Gender Detection via Deep Learning

A powerful offline application for **gender classification** based solely on **eye patterns** from images and videos. Leveraging the capabilities of deep learning, PyTorch, and Streamlit, this system can predict whether an eye belongs to a male or female.

---

## 🚀 Features

- 🎯 **High-accuracy gender classification** from eye images  
- 🧠 **Pretrained ResNet-18 model** fine-tuned for eye-based gender recognition  
- 🎥 **Video stream analysis** with real-time Haar cascade eye detection  
- 🖼️ Supports **image and video uploads**  
- 🧩 **Dark-themed professional UI** built with Streamlit  
- ⚙️ Completely **offline** and privacy-focused  

---

## 🗂️ Project Structure

```
eye-gender-detector/
│
├── best_model.pth                  # Trained PyTorch model
├── eye_gender_streamlit_pro.py    # Streamlit app
├── processed_eye_dataset/         # Structured dataset
│   ├── train/
│   │   ├── female/
│   │   └── male/
│   ├── val/
│   │   ├── female/
│   │   └── male/
│   └── test/
│       ├── female/
│       └── male/
└── README.md
```

---

## 🧪 Dataset Details

The dataset consists of over **11,500+ eye images**:
- Female eyes: `~5200`
- Male eyes: `~6300`
- All images are preprocessed using Haar cascades and named as:
  - `F_XXXXX.jpg` for females
  - `M_XXXXX.jpg` for males

---

## 🛠️ Installation

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/eye-gender-detector.git
cd eye-gender-detector
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On macOS/Linux
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app:
```bash
streamlit run eye_gender_streamlit_pro.py
```

---

## 🖥️ Usage

1. Launch the app and choose **Image** or **Video** input mode.  
2. Upload an eye image (`.jpg`, `.png`) or a short video (`.mp4`, `.avi`).  
3. The model will predict and display the gender prediction based on the eye region.  

---

## 🧠 Model Architecture

- **Base Model:** ResNet-18  
- **Modifications:** Final fully connected layer adapted for binary classification  
- **Input Size:** 128×128 RGB  
- **Loss Function:** CrossEntropyLoss  
- **Optimizer:** Adam  

### 🔁 Data Augmentations:
- Random Rotations  
- Horizontal Flips  
- Brightness & Contrast Jitter  

---

## 🎓 Research Background

This project is inspired by studies on **biometric recognition** and explores the potential of **gender identification using ocular features** such as iris patterns and periocular texture.  

---

## 📦 Dependencies

- `torch`  
- `torchvision`  
- `opencv-python`  
- `streamlit`  
- `Pillow`  
- `numpy`  

Install all using:

```bash
pip install -r requirements.txt
```

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the project, submit issues, or open pull requests to enhance features, model accuracy, or UI.

---

## 🔗 Contact

👨‍💻 **Made by:** Ali Shan  
📧 Email: [Ali3819381@gmail.com](mailto:Ali3819381@gmail.com)  
🌐 Portfolio: [https://029rrct3v1.app.yourware.so/](https://029rrct3v1.app.yourware.so/)
```
