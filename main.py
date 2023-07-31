from pytube import YouTube
from moviepy.editor import *
import customtkinter as ctk
import tkinter
from tkinter import filedialog as fd
from tkinter import ttk

class Short():
    def __init__(self, video, ytLink, dwnlDir, startTime, endTime, resolution, cropArea, captions):
        self.video = video
        self.ytLink = ytLink
        self.dwnlDir = dwnlDir
        self.startTime = startTime
        self.endTime = endTime
        self.resolution = resolution
        self.cropArea = cropArea
        self.captions = captions

        if len(self.video) == 0:
            #try:
                ytObject = YouTube(self.ytLink)
                video = ytObject.streams.get_highest_resolution()
                video.download(self.dwnlDir, filename='clip.mp4')

                clip = (VideoFileClip(self.dwnlDir + '\\' + 'clip.mp4').resize((self.resolution[0], self.resolution[1])).subclip(self.startTime, self.endTime).crop(self.cropArea[0], self.cropArea[1], self.cropArea[2], self.cropArea[3]))
                if len(self.captions) != 0:
                    captionsClip = concatenate(self.captions, method='compose')
                    composition = CompositeVideoClip([clip, captionsClip.set_pos('center')]) 
                    composition.write_videofile(self.dwnlDir + '\\' + 'clipCut.mp4')
                else:
                    clip.write_videofile(self.dwnlDir + '\\' + 'clipCut.mp4')
                clip.reader.close()
                clip.audio.reader.close_proc()
            #except:
                #print('SOMETHING WENT WRONG!')
        else:
           #try:
                clip = (VideoFileClip(self.video).resize((self.resolution[0], self.resolution[1])).subclip(self.startTime, self.endTime).crop(self.cropArea[0], self.cropArea[1], self.cropArea[2], self.cropArea[3]))
                if len(self.captions) != 0:
                    captionsClip = concatenate(self.captions, method='compose')
                    composition = CompositeVideoClip([clip, captionsClip.set_pos('center')]) 
                    composition.write_videofile(self.dwnlDir + '\\' + 'clipCut.mp4')
                else:
                    clip.write_videofile(self.dwnlDir + '\\' + 'clipCut.mp4')
                clip.reader.close()
                clip.audio.reader.close_proc()
          #except:
               # print('SOMETHING WENT WRONG!')
    
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #setup
        self.geometry('1024x600')
        self.title('Shorts Creator')
        self.resizable(False, False)
        self.captions = []
        self.video = ''
        self.dwnlDir = ''

        #title
        self.title = ctk.CTkLabel(self, text='Shorts Creator', font=('Arial', 32, 'bold'))
        self.title.place(x=410, y=25)

        #clipTitle
        self.clipTitle = ctk.CTkLabel(self, text='Clip Settings', font=('Arial', 24, 'bold'))
        self.clipTitle.place(x=170, y=110)

        #captionsTitle
        self.captionsTitle = ctk.CTkLabel(self, text='Captions', font=('Arial', 24, 'bold'))
        self.captionsTitle.place(x=745, y=110)

        #chooseVideo
        self.chsVidLbl = ctk.CTkLabel(self, text='CHOOSE VIDEO: ', font=('Arial', 14,))
        self.chsVidLbl.place(x=20, y=195)

        link = tkinter.StringVar()
        self.linkEntry = ctk.CTkEntry(self, width=170, height=15, textvariable=link)
        self.linkEntry.insert(0, 'Insert YT link...')
        self.linkEntry.place(x=150, y=197)

        self.orLbl = ctk.CTkLabel(self, text='OR', font=('Arial', 14))
        self.orLbl.place(x=345, y=195)

        def getVideo():
            self.video = fd.askopenfilename()
        self.chsVidBtn = ctk.CTkButton(self, text='Choose video', width=40, command=getVideo)
        self.chsVidBtn.place(x=390, y=194)

        #resizeVideo
        self.chgResLbl = ctk.CTkLabel(self, text='CHANGE RES.: ', font=('Arial', 14,))
        self.chgResLbl.place(x=20, y=275)

        width = tkinter.StringVar()
        self.widthResEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=width)
        self.widthResEntry.place(x=150, y=277)

        height = tkinter.StringVar()
        self.heightResEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=height)
        self.heightResEntry.place(x=260, y=277)

        #cropVideo
        self.cropLbl = ctk.CTkLabel(self, text='CROP AREA: ', font=('Arial', 14,))
        self.cropLbl.place(x=20, y=355)

        xTop = tkinter.StringVar()
        self.xtopEntry = ctk.CTkEntry(self, width=50, height=15, textvariable=xTop)
        self.xtopEntry.insert(0, 'Top Left X')
        self.xtopEntry.place(x=150, y=357)

        yTop = tkinter.StringVar()
        self.ytopEntry = ctk.CTkEntry(self, width=50, height=15, textvariable=yTop)
        self.ytopEntry.insert(0, 'Top Left Y')
        self.ytopEntry.place(x=220, y=357)

        xBottom = tkinter.StringVar()
        self.xbotEntry = ctk.CTkEntry(self, width=50, height=15, textvariable=xBottom)
        self.xbotEntry.insert(0, 'Bott. Right X')
        self.xbotEntry.place(x=290, y=357)

        yBottom = tkinter.StringVar()
        self.ybotEntry = ctk.CTkEntry(self, width=50, height=15, textvariable=yBottom)
        self.ybotEntry.insert(0, 'Bott. Right Y')
        self.ybotEntry.place(x=360, y=357)

        #videoDuration
        self.cutVidLbl = ctk.CTkLabel(self, text='CUT VIDEO: ', font=('Arial', 14,))
        self.cutVidLbl.place(x=20, y=435)

        cutStart = tkinter.StringVar()
        self.startEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=cutStart)
        self.startEntry.place(x=150, y=437)

        cutEnd = tkinter.StringVar()
        self.endEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=cutEnd)
        self.endEntry.place(x=260, y=437)

        #captionAdd
        capText = tkinter.StringVar()
        self.capTextEntry = ctk.CTkEntry(self, width=190, height=15, textvariable=capText)
        self.capTextEntry.insert(0, 'Caption Text...')
        self.capTextEntry.place(x=565, y=197)

        capStartTime = tkinter.StringVar()
        self.startTimeEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=capStartTime)
        self.startTimeEntry.insert(0, 'Start time')
        self.startTimeEntry.place(x=770, y=197)

        capEndTime = tkinter.StringVar()
        self.durationEntry = ctk.CTkEntry(self, width=80, height=15, textvariable=capEndTime)
        self.durationEntry.insert(0, 'Duration')
        self.durationEntry.place(x=865, y=197)


        def capAdd():
            self.capView.insert('', 'end', values=(self.capTextEntry.get(), self.startTimeEntry.get(), self.durationEntry.get()))
            caption = TextClip(txt=self.capTextEntry.get(), color='white', stroke_color='black', stroke_width=1, fontsize=48)
            caption = caption.set_start(self.startTimeEntry.get())
            caption = caption.set_duration(self.durationEntry.get()).set_pos('center')
            self.captions.append(caption)
        self.addButton = ctk.CTkButton(self, text='Add',width=30, command=capAdd)
        self.addButton.place(x=960, y=194)

        columns = ('Text', 'Start Time', 'Duration')
        self.capView = ttk.Treeview(self, columns=columns, show='headings')
        self.capView.place(x=650, y=237, width=280)

        #downloadChangeButtons
        def getDwnlDir():
            self.dwnlDir = fd.askdirectory()
        self.changeDwnlDirBtn = ctk.CTkButton(self, text='Change Download Place', width=60, command=getDwnlDir)
        self.changeDwnlDirBtn.place(x=385, y=540)

        def makeShort():
            short = Short(self.video, self.linkEntry.get(), self.dwnlDir, self.startEntry.get(), self.endEntry.get(), (self.widthResEntry.get(), self.heightResEntry.get()), (self.xtopEntry.get(), self.ytopEntry.get(), self.xbotEntry.get(), self.ybotEntry.get()), self.captions)
        self.makeShortBtn = ctk.CTkButton(self, text='Create Short', width=60, command=makeShort)
        self.makeShortBtn.place(x=565, y=540)
  
if __name__ == "__main__":
    app = App()
    app.mainloop()
    #main()