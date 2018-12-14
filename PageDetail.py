from DomPosition import DomPosition
class PageDetail(object):
    """页面详细信息"""
    Name = "";
    ImgSrc = "";
    DomDic = {};
    Back = (56,37);

    def __init__(self,name,imgSrc,dic):
        self.Name = name;
        self.ImgSrc = imgSrc;
        self.DomDic = dic;
        if "back" in dic.keys():
            Back = dic["back"]

