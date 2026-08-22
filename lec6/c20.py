# opens and saves binary files

import sys

from PIL import Image

images =[]

for arg in sys.argv[1:]:
    image= Image.open(arg)
    images.append(image)


images[0].save(

    "new.gif", save_all=True, append_images=[images[1]], duration=300, loop=0

)


gif = Image.open("new.gif")

print(gif.n_frames)