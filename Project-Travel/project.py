import tkinter as tk
import random
from abc import ABC, abstractmethod

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

        self.tour_guides = [
            tourguide_history('Mark', 'Medieval History'),
            tourguide_photograph('Ericsson', 'Wildlife and Photography'),
            tourguide_med('Zeynep', 'Mediterranean Landscape')
        ]

        label = tk.Label(self.frame1, text='AFS Tourism', bg='#3F3F3F', fg='#FFFFFF', font=('Arial', 32))
        label.pack(pady=25)

        toursbtn = tk.Button(self.frame1, text='Tours', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.show_frame2)
        toursbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)

        cartbtn = tk.Button(self.frame1, text='Your cart', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=lambda:[self.show_frame3(), self.warning()])
        cartbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)

        goback1 = tk.Button(self.frame2, text='Go Back', font=('Arial', 16), bg="#303030", fg='#FFFFFF', command=self.show_frame1)
        goback1.pack(anchor='nw')

        label_tours_guides = tk.Label(self.frame2, text=r'Tours     \\     Guides', font=('Arial', 25), bg='#3F3F3F', fg='#FFFFFF', width=100)
        label_tours_guides.pack()

        goback2 = tk.Button(self.frame3, text='Go Back', font=('Arial', 16), bg='#303030', fg='#FFFFFF', command=self.show_frame1)
        goback2.pack(anchor='nw')

        infolabel = tk.Label(self.frame3, text='Finish payment', font=('Arial', 24), bg='#3F3F3F', fg='#FFFFFF', width=100)
        infolabel.pack()

        infotext = tk.Text(self.frame3, height=3, width=45, bg='#3F3F3F', fg='#83D189', font=('Arial', 16))
        infotext.insert('1.0', 'GREAT OPPORTUNITY!! ALL TOURS ARE 150 EUROS!!\nIf you use credit card, some of the money will\ngo to charity.')
        infotext.config(state='disabled')
        infotext.pack(pady=25)

        ccbtn = tk.Button(self.frame3, text='Credit Card', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedCC)
        ccbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)

        cbtn = tk.Button(self.frame3, text='Cash', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedC)
        cbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)

        btcbtn = tk.Button(self.frame3, text='Bitcoin', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedBTC)
        btcbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)

        xmrbtn = tk.Button(self.frame3, text='Monero', font=('Arial', 24), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedXMR)
        xmrbtn.pack(side='left', fill='both', expand=True, padx=75, pady=175)



        text_ant = tk.Text(self.frame2, height=1, width=16, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_ant.insert('1.0', 'Türkiye Antalya Tour')
        text_ant.config(state='disabled')
        text_ant.pack(padx=50, anchor='nw')

        # I don't think entry has a feature where you can change it's bg color. From my experience, only the fg color would change.

        btn_ant = tk.Button(self.frame2, text='Select', font=('Arial', 14), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedTurkiye)
        btn_ant.pack(padx=90, anchor='nw')

        text_guide_a = tk.Text(self.frame2, height=2, width=24, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_guide_a.insert('1.0', 'Mark\n - 10 years of experience')
        text_guide_a.config(state='disabled')
        text_guide_a.pack(padx=50, anchor='ne')

        btn_guide_a = tk.Button(self.frame2, text='Choose guide', font=('Arial', 16), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedMark)
        btn_guide_a.pack(padx=125, anchor='ne')

        text_southdakota = tk.Text(self.frame2, height=1, width=18, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_southdakota.insert('1.0', 'US South Dakota Tour')
        text_southdakota.config(state='disabled')
        text_southdakota.pack(padx=50, anchor='nw')

        btn_sd = tk.Button(self.frame2, text='Select', font=('Arial', 14), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedUS)
        btn_sd.pack(padx=90, anchor='nw')

        text_guide_b = tk.Text(self.frame2, height=2, width=24, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_guide_b.insert('1.0', 'Ericsson\n - 16 years of experience')
        text_guide_b.config(state='disabled')
        text_guide_b.pack(padx=50, anchor='ne')

        btn_guide_b = tk.Button(self.frame2, text='Choose guide', font=('Arial', 16), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedEricsson)
        btn_guide_b.pack(padx=125, anchor='ne')

        text_helsinki = tk.Text(self.frame2, height=1, width=18, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_helsinki.insert('1.0', 'Finland Helsinki Tour')
        text_helsinki.config(state='disabled')
        text_helsinki.pack(padx=50, anchor='nw')

        btn_hels = tk.Button(self.frame2, text='Select', font=('Arial', 14), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedFinland)
        btn_hels.pack(padx=90, anchor='nw')

        text_guide_c = tk.Text(self.frame2, height=2, width=24, font=('Arial', 16), bg='#3F3F3F', fg='#FFFFFF')
        text_guide_c.insert('1.0', 'Zeynep\n - 14 years of experience')
        text_guide_c.config(state='disabled')
        text_guide_c.pack(padx=50, anchor='ne')

        btn_guide_b = tk.Button(self.frame2, text='Choose guide', font=('Arial', 16), bg='#F74AA0', fg='#FFFFFF', command=self.update_isPickedZeynep)
        btn_guide_b.pack(padx=125, anchor='ne')

        note_label = tk.Label(self.frame2, text='The information and plan will be given to you by our tour guides.\nThe price of the tour guides are included in the total price of the tour.', bg='#3F3F3F', fg='#FFFFFF', font=('Arial', 16))
        note_label.pack(pady=20)

        recommend_btn = tk.Button(self.frame2, text='Recommend a tour guide', font=('Arial', 18), bg='#F74AA0', fg='#FFFFFF', command=self.show_recommendation)
        recommend_btn.pack()

        goback3 = tk.Button(self.frame9, text='Go Back', font=('Arial', 16), bg='#303030', fg='#FFFFFF', command=self.show_frame1)
        goback3.pack(anchor='n')

        self.result_label = tk.Label(self.frame2, text='', bg='#3F3F3F', fg='#FFFFFF', font=('Arial', 20))
        self.result_label.pack()


        root.mainloop()

    def warning(self):
        if not (isPickedTurkiye or isPickedUS or isPickedFinland):
            warn_label = tk.Label(self.frame9, text='Come back after you picked your tour', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF')
            warn_label.pack(anchor='s')
            self.show_frame9()

    def show_recommendation(self):
        global isPickedTurkiye
        global isPickedUS
        global isPickedFinland
        if isPickedTurkiye:
            tour_type = 'Mediterranean Landscape'
        elif isPickedUS:
            tour_type = 'Wildlife and Photography'
        elif isPickedFinland:
            tour_type = 'Medieval History'
        else:
            self.result_label.config(text='Pick a tour guide before getting recommendations.')
            return
        
        recommendations = get_recommendations(self.tour_guides, tour_type)
        if recommendations:
            guide_names = ', '.join(str(g) for g in recommendations)
            self.result_label.config(text=f'Recommended guide(s): {guide_names} ({tour_type})')

    def charity_tax(self):
        return round(50 ** random.uniform(0.8, 0.9))


    def payment_screen(self):
        if isPickedCC:
            cc_screen = tk.Label(self.frame5, text=f'You paid {self.charity_tax()} dollars to charity and 150 in total using credit card.\nYou can now exit this app.', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF', height=2, width=60)
            cc_screen.pack()
        elif isPickedC:
            c_screen = tk.Label(self.frame5, text='You paid 150 dollars in total using cash.\nYou can now exit this app.', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF', height=2, width=60)
            c_screen.pack()
        elif isPickedBTC:
            btc_screen = tk.Label(self.frame5, text='You paid 150 dollars in total using bitcoin.\nYou can now exit this app.', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF', height=2, width=60)
            btc_screen.pack()
        elif isPickedXMR:
            xmr_screen = tk.Label(self.frame5, text='You paid 150 dollars in total using monero.\nYou can now exit this app.', font=('Arial', 20), bg='#3F3F3F', fg='#FFFFFF', height=2, width=60)
            xmr_screen.pack()

                    

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

    def update_isPickedCC(self):
        global isPickedCC
        global isPickedC
        global isPickedBTC
        global isPickedXMR
        isPickedCC = True
        isPickedC = False
        isPickedBTC = False
        isPickedXMR = False
        self.show_frame5()
        self.payment_screen()

    def update_isPickedC(self):
        global isPickedC
        global isPickedCC
        global isPickedBTC
        global isPickedXMR
        isPickedC = True
        isPickedCC = False
        isPickedBTC = False
        isPickedXMR = False
        self.show_frame5()
        self.payment_screen()

    def update_isPickedBTC(self):
        global isPickedBTC
        global isPickedCC
        global isPickedC
        global isPickedXMR
        isPickedBTC = True
        isPickedC = False
        isPickedCC = False
        isPickedXMR = False
        self.show_frame5()
        self.payment_screen()

    def update_isPickedXMR(self):
        global isPickedXMR
        global isPickedC
        global isPickedBTC
        global isPickedCC
        isPickedXMR = True
        isPickedC = False
        isPickedBTC = False
        isPickedCC = False
        self.show_frame5()
        self.payment_screen()

# a, b and c inherits from tourguide. the groundwork for polymorphism starts from here.
class tourguide:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def match_tour(self, tour_type):
        pass

    def __str__(self):
        return f'{self.name}'

class tourguide_history(tourguide):
    def __init__(self, name, expertise):
        super().__init__(name)
        self.expertise = expertise

    def match_tour(self, tour_type):
        return tour_type.lower() in self.expertise.lower()

class tourguide_photograph(tourguide):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

    def match_tour(self, tour_type):
        return tour_type.lower() in self.specialty.lower()

class tourguide_med(tourguide):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession

    def match_tour(self, tour_type):
        return tour_type.lower() in self.profession.lower()
    
def get_recommendations(tour_guides, tour_type):
    return [guide for guide in tour_guides if guide.match_tour(tour_type)]

# in my opinion, expertise and specialty are different things.
# specialty is more like less people would have
# expertise is in the middle
# and profession is the last one

tour_guides = [
    tourguide_history('Mark', 'Medieval History'),
    tourguide_photograph('Ericsson', 'Wildlife and Photography'),
    tourguide_med('Zeynep', 'Mediterranean Landscape')
]

tourGUI()
