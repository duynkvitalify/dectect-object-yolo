
# TODO: Rm try-except with scipy 1.10 is the minimum supported version

try:
    from scipy.datasets import face
except ImportError:  # Data was in scipy.misc prior to scipy v1.10
    from scipy.misc import face

img = face()
import matplotlib.pyplot as plt

plt.imshow(img)
plt.show()


print(img[:,:,0])