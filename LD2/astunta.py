import glob
from dominate import document
from dominate.tags import *
import os

photos = glob.glob('uzduotis3\*.png')

with document(title='Photos') as doc:
    h1('Photos')
    for path in photos:
        div(img(src=os.path.basename(path)), _class='photo')


with open(r'uzduotis3\gallery.html', 'w') as f:
    f.write(doc.render())