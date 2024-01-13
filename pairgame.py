from tkinter import *

def filler():

    hide_stuff(howtotext)
    hide_stuff(backhome)
    
    hide_stuff(frame1)
    hide_stuff(frame2)
    hide_stuff(frame3)   
    
        


def howtoplayinst(start,quit,howto):
    hide_stuff(start)
    hide_stuff(quit)
    hide_stuff(howto)
    
    
    show_stuff(howtotext)
    show_stuff(backhome)


def homepage():
    hide_stuff(howtotext)
    hide_stuff(backhome)

    show_stuff(start)
    start.pack(padx=20,pady=20)
    show_stuff(howto)    
    show_stuff(quitgame)
    quitgame.pack(padx=20,pady=20)
    
def startgame():
    hide_stuff(start)
    hide_stuff(howto)
    hide_stuff(quitgame)
    
    show_stuff(frame1)
    show_stuff(frame2)
    show_stuff(frame3) 
           
def hide_stuff(widget):
    widget.pack_forget()

def show_stuff(widget):
    widget.pack()
    



root  = Tk(className="Pair Game")
root.geometry('700x700')
root.configure(bg='green')
root.title("Match The Pair By Pranav Veeraghanta")

# home section

topfiller = Label(root,text="\n\n\n\n\n\n\n\n\n\n\n\n",
                  bg='green')
topfiller.pack()

start = Button(root,text="Start Game",
               font=("Arial",25),
               bg="black",
               padx=40,
               fg='white',
               command=lambda:startgame())
start.pack(padx=24,pady=20)

howto = Button(root,text="How to Play",
               font=("Arial",25),
               bg="black",
               fg='white',
               padx=37,
               command=lambda:howtoplayinst(start,quitgame,howto))
howto.pack(padx=20)


quitgame = Button(root,text="Exit",
                  command=quit,
                  font=("Arial",25),
                   bg="black",
                   padx=95,
                   fg='white')
quitgame.pack(padx=20,pady=20)

# how to play section

howtotext = Label(root,text="\t     HOW TO PLAY\n\n1. Click on any 2 squares to reveal a number.\n\n2.If the numbers match you will get 100 points.\n\n3. If the numbers don't match the squares\n    will be hidden and you can try again.\n\n4. You have infinite number of tries!!!\n\n",
                  font=('Arial',15),
                  bg='green',
                  fg='white',
                  padx=95,
                  justify=LEFT)



backhome = Button(root,text="Back",
                  font=("Arial",25),
               bg="black",
               fg='white',
               padx=90,
               command=lambda:homepage())

# game section:


frame1 = Frame(root)
frame1.pack(side=TOP, padx=5, pady=5)

frame2 = Frame(root)
frame2.pack(side=TOP, padx=5, pady=5)

frame3 = Frame(root)
frame3.pack(side=TOP, padx=5, pady=5)

cell1 = Button(root,text="1",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell2 = Button(root,text="2",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell3 = Button(root,text="3",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell4 = Button(root,text="4",
              font=("Arial",25),
               bg="black",
               fg='white',)


#############################################################

cell5 = Button(root,text="5",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell6 = Button(root,text="6",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell7 = Button(root,text="7",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell8 = Button(root,text="8",
              font=("Arial",25),
               bg="black",
               fg='white',)


########################################################

cell9 = Button(root,text="9",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell10 = Button(root,text="10",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell11 = Button(root,text="11",
              font=("Arial",25),
               bg="black",
               fg='white',)


cell12 = Button(root,text="12",
              font=("Arial",25),
               bg="black",
               fg='white',)

cell1.pack(frame1,side=LEFT)
cell2.pack(frame1,side=LEFT)
cell3.pack(frame1,side=LEFT)
cell4.pack(frame1,side=LEFT)
      
cell5.pack(frame2,side=LEFT)
cell6.pack(frame2,side=LEFT)
cell7.pack(frame2,side=LEFT)
cell8.pack(frame2,side=LEFT)
       
cell9.pack(frame3,side=LEFT)
cell10.pack(frame3,side=LEFT)
cell11.pack(frame3,side=LEFT)
cell12.pack(frame3,side=LEFT)






















filler()


root.mainloop()
