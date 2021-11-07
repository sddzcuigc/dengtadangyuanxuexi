"""
备注：
浏览器断点调试，不需要每次都要重新跑 函数实现
"""
import os
from selenium.webdriver.chrome.options import Options
import socket
# path1=r';%PROGRAMFILES(X86)%\Google\Chrome\Application\;'
# path2=r'%PROGRAMFILES%\Google\Chrome\Application\;'
# path3=r'%HOMEPATH%\AppData\Local\Google\Chrome\Application\;'
# os.environ['PATH'] +=path1 +path2+path3
# print(os.environ['PATH'])
# 单独打开浏览器，使用9222端口，信息保存到E:/pythonwork/testfile
# 请在这个浏览器下面安装xpath-help儿插件
driver = None
def debug_browser():
    global driver
    ip = '127.0.0.1'
    port = 9222
    user_file = 'D:\selenium_ui_auto\chrome_temp'
    chrome_option = Options()
    """
    判断调试端口是否监听
    :return:check 是否监听
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        check = True
    else:
        check = False
    sock.close()
    """
    :return: chrome_option 浏览器调试选项
    """
    # 判断是否已经启动调试端口，已启动直接添加监听选项
    if check:
        chrome_option.add_experimental_option('debuggerAddress', '{}:{}'.format(ip, port))
    # 未启动则重新启动浏览器并监听调试端口
    else:
        os.popen('chrome.exe --remote-debugging-port="{}" --user-data-dir="{}"'.format(port, user_file))
        chrome_option.add_experimental_option('debuggerAddress', '{}:{}'.format(ip,  port))
    return chrome_option
if __name__ == '__main__':
    debug_browser()
