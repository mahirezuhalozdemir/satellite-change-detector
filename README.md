# 🌍 Satellite Change Detector  

A Python-based system that detects and visualizes meaningful changes between two satellite images taken at different times, using image processing and AI techniques.  

---

## 📌 Features  
- Compare two satellite images and highlight significant changes  
- Image preprocessing (resizing, denoising, normalization)  
- Change detection using image differencing + AI-based methods  
- Visualization of detected change regions  
- Modular and extensible Python codebase  

---

## 🛠️ Technologies  
- **Python 3.9+**  
- **OpenCV** – image processing  
- **NumPy / Pandas** – data handling  
- **Matplotlib / Seaborn** – visualization  
- **Scikit-learn / PyTorch / TensorFlow** (depending on chosen AI method)  

---

## 📂 Project Structure  
```
satellite-change-detector/
│── data/ # Sample input images
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Source code
│ ├── preprocess.py # Preprocessing steps
│ ├── detect.py # Change detection logic
│ ├── visualize.py # Visualization of results
│── requirements.txt # Dependencies
│── README.md # Project documentation
```


---

## 🚀 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/satellite-change-detector.git
   cd satellite-change-detector

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
