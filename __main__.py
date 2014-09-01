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
        projectFrame.grid(row=0, column=0, sticky="w", padx=default_padx, pady=default_pady, ipadx=default_ipadx, ipady=default_ipady)

        directoryLabel = Label(projectFrame, text="Qual o diretório do projeto?")
        directoryLabel.grid(row=0, column=0, sticky="w")

        directory = Entry(projectFrame)
        directory.grid(row=0, column=1, sticky="e")

        buttonsFrame = LabelFrame(self.master, text="O que fazer?")
        buttonsFrame.grid(row=1, columnspan=7, sticky="ns", ipadx=default_ipadx, ipady=default_ipady)

        sair = Button(buttonsFrame, text="Sair", command=self.quit)
        sair.grid(row=0, column=0, sticky="w")

        hello = Button(buttonsFrame, text="Hello", command=self.helloWorld)
        hello.grid(row=0, column=1, sticky="w")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
root.geometry('600x600+400+200')

kommtr = Config(master=root)
kommtr.master.title("Kommtr - Nunca mais se esqueça de um commit")

kommtr.mainloop()
root.destroy()