import sys
import os
from AdbTools import AdbTools

def main():
    tool = AdbTools()
    #tool.start_application("com.netease.h48.vivo")
    #tool.screenshot("./shot/xxd.png")
    print(tool.get_screen_normal_size())
    tool.tap(119,126)
    return 0
def enter(tool):
    pass

if __name__ == "__main__":
    sys.exit(int(main() or 0))
