import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image
from torchvision import models, transforms
import tempfile

# -----------------------
# Streamlit Config & Style
# -----------------------
st.set_page_config(page_title="Eye Gender Detector", layout="centered", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stApp {
        background-color: #0e1117;
    }
    .css-1v3fvcr, .css-1d391kg, .css-18e3th9 {
        background-color: #161c28;
        border-radius: 10px;
        padding: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Eye Gender Detection")
st.caption("Detect gender from eye images or videos — powered by PyTorch")

# -----------------------
# Load Model
# -----------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load("best_model.pth", map_location=device))
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# -----------------------
# Helper Functions
# -----------------------
def predict_eye(img):
    img_tensor = transform(img).unsqueeze(0).to(device)
    output = model(img_tensor)
    _, pred = torch.max(output, 1)
    return "Male" if pred.item() == 1 else "Female"

def process_image(uploaded_image):
    img = Image.open(uploaded_image).convert("RGB")
    label = predict_eye(img)
    st.image(img, caption=f"Prediction: {label}", use_column_width=True)

def process_video(video_file):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in eyes:
            eye_crop = frame[y:y+h, x:x+w]
            eye_img = cv2.cvtColor(eye_crop, cv2.COLOR_BGR2RGB)
            eye_pil = Image.fromarray(eye_img)
            label = predict_eye(eye_pil)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
            cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        stframe.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)

    cap.release()

# -----------------------
# Streamlit UI
# -----------------------
mode = st.sidebar.radio("Choose Input Type", ("Image", "Video"))

if mode == "Image":
    uploaded_image = st.file_uploader("Upload an eye image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        process_image(uploaded_image)

elif mode == "Video":
    uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi"])
    if uploaded_video:
        process_video(uploaded_video)
