import torch

if torch.cuda.is_available():
    print("Menggunakan GPU:", torch.cuda.get_device_name(0))
else:
    print("Tidak menggunakan GPU")