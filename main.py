import yaml
import os
import torch
from precompute.generate_keys import KeyGenerator
from search.key_search import KeySearcher
from utils.logger import setup_logger
from utils.gpu import check_cuda

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

logger = setup_logger()

def main():
    logger.info("🚀 Starting the Private Key Search System")

    # Check CUDA
    check_cuda()

    # Step 1: Precompute Keys
    logger.info("🔄 Precomputing necessary keys...")
    key_generator = KeyGenerator(config["precompute"])
    key_generator.generate()

    # Step 2: Start Key Search
    logger.info("🔍 Running the Pollard Rho Kangaroo Search...")
    searcher = KeySearcher(config["search"], config["gpu"])
    searcher.run()

if __name__ == "__main__":
    main()
