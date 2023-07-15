import tkinter
import subprocess
import sys
import time
from tkinter import filedialog, OptionMenu

category_list = (
    "AudioVideo",
    "Audio",
    "Video",
    "Development",
    "Education",
    "Game",
    "Graphics",
    "Network",
    "Office",
    "Settings",
    "System",
    "Utility"
)

def enter_data():
    name = name_entry.get()
    route = route_entry.get()
    version = version_entry.get()
    category = category_var.get()
    icon = icon_entry.get()

    allFields = (name, route, version, category, icon)

    if not icon.endswith(('.png', '.jpg')):
        tkinter.messagebox.showwarning(title="Error", message="Icon must be a png or jpg file")
        return
    
    if all(allFields):    
        with open('config.mk', 'w') as file:

            icon = icon.split('/')[-1].split('.')[0]

            file.write(f'NAME={name}\n')
            file.write(f'ROUTE={route}\n')
            file.write(f'VERSION={version}\n')
            file.write(f'CATEGORY={category}\n')
            file.write(f'ICON={icon}\n')
            file.write(f'DESKTOP={name}.desktop')

        ## /home/dyallo/Documents/Proyectos/lua

        subprocess.run(f'cp -r {route}/* usr/src', shell=True)
        subprocess.run('make build', shell=True)

        ## Find file inside usr/build, if exists we reply a message
        if subprocess.run(['find', 'usr/build', '-name', f'{name}.AppImage']).returncode == 0:
            tkinter.messagebox.showinfo(title="Success", message="AppImage created successfully")
            exit_program()

        
        ## If not, we reply an error message
        tkinter.messagebox.showerror(title="Error", message="An error has ocurred")
        exit_program()

    else:
        tkinter.messagebox.showwarning(title="Error", message="Please fill all the fields")

def exit_program():
    time.sleep(1)
    sys.exit()

def select_route():
    route = filedialog.askdirectory()
    route_entry.delete(0, tkinter.END)
    route_entry.insert(0, route)

def select_icon():
    icon = filedialog.askopenfilename()
    icon_entry.delete(0, tkinter.END)
    icon_entry.insert(0, icon)

window = tkinter.Tk()
window.title("AppImage Creator")

frame = tkinter.Frame(window)
frame.pack()

# Grid
name_label = tkinter.Label(frame, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tkinter.E)
name_entry = tkinter.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

route_label = tkinter.Label(frame, text="Folder")
route_label.grid(row=1, column=0, padx=10, pady=5, sticky=tkinter.E)
route_entry = tkinter.Entry(frame)
route_entry.grid(row=1, column=1, padx=10, pady=5)

route_button = tkinter.Button(frame, text="Select", command=select_route)
route_button.grid(row=1, column=2, padx=5, pady=5)

icon_label = tkinter.Label(frame, text="Icon")
icon_label.grid(row=2, column=0, padx=10, pady=5, sticky=tkinter.E)
icon_entry = tkinter.Entry(frame)
icon_entry.grid(row=2, column=1, padx=10, pady=5)

icon_button = tkinter.Button(frame, text="Select", command=select_icon)
icon_button.grid(row=2, column=2, padx=5, pady=5)

category_label = tkinter.Label(frame, text="Categoría")
category_label.grid(row=3, column=0, padx=10, pady=5, sticky=tkinter.E)
category_var = tkinter.StringVar(value=category_list[-1])
category_optionmenu = OptionMenu(frame, category_var, "", *category_list)
category_optionmenu.grid(row=3, column=1, padx=10, pady=5)

version_label = tkinter.Label(frame, text="Version")
version_label.grid(row=4, column=0, padx=10, pady=5, sticky=tkinter.E)
version_entry = tkinter.Entry(frame)
version_entry.grid(row=4, column=1, padx=10, pady=5)

button = tkinter.Button(frame, text="Create AppImage", command=enter_data)
button.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

window.mainloop()
