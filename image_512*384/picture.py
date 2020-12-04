# 原图片采用4:3，不管到底是多大
# 处理后的图片也是4:3，大小是512*384像素
# 反正3:4也行，处理完就是384*512而已
# 将该文件中的路径替换成自己的路径
# for jpgfile in glob.glob("C:\\Users\\hanwa\\Desktop\\before\*.*"):
#     convertjpg(jpgfile,"C:\\Users\\hanwa\\Desktop\\after")
# 上面两行的代码，""里面的是路径
# 根据C++的知识可以得到，不能直接全用"\"表示的
# 对于文件夹的一层一层展开，应该使用"\\"，而其中的文件是用"\"展开
# '*.*'前面是文件的名称，后面是文件的格式
# 路径可以是带有中文名字的，文件的名称同理
# 上面代码的第一行是原来的图片路径，下面一行的路径是修改后的图片储存路径
# Have Fun in Writing News!
from PIL import Image
from math import fabs
import os.path
import glob
def detect(jpgfile):
    img=Image.open(jpgfile)
    b = (img.width)/(img.height)
    if fabs(b - 4/3) < 0.01:
        return 0
    elif fabs(b - 3/4) < 0.01:
        return 1
    else:
        return 2
def convertjpg_43(jpgfile,outdir,width=512,height=384):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
def convertjpg_34(jpgfile,outdir,width=384,height=512):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("C:\\Users\\hanwa\\Desktop\\before\*.*"):
# convertjpg_43(jpgfile,"C:\\Users\\hanwa\\Desktop\\after")
    a = detect(jpgfile)
    if a == 0:
        convertjpg_43(jpgfile,"C:\\Users\\hanwa\\Desktop\\after")
    elif a == 1:
        convertjpg_34(jpgfile,"C:\\Users\\hanwa\\Desktop\\after")
    elif a == 2:
        print('Sorry, please use Photoshop to edit this picture\n')
    else:
        print('Wrong')
