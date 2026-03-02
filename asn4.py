import tkinter
from PIL import Image, ImageTk

class FoodGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Food Viewer")
        self.root.minsize(400,300)
        
        self.img_frame = tkinter.Frame(self.root)
        self.rbdBtn_frame = tkinter.Frame(self.root)
        
        self.img1=Image.open("chicken.jpg")
        self.img1=self.img1.resize((400,300))
        self.imgOne = ImageTk.PhotoImage(self.img1)
        self.img2=Image.open("pie.jpg")
        self.img2=self.img2.resize((400,300))
        self.imgTwo = ImageTk.PhotoImage(self.img2)
        self.img3=Image.open("pizza.jpg")
        self.img3=self.img3.resize((350,300))
        self.imgThree = ImageTk.PhotoImage(self.img3)
        self.img4=Image.open("steak.jpg")
        self.img4=self.img4.resize((300,300))
        self.imgFour = ImageTk.PhotoImage(self.img4)
        
        self.lbl = tkinter.Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()
        
        self.var = tkinter.IntVar()
        
        for text, value in [("Chicken", 1),("Pie", 2),("Pizza", 3),("Steak", 4)]:
            tkinter.Radiobutton(self.rbdBtn_frame, text=text, value=value, variable=self.var, command=self.on_radio_select).pack(side = 'left', padx=10)
        
        self.img_frame.pack()
        self.rbdBtn_frame.pack()
        
        tkinter.mainloop()
    
    def on_radio_select(self):
        choice = self.var.get()
        if choice == 1:
            self.lbl.config(image=self.imgOne)
        if choice == 2:
            self.lbl.config(image = self.imgTwo)
        if choice == 3:
            self.lbl.config(image = self.imgThree)
        if choice == 4:
            self.lbl.config(image = self.imgFour)

if __name__ == '__main__':
    food = FoodGUI()