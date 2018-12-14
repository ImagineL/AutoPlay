from AdbTools import AdbTools
from ImgCompare import CompareImage
from PageDetail import PageDetail

class BaseServices(object):
    tool = AdbTools();
    imgTool = CompareImage();
    page = PageDetail("xiulian","/ScreenShot/xiulian-chuji.jpg",{"特级":(1555,720),"开始修炼":(747,851)});
    tempPath = "./ScreenShot/";
    name = "base";
    dissMinPoint = "0.7";
    tempJpgPath = "";
    """进入页面的基类"""
    def __init__(self):
        self.tempJpgPath = self.tempPath + self.page.Name + ".png"; 
    
    def Enter(self):
        self.__getShot__()
        #diffPoint = self.imgTool.compare_image(self.tempJpgPath,self.page.ImgSrc);
        #if diffPoint < self.dissMinPoint:
        #    raise print("图片相似度过低，被认为未进入页面:");
        #print("=============进入正确页面=============");
        self.doPoint()

    def __getShot__(self):
        self.tool.screenshot(self.tempJpgPath)
    def doPoint(self):

        pass
