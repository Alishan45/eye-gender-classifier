📁 README.md
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
eye-gender-detector/ │ ├── best_model.pth # Trained PyTorch model ├── eye_gender_streamlit_pro.py # Streamlit app ├── processed_eye_dataset/ # Structured dataset │ ├── train/female/ │ ├── train/male/ │ ├── val/female/ │ ├── val/male/ │ └── test/female/ │ └── test/male/ └── README.md


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

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/eye-gender-detector.git
   cd eye-gender-detector
Create and activate virtual environment:

python -m venv venv
venv\\Scripts\\activate  # Windows
source venv/bin/activate  # Linux/macOS
Install dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run eye_gender_streamlit_pro.py
🖥️ Usage
Launch the app and choose Image or Video input mode.
Upload an eye image (JPEG, PNG) or a short video (MP4, AVI).
Let the model predict gender based on eye region only.
🧠 Model Architecture
Base model: ResNet-18
Fine-tuning: Last FC layer modified for binary classification
Input size: 128×128 RGB
Loss: CrossEntropyLoss
Optimizer: Adam
Data Augmentations:
Random rotations
Horizontal flips
Brightness & contrast jitter
🎓 Research Background
This project was inspired by studies on human biometric identification and the possibility of gender classification from ocular features like iris patterns and periocular texture.

📦 Dependencies
torch
torchvision
opencv-python
streamlit
Pillow
numpy
Install all using:

pip install -r requirements.txt
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing
Contributions are welcome! Feel free to fork the project, open issues, or submit pull requests.

🔗 Contact
Made by Ali Shan
📧 [Ali3819381@gmail.com]
🌐 [https://029rrct3v1.app.yourware.so/]


