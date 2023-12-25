import os
import random
import shutil
import tkinter as tk
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox

def confirm_popup():
    answer = messagebox.askyesno("Confirmation", "Is this the folder you wish to randomize?")
    return answer

def open_folder_dialog():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        if confirm_popup():
            current_datetime = datetime.now()
            date_time_str = current_datetime.strftime("%Y%m%d_%H%M%S")
            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')  # Get the path to the Downloads folder
            answer_key = os.path.join(downloads_path, date_time_str + "_ANSWER_KEY.txt")  # Create the complete file path

            new_folder = os.path.join(downloads_path, date_time_str)  # Create the complete file path
            copy_directory(folder_selected, new_folder)
            rename(new_folder, answer_key)
        else:
            exit()


def copy_directory(source, destination):
    try:
        shutil.copytree(source, destination)
        print(f"Directory '{source}' copied to '{destination}' successfully.")
    except shutil.Error as e:
        print(f"Directory copy failed: {e}")
    except OSError as e:
        print(f"Directory copy failed: {e}")
    print("Copied succesfully")
            

def rename(pathName, answer_key):
    f = open(answer_key, "w")
    #for each folder in the current folder...
    for directory in os.listdir(pathName):
        #generate a random number (really it's 2 that are being added together for more randomness)
        randomNum1 = random.randint(0, 10000)
        randomNum1 += random.randint(0,10000)
        #the new folder name will be this number in string format
        newDirName = str(randomNum1)
        #write the change to the answer key
        f.write(repr(directory) + " was renamed to " + newDirName + ".txt\n")
        dirPath = os.path.join(pathName, directory)
        newDirPath = os.path.join(pathName, newDirName)
        #rename the current directory path to the new directory path
        os.rename(dirPath, newDirPath)
        
        if os.path.isdir(newDirPath):
            #for each file WITHIN each of the folders...
            for file in os.listdir(newDirPath):
                #make another random number that will be the new image name, same process as above
                randomNum2 = random.randint(0, 10000)
                randomNum2 = random.randint(0, 10000)
                newImgName = str(randomNum2)
                #filepath is the absolute filepath of the old name
                filePath = os.path.join(newDirPath, file)
                #get the extension so that we are not converting any images to different file types
                extension = os.path.splitext(file)[1]  # Get the file extension
                #put it all together !
                newImgPath = os.path.join(newDirPath, newImgName + extension)
                os.rename(filePath, newImgPath)
                #write the change to the answer key, then format with newlines
                f.write("->" + repr(file) + " was renamed to " + repr(newImgName + extension) + "\n")
        f.write("\n\n")
    print("\n\n")

if __name__ == "__main__":       
    root = tk.Tk()
    root.geometry("300x500")
    root.title("Image-Blind-GUI")

    button1 = tk.Button(root, text="Randomize Files", command=open_folder_dialog, width=20, height=20)
    # button1.pack()
    button1.grid(row=0, column=0, padx=0, pady=0)  # Adjust padx and pady as needed


    button2 = tk.Button(root, text="Exit", command=exit)
    # button2.pack()
    button2.grid(row=1, column=0, padx=10, pady=0)  # Adjust padx and pady as needed

    root.mainloop()