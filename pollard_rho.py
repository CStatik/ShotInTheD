import random
import ecdsa
from utils.logger import setup_logger

class PollardRho:
    def __init__(self, start, end, target_public_key):
        self.start = start
        self.end = end
        self.target_public_key = target_public_key
        self.logger = setup_logger()

    def search(self):
        self.logger.info("🔄 Running Pollard Rho Algorithm...")
        x = random.randint(self.start, self.end)
        while x <= self.end:
            sk = ecdsa.SigningKey.from_secret_exponent(x, curve=ecdsa.SECP256k1)
            pk = sk.verifying_key.to_string().hex()
            if pk == self.target_public_key:
                return x
            x += 1  # Incremental step (simplified)
        return None
