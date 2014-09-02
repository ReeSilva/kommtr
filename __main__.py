from Tkinter import *

default_padx = 5
default_pady = 15

default_ipadx = 15
default_ipady = 30

class Config(Frame):
    def helloWorld(self):
        print "Hello, world!"

    def createWidgets(self):
        projectFrame = LabelFrame(self.master, text="Defina os detalhes do projeto")
        # projectFrame.grid_columnconfigure(projectFrame, minsize=100)
        projectFrame.grid(row=0, column=0, sticky="we", ipadx=default_ipadx, ipady=default_ipady)

        directoryLabel = Label(projectFrame, text="Qual o diretório do projeto?")
        directoryLabel.grid(row=0, column=0, sticky="w")

        directory = Entry(projectFrame)
        directory.grid(row=0, column=1, sticky="e")

        sair = Button(root, text="Sair", command=self.quit)
        sair.grid(row=1, column=0, sticky="w")

        hello = Button(root, text="Hello", command=self.helloWorld)
        hello.grid(row=1, column=1, sticky="w")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
root.geometry('600x600+400+200')

kommtr = Config(master=root)
kommtr.master.title("Kommtr - Nunca mais se esqueça de um commit")

kommtr.mainloop()
root.destroy()