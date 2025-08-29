from flask import Flask, render_template, request, send_file, url_for
import torch
from PIL import Image
import numpy as np
import io
import semantic_segmentation as seg
from unet import UNet
import base64
import os
import uuid
import torchvision.transforms as T

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),  # [C, H, W] formatında verir, [0,1] normalize eder
])


device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model = UNet(3,1)
model.load_state_dict(torch.load(r"C:/Users/ZühalÖzdemir/PycharmProjects/satellite-change-detector/unet_model.pth",map_location=device))
model.to(device)

app = Flask(__name__)

UPLOAD_FOLDER = "static/results"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route('/', methods=["GET","POST"])
def main():
    return render_template("index.html")


@app.route('/createmask', methods=["GET","POST"])
def createmask():
    img3 = None
    if request.method == "POST":
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")
        if file1 and file2:
            # İSİMLENDİRMELER
            img1_name = f"{uuid.uuid4().hex}file1.png"
            img2_name = f"{uuid.uuid4().hex}file2.png"
            img3_name = f"{uuid.uuid4().hex}diff_img.png"
            mask1_name = f"{uuid.uuid4().hex}mask1.png"
            mask2_name = f"{uuid.uuid4().hex}mask2.png"
            mask3_name = f"{uuid.uuid4().hex}diff_mask.png"

            # YÜKLENEN GÖRSELLER
            img1 = Image.open(file1).convert("RGB")
            img2 = Image.open(file2).convert("RGB")

            file_path_img1 = os.path.join(UPLOAD_FOLDER, img1_name)
            file_path_img2 = os.path.join(UPLOAD_FOLDER, img2_name)

            img1.save(file_path_img1, "PNG")
            img2.save(file_path_img2, "PNG")

            # ************************************************************************

            # OLUŞAN MASKELER
            img1_tensor = seg.load_image_as_tensor(file_path_img1)
            img2_tensor = seg.load_image_as_tensor(file_path_img2)

            # Maskeleri tahmin et
            mask_1 = seg.predict_mask(model, img1_tensor, device)
            mask_2 = seg.predict_mask(model, img2_tensor, device)

            mask_1_img = Image.fromarray(mask_1 * 255)
            mask_2_img = Image.fromarray(mask_2 * 255)

            file_path_mask1 = os.path.join(UPLOAD_FOLDER, mask1_name)
            file_path_mask2 = os.path.join(UPLOAD_FOLDER, mask2_name)

            mask_1_img.save(file_path_mask1, "PNG")
            mask_2_img.save(file_path_mask2, "PNG")

            # ************************************************************************

            # FARK GÖRÜNTÜSÜ
            diff_img = seg.diff_img_func(img1_tensor, img2_tensor)
            diff_img = diff_img.permute(1, 2, 0)  # CHW -> HWC
            diff_np = diff_img.cpu().numpy().astype("uint8")
            diff_pil = Image.fromarray(diff_np)
            file_path_diff = os.path.join(UPLOAD_FOLDER, img3_name)
            diff_pil.save(file_path_diff, "PNG")

            # ************************************************************************

            # FARK MASKESİ
            diff_mask = seg.xor_masks(mask_1_img,mask_2_img)
            print("DIFF MASK: ",diff_mask.shape)
            diff_pil_mask = Image.fromarray(diff_mask)
            file_path_diff_mask = os.path.join(UPLOAD_FOLDER, mask3_name)
            diff_pil_mask.save(file_path_diff_mask, "PNG")

            # Sonucu template’e gönder
            return render_template("result.html",
                                   img1=url_for("static", filename=f"results/{img1_name}"),
                                   img2=url_for("static", filename=f"results/{img2_name}"),
                                   mask1=url_for("static", filename=f"results/{mask1_name}"),
                                   mask2=url_for("static", filename=f"results/{mask2_name}"),
                                   diff_image=url_for("static", filename=f"results/{img3_name}"),
                                   diff_mask=url_for("static", filename=f"results/{mask3_name}")
                                   )
    else:
        return render_template("index.html")

if __name__ =='__main__':
    app.run(debug=True)