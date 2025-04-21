# 👁️ Eye Gender Detection via Deep Learning

A powerful offline application for **gender classification** based solely on **eye patterns** from images and videos. Leveraging deep learning, PyTorch, and Streamlit, this system predicts whether an eye belongs to a male or female with high accuracy.

---

## 🚀 Features

- 🎯 **High-accuracy classification** from eye images
- 🧠 **Pretrained ResNet-18** model fine-tuned for ocular-based recognition
- 🎥 Real-time **video stream analysis** with Haar cascade eye detection
- 🖼️ **Image and video** upload support
- 🌑 **Dark-themed, professional UI** built in Streamlit
- 🔒 100% **offline and privacy-friendly**

---

## 🗂️ Project Structure
eye-gender-detector/ │ ├── best_model.pth # Trained PyTorch model ├── eye_gender_streamlit_pro.py # Streamlit app ├── processed_eye_dataset/ # Structured dataset │ ├── train/ │ │ ├── female/ │ │ └── male/ │ ├── val/ │ │ ├── female/ │ │ └── male/ │ └── test/ │ ├── female/ │ └── male/ └── README.md


---

## 🧪 Dataset Details

The dataset includes over **11,500+ eye images**:
- 👁️ Female eyes: ~5,200
- 👁️ Male eyes: ~6,300

Each image is:
- Cropped using `haarcascade_eye.xml`
- Renamed as:
  - `F_XXXXX.jpg` → Female
  - `M_XXXXX.jpg` → Male

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eye-gender-detector.git
   cd eye-gender-detector
Create and activate virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Run the Streamlit app

streamlit run eye_gender_streamlit_pro.py
🖥️ Usage
Open the app
Select Image or Video mode
Upload an eye image or video clip
View gender prediction instantly on screen
🧠 Model Architecture
Base model: ResNet-18
Fine-tuned layer: Custom FC layer for binary output
Input shape: 128×128 RGB images
Loss: CrossEntropyLoss
Optimizer: Adam
Data Augmentation:
Random rotations
Horizontal flips
Brightness and contrast jittering
🎓 Research Background
This project explores the possibility of determining gender using ocular features such as the iris, eyelids, and periocular texture. Inspired by biometrics and human behavioral science, this system pushes the boundaries of gender prediction using minimal visual input.

📦 Dependencies
torch
torchvision
opencv-python
streamlit
Pillow
numpy
Install via:

pip install -r requirements.txt
📄 License
This project is licensed under the MIT License.
See the LICENSE file for full terms.

🤝 Contributing
Contributions are welcome!
Feel free to:

Fork the project
Suggest enhancements
Open issues
Submit PRs
🔗 Contact
👤 Made by Ali Shan
📧 Email: Ali3819381@gmail.com
🌐 Portfolio: https://029rrct3v1.app.yourware.so/

