import random
from tkinter import *
from tkinter import messagebox

skors = 0

class MyApp:
    def __init__(self, master):
        global en_user
        global en_hasil

        self.master = master
        self.master.title("Suit")
        self.master.configure(background='skyblue')
        self.master.resizable(0,0)
        
        Label(master, text="", bg='skyblue').grid(row=0, column=0)
        self.label = Label(master, text="SELAMAT DATANG", bg='skyblue')
        self.label.grid(row=0, columnspan=3)
        self.label.config(font=("Comic Sans MS", 15, 'bold'))

        Label(master, text="", bg='skyblue').grid(row=1, column=0)
        self.rules = Label(master, text="Silahkan memilih pilihan Anda: Batu, Gunting, atau Kertas", bg='skyblue')
        self.rules.grid(row=2, columnspan=3)
        self.rules.config(font=("Comic Sans MS", 10))

        self.pil = Label(master, text="Pilihan Anda", bg='skyblue')
        self.pil.grid(row=3, column=1)
        self.pil.config(font=("Comic Sans MS", 10))
        self.en_user = Entry(master, width=30, exportselection=True, justify=CENTER)
        self.en_user.grid(row=3, column=2, pady=5)
        self.en_user.config(font=("Comic Sans MS", 10))

        self.btn_play = Button(master, text="Main", command=lambda:self.play(self.en_user.get()))
        self.btn_play.grid(row=4, columnspan=3, pady=10)
        self.btn_play.config(font=("Comic Sans MS", 10))

        Label(master, text="", bg='skyblue').grid(row=5, column=0)

        self.hasil = Label(master, text="Hasil", bg='skyblue')
        self.hasil.grid(row=6, column=1)
        self.hasil.config(font=("Comic Sans MS", 10))
        self.en_hasil = Entry(master, width=45, justify=CENTER)
        self.en_hasil.grid(row=6, column=2)
        self.en_hasil.config(font=("Comic Sans MS", 10))

        Label(master, text="", bg='skyblue').grid(row=7, column=0)

        # self.btn_reset = Button(master, text="Reset").grid(row=8, column=0)
        self.btn_quit = Button(master, text="Keluar", command=self.master.destroy)
        self.btn_quit.grid(row=8, columnspan=3)
        self.btn_quit.config(font=("Comic Sans MS", 10))

        self.skor = Label(root, text="Skor: {}".format(skors), bg='skyblue')
        self.skor.grid(row=9, columnspan=3, pady=5)
        self.skor.config(font=("Comic Sans MS", 10))    
    # def Reset(self, skor):
    #     global skors
    #     self.skor = skor
    #     skor = Label(root, text="Skor: {}".format(self.skor)).grid(row=9, columnspan=3, pady=5)
    def Skor(self, nilai):
        global skors
        self.nilai = nilai
        if self.nilai == 1:
            skors += 10
            # return skors
        elif self.nilai == 0:
            skors -= 10
            # return skors
        skor = Label(root, text="Skor: {}".format(skors), bg='skyblue')
        skor.grid(row=9, columnspan=3, pady=5)
        skor.config(font=("Comic Sans MS", 10))    

    def Hasil(self, player, com):
        self.player = player
        self.com = com
        if self.player == 1:
            if self.com == 1:
                self.en_hasil.insert(0, "Seri, Komputer Memilih Gunting")  
            elif self.com == 2:
                self.en_hasil.insert(0, "Kalah, Komputer Memilih Batu")
                self.Skor(0)    
            elif self.com == 3:
                self.en_hasil.insert(0, "Menang, Komputer Memilih Kertas")
                self.Skor(1)

        elif self.player == 2:
            if self.com == 1:
                self.en_hasil.insert(0, "Menang, Komputer Memilih Gunting")  
                self.Skor(1)
            elif self.com == 2:
                self.en_hasil.insert(0, "Seri, Komputer Memilih Batu")    
            elif self.com == 3:
                self.en_hasil.insert(0, "Kalah, Komputer Memilih Kertas")
                self.Skor(0)

        elif self.player == 3:
            if self.com == 1:
                self.en_hasil.insert(0, "Kalah, Komputer Memilih Gunting")  
                self.Skor(0)
            elif self.com == 2:
                self.en_hasil.insert(0, "Menang, Komputer Memilih Batu")    
                self.Skor(1)
            elif self.com == 3:
                self.en_hasil.insert(0, "Seri, Komputer Memilih Kertas")
    
    def play(self, player):
        self.en_hasil.delete(0, END)
        com = random.randint(1,3)        
        self.player = str(player).lower()
        if self.player == 'gunting':
            self.player = 1
        elif self.player == 'batu':
            self.player = 2
        elif self.player == 'kertas':
            self.player = 3
        elif self.player == '':
            # messagebox.showwarning('Peringatan', "Pilihan Tidak Boleh Kosong!")
            self.en_hasil.insert(0, "Pilihan Tidak Boleh Kosong")
        else:
            # messagebox.showwarning("Peringatan", "Pilihan Tidak Diketahui!")
            text = "Pilihan Tidak Diketahui"
            self.en_hasil.insert(0, text)
            self.en_user.delete(0,END)
        self.Hasil(self.player, com)

if __name__ == "__main__":
    root = Tk()
    gui = MyApp(root)
    root.mainloop()