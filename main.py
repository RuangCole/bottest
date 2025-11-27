import tkinter as tk
from tkinter import messagebox
import time
now = time.localtime()
weekday = now.tm_wday + 1
weekday_name = ["", "周一", "周二", "周三", "周四", "周五", "周六", "周日"]
if weekday == 1:
    content = f"今天是{weekday_name[weekday]}\n麦当劳会员日\n一起去吃麦当劳吧"
elif weekday == 2:
    content = f"今天是{weekday_name[weekday]}\n塔斯汀会员日\n美味的汉堡和披萨"
elif weekday == 3:
    content = f"今天是{weekday_name[weekday]}\n必胜客尖叫星期三\nCome on必胜客！"
elif weekday == 4:
    content = f"今天是{weekday_name[weekday]}\nKFC疯狂星期四\n罚你请我吃KFC疯狂星期四！"
elif weekday == 5:
    content = f"今天是{weekday_name[weekday]}\n华莱士买一送一\n赶紧去买吧\n然后送我一份"
elif weekday == 6:
    content = f"今天是{weekday_name[weekday]}\n又是躺在床上度过的一天\n不行，我要起床玩MC"
elif weekday == 7:
    content = f"今天是{weekday_name[weekday]}\n哎，明天又有早八了\n布豪！我的作业还没写！"
else:
    content = "获取星期失败！"
root = tk.Tk()
root.withdraw()
root.tk.call('wm', 'attributes', '.', '-topmost', True)
messagebox.showinfo(
    title="What To Eat Today?",
    message=content
)
root.destroy()
