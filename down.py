import pytube 
from tkinter import*

vd = Tk()
vd.title("Youtube downloader")
vd.geometry("800x700")
vd.iconbitmap('youtube.ico')
r = IntVar()
url = StringVar()
url.set("")
r.set(2)
btn = Button(vd , text="start" , width= 10 , height= 2  , bg = "#e91e63" , fg = "white" , borderwidth=0, font=("Arial" , 40) , command=lambda: [start(),btn.pack_forget()])
btn.pack(side=TOP, expand=YES)
def start() :
    st = Label(vd,text="Write the URL of video",height=3 ,font=("Arial" , 30))
    st.pack()
    Radiobutton(vd, text="audio only" , height=2 ,font=("Arial" , 14), variable=r ,value = 1 ).pack()
    Radiobutton(vd, text="low quality" ,  height=2 ,font=("Arial" , 14), variable=r , value = 2 ).pack()
    Radiobutton(vd, text="High quality" , height=2 ,font=("Arial" , 14), variable=r , value = 3 ).pack()
    
    url_input = Entry(vd , width= 20 , font = ("Arial" , 20) , textvariable= url)
    url_input.pack()
    down_btn = Button(vd , text="Download" , width= 10 , height= 3  , bg = "green" , fg = "black" , borderwidth=0, font=("Arial" , 20) , command=lambda: down()).pack()
def down() :
    if r.get() == 1:
        pytube.YouTube(url.get()).streams.get_audio_only().download('New folder')
    elif r.get() == 2:
        pytube.YouTube(url.get()).streams.get_lowest_resolution().download('New folder')
    else :
        pytube.YouTube(url.get()).streams.get_highest_resolution().download('New folder')
                
vd.mainloop()  
