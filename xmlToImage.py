
from PIL import Image
import xml.etree.ElementTree as ET

def progressBar(progress, maxVal, prefix = "", suffix = ""):
    ratio = float(progress/(maxVal-1))
    bar = int(round(ratio*20, 0))
    text = "[{0}] {1}%".format(("#"*bar)+"-"*(20-bar), int(ratio*100))
    print(prefix, text, suffix, end="\r")
list=list()
file = open(input("file: ")).read()
print("reading xml")
xml=ET.fromstring(file)
print("read xml")
image=xml.findall("image")
for item in image:
    w=int(item.get("width"))
    h=int(item.get("heigth"))
    print("size:", w, h)
img=Image.new("RGB", (w, h), color=0)
pxl=img.load()
for imageItem in image:
    row=imageItem.findall("row")
    for rowItem in row:
        rownum=int(rowItem.get("num"))
        progressBar(rownum, w)
        col=rowItem.findall("col")
        for colItem in col:
            colnum=int(colItem.get("num"))
            pxl[colnum, rownum]=(int(colItem.find("red").text), int(colItem.find("green").text), int(colItem.find("blue").text))
img.save("out.bmp")
