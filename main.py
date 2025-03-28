import pynput
import time
import chardet


keyboaed_controller = pynput.keyboard.Controller()
with open("./answer.txt", "rb") as fb:
    data = fb.read()
    encoding = chardet.detect(data)["encoding"]
with open("./answer.txt", "r", encoding=encoding) as f:
    s = f.read()
print("请把鼠标移到你要输入的文本框当中，五秒后开始输入")
time.sleep(5)
keyboaed_controller.type(s)
print("输入完成")
input()
