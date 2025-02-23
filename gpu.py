import torch

def check_cuda():
    if torch.cuda.is_available():
        print("✅ CUDA is available! Running on GPU.")
    else:
        print("⚠️ CUDA is NOT available! Running on CPU.")
