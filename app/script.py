import ftplib
import os
from PIL import Image

yourpath = ''


def send_to_ftp(folder):
    ftp = ftplib.FTP('kislov.myjino.ru', 'kislov_herb', 'fjskibn1')
    ftp.cwd('jpgimgs')

    for subdir, dirs, files in os.walk(folder):
        for file in files:
            file = os.path.join(subdir, file)
            print("Uploading", file)
            file_ = open(file, 'rb')
            name = str(file_).split('\\')[-3] + '||' + str(file_).split('\\')[-1]
            ftp.storbinary('STOR ' + name[:-2:], file_)
            file_.close()


def convert(wpercent, quality, new_folder):
    for root, dirs, files in os.walk(yourpath, topdown=False):
        for name in files:
            if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif" or \
                    os.path.splitext(os.path.join(root, name))[1].lower() == ".tiff":
                outfile = os.path.splitext(os.path.join(new_folder, name))[0] + ".jpg"
                try:
                    im = Image.open(os.path.join(root, name))
                    if wpercent == 150:
                        width = 150
                        height = 150
                    else:
                        width = int(float(im.size[0]) * (wpercent / 100))
                        height = int(float(im.size[1]) * (wpercent / 100))
                    im = im.resize((width, height), Image.ANTIALIAS)
                    im.save(outfile, "JPEG", quality=quality)
                    print("Generating jpeg for %s" % name)
                except Exception as e:
                    print(e)
