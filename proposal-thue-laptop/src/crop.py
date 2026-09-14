# -*- coding: utf-8 -*-
"""Cắt bỏ viền trắng thừa quanh ảnh hình minh hoạ."""
import sys, os
from PIL import Image, ImageChops

def trim(path, pad=24, bg=(255, 255, 255)):
    im = Image.open(path).convert("RGB")
    bgim = Image.new("RGB", im.size, bg)
    diff = ImageChops.difference(im, bgim)
    box = diff.getbbox()
    if not box:
        return im.size
    l, t, r, b = box
    l = max(0, l - pad); t = max(0, t - pad)
    r = min(im.width, r + pad); b = min(im.height, b + pad)
    im.crop((l, t, r, b)).save(path)
    return (r - l, b - t)

if __name__ == "__main__":
    for p in sys.argv[1:]:
        w, h = trim(p)
        print("%-46s %5d x %5d  ratio %.2f" % (os.path.basename(p), w, h, w / h))
