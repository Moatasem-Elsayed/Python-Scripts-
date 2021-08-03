from PIL  import Image
from PIL.ExifTags import TAGS
from stegano import exifHeader

#secret=exifHeader.hide("D:\\junction\\personal\\20200829_113745.jpg","ID.jpg",secret_message="Moatasem")
#print(exifHeader.reveal("ID.jpg").decode("UTF-8"))

image=Image.open("ID.jpg")
exifdata=image.getexif()

for tagid in exifdata:
    tagname=TAGS.get(tagid)
    value=exifdata.get(tagid)
    
    if tagname =="ImageDescription":
        print (exifHeader.reveal("ID.jpg").decode("UTF-8"))
    else:
        print(f"{tagname} :{value}")