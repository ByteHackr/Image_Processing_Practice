import imageio
import matplotlib.pyplot as plt

pic = imageio.imread('parrotsec.png')
plt.figure(figsize = (6,6))
plt.imshow(255 - pic);
