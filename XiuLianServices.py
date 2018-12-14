from AdbTools import AdbTools
from BaseServices import BaseServices
from Constant import Constant;
import time;
class XiuLianServices(BaseServices):
    """刷书页服务"""
    page = Constant.XiuLianPage;
    def __init__(self):
        BaseServices.__init__(self);
        """构造函数，定义初始配置"""
        pass
    def bettle(self):
        for i in range(30):
            self.tool.tap(1720,505)
            self.tool.tap(1878,506)
            self.tool.tap(2031,507)
            self.tool.tap(1790,959)
            time.sleep(2)
        time.sleep(3)
        pass

    def doPoint(self):
        x = self.page.DomDic["书页特级"][0];
        y = self.page.DomDic["书页特级"][1];
        self.tool.tap(x,y)
        self.tool.tap(x,y)
        time.sleep(1);
        self.tool.tap(728,845)
        self.tool.tap(728,845)
        time.sleep(1);
        self.tool.tap(560,548)
        self.tool.tap(560,548)

        time.sleep(1);
        self.tool.tap(1643,954)
        self.tool.tap(1643,954)
        time.sleep(3);
        self.bettle()
        pass

server=XiuLianServices()
server.doPoint();

