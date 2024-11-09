import customtkinter
from customtkinter import filedialog
import webbrowser
import requests
#by 80dropz


def keysave(key):
    print(f"passed key as: {key}")
    test = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5000&convert=USD"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": key
    }
    response = requests.get(test, headers=headers)
    print(f"returned with response code {response.status_code}")
    if response.status_code == 200:
        with open("key.key", "w") as f:
            f.write(key)
            responselabel.configure(text="Key Saved!", text_color="Green")
    else:
        responselabel.configure(text="Something is wrong with the key", text_color="red")
        print("it did not work")

    file = open("key.txt", "w")
    file.write(key)
    file.close()
    print("Success")


global responselabel
main = customtkinter.CTk()
main.title("BlockSage - Setup")
main.geometry("400x300")
main.resizable(False, False)
main.iconbitmap("images/logo.ico")


header = customtkinter.CTkLabel(main, text="BlockSage - setup", font=("roboto", 24, "bold"))
header.place(relx=.5, rely=.05, anchor="center")
subheader = customtkinter.CTkLabel(main, text="By: @80dropz", font=("roboto", 16, "bold"))
subheader.place(relx=.5, rely=.14, anchor="center")


#opens website to get api key and enter into key entry
getkey = customtkinter.CTkButton(main, text="Get API key", width=40, height=20, command=lambda: webbrowser.open("https://coinmarketcap.com/"))
getkey.place(relx=.13, rely=.07, anchor="center")
#enters the api key and will eventully full work and add to file aswell as test the file
APIkey = customtkinter.CTkEntry(main, placeholder_text="API key")
APIkey.place(relx=.5, rely=.3, anchor="center")
#tests the api key and if it is functioning it will write to a key file if not it will not write to a key file and provide an error
responselabel = customtkinter.CTkLabel(main, text=" ", font=("roboto", 16))
responselabel.place(relx=5, rely=.7, anchor="center")

#just the basic response from saving your key with command keysave
testkey = customtkinter.CTkButton(main, text="SaveKey", command=lambda: keysave(str(APIkey.get())))
testkey.place(relx=.5, rely=.4, anchor="center")

main.mainloop()

