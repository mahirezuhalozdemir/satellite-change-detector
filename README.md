# 🌍 Satellite Change Detector  
This project is a **web application for satellite image change detection**.  
Users can upload two satellite images, and the app will:  

- Generate **segmentation masks** for both images  
- Create a **difference image**  
- Produce a **difference mask** (highlighting the changes between the two images)  
- Display all results in a simple web interface  
---


## 📑 Table of Contents  

- [📌 Features](#-features)  
- [🛠️ Technologies](#️-technologies)  
- [📂 Project Structure](#-project-structure)  
- [🚀 Installation](#-installation)  
- [▶️ Usage](#️-usage)  
- [📌 Notes](#-notes)  
- [🖼️ Example Outputs](#example-outputs)  

---

## 📌 Features  

- **UNet-based Semantic Segmentation** for mask prediction  
- Generates difference image between two satellite images  
- Computes XOR-based difference mask to highlight changed areas  
- Web interface for uploading images and visualizing results  
---

## 🛠️ Technologies  
- **Flask** – Web framework  
- **PyTorch** – Deep learning inference (UNet model)  
- **Pillow (PIL)** – Image processing  
- **Torchvision** – Image transforms  
- **NumPy** – Array operations  

---

## 📂 Project Structure  
```
satellite-change-detector/
│── dataset/ # Example input satellite images
│── src/ # Core image processing & detection logic
│── static/ # CSS, JS, and output result images
│── templates/ # HTML templates (Flask frontend)
│── uploads/ # User-uploaded images
│── app.py # Main Flask application
│── requirements.txt # Dependencies
│── README.md # Project documentation
```


---

## 🚀 Installation  
1. Clone the repository:  
   ``` bash
   git clone https://github.com/mahirezuhalozdemir/satellite-change-detector.git
   cd satellite-change-detector
   
2. Install dependencies: 
   ``` bash
   pip install -r requirements.txt


3. Run the Flask app
   ``` bash
   python app.py
   ```


4. Open in browser
   ``` bash
   http://127.0.0.1:5000


---

## ▶️ Usage

1. Upload two satellite images from the home page

2. Click "Generate Masks"

3. View results:

   - Uploaded images

   - Segmentation masks

   - Difference image

   - Difference mask

---


## 📌 Notes

- Images are resized to 224x224 before inference

- The model runs on GPU if available, otherwise CPU

- All results are saved under static/results

---

## Example Outputs

<img width="1625" height="427" alt="Screenshot 2025-08-29 164532" src="https://github.com/user-attachments/assets/1f6d6601-94ca-4b48-8031-946bb3964b66" />
<img width="1765" height="535" alt="Screenshot 2025-08-29 164542" src="https://github.com/user-attachments/assets/db9c2fe1-f532-40f5-be0a-d9808a496359" />

<img width="1699" height="690" alt="Screenshot 2025-08-29 170916" src="https://github.com/user-attachments/assets/e584df8d-a1c8-49da-a126-75beab70a826" />
<img width="1571" height="680" alt="Screenshot 2025-08-29 170924" src="https://github.com/user-attachments/assets/369e70a9-b963-4c6a-8e32-a6aa3982ab05" />

