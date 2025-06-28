import tkinter as tk

isPickedMark = False
isPickedEricsson = False
isPickedZeynep = False

isPickedTurkiye = False
isPickedUS = False
isPickedFinland = False

isPickedCC = False
isPickedC = False
isPickedBTC = False
isPickedXMR = False

# not glad I had to use global variables. A bunch of them in fact.

class tourGUI:

    def __init__(self):

        
        
        root = tk.Tk()
        root.title('AFS Tourism Application')
        root.geometry('1200x785')
        root.configure(bg="#3F3F3F")

        self.frame1 = tk.Frame(root)
        self.frame1.configure(bg='#3F3F3F')
        self.frame1.pack()

        self.frame2 = tk.Frame(root)
        self.frame2.configure(bg='#3F3F3F')
        self.frame2.pack_forget()

        self.frame3 = tk.Frame(root)
        self.frame3.configure(bg='#3F3F3F')
        self.frame3.pack_forget()

        self.frame4 = tk.Frame(root)
        self.frame4.configure(bg='#3F3F3F')
        self.frame4.pack_forget()

        self.frame5 = tk.Frame(root)
        self.frame5.configure(bg='#3F3F3F')
        self.frame5.pack_forget()

        self.frame6 = tk.Frame(root)
        self.frame6.configure(bg='#3F3F3F')
        self.frame6.pack_forget()

        self.frame7 = tk.Frame(root)
        self.frame7.configure(bg='#3F3F3F')
        self.frame7.pack_forget()

        self.frame8 = tk.Frame(root)
        self.frame8.configure(bg='#3F3F3F')
        self.frame8.pack_forget()

        self.frame9 = tk.Frame(root)
        self.frame9.configure(bg='#3F3F3F')
        self.frame9.pack_forget()

        label = tk.Label(self.frame1, text='AFS Tourism', bg='#3F3F3F', fg='#FFFFFF', font=('Arial', 32))
        label.pack(pady=25)

        toursbtn = tk.Button(self.frame1, text='Tours', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.show_frame2)
        toursbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)


        root.mainloop()

    def warning(self):
        if not (isPickedTurkiye or isPickedUS or isPickedFinland):
            warn_label = tk.Label(self.frame9, text='Come back after you picked your tour', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF')
            warn_label.pack(anchor='s')
            self.show_frame9()
    
     # accesses polymorphism with "for guide in tour_guides"
    def get_recommendation(self):
        if isPickedTurkiye:
            for guide in tour_guides:
                if guide.language == 'Turkish':
                    rcm_label_z = tk.Label(self.frame6, text=f'Recommended tour guide(s): {guide.name}', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF')
                    rcm_label_z.pack(anchor='s')
                    self.show_frame6()
                    self.frame7.pack_forget()
                    self.frame8.pack_forget()
                attribute_name = 'expertise'
                if hasattr(guide, attribute_name) and getattr(guide, attribute_name) == 'Medieval History':
                    rcm_label_y = tk.Label(self.frame6, text=f'Might also be according to your liking: {guide.name}', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF')
                    rcm_label_y.pack(anchor='s')
        if isPickedUS:
            for guide in tour_guides:
                attribute_name2 = 'specialty'
                if guide.language == 'English':
                    rcm_label_z = tk.Label(self.frame7, text=f'Recommended tour guide(s): {guide.name}', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF')
                    rcm_label_z.pack(anchor='s')
                    self.show_frame7()
                    self.frame6.pack_forget()
                    self.frame8.pack_forget()
                if hasattr(guide, attribute_name2) and getattr(guide, attribute_name2) == 'Wildlife and Photography':
                    rcm_label_y = tk.Label(self.frame7, text=f'Might also be according to your liking: {guide.name}', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF')
                    rcm_label_y.pack(anchor='s')
        if isPickedFinland:
            for guide in tour_guides:
                if guide.language == 'Finnish':
                    rcm_label_z = tk.Label(self.frame8, text=f'Recommended tour guide(s): {guide.name}\n-', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF')
                    rcm_label_z.pack(anchor='s')
                    self.show_frame8()
                    self.frame6.pack_forget()
                    self.frame7.pack_forget()
    # accesses polymorphism with "for guide in tour_guides"


    
    def show_frame1(self):
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame1.pack()

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame2.pack()

    def show_frame3(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame3.pack()

    def show_frame4(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame4.pack()

    # payment frame is frame5
    def show_frame5(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame5.pack()

    def show_frame6(self):
        self.frame6.pack()

    def show_frame7(self):
        self.frame7.pack()

    def show_frame8(self):
        self.frame8.pack()

    def show_frame9(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack()

    # im sorry for the amount of repeating code in this. GUI makes things really hard.

    def update_isPickedMark(self):
        global isPickedMark
        global isPickedEricsson
        global isPickedZeynep
        isPickedMark = True
        isPickedZeynep = False
        isPickedEricsson = False

    def update_isPickedEricsson(self):
        global isPickedEricsson
        global isPickedZeynep
        global isPickedMark
        isPickedEricsson = True
        isPickedZeynep = False
        isPickedMark = False

    def update_isPickedZeynep(self):
        global isPickedZeynep
        global isPickedMark
        global isPickedEricsson
        isPickedZeynep = True
        isPickedMark = False
        isPickedEricsson = False

    def update_isPickedTurkiye(self):
        global isPickedTurkiye
        global isPickedUS
        global isPickedFinland
        isPickedTurkiye = True
        isPickedFinland = False
        isPickedUS = False

    def update_isPickedUS(self):
        global isPickedUS
        global isPickedTurkiye
        global isPickedFinland
        isPickedUS = True
        isPickedFinland = False
        isPickedTurkiye = False

    def update_isPickedFinland(self):
        global isPickedFinland
        global isPickedTurkiye
        global isPickedUS
        isPickedFinland = True
        isPickedTurkiye = False
        isPickedUS = False

# a, b and c inherits from tourguide. the groundwork for polymorphism starts from here.
class tourguide:
    def __init__(self, name, language):
        self.name = name
        self.language = language

class tourguide_a(tourguide):
    def __init__(self, name, language, expertise):
        super().__init__(name, language)
        self.expertise = expertise


class tourguide_b(tourguide):
    def __init__(self, name, language, specialty):
        super().__init__(name, language)
        self.specialty = specialty

class tourguide_c(tourguide):
    def __init__(self, name, language, profession):
        super().__init__(name, language)
        self.profession = profession

# in my opinion, expertise and specialty are different things.
# specialty is more like less people would have
# expertise is in the middle
# and profession is the last one

tour_guides = [
    tourguide_a('Mark', 'English', 'Medieval History'),
    tourguide_b('Ericsson', 'Finnish', 'Wildlife and Photography'),
    tourguide_c('Zeynep', 'Turkish', 'None')
]

#the get_recommendation function uses this.


    
   


tourGUI()
