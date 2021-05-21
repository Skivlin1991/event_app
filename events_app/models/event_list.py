import events_app
from app.modules.event import *
import datetime 

event_1 = Events(datetime.date)(2021, 5, 31), "Cult BBQ", 21, 6, "sacrificial offering to our one true saviour", True
event_2 = Event(datetime.date)(2021, 6, 12), "Free drinks festival", 350, 15, "The day I take you all out for drinks on me!",True
event_3 = Event(datetime.date)(2021, 5, 27), "star wars club", 500, 12, "R2D2 is the evil one not vader!!!!",False
event_4 = Event(datetime.date)(2021, 5, 23), "smiths wedding", 50, 14, "he was married to her sister oh my !!",False 

events_list = [event_1, event_2, event_3, event_4]

def create_new_event(event):
    events_list.append(event)