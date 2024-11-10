from elevate import elevate
import customtkinter

try:
    open("config.txt", "r")
except:
    with open("config.txt", "w") as f:
        f.write(" ")


#read the coins in the config file
with open("config.txt", "r") as f:
    specific_line = f.readlines()
active_coins = specific_line[0] if specific_line else ""

def save():
    global active_coins
    with open("config.txt", "r") as r:
        if coins.get() not in r.read():
            with open("config.txt", "a") as f:
                f.write(f"{coins.get()}, ")
            # Re-read the file to update active_coins
            with open("config.txt", "r") as f:
                specific_line = f.readlines()
            active_coins = specific_line[0] if specific_line else ""
            coinslabel.configure(text=active_coins)

def clear():
    global active_coins
    with open("config.txt", "w") as f:
        f.write(" ")
    active_coins = ""
    coinslabel.configure(text=active_coins)


# List of supported coins
working_coins = ["BTC", "ETH", "SOL", "DOGE", "SHiBU", "LTC", "BONK", "XMR", "MOG", "USDT"]


# Start the window
main = customtkinter.CTk()
main.title("CryptoSage - Setup")
main.geometry("400x300")
main.resizable(False, False)
main.iconbitmap("images/logo.ico")


#simple headers for the file's
header = customtkinter.CTkLabel(main, text="CryptoSage - setup", font=("roboto", 24, "bold"))
header.place(relx=.5, rely=.05, anchor="center")
subheader = customtkinter.CTkLabel(main, text="By: @80dropz", font=("roboto", 16, "bold"))
subheader.place(relx=.5, rely=.14, anchor="center")
coinsheader = customtkinter.CTkLabel(main, text="Coins", font=("Roboto", 18, "bold"))
coinsheader.place(relx=.5, rely=.4, anchor="center")


#save and clear buttons
savebutton = customtkinter.CTkButton(main, text="Save Coin", command=save, fg_color="green", width=100, height=25)
savebutton.place(relx=.35, rely=.85, anchor="center")
clearcryptobutton = customtkinter.CTkButton(main, text="Clear Coins", command=clear, fg_color="red", width=100, height=25)
clearcryptobutton.place(relx=.65, rely=.85, anchor="center")


#Coin selection
coins = customtkinter.CTkOptionMenu(main, values=working_coins)
coins.place(relx=.5, rely=.7, anchor="center")


#displies the saved coins that are in the config file
coinslabel = customtkinter.CTkLabel(main, text=active_coins, font=("roboto", 16, "bold"))
coinslabel.place(relx=.5, rely=.95, anchor="center")


# Run the window loop
main.mainloop()
