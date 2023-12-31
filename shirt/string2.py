
import os

import sys
from PIL import Image,ImageOps
a=str(sys.argv[1])

b=str(sys.argv[2])
image=Image.open(a)


shirt = Image.open("shirt.png")
d=shirt.copy()
image=ImageOps.fit(image,shirt.size)
image.paste(shirt,mask=shirt)
image.save(b)




