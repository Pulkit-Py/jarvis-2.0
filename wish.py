import datetime
from speek import sp
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        sp("    Good Moring")
    elif hour>=12 and hour<18:
        sp("    Good Afternoon")
    else:
        sp("    Good Evening")
    sp("Hello sir, I Am jarvis How may i help you")