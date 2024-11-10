try:
    import customtkinter
    from customtkinter import filedialog
    import webbrowser
    import requests
    from elevate import elevate
except:
    import os
    os.system("pip install -r requirements.txt")
    import customtkinter
    from customtkinter import filedialog
    import webbrowser
    import requests
    from elevate import elevate



#by 80dropz
elevate()
main = customtkinter.CTk()
main.title("CryptkSage - Setup")
main.geometry("400x300")
main.resizable(False, False)
main.iconbitmap("images/logo.ico")


responselabel = customtkinter.CTkLabel(main, text=" ", font=("roboto", 16))
responselabel.place(relx=5, rely=.7, anchor="center")

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
            print("Key saved successfully")
            print("You can now start CryptoSage if your config file and settings are correct")
            input("")
            exit()
    else:
        responselabel.configure(text="Something is wrong with your key", text_color="red")





#simple headers for the file's
header = customtkinter.CTkLabel(main, text="CryptoSage - setup", font=("roboto", 24, "bold"))
header.place(relx=.5, rely=.05, anchor="center")
subheader = customtkinter.CTkLabel(main, text="By: @80dropz", font=("roboto", 16, "bold"))
subheader.place(relx=.5, rely=.14, anchor="center")


#opens website to get api key and enter into key entry
getkey = customtkinter.CTkButton(main, text="Get API key", width=40, height=20, command=lambda: webbrowser.open("https://pro.coinmarketcap.com/account"))
getkey.place(relx=.13, rely=.07, anchor="center")
#enters the api key and will eventully full work and add to file aswell as test the file
APIkey = customtkinter.CTkEntry(main, placeholder_text="API key")
APIkey.place(relx=.5, rely=.3, anchor="center")
#tests the api key and if it is functioning it will write to a key file if not it will not write to a key file and provide an error


#just the basic response from saving your key with command keysave
testkey = customtkinter.CTkButton(main, text="SaveKey", command=lambda: keysave(str(APIkey.get())))
testkey.place(relx=.5, rely=.4, anchor="center")




main.mainloop()

