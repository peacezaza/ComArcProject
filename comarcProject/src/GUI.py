import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os
from main import HDD , RAID

RESIZE = 8

RAID_LIST = []

R1 = RAID('RAID1',5)


RAID_LIST.append(R1)


H1 = HDD('HDD1',2)
H2 = HDD('HDD2',2)
H3 = HDD('HDD3',2)
H4 = HDD('HDD4',1)
R1.addHDD(H1)
R1.addHDD(H2)
R1.addHDD(H3)
R1.addHDD(H4)
for i in R1.getRAIDLS():
    print(f'NAME HDD : {i.getName()} CAPACITY : {i.getCapacity()}TB ')

if isinstance(R1.getSUMcapacity(), int):
    print(f'{R1.getSUMcapacity()}TB')
else:
    print(f'{R1.getSUMcapacity()}')



def on_raid_listbox_click(event):
    selected_index = RAID_Listbox.curselection()
    print(selected_index)
    if selected_index:

        for widget in LEFT_LOWER.winfo_children():
            widget.destroy()

        HHD_Listbox = tk.Listbox(LEFT_LOWER, width=50)
        HHD_Listbox.grid(rowspan=1, columnspan=2, sticky='nsew' , padx=0)

        # Clear existing elements in the HHD_Listbox
        HHD_Listbox.delete(0, tk.END)

        index = 1
        print(selected_index[0])
        print(RAID_LIST[selected_index[0]].getRAIDLS())
        capacity = RAID_LIST[selected_index[0]].getSUMcapacity()

        if len(RAID_LIST[selected_index[0]].getRAIDLS()) != 0:
            for hdd in RAID_LIST[selected_index[0]].getRAIDLS():
                HHD_Listbox.insert(index, f'NAME HDD : {hdd.getName()} CAPACITY : {hdd.getCapacity()}TB ')
                index += 1
        else:
            HHD_Listbox.insert(1,"You need add HDD in RAID before Simulator ! ")

        progress_bar = ttk.Progressbar(RIGTH_FARME, orient='horizontal', length=660, mode='determinate', variable=100)
        progress_bar['value'] = 100
        progress_bar.grid(row=0, column=0, padx=20, pady=30)
        label_status = tk.Label(RIGTH_FARME, text=f'{capacity}TB')
        # if isinstance(capacity, int):
        #     label_status = tk.Label(RIGTH_FARME,text=f'{capacity}TB')
        # else:
        #     label_status = tk.Label(RIGTH_FARME,text=f'{capacity}')



window = tk.Tk()
window.maxsize(1024,800)
window.config(bg='gray')
window.title('RAID SIMULATION')
path = os.getcwd()

photo_addDriver = tk.PhotoImage(file = f'{path}\comArcProject\\image\\addDriver.png')
photo_addRAID = tk.PhotoImage(file = f'{path}\comArcProject\\image\\addRAID.png')
photo_addRAID = tk.PhotoImage(file = f'{path}\comArcProject\\image\\addRAID.png')
photo_deleteDriver = tk.PhotoImage(file = f'{path}\comArcProject\\image\\deleteDriver.png')
photo_setting = tk.PhotoImage(file = f'{path}\comArcProject\\image\\settings.png')



resized_image_addDriver  = photo_addDriver.subsample(RESIZE, RESIZE)
resized_image_addRAID  = photo_addRAID.subsample(RESIZE, RESIZE)
resized_image_deleteDriver  = photo_deleteDriver.subsample(RESIZE, RESIZE)
resized_image_setting  = photo_setting.subsample(RESIZE, RESIZE)



# tk.Button(window , text='A' , bg='red' , width=2).pack(side = tk.LEFT , fill = tk.BOTH , expand = True)
# tk.Button(window , text='B' , bg='red').pack(side = tk.TOP , fill = tk.BOTH , expand = True)
# tk.Button(window , text='C' , bg='red').pack(side = tk.LEFT , fill = tk.BOTH , expand = True)
TOP_FARME = tk.Frame(window , width=1024,height=80 , bg='#1B1A55' , highlightbackground='#070F2B' , highlightthickness=2)
LEFT_FARME = tk.Frame(window , width=300,height=720 , bg='#535C91' , highlightbackground='#070F2B' , highlightthickness=2)
RIGTH_FARME = tk.Frame(window , width=774,height=720 , bg='#9290C3')


LEFT_UPPER = tk.Frame(LEFT_FARME , width=250 , height=300 , bg='white' , highlightbackground='black' , highlightthickness=2)
LEFT_LOWER = tk.Frame(LEFT_FARME , width=250 , height=300 , bg='white' , highlightbackground='black' , highlightthickness=2)

Button_AddDriver = tk.Button(TOP_FARME , image=resized_image_addDriver ,bg='#9290C3')
Button_AddRAID = tk.Button(TOP_FARME , image=resized_image_addRAID ,bg='#9290C3')
Button_DeleteDriver = tk.Button(TOP_FARME , image=resized_image_deleteDriver ,bg='#9290C3')
Button_Setting = tk.Button(TOP_FARME , image=resized_image_setting ,bg='#9290C3')

# Button_AddDriver.pack(side='left')
Button_AddDriver.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)
Button_AddRAID.grid(row=0, column=1, sticky='nsew', padx=20, pady=10)
Button_DeleteDriver.grid(row=0, column=2, sticky='nsew', padx=20, pady=10)
Button_Setting.grid(row=0, column=3, sticky='nsew', padx=20, pady=10)
# Button_AddDriver.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

TOP_FARME.grid(row=0 , columnspan=3 ,sticky='nsew')
LEFT_FARME.grid(row=1 , column=0 ,sticky='nsew')
RIGTH_FARME.grid(row=1 , column=2 ,sticky='nsew')


LEFT_UPPER.grid(row=0,columnspan=2 , sticky='nsew' ,  pady=20 )
LEFT_LOWER.grid(row=1,columnspan=2 , sticky='nsew' , pady=20)

RAID_Listbox = tk.Listbox(LEFT_UPPER ,width=50 )
RAID_Listbox.grid(rowspan=1,columnspan=3 ,sticky='nsew')
index = 1
for raid in RAID_LIST:
    RAID_Listbox.insert(index,raid.getName())
    index+=1




RAID_Listbox.bind('<ButtonRelease-1>', on_raid_listbox_click)


# TOP_FARM.pack()
# LEFT_FARM.pack()

# Disable resizing for LEFT_FARME and RIGTH_FARME
LEFT_FARME.pack_propagate(False)
RIGTH_FARME.pack_propagate(False)
LEFT_UPPER.pack_propagate(False)
LEFT_LOWER.pack_propagate(False)

# Configure row and column weights for resizing behavior
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

window.geometry('1024x800')
window.mainloop()