#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np

demo = cv2.imread(r"C:\Users\Asus\Documents\SEMESTER 3\PRAKTIK SISTEM KEAMANAN DATA\V3922012_CLARIVA MEYDIETA WIDAGDO_RSA-ENKRIPSI GAMBAR\roti-sobek.jpg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)
cv2.imwrite(r"C:\Users\Asus\Documents\SEMESTER 3\PRAKTIK SISTEM KEAMANAN DATA\V3922012_CLARIVA MEYDIETA WIDAGDO_RSA-ENKRIPSI GAMBAR\roti-sobek.jpg", key)

cv2.imshow("demo", demo)
cv2.imshow("key", key)

encryption = cv2.bitwise_xor(demo, key)
cv2.imwrite(r"C:\Users\Asus\Documents\SEMESTER 3\PRAKTIK SISTEM KEAMANAN DATA\V3922012_CLARIVA MEYDIETA WIDAGDO_RSA-ENKRIPSI GAMBAR\ENKRIPSI-roti-sobek.jpg", encryption)
decryption = cv2.bitwise_xor(encryption, key)
cv2.imwrite(r"C:\Users\Asus\Documents\SEMESTER 3\PRAKTIK SISTEM KEAMANAN DATA\V3922012_CLARIVA MEYDIETA WIDAGDO_RSA-ENKRIPSI GAMBAR\DESKRIPSI-roti-sobek.jpg", decryption)

cv2.imshow("encryption", encryption)
cv2.imshow("decryption", decryption)

cv2.waitKey(-1)
cv2.destroyAllWindows()


# In[ ]:




