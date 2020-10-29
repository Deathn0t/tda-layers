import os

import numpy as np

from tqdm import tqdm

from PIL import Image
# from libtiff import TIFF


from shared_code import check_pershombox_availability
check_pershombox_availability()
from pershombox import calculate_discrete_NPHT_2d

HERE = os.path.dirname(os.path.abspath(__file__))

data_root = os.path.join("..", "assets", "animal")
classes = [f for f in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, f))]
print(len(classes), "classes")
labels = [c_i for c_i, _ in enumerate(classes)]

X, y = [], []
n_directions = 1
debug = False

for c_i, c in enumerate(classes):
    c_path = os.path.join(data_root, c)
    for f in tqdm(os.listdir(c_path)):
        if os.path.isfile(os.path.join(c_path, f)) and f[-4:] == ".tif":
            im_path = os.path.join(c_path, f)
            print(im_path)
            im = Image.open(im_path)
#             tif = TIFF.open(im_path, mode="r")
#             im = tif.read_image()
            imarray = im.getdata()
            # imarray = np.array(im)
            continue

            pdgm = calculate_discrete_NPHT_2d(imarray, n_directions)
            X.append(pdgm)
#             X.append(imarray)
            y.append(c_i)
            if debug:
                break