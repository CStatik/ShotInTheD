import os
import struct
from utils.logger import setup_logger

class KeyGenerator:
    def __init__(self, config):
        self.start = int(config["key_range"].split(":")[0])
        self.end = int(config["key_range"].split(":")[1])
        self.batch_size = config["batch_size"]
        self.storage_path = config["storage_path"]
        self.logger = setup_logger()

    def generate(self):
        self.logger.info(f"📝 Generating keys from {hex(self.start)} to {hex(self.end)}")
        
        with open(self.storage_path, "wb") as f:
            current = self.start
            while current < self.end:
                batch_end = min(current + self.batch_size, self.end)

                # Generate numbers in batch
                batch = list(range(current, batch_end))

                # Convert numbers to 16-byte Big Endian format and write
                for num in batch:
                    f.write(num.to_bytes(16, "big"))  # Store each as 16-byte integer

                self.logger.info(f"✅ Generated keys from {hex(current)} to {hex(batch_end)}")
                current = batch_end

        self.logger.info(f"✅ Precomputed keys saved at {self.storage_path}")

if __name__ == "__main__":
    KeyGenerator().generate()
