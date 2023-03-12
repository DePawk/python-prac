import time
from winotify import Notification, audio

toast = Notification(app_id="Python Practice",
                     title = "Message Title",
                     msg="Practice Python",
                     duration="short",
                     icon=r"C:\Users\Daniel Zaharan\Desktop\תיקייה חדשה") # enter your location

toast.add_actions(label="Click Me!",launch="https://google.com")
toast.set_audio(audio.Default,loop=False)
toast.show()