from threading import Thread, Event
msg = ""
e = Event()
def person():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()

t = Thread(target=person)
t.start()

print("说对口令是自己人")
e.wait()
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他")

