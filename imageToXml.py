
from PIL import Image

def progressBar(progress, maxVal, prefix = "", suffix = ""):
    ratio = float(progress/(maxVal-1))
    bar = int(round(ratio*20, 0))
    text = "[{0}] {1}%".format(("#"*bar)+"-"*(20-bar), int(ratio*100))
    print(prefix, text, suffix, end="\r")
img = Image.open(input("image path: ")).convert("RGB")
pxl = img.load()
w, h = img.size
string = '<xml> <image width="{0}" heigth="{1}">\n'.format(w, h)
for i in range(h):
    progressBar(i, h)
    string = string + '  <row num="{0}">\n'.format(i,)
    for j in range(w):
        string = string + '   <col num="{0}">\n    <red>{1}</red>\n    <green>{2}</green>\n    <blue>{3}</blue>\n   </col>\n'.format(j,pxl[j, i][0], pxl[j, i][1], pxl[j, i][2])
    string = string + " </row>\n"
string = string + " </image></xml>"
file = open(input("\nsave to: "),"w")
file.write(string)
file.close()
