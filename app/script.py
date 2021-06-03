import os
from PIL import Image

yourpath = ''

def convert(basewidth,quality,new_folder):
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files:
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif":
                outfile = os.path.splitext(os.path.join(new_folder, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    print ("Generating jpeg for %s" % name)
                    wpercent = (basewidth / float(im.size[0]))
                    hsize = int((float(im.size[1]) * float(wpercent)))
                    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
                    im.save(outfile, "JPEG", quality=quality)
                except Exception as e:
                    print (e)
