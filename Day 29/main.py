from customtkinter import *
from PIL import Image
import random
from CTkMessagebox import CTkMessagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ------------------------ PASSWORD GENERATOR---------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for iteration in range(randint(8, 10))]
    password_symbols = [choice(symbols) for iteration in range(randint(2, 4))]
    password_numbers = [choice(numbers) for iteration in range(randint(2, 4))]

    pasword_list = password_letters+password_symbols+password_numbers
    shuffle(pasword_list)

    password = "".join(pasword_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD --------------------------- #


def success_notification ():
    CTkMessagebox(master=window, title="Notification From Nycepter", message="Your password has been successfully saved!", icon="check")

def notification_blank_website ():
    CTkMessagebox(master=window, title="Notification From Nycepter", message="The Website/App field cannot be blank, please fill it out.", icon="warning")

def notification_blank_username ():
    CTkMessagebox(master=window, title="Notification From Nycepter", message="The Email/Username field cannot be blank, please fill it out.", icon="warning")

def notification_blank_password ():
    CTkMessagebox(master=window, title="Notification From Nycepter", message="The Password field cannot be blank, please fill it out.", icon="warning")

def ask_confirmation():
    # get yes/no answers
    msg = CTkMessagebox(master=window, title="Inquiry From Nycepter",  message=f"Here are the details you have entered. \n\n Website/App:\n {website_entry.get()} \n\n Email/Username: \n{username_entry.get()} \n\n Password:\n {password_entry.get()} \n\n Are these correct?",
                        icon="question", option_1="Yes", option_2="No")
    response = msg.get()
    
    return response     




def Save():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: 
                {"Username": username, "Password": password}
                }

    if len(website) < 1:
        notification_blank_website ()
    elif len(username) < 1:
        notification_blank_username ()
    elif len(password) < 1:
        notification_blank_password()
    else:
        response = ask_confirmation() 
        if response == "Yes":
            try:
                with open("data.json", "r") as data_file:

                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:           
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                success_notification()
            
        else:
            pass

def get_main_keys_from_json():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            main_keys = list(data.keys())
            return main_keys
    except FileNotFoundError:
        print(f"Error: The file {data.json} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {data.json} does not contain valid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
    
def get_username_subkeys():
    usernames = []
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            for sub_dict in data.values():
                # Check if 'Username' key exists in the sub-dictionary
                if 'Username' in sub_dict:
                    usernames.append(sub_dict['Username'])
                else:
                    usernames.append('Username not found')
        return usernames
    except FileNotFoundError:
        print(f"Error: The file {data.json} was not found.")
        return usernames  # Return empty list or already accumulated usernames
    except json.JSONDecodeError:
        print(f"Error: The file {data.json} does not contain valid JSON.")
        return usernames  # Return empty list or already accumulated usernames
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
def get_password_subkeys():
    passwords = []
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            for sub_dict in data.values():
                # Check if 'password' key exists in the sub-dictionary
                if 'Password' in sub_dict:
                    passwords.append(sub_dict['Password'])
                else:
                    passwords.append('password not found')
        return passwords
    except FileNotFoundError:
        print(f"Error: The file {data.json} was not found.")
        return passwords  # Return empty list or already accumulated passwords
    except json.JSONDecodeError:
        print(f"Error: The file {data.json} does not contain valid JSON.")
        return passwords  # Return empty list or already accumulated passwords
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def list_button_press():


    rowsite= 0
    rowname= 0
    rowpass= 0
    website_list = get_main_keys_from_json()
    username_list = get_username_subkeys()
    password_list = get_password_subkeys()
    copy_image_path = "copy.png"
    copy_image = CTkImage(dark_image=Image.open(copy_image_path), size=(20, 20))


    list_popup = CTkToplevel(master=window)
    list_popup.title("Websites and Apps")
    list_popup.config(padx=20, pady=20)
    list_popup.attributes('-topmost', True)

    list_popup_list = CTkScrollableFrame(master=list_popup, height=400, width=250)
    list_popup_list.pack()

    def copy_password(password):
        pyperclip.copy(password)

    for item in website_list:
        
        CTkLabel(list_popup_list, text=f"{item}:").grid(row=rowsite, column=0)
        rowsite += 1
    for item in username_list:
        
        CTkLabel(list_popup_list, text=item).grid(row=rowname, column=1, padx=5)
        rowname += 1

    for item in password_list:
        copy = lambda password=item: copy_password(password)
        CTkButton(list_popup_list, image=copy_image, width=30, height=30, text="", command=copy).grid(row=rowpass, column=2, padx=5)
        rowpass += 1

    
default_username = "default_value.txt"

def save_default_value():
    with open(default_username, 'w') as file:
        file.write(username_entry.get())

def load_default_value():
    try:
        with open(default_username, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ""

        
def on_program_start():
    default_value = load_default_value()
    return default_value



# ---------------------------- UI SETUP ------------------------------- #

set_appearance_mode("Dark")
window = CTk()
window.title("Nycepter's Password Manager")
window.config(padx=20, pady=20, height=400, width=400)


image_path = "logo.png"  
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print("Image file not found. Please check the path.")
    exit()


logo_img = CTkImage(dark_image=image, size=(150, 150))  


logo_label = CTkLabel(window, image=logo_img, text="")
logo_label.grid(row=0, column=1, sticky='e')

website_label = CTkLabel(window, text="Website/App:")
username_label = CTkLabel(window, text="Email/Username: ")
password_label = CTkLabel(window, text="Password:")
website_entry = CTkEntry(window, width=350)
window.update()
website_entry.focus()
username_entry = CTkEntry(window, width=350)
password_entry = CTkEntry(window, width=210)
generate_button = CTkButton(window, text="Generate Password", corner_radius=25, command=generate_password)
add_button = CTkButton(window, text="Save Password", width=350, corner_radius=25, fg_color="#bb0000", hover_color="#800000", command=Save)
list_button = CTkButton(window, text="Show Current Websites/Apps", width=350, corner_radius=25, command=list_button_press)
default_button = CTkButton(window, text="Set Current Email/Username as Default", width=150, corner_radius=25, command=save_default_value)


website_label.grid(row=2, column=0,)
username_label.grid(row=3, column=0)
password_label.grid(row=4, column=0)
website_entry.grid(row=2, column=1, columnspan=2)
username_entry.grid(row=3, column=1, columnspan=2)
username_entry.insert(0, on_program_start())
password_entry.grid(row=4, column=1)

generate_button.grid(row=4, column=2)
add_button.grid(row=5, column=1, columnspan=2)
list_button.grid(row=6, column=1, columnspan=2)
default_button.grid(row=8, column=1, columnspan=2)

window.grid_rowconfigure(1, minsize=20)
window.grid_rowconfigure(7, minsize=20)


window.mainloop()
