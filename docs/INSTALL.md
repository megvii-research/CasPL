# Installation

### Acknowledgement: This readme file for installing datasets is modified from [MaPLe's](https://github.com/muzairkhattak/multimodal-prompt-learning) official repository.

* Setup conda environment (recommended).
```bash
# Create a conda environment
conda create -y -n caspl python=3.9.19

# Activate the environment
conda activate caspl

# Install torch (requires version >= 1.8.1) and torchvision
# Please refer to https://pytorch.org/ if you need a different cuda version
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
```



* Clone CasPL code repository and install requirements
```bash
# Clone PromptSRC code base
git clone https://github.com/megvii-research/CasPL.git

cd CasPL/
# Install requirements

pip install -r requirements.txt

# Update setuptools package 
pip install setuptools==69.5.1
```
