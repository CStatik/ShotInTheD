import torch
import struct

class KeyStorage:
    def __init__(self, storage_path="./precompute/lookup_table.bin"):
        self.storage_path = storage_path

    def load_keys(self):
        with open(self.storage_path, "rb") as f:
            data = f.read()
            return torch.tensor(struct.unpack(f"{len(data)//8}Q", data), dtype=torch.int64)
