import numpy as np
import torch
import sys
import os
import matplotlib.pyplot as plt
import cv2
from unet import UNet

from PIL import Image
import torchvision.transforms as transforms
import torch


device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
model = UNet(3,1)
model.load_state_dict(torch.load(r"C:/Users/ZühalÖzdemir/PycharmProjects/satellite-change-detector/unet_model.pth",map_location=device))
model.to(device)


def load_image_as_tensor(image_path):
    # Görüntüyü aç
    image = Image.open(image_path).convert('RGB')  # 3 kanal renkli

    # Ön işleme: tensor'a çevir, normalize et
    preprocess = transforms.Compose([
        transforms.Resize((1024, 1024)),  # Modelin beklediği boyuta göre ayarla
        transforms.ToTensor(),  # [0,255] -> [0,1] ve CxHxW tensor
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Eğer modelin ImageNet gibi standart norm bekliyorsa
                             std=[0.229, 0.224,  0.225])
    ])

    image_tensor = preprocess(image)  # Tensor formatında
    return image_tensor



def predict_mask(model, image_tensor, device):
    model.eval()
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        output = model(image_tensor.unsqueeze(0))

        probs = torch.sigmoid(output)
        mask = (probs > 0.5).cpu().numpy().astype(np.uint8)[0,0]
    return mask

def xor_masks(mask1,mask2):
    return np.bitwise_xor(mask1,mask2)

def diff_img_func(img1,img2):
    outputRGB = torch.zeros_like(img1, dtype=torch.uint8)
    threshold = 0.9

    mask = (img1 / (img2 + 1e-6)) < threshold

    img2_uint8 = img2.to(torch.uint8)
    outputRGB[mask] = img2_uint8[mask]

    # Diğer pikselleri beyaz yap
    outputRGB[~mask] = 255

    return outputRGB
#
# device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
# model = UNet(3,1)
# model.load_state_dict(torch.load("unet_model.pth"))
# model.to(device)
#
# image1 = load_image_as_tensor('../../uploads/1.png')
# image2 = load_image_as_tensor('../../uploads/2.png')
#
#
# mask_1 = predict_mask(model,image1, device)
# mask_2 = predict_mask(model,image2, device)
#
# diff_mask = xor_masks(mask_1, mask_2)
# diff_img = diff_img_func(image1, image2)
#
#
# plt.figure(figsize=(12,8))
# plt.subplot(2,3,1)
# plt.title('Image 1')
# image1 = torch.permute(image1,(1,2,0)) #kanal x yükseklik x genişlik -> yükseklik x genişlik x kanal
# plt.imshow(image1)
#
# plt.subplot(2,3,4)
# plt.title('Mask 1')
# plt.imshow(mask_1, cmap='gray')
#
# plt.subplot(2,3,2)
# plt.title('Image 2')
# image2 = torch.permute(image2,(1,2,0))
# plt.imshow(image2)
#
# plt.subplot(2,3,5)
# plt.title('Mask 2')
# plt.imshow(mask_2, cmap='gray')
#
# plt.subplot(2,3,3)
# plt.title('Fark Görüntüsü (XOR)')
# diff_img = torch.permute(diff_img,(1,2,0))
# plt.imshow(diff_img)
#
# plt.subplot(2,3,6)
# plt.title('Fark Maskesi (XOR)')
# plt.imshow(diff_mask, cmap='gray')
#
# plt.show()