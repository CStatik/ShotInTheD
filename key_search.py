import time
import torch
from search.kangaroo import KangarooSearch
from utils.logger import setup_logger
from precompute.key_storage import KeyStorage

class KeySearcher:
    def __init__(self, search_config, gpu_config):
        self.target_public_key = search_config["target_public_key"]
        self.device = torch.device(gpu_config["device"]) if gpu_config["use_cuda"] else torch.device("cpu")
        self.batch_size = gpu_config["batch_size"]
        self.logger = setup_logger()
        self.key_storage = KeyStorage()

    def run(self):
        self.logger.info(f"🔍 Searching for private key that matches: {self.target_public_key}")
        solver = KangarooSearch(self.target_public_key, self.device, self.batch_size, self.key_storage)
        result = solver.search()

        if result:
            self.logger.info(f"✅ Private key found: {hex(result)}")
        else:
            self.logger.warning("❌ No key found.")

if __name__ == "__main__":
    searcher = KeySearcher()
    searcher.run()
