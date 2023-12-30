
import tkinter as tk
from PIL import ImageTk, Image
import json
from io import BytesIO
import requests

from tkinter import ttk

from threading import Thread

import requests
from pokemon_data import Pokemon_Data_Model








#Loads all the pokemon
def load_pokemon(data_model, pokemon_name_id):
    #Gets the pokemon from our custom data_model
    return data_model.get_pokemon(pokemon_name_id)





data_model = Pokemon_Data_Model('https://pokeapi.co/api/v2/')
pre_data = data_model.get_pokemon("pikachu")


window = tk.Tk()
window.geometry("500x600")
window.config(padx=10, pady=10)


main_title = tk.Label(window, text="Welcome to the PokeDex!")
main_title.config(font= ("Arial", 20))
main_title.pack(padx = 10, pady=10)



img_content = requests.get(pre_data.image).content

img = ImageTk.PhotoImage(Image.open(BytesIO(img_content)))
# Create a Label Widget to display the text or Image
pokemon_image = tk.Label(window, image = img)
pokemon_image.pack(padx = 10, pady=10)

pokemon_name = tk.Label(window)
pokemon_name.config(text = pre_data.name, font=("Arial", 12))
pokemon_name.pack(padx=5, pady=5)


p_height = tk.Label(window)
p_height.config(text = "Height: " + str(pre_data.height), font = ("Arial", 7))
p_height.pack()

p_weight = tk.Label(window)
p_weight.config(text = "Weight: "+str(pre_data.weight) , font = ("Arial", 7))
p_weight.pack()

list_view = ttk.Treeview(window, columns = ("abilities"), show="headings", height=10)
list_view.heading("abilities", text="Abilities")

list_view.pack(padx=10, pady=10)

search_bar = tk.Entry(width = 200)
search_bar.config(font=("Arial", 9))
search_bar.pack(padx=10, pady=10)



def check_pokemon_validity(text12=None):
    if text12 == None:
        search_text = search_bar.get().lower()
    else:
        search_text = text12
    
    if len(search_text.strip()) == 0:
        
        return None
    
    new_data = data_model.get_pokemon(search_text)
    return new_data

def update_pokemon(text12=None):
    
    if text12 == None:
        new_data = check_pokemon_validity()
    else:
        new_data = check_pokemon_validity(text12)

    if new_data == None:
        search_button.config(state='normal')
        return
    
    
    img_content = requests.get(new_data.image).content

    img = ImageTk.PhotoImage(Image.open(BytesIO(img_content)))
    pokemon_image.config(image=img)
    pokemon_image.image = img

    if new_data.name == 'snorlax':

        pokemon_name.config(text="Samraaj")
    else:
        pokemon_name.config(text = new_data.name)
    p_height.config(text = f"Height: {new_data.height} ft")
    p_weight.config(text = f"Weight: {new_data.weight} lbs")



    for item in list_view.get_children():
        list_view.delete(item)


    abilities = new_data.abilities
    for i in range(0, len(abilities)):
       
        list_view.insert(parent = '',index = i,  values = (abilities[i]))
    
    search_button.config(state="normal")
        


def on_button_click():
    search_button.config(state = "disabled")
    Thread(target = update_pokemon).start()
    

search_button = tk.Button(width=50, height=30, text="Search Pokemon")
search_button.config(command=on_button_click)

search_button.pack(padx=10, pady=10)
update_pokemon("pikachu")






window.mainloop()



