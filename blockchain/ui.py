from tkinter import *
from blockchain import Blockchain
import json

bchain = Blockchain()

"""
User Interface
"""
ui = Tk()

ui.title('Blockchain IIM')
ui.geometry("1200x600+20+20")

label = Label(ui, text="Nom de block :")
label.pack()

data = StringVar()

input = Entry(ui, textvariable = data)
input.pack()

def create():
    block = bchain.new_block(input.get())
    bchain.add_block(block)

    data = bchain.format_data(block)

    input.delete(0,END)
    list.insert(END, data)
 
# def delete_all():
#     with open('blockchain/blocks.json', 'r') as data_file:
#         data = json.load(data_file)

#     # for element in data:
#     #     del element.pop()

#     list.delete(0, END)
 
# def delete():
# 	list.delete(ANCHOR)

button = Button(ui, text="Créer", width = 10 , command = create)
button.pack()

# btn_delete_all = Button(text = "Supprimer tout", command = delete_all)
# btn_delete_all.pack()

# btn_delete = Button(text = "Supprimer par sélection", command = delete)
# btn_delete.pack()

list = Listbox(ui, width = 600)
list.pack()

ui.mainloop()