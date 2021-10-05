import os
from voicefixer.vocoder.config import Config

if (not os.path.exists(Config.ckpt)):
    os.makedirs(os.path.dirname(Config.ckpt), exist_ok=True)
    print("Downloading the weight of neural vocoder: TFGAN")
    cmd = "wget https://zenodo.org/record/5469951/files/model.ckpt-1490000_trimed.pt?download=1 -O " + Config.ckpt
    os.system(cmd)
