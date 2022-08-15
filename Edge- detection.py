from cProfile import label
import skimage 
from skimage import io
import matplotlib.pyplot as plt
from skimage.filters import prewitt_h, roberts, scharr, sobel_v,roberts_pos_diag

img2= io.imread(".../image.jpg",as_gray=True)
horizontal_edge= prewitt_h(img2, mask=None)
vertical_edge= sobel_v(img2, mask=None)
cross_edge= roberts_pos_diag(img2, mask=None)

# plt.imshow(edge1, cmap='gray')
plt.figure('horizontal_edge')
# plt.imshow(horizontal_edge, cmap='gray',)
plt.figure('vertical_edge')
# plt.imshow(vertical_edge, cmap='gray',)
plt.figure('cross_edge')

plt.imsave("C:/Users/dell/Desktop/Project/images/Results/Image(2).Edge_detection/horizontal_edge.jpg",horizontal_edge,cmap='gray')
plt.imsave("C:/Users/dell/Desktop/Project/images/Results/Image(2).Edge_detection/vertical_edge.jpg",vertical_edge,cmap='gray')
plt.imsave("C:/Users/dell/Desktop/Project/images/Results/Image(2).Edge_detection/cross_edge.jpg",cross_edge,cmap='gray')
# plt.imshow(cross_edge, cmap='gray',)
# plt.show()
