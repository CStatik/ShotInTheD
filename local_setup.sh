#!/bin/bash
echo "🚀 Setting up the local environment"
pip3 install -r requirements
python3 -c "import torch; print('CUDA Available:', torch.cuda.is_available())"
echo "✅ Setup Complete!"
