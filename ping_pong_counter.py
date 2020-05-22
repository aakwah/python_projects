import slowclap as sc
from tkinter import *
feed = sc.MicrophoneFeed()
detector = sc.AmplitudeDetector(feed, threshold=270000)
i=0


#def tk(text):
#    yourData = text
#    frame = Frame(root, width=500, height=500)
#    lab = Label(frame,text=yourData)
#    lab['text'] = yourData
#    root.mainloop()


for clap in detector:
    # do something
    i=i+1
    print(i,end='\r')


