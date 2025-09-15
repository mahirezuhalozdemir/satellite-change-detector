# 🌍 Satellite Change Detector  

A Python-based system that detects and visualizes meaningful changes between two satellite images taken at different times, using image processing and AI techniques.  

---

## 📌 Features  
- Upload two satellite images and detect differences  
- Image preprocessing (resize, denoise, normalize)  
- Change detection using image differencing + AI-based methods  
- Web interface built with Flask (upload & results page)  
- Visualization of detected change regions 

---

## 🛠️ Technologies  
- **Python 3.9+**  
- **Flask** – web framework  
- **OpenCV** – image processing  
- **NumPy / Pandas** – data handling  
- **Matplotlib** – visualization  
- **Scikit-learn / PyTorch / TensorFlow**

---

## 📂 Project Structure  
```
satellite-change-detector/
│── pycache/ # Python cache files
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
   ```bash
   git clone https://github.com/yourusername/satellite-change-detector.git
   cd satellite-change-detector
1. Create a virtual environment & install dependencies: 
   ```bash

   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)

   pip install -r requirements.txt


---

## ▶️ Usage

Run the detector with two input satellite images:

---


## Example Outputs

<img width="1625" height="427" alt="Screenshot 2025-08-29 164532" src="https://github.com/user-attachments/assets/1f6d6601-94ca-4b48-8031-946bb3964b66" />
<img width="1765" height="535" alt="Screenshot 2025-08-29 164542" src="https://github.com/user-attachments/assets/db9c2fe1-f532-40f5-be0a-d9808a496359" />

<img width="1699" height="690" alt="Screenshot 2025-08-29 170916" src="https://github.com/user-attachments/assets/e584df8d-a1c8-49da-a126-75beab70a826" />
<img width="1571" height="680" alt="Screenshot 2025-08-29 170924" src="https://github.com/user-attachments/assets/369e70a9-b963-4c6a-8e32-a6aa3982ab05" />

## Future Improvements

- Deep learning models (CNN/UNet) for more accurate change detection

- Support for multispectral satellite images

- Interactive dashboard for visualization
