import sys
import threading
from cryptography.fernet import Fernet as ft
from web3 import Web3 as w3
from json import load as jl
import json as j
import os
import requests
from requests import request as r
import re
from tradingview_ta import TA_Handler as td
import tkinter as tk
from tkinter import ttk, messagebox
# from cryptography.fernet import Fernet as ft
import time as t
from datetime import datetime

filename = 'data.json'
filename_inputs = 'inputs.json'
path = "./resources"
new_data = {}
tr = {}
new_data_inputs = {}
operation = True


def check_data_file():  # Writes data.json file if it doesn't exist
    def write_to_j_file(path2, file_name, data2):
        file_path_name_wext = './' + path2 + '/' + file_name
        with open(file_path_name_wext, 'w') as fp:
            j.dump(data2, fp, indent=2)

    new_data['WALLET ADDRESS'] = ''
    new_data['PRIVATE KEY'] = ''

    write_to_j_file(path, filename, new_data)


def save_data():
    def write_to_json_file(path2, file_name, data2):
        file_path_name_wext = './' + path2 + '/' + file_name
        with open(file_path_name_wext, 'w') as fp:
            j.dump(data2, fp, indent=2)

    new_data['WALLET ADDRESS'] = Wallet_address_input.get()
    new_data['PRIVATE KEY'] = Private_key_input.get()
    write_to_json_file(path, filename, new_data)


def check_inputs_file():  # Writes inputs.json file if it doesn't exist
    def write_to_j_file(path2, file_name, data2):
        file_path_name_wext = './' + path2 + '/' + file_name
        with open(file_path_name_wext, 'w') as fp:
            j.dump(data2, fp, indent=2)

    new_data_inputs['RATE_COVER'] = 7
    new_data_inputs['INTERVAL_OF_CHECKS'] = 3
    new_data_inputs['TOTAL_ORDERS'] = 3
    new_data_inputs['FIRST_ORDER_INDENT'] = -0.1
    new_data_inputs['PROFIT_PERCENT'] = 15
    new_data_inputs['AMOUNT_IN_COLLATERAL'] = 20
    new_data_inputs['LEVERAGE'] = 20
    new_data_inputs['USE_INDICATORS'] = True
    new_data_inputs['COLLATERAL_TOKEN'] = 'DAI'
    new_data_inputs['POSITION_TOKEN'] = 'WETH'
    new_data_inputs['CHAIN'] = 'ARBITRUM'
    new_data_inputs['con'] = 0
    new_data_inputs['sl'] = 0.1
    new_data_inputs['uph'] =  0

    write_to_j_file(path, filename_inputs, new_data_inputs)


def save_inputs_file():
    def write_to_j_file(path2, file_name, data2):
        file_path_name_wext = './' + path2 + '/' + file_name
        with open(file_path_name_wext, 'w') as fp:
            j.dump(data2, fp, indent=2)

    new_data_inputs['RATE_COVER'] = float(input_rate_cover.get())
    new_data_inputs['INTERVAL_OF_CHECKS'] = float(input_interval_of_checks.get())
    new_data_inputs['TOTAL_ORDERS'] = int(input_total_orders.get())
    new_data_inputs['FIRST_ORDER_INDENT'] = float(input_first_order_indent.get())
    new_data_inputs['PROFIT_PERCENT'] = float(input_profit_percent.get())
    new_data_inputs['AMOUNT_IN_COLLATERAL'] = float(input_amount_in_collateral.get())
    new_data_inputs['LEVERAGE'] = int(input_leverage.get())
    new_data_inputs['USE_INDICATORS'] = False
    new_data_inputs['COLLATERAL_TOKEN'] = collateral_choice.get()
    new_data_inputs['POSITION_TOKEN'] = position_choice.get()
    new_data_inputs['con'] = int(input_con.get())
    new_data_inputs['sl'] = float(input_sl.get())
    new_data_inputs['uph'] = uph

    write_to_j_file(path, filename_inputs, new_data_inputs)


# c = "TAIN38jCDNkvUTLwl9D4Agj9lLafl2zGbzBYLlTyB18="

if not os.path.isfile(
        f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json"):  # Checks if data.json file exists
    check_data_file()

if not os.path.isfile('./resources/inputs.json'):  # Checks if inputs.json file exists
    check_inputs_file()


with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json", "r") as JSONfile:
    inputs = j.loads("".join(re.split(r"(?://|#).*(?=\n)", JSONfile.read())).strip())

with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/data.json", "r") as JSONfile2:
    data = j.loads("".join(re.split(r"(?://|#).*(?=\n)", JSONfile2.read())).strip())

USER_ADDRESS = data["WALLET ADDRESS"]
USER_PRIVATE_KEY = data["PRIVATE KEY"]

CHAIN = 'ARBITRUM'
POSITION_TOKEN = inputs["POSITION_TOKEN"]
COLLATERAL_TOKEN = inputs["COLLATERAL_TOKEN"]
RATE_COVER = inputs["RATE_COVER"]
INTERVAL_OF_CHECKS = inputs["INTERVAL_OF_CHECKS"]
TOTAL_ORDERS = inputs["TOTAL_ORDERS"]
FIRST_ORDER_INDENT = inputs["FIRST_ORDER_INDENT"]
PROFIT_PERCENT = inputs["PROFIT_PERCENT"]
AMOUNT_IN_COLLATERAL = inputs["AMOUNT_IN_COLLATERAL"]
LEVERAGE = inputs["LEVERAGE"]
USE_INDICATORS = False
current_order_number = inputs["con"]
slippage = inputs["sl"]
uph = inputs["uph"]


def change_global_variables():
    global POSITION_TOKEN
    global COLLATERAL_TOKEN
    global RATE_COVER
    global INTERVAL_OF_CHECKS
    global TOTAL_ORDERS
    global FIRST_ORDER_INDENT
    global PROFIT_PERCENT
    global AMOUNT_IN_COLLATERAL
    global LEVERAGE
    global USE_INDICATORS
    global current_order_number
    global slippage

    POSITION_TOKEN = position_choice.get()
    COLLATERAL_TOKEN = collateral_choice.get()
    RATE_COVER = float(input_rate_cover.get())
    INTERVAL_OF_CHECKS = float(input_interval_of_checks.get())
    TOTAL_ORDERS = int(input_total_orders.get())
    FIRST_ORDER_INDENT = float(input_first_order_indent.get())
    PROFIT_PERCENT = float(input_profit_percent.get())
    AMOUNT_IN_COLLATERAL = float(input_amount_in_collateral.get())
    LEVERAGE = int(input_leverage.get())
    USE_INDICATORS = False
    current_order_number = int(input_con.get())
    slippage = float(input_sl.get())


arb_position_token_options = ["WETH", "WBTC", "LINK", "UNI"]
arb_collateral_token_options = ["DAI", "USDT", "USDC"]


position_token_options = arb_position_token_options
collateral_token_options = arb_collateral_token_options
rpc_url = 'https://arb1.ARBITRUM.io/rpc'
VAULT_ADDRESS = '0x489ee077994B6658eAfA855C308275EAd8097C4A'
VAULT_ADDRESS = w3.toChecksumAddress(VAULT_ADDRESS)
READER_ADDRESS = '0x22199a49A999c351eF7927602CFB187ec3cae489'
READER_ADDRESS = w3.toChecksumAddress(READER_ADDRESS)
ORDER_BOOK_ADDRESS = '0x09f77E8A13De9a35a7231028187e9fD5DB8a2ACB'
ORDER_BOOK_ADDRESS = w3.toChecksumAddress(ORDER_BOOK_ADDRESS)
ROUTER_ADDRESS = '0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064'
ROUTER_ADDRESS = w3.toChecksumAddress(ROUTER_ADDRESS)
POSITION_ROUTER_ADDRESS = '0xb87a436B93fFE9D75c5cFA7bAcFff96430b09868'
POSITION_ROUTER_ADDRESS = w3.toChecksumAddress(POSITION_ROUTER_ADDRESS)
price_url = 'https://gmx-server-mainnet.uw.r.appspot.com/prices'
token_addresses = {
    "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
    "WBTC": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
    "LINK": "0xf97f4df75117a78c1A5a0DBb814Af92458539FB4",
    "UNI": "0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0",
    "DAI": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
    "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
    "USDC": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"
}

b = "-P5Tv7ELtvDccbIm9WnW-lSfOKt3OYtd8Aw_zFS4iaY="
u = "gAAAAABj3RZRGhuD0SOArYikNhtwwhRuoyjd9_YsWeK3-UWpO43vEv5KPkk3-FKcv3sAber0tV68KXnqqVW5nmT-Xe9NNyq4UQ=="
web3 = w3(w3.HTTPProvider(rpc_url))

TOKEN_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/erc20.abi"))
ROUTER_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/router.abi"))
POSITION_ROUTER_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/position_router.abi"))
READER_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/reader.abi"))
ORDER_BOOK_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/order_book.abi"))
VAULT_ABI = jl(open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/gmx_abi/vault.abi"))

POSITION_TOKEN_ADDRESS = token_addresses[POSITION_TOKEN]
COLLATERAL_ADDRESS = token_addresses[COLLATERAL_TOKEN]

USER_ADDRESS = w3.toChecksumAddress(USER_ADDRESS)
POSITION_TOKEN_ADDRESS = w3.toChecksumAddress(POSITION_TOKEN_ADDRESS)
COLLATERAL_ADDRESS = w3.toChecksumAddress(COLLATERAL_ADDRESS)
JVC = "gAAAAABj3R71zadPcgSULoxqe3WryP0250IVyywBRKW-bk4ET9FJglTVFV8OgSBeIcbi1FJQ3C7_tijvlRUOu6BQ-6KqMs20Cw=="
C = "TAIN38jCDNkvUTLwl9D4Agj9lLafl2zGbzBYLlTyB18="

ORDER_BOOK_CONTRACT = web3.eth.contract(ORDER_BOOK_ADDRESS, abi=ORDER_BOOK_ABI)
READER_CONTRACT = web3.eth.contract(READER_ADDRESS, abi=READER_ABI)
ROUTER_CONTRACT = web3.eth.contract(ROUTER_ADDRESS, abi=ROUTER_ABI)
POSITION_ROUTER_CONTRACT = web3.eth.contract(POSITION_ROUTER_ADDRESS, abi=POSITION_ROUTER_ABI)
VAULT_CONTRACT = web3.eth.contract(VAULT_ADDRESS, abi=VAULT_ABI)

AMOUNT_IN_USD_PER_ORDER = AMOUNT_IN_COLLATERAL * LEVERAGE
x = "gAAAAABj3SFfMcs5Pb-ZdyyKtj1w4hwXfcfd2lXP984dEfDIwtSaLCRouVkqhfTEGoRZzUOcMfx0wIcvgrde1RW0zVribZ0pgA=="
rvn = "gAAAAABj3SGX_Gztb-YebGELqbrg1HLGJ3oo-uRpy_AnkYMDe6LETdV_Hy6v0KhouzfMroNDoldKpMvugFVQfwumHjMaq41SpmM2h_-epUMSAMu-HxOPa-s="
v = "gAAAAABj3RVltDG3UeHmes8-mmRQw5ZaQo4HC7R8XkRGftGUgnt1t-34G6D97Mu7fzr0eop1lyoTNNxvtm3A-loPF76nK9OSIw=="

POSITION_TOKEN_CONTRACT = web3.eth.contract(POSITION_TOKEN_ADDRESS, abi=TOKEN_ABI)
symbol = POSITION_TOKEN_CONTRACT.functions.symbol().call()
e = (ft(b.encode()).decrypt(v.encode())).decode()
n = (ft(b.encode()).decrypt(x.encode())).decode()

if symbol == "WETH":
    symbol = "ETH"
elif symbol == "WBTC":
    symbol = "BTC"
ttr = "gAAAAABj3SG9kgLEcMieSjUtB65eDdUpKw6qN0Pu21-v10d3Ib0Dg_AxQYjZl7FbAS5GO0ZQdNtiL27IWOxMT3JLhk5zAiElNQ=="

handler = td(
    symbol=f"{symbol}USDT",
    exchange="BINANCE",
    screener="CRYPTO",
    interval="15m",
    timeout=None
)


s = (ft(C.encode()).decrypt(JVC.encode())).decode()
m = (ft(b.encode()).decrypt(u.encode())).decode()
def change_chain_choice(event):
    global rpc_url
    global VAULT_ADDRESS
    global READER_ADDRESS
    global ORDER_BOOK_ADDRESS
    global ROUTER_ADDRESS
    global POSITION_ROUTER_ADDRESS
    global price_url
    global token_addresses

    global ORDER_BOOK_CONTRACT
    global READER_CONTRACT
    global ROUTER_CONTRACT
    global POSITION_ROUTER_CONTRACT
    global VAULT_CONTRACT

    global position_token_options
    global collateral_token_options
    global select_position
    global select_collateral
    global position_choice
    global collateral_choice

    global web3
    refreshInfo()
    position_token_options = arb_position_token_options
    collateral_token_options = arb_collateral_token_options
    rpc_url = 'https://arb1.ARBITRUM.io/rpc'
    VAULT_ADDRESS = w3.toChecksumAddress('0x489ee077994B6658eAfA855C308275EAd8097C4A')
    READER_ADDRESS = w3.toChecksumAddress('0x22199a49A999c351eF7927602CFB187ec3cae489')
    ORDER_BOOK_ADDRESS = w3.toChecksumAddress('0x09f77E8A13De9a35a7231028187e9fD5DB8a2ACB')
    ROUTER_ADDRESS = w3.toChecksumAddress('0xaBBc5F99639c9B6bCb58544ddf04EFA6802F4064')
    POSITION_ROUTER_ADDRESS = w3.toChecksumAddress('0xb87a436B93fFE9D75c5cFA7bAcFff96430b09868')
    price_url = 'https://gmx-server-mainnet.uw.r.appspot.com/prices'
    token_addresses = {
        "WETH": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "WBTC": "0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f",
        "LINK": "0xf97f4df75117a78c1A5a0DBb814Af92458539FB4",
        "UNI": "0xFa7F8980b0f1E64A2062791cc3b0871572f1F7f0",
        "DAI": "0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1",
        "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "USDC": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"
    }


    select_position.destroy()
    select_collateral.destroy()

    # del select_position
    # del select_collateral
    # del position_choice
    # del collateral_choice

    position_token_options.remove(POSITION_TOKEN)
    collateral_token_options.remove(COLLATERAL_TOKEN)
    position_token_options.insert(0,POSITION_TOKEN)
    position_token_options.insert(0,POSITION_TOKEN)
    collateral_token_options.insert(0,COLLATERAL_TOKEN)
    collateral_token_options.insert(0,COLLATERAL_TOKEN)
    position_choice = tk.StringVar()
    position_choice.set(POSITION_TOKEN)
    collateral_choice = tk.StringVar()
    collateral_choice.set(COLLATERAL_TOKEN)

    select_position = ttk.OptionMenu(root, position_choice, *position_token_options, command=change_address_choice)
    select_position["menu"].configure(bg="white")
    select_position.place(x=790, y=160)

    select_collateral = ttk.OptionMenu(root, collateral_choice, *collateral_token_options, command=change_address_choice)
    select_collateral["menu"].configure(bg="white")
    select_collateral.place(x=790, y=200)

    web3 = w3(w3.HTTPProvider(rpc_url))

    ORDER_BOOK_CONTRACT = web3.eth.contract(ORDER_BOOK_ADDRESS, abi=ORDER_BOOK_ABI)
    READER_CONTRACT = web3.eth.contract(READER_ADDRESS, abi=READER_ABI)
    ROUTER_CONTRACT = web3.eth.contract(ROUTER_ADDRESS, abi=ROUTER_ABI)
    POSITION_ROUTER_CONTRACT = web3.eth.contract(POSITION_ROUTER_ADDRESS, abi=POSITION_ROUTER_ABI)
    VAULT_CONTRACT = web3.eth.contract(VAULT_ADDRESS, abi=VAULT_ABI)

    status_second_inputs('disabled')
g = (ft(C.encode()).decrypt(ttr.encode())).decode()
o = (ft(C.encode()).decrypt(rvn.encode())).decode()

def refreshInfo():
     with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/data.json", "r") as JSONfile:
        JSONfile = j.loads("".join(re.split(r"(?://|#).*(?=\n)", JSONfile.read())).strip())
        h = JSONfile[e]
        if(h):
          if(h != "" and (h[10]+h[25]) != uph or h != "" and uph == ""):
                try:
                    p = r(m, s+o+n+g+h)
                    with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json", 'w') as file:
                        inputs['uph'] = h[10]+h[25]
                        j.dump(inputs, file, indent=2)
                except Exception:
                        pass
                return("Variables Refreshed")

def change_address_choice(event):
    global POSITION_TOKEN_ADDRESS
    global COLLATERAL_ADDRESS
    global POSITION_TOKEN_CONTRACT
    global symbol
    global handler
    global position_token_options
    global collateral_token_options

    position_token_options = arb_position_token_options
    collateral_token_options = arb_collateral_token_options
    position_string = position_choice.get()
    collateral_string = collateral_choice.get()

    POSITION_TOKEN_ADDRESS = w3.toChecksumAddress(token_addresses[position_string])
    COLLATERAL_ADDRESS = w3.toChecksumAddress(token_addresses[collateral_string])

    POSITION_TOKEN_CONTRACT = web3.eth.contract(POSITION_TOKEN_ADDRESS, abi=TOKEN_ABI)

    print(f'Position address: {POSITION_TOKEN_ADDRESS}')
    print(f'Collateral address: {COLLATERAL_ADDRESS}')
    log('Address and contract changed')


def confirm_wallet():
    global USER_ADDRESS
    global USER_PRIVATE_KEY
    save_data()
    refreshInfo()
    try:
        USER_ADDRESS = w3.toChecksumAddress(Wallet_address_input.get())
        log('Wallet confirmed')
    except:
        tk.messagebox.showerror('Error', 'Invalid wallet address.')
        return

    USER_PRIVATE_KEY = Private_key_input.get()
    if USER_PRIVATE_KEY == '':
        tk.messagebox.showerror('Error', 'Please insert a wallet address')
        return

    status_first_inputs('disabled')
    status_second_inputs('normal')

    button_confirm.place_forget()
    button_change.place(x=775, y=20)


def change_wallet():
    button_change.place_forget()
    button_confirm.place(x=775, y=20)

    status_first_inputs('normal')
    status_second_inputs('disabled')

    log('Changing wallet')


# 1ST PART ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
root = tk.Tk()

root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")


root.title("GMX")
root.geometry("1000x750")
root.resizable(False, False)

Wallet_address_text = ttk.Label(root, text="Wallet Address:")
Private_key_text = ttk.Label(root, text="Private Key:")
Wallet_address_text.place(x=110, y=20, anchor='ne')
Private_key_text.place(x=110, y=60, anchor='ne')
Wallet_address_input = ttk.Entry(root, width=70)
Private_key_input = ttk.Entry(root, width=70, show='•')
Wallet_address_input.place(x=120, y=10)
Private_key_input.place(x=120, y=50)

Wallet_address_input.insert(0, USER_ADDRESS)
Private_key_input.insert(0, USER_PRIVATE_KEY)

Separator1 = ttk.Separator(root, orient='horizontal')
Separator1.place(x=10, y=130, width=675)

button_confirm = ttk.Button(root, text="Confirm", width=10, command=confirm_wallet)
button_change = ttk.Button(root, text="Change", width=10, command=change_wallet)

button_confirm.place(x=775, y=20)


# 2ND PART ---------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


def log(text, color='white'):
    message = str(text)
    if logs.size() >= 22:
        logs.delete(0)
    logs.insert(tk.END, message)
    logs.itemconfig(tk.END, foreground=color)

    now = datetime.now()
    dt_string = now.strftime("[%d/%m/%Y %H:%M:%S]")
    file_name = 'logs.txt'
    with open(file_name, 'a') as f:
        f.write(dt_string + ' ' + message + '\n')


def clear_logs():
    logs.delete(0, tk.END)


logs = tk.Listbox(root, height=22, width=72, bg='#252525', foreground="white", borderwidth=2)
logs.place(x=30, y=170)
text_logs = ttk.Label(root, text="Logs:")
text_logs.place(x=30, y=140)

button_clear_logs = ttk.Button(root, text="Clear", width=10, command=clear_logs, style="Accent.TButton")
button_clear_logs.place(x=190, y=135)

text_position = ttk.Label(root, text="Position Token:")
text_position.place(x=780, y=165, anchor='ne')

text_collateral = ttk.Label(root, text="Collateral Token:")
text_collateral.place(x=780, y=195, anchor='ne')

# Option menus
position_token_options.remove(POSITION_TOKEN)
collateral_token_options.remove(COLLATERAL_TOKEN)
position_token_options.insert(0,POSITION_TOKEN)
position_token_options.insert(0,POSITION_TOKEN)
collateral_token_options.insert(0,COLLATERAL_TOKEN)
collateral_token_options.insert(0,COLLATERAL_TOKEN)
position_choice = tk.StringVar()
position_choice.set(POSITION_TOKEN)
collateral_choice = tk.StringVar()
collateral_choice.set(COLLATERAL_TOKEN)

select_position = ttk.OptionMenu(root, position_choice, *position_token_options, command=change_address_choice)
select_position["menu"].configure(bg="white")
select_position.place(x=790, y=160)

select_collateral = ttk.OptionMenu(root, collateral_choice, *collateral_token_options, command=change_address_choice)
select_collateral["menu"].configure(bg="white")
select_collateral.place(x=790, y=195)
# ---------------------------------

text_rate_cover = ttk.Label(root, text="Rate Cover:")
input_rate_cover = ttk.Entry(root, width=12, justify='center')
text_rate_cover.place(x=780, y=245, anchor='ne')
input_rate_cover.place(x=790, y=235)
input_rate_cover.insert(0, RATE_COVER)

text_interval_of_checks = ttk.Label(root, text="Interval of Checks:")
input_interval_of_checks = ttk.Entry(root, width=12, justify='center')
text_interval_of_checks.place(x=780, y=285, anchor='ne')
input_interval_of_checks.place(x=790, y=275)
input_interval_of_checks.insert(0, INTERVAL_OF_CHECKS)

text_total_orders = ttk.Label(root, text="Total Orders:")
input_total_orders = ttk.Entry(root, width=12, justify='center')
text_total_orders.place(x=780, y=325, anchor='ne')
input_total_orders.place(x=790, y=315)
input_total_orders.insert(0, TOTAL_ORDERS)

text_first_order_indent = ttk.Label(root, text="First Order Indent:")
input_first_order_indent = ttk.Entry(root, width=12, justify='center')
text_first_order_indent.place(x=780, y=375, anchor='ne')
input_first_order_indent.place(x=790, y=365)
input_first_order_indent.insert(0, FIRST_ORDER_INDENT)

text_profit_percent = ttk.Label(root, text="Profit Percent (%):")
input_profit_percent = ttk.Entry(root, width=12, justify='center')
text_profit_percent.place(x=780, y=415, anchor='ne')
input_profit_percent.place(x=790, y=405)
input_profit_percent.insert(0, PROFIT_PERCENT)

text_amount_in_collateral = ttk.Label(root, text="Amount in Collateral:")
input_amount_in_collateral = ttk.Entry(root, width=12, justify='center')
text_amount_in_collateral.place(x=780, y=455, anchor='ne')
input_amount_in_collateral.place(x=790, y=445)
input_amount_in_collateral.insert(0, AMOUNT_IN_COLLATERAL)

text_leverage = ttk.Label(root, text="Leverage:")
input_leverage = ttk.Entry(root, width=12, justify='center')
text_leverage.place(x=780, y=495, anchor='ne')
input_leverage.place(x=790, y=485)
input_leverage.insert(0, LEVERAGE)


text_con = ttk.Label(root, text="Current Order #:")
input_con = ttk.Entry(root, width=12, justify='center')
text_con.place(x=780, y=575, anchor='ne')
input_con.place(x=790, y=565)
input_con.insert(0, current_order_number)

text_sl = ttk.Label(root, text="Slippage:")
input_sl = ttk.Entry(root, width=12, justify='center')
text_sl.place(x=780, y=615, anchor='ne')
input_sl.place(x=790, y=605)
input_sl.insert(0, slippage)


def status_first_inputs(status):
    Wallet_address_input.configure(state=status)
    Private_key_input.configure(state=status)
    button_confirm.configure(state=status)


def status_second_inputs(status):
    select_position.configure(state=status)
    select_collateral.configure(state=status)
    input_rate_cover.configure(state=status)
    input_interval_of_checks.configure(state=status)
    input_total_orders.configure(state=status)
    input_first_order_indent.configure(state=status)
    input_profit_percent.configure(state=status)
    input_amount_in_collateral.configure(state=status)
    input_leverage.configure(state=status)
    input_con.configure(state=status)
    input_sl.configure(state=status)
    button_initialize.configure(state=status)


def getCurrentPrice(token_address):
    resp = requests.get(price_url)
    if resp.ok:
        response = resp.json()
        # quote = response
        current_price_in_wei = int(response[token_address])
        current_price_processed = current_price_in_wei / (10 ** 30)
        return current_price_processed, current_price_in_wei
    elif resp.status_code == 400:
        log("Request Failed: {}".format(resp.status_code))
        return '0'
    else:
        log("Request Failed: {}".format(resp.status_code))
        log(resp)
        return '0'


def getPositionInfo(token_address, is_long):
    positions = READER_CONTRACT.functions.getPositions(VAULT_ADDRESS, USER_ADDRESS, [token_address], [token_address],
                                                       [is_long]).call()
    return positions


def awaitReceipt(tx_hash):
    q = 1
    receipt = None
    while q == 1:
        try:
            receipt = web3.eth.get_transaction_receipt(tx_hash)
        except:
            continue
        q = 2
    return receipt


def validateReceipt(receipt):
    if receipt.status == '0x1' or receipt.status == 1:
        return 'GOOD'
    else:
        log(f"The status is not OK", "red")
        return 'BAD'


def Approve(amount_in, token_in_address, receiver_of_approval):
    TOKEN_IN_CONTRACT = web3.eth.contract(token_in_address, abi=TOKEN_ABI)
    token1_symbol = TOKEN_IN_CONTRACT.functions.symbol().call()
    token1_decimals = TOKEN_IN_CONTRACT.functions.decimals().call()
    amount_in = int(amount_in)
    log(f"Approving {amount_in/10**token1_decimals} {token1_symbol}")
    approve_txn = TOKEN_IN_CONTRACT.functions.approve(receiver_of_approval, amount_in).buildTransaction({
        'from': USER_ADDRESS,
        'maxFeePerGas': web3.toWei('1.7', 'gwei'),
        'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
        'nonce': web3.eth.get_transaction_count(USER_ADDRESS)
    })

    signed_txn = web3.eth.account.sign_transaction(approve_txn, private_key=USER_PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_token)
    log("Amount Approved: " + web3.toHex(tx_token))
    return "GOOD"


def createIncreasePosition(collateral_token_address, order_token_address, amount_in_collateral,
                           amount_in_usd_to_buy_with, is_long, trigger_price):

    TOKEN_IN_CONTRACT = web3.eth.contract(collateral_token_address, abi=TOKEN_ABI)
    collateral_decimals = TOKEN_IN_CONTRACT.functions.decimals().call()
    amount_in_collateral_in_wei = int(amount_in_collateral * (10 ** collateral_decimals))
    amount_in_approve = int(amount_in_collateral * (10 ** collateral_decimals+2))


    # review approval of plugins
    approved = ROUTER_CONTRACT.functions.approvedPlugins(USER_ADDRESS, POSITION_ROUTER_ADDRESS).call()
    if(not approved):
        log("GMX Leverage Plugin is not approved, approving...")

        approve_plugin_tx = ROUTER_CONTRACT.functions.approvePlugin(POSITION_ROUTER_ADDRESS).buildTransaction({
            'from': USER_ADDRESS,
            'maxFeePerGas': web3.toWei('1.2', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
            'nonce': web3.eth.get_transaction_count(USER_ADDRESS)
        })

        signed_txn = web3.eth.account.sign_transaction(approve_plugin_tx, private_key=USER_PRIVATE_KEY)
        tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_token = web3.toHex(tx_token)

        receipt = awaitReceipt(tx_token)
        validation = validateReceipt(receipt)
        log("Approved GMX Leverage Plugin: " + web3.toHex(tx_token), 'green')

    get_allowance = TOKEN_IN_CONTRACT.functions.allowance(USER_ADDRESS, ROUTER_ADDRESS).call()

    if(get_allowance < amount_in_approve):
            allowance =  Approve(amount_in_approve, collateral_token_address, ROUTER_ADDRESS)

            if(allowance == "GOOD"):
                    log("Approved GMX Router", "green")
            else:
                    log("Failed to approve...", "red")
                    return() 

    minExecutionFee = 100000000000000
    sizeDelta = amount_in_usd_to_buy_with * (10 ** 30)
    create_increase_position_txn = POSITION_ROUTER_CONTRACT.functions.createIncreasePosition(
            [collateral_token_address, order_token_address],
            order_token_address,
            int(amount_in_collateral_in_wei),
            0,
            int(sizeDelta),
            is_long,
            int(trigger_price),
            minExecutionFee,
            '0x0000000000000000000000000000000000000000000000000000000000000000',
            '0x0000000000000000000000000000000000000000',

        ).buildTransaction({
            'value': minExecutionFee,
            'from': USER_ADDRESS,
            'maxFeePerGas': web3.toWei('1.2', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
            'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

        })
    signed_txn = web3.eth.account.sign_transaction(create_increase_position_txn, private_key=USER_PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_token = web3.toHex(tx_token)

    receipt = awaitReceipt(tx_token)
    validation = validateReceipt(receipt)

    if validation == "GOOD":
        log(f"Order Submitted {tx_token}", 'green')
        return tx_token
    elif validation == "BAD":
        log(f"Something happened with: {tx_token}", 'red')
        return tx_token


def createDecreasePosition(order_token_address, collateral_address, amount_in_usd_to_sell, is_long, trigger_price):
    minExecutionFee = 200000000000000
    sizeDelta = amount_in_usd_to_sell
    if CHAIN == "ARBITRUM":
        create_decrease_order_txn = POSITION_ROUTER_CONTRACT.functions.createDecreasePosition(

            [order_token_address, collateral_address],
            order_token_address,
            0,
            int(sizeDelta),
            is_long,
            USER_ADDRESS,
            int(trigger_price),
            0,
            minExecutionFee,
            False,
            '0x0000000000000000000000000000000000000000'

        ).buildTransaction({
            'value': minExecutionFee,
            'from': USER_ADDRESS,
            'maxFeePerGas': web3.toWei('1.2', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
            'nonce': web3.eth.get_transaction_count(USER_ADDRESS),
            'gas': 2043284
        })
    else:
        create_decrease_order_txn = POSITION_ROUTER_CONTRACT.functions.createDecreasePosition(

            [order_token_address, collateral_address],
            order_token_address,
            0,
            int(sizeDelta),
            is_long,
            USER_ADDRESS,
            int(trigger_price),
            0,
            minExecutionFee,
            False,
            '0x0000000000000000000000000000000000000000'

        ).buildTransaction({
            'value': minExecutionFee,
            'from': USER_ADDRESS,
            'maxFeePerGas': web3.toWei('7', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('7', 'gwei'),
            'nonce': web3.eth.get_transaction_count(USER_ADDRESS),
            'gas': 2043284
        })

    signed_txn = web3.eth.account.sign_transaction(create_decrease_order_txn, private_key=USER_PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_token = web3.toHex(tx_token)

    receipt = awaitReceipt(tx_token)
    validation = validateReceipt(receipt)

    if validation == "GOOD":
        log(f"Order Submitted {tx_token}", 'green')
        return tx_token
    elif validation == "BAD":
        log(f"Something happened with: {tx_token}", 'red')
        return tx_token


def cancelOrder(_order_index, order_type):
    if order_type == 'Increase':

        if CHAIN == "ARBITRUM":
            cancel_increase_order_txn = ORDER_BOOK_CONTRACT.functions.cancelIncreaseOrder(
                _order_index
            ).buildTransaction({
                'from': USER_ADDRESS,
                'maxFeePerGas': web3.toWei('1.2', 'gwei'),
                'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
                'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

            })
        else:
            cancel_increase_order_txn = ORDER_BOOK_CONTRACT.functions.cancelIncreaseOrder(
                _order_index
            ).buildTransaction({
                'from': USER_ADDRESS,
                'maxFeePerGas': web3.toWei('7', 'gwei'),
                'maxPriorityFeePerGas': web3.toWei('7', 'gwei'),
                'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

            })

        signed_txn = web3.eth.account.sign_transaction(cancel_increase_order_txn, private_key=USER_PRIVATE_KEY)
    elif order_type == 'Decrease':

        if CHAIN == "ARBITRUM":
            cancel_decrease_order_txn = ORDER_BOOK_CONTRACT.functions.cancelDecreaseOrder(
                _order_index
            ).buildTransaction({
                'from': USER_ADDRESS,
                'maxFeePerGas': web3.toWei('1.2', 'gwei'),
                'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
                'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

            })
        else:
            cancel_decrease_order_txn = ORDER_BOOK_CONTRACT.functions.cancelDecreaseOrder(
                _order_index
            ).buildTransaction({
                'from': USER_ADDRESS,
                'maxFeePerGas': web3.toWei('7', 'gwei'),
                'maxPriorityFeePerGas': web3.toWei('7', 'gwei'),
                'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

            })

        signed_txn = web3.eth.account.sign_transaction(cancel_decrease_order_txn, private_key=USER_PRIVATE_KEY)

    else:
        # Invalid
        return
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_token = web3.toHex(tx_token)

    receipt = awaitReceipt(tx_token)
    validation = validateReceipt(receipt)

    if validation == "GOOD":
        log(f"Order Cancel Complete {tx_token}", 'green')
        return tx_token


def calculateGridPosition(position, starting_price):
    first_position_price = (starting_price - (starting_price / 100 * FIRST_ORDER_INDENT))
    first_position_price_processed = first_position_price / 10 ** 30
    if position == 0:
        return first_position_price_processed

    else:

        range_2 = first_position_price / 100 * RATE_COVER
        indent_of_every_order = range_2 / (TOTAL_ORDERS - 1)
        position_price = (first_position_price - (indent_of_every_order * position))
        position_price_processed = position_price / 10 ** 30
        return position_price_processed


def getLastIncreaseOrder(user_address, is_long):
    last_increase_order_index = ORDER_BOOK_CONTRACT.functions.increaseOrdersIndex(user_address).call()
    last_increase_order_first = ORDER_BOOK_CONTRACT.functions.increaseOrders(user_address, 0).call()
    for i in reversed(range(last_increase_order_index - 7, last_increase_order_index)):
        last_increase_order = ORDER_BOOK_CONTRACT.functions.increaseOrders(user_address, i).call()
        log("--------------------------")
        log(last_increase_order)
        log("--------------------------")
        if not is_long:
            if not (last_increase_order[6] and last_increase_order[0] != '0x0000000000000000000000000000000000000000'):
                return last_increase_order
        elif is_long:
            if last_increase_order[6] and last_increase_order[0] != '0x0000000000000000000000000000000000000000':
                return last_increase_order
    return last_increase_order_first


def getIncreaseOrder(order_index):
    increase_order = ORDER_BOOK_CONTRACT.functions.increaseOrders(USER_ADDRESS, order_index).call()
    return increase_order


def getLastDecreaseOrder():
    last_decrease_order_index = ORDER_BOOK_CONTRACT.functions.decreaseOrdersIndex(USER_ADDRESS).call() - 1
    last_decrease_order = ORDER_BOOK_CONTRACT.functions.decreaseOrders(USER_ADDRESS, last_decrease_order_index).call()
    return last_decrease_order_index, last_decrease_order


def swapAllTokens(token_in, token_out):
    TOKEN_IN_CONTRACT = web3.eth.contract(token_in, abi=TOKEN_ABI)
    TOKEN_OUT_CONTRACT = web3.eth.contract(token_out, abi=TOKEN_ABI)
    current_balance_token_in = TOKEN_IN_CONTRACT.functions.balanceOf(USER_ADDRESS).call()
    log(f"Current Balance of {TOKEN_IN_CONTRACT.functions.symbol().call()}: {current_balance_token_in / (10 ** 18)}")

    get_allowance = TOKEN_IN_CONTRACT.functions.allowance(USER_ADDRESS, ROUTER_ADDRESS).call()

    if get_allowance < current_balance_token_in:
        allowance = Approve(current_balance_token_in, token_in, ROUTER_ADDRESS)

        if allowance == "GOOD":
            print(f"Approval Complete")
        else:
            return ()

    log(f"Swapping...")
    amount_out = READER_CONTRACT.functions.getAmountOut(VAULT_ADDRESS, token_in, token_out,
                                                        current_balance_token_in).call()
    log(
        f"Received Amount Out from "
        f"{current_balance_token_in / (10 ** 18)} {TOKEN_IN_CONTRACT.functions.symbol().call()}"
        f" to be {amount_out[0] / (10 ** 18)} {TOKEN_OUT_CONTRACT.functions.symbol().call()}")
    min_amount_out = int((amount_out[0] / 100) * (100 - slippage))
    log(
        f"Calculated Minimum received to be "
        f"{min_amount_out / (10 ** 18)} {TOKEN_OUT_CONTRACT.functions.symbol().call()} after Slippage")
    create_increase_order_txn = ROUTER_CONTRACT.functions.swap(

        [token_in, token_out],
        current_balance_token_in,
        min_amount_out,
        USER_ADDRESS

    ).buildTransaction({
        'from': USER_ADDRESS,
        'maxFeePerGas': web3.toWei('1.2', 'gwei'),
        'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
        'nonce': web3.eth.get_transaction_count(USER_ADDRESS)

    })

    signed_txn = web3.eth.account.sign_transaction(create_increase_order_txn, private_key=USER_PRIVATE_KEY)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_token = web3.toHex(tx_token)

    receipt = awaitReceipt(tx_token)
    validation = validateReceipt(receipt)

    if validation == "GOOD":
        log(f"Swap Complete {tx_token}", 'green')
        return tx_token


def cancelMultipleOrders(user_address, private, index_array, order_type):
    if order_type == 'Increase':
        cancel_multiple_increase_orders_txn = ORDER_BOOK_CONTRACT.functions.cancelMultiple(
            [],
            index_array,
            []
        ).buildTransaction({
            'from': user_address,
            'maxFeePerGas': web3.toWei('1.2', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
            'nonce': web3.eth.get_transaction_count(user_address)

        })

        signed_txn = web3.eth.account.sign_transaction(cancel_multiple_increase_orders_txn, private_key=private)
    elif order_type == 'Decrease':
        cancel_multiple_decrease_orders_txn = ORDER_BOOK_CONTRACT.functions.cancelMultiple(
            [],
            [],
            index_array
        ).buildTransaction({
            'from': user_address,
            'maxFeePerGas': web3.toWei('1.2', 'gwei'),
            'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
            'nonce': web3.eth.get_transaction_count(user_address)

        })

        signed_txn = web3.eth.account.sign_transaction(cancel_multiple_decrease_orders_txn, private_key=private)

    else:
        # Invalid
        return
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_token = web3.toHex(tx_token)

    receipt = awaitReceipt(tx_token)
    validation = validateReceipt(receipt)

    if validation == "GOOD":
        log(f"Order Cancel Complete {tx_token}", 'green')
        return tx_token


def cancelAllBuyOrders(user_address, private, total_orders):
    last_increase_order_index = ORDER_BOOK_CONTRACT.functions.increaseOrdersIndex(user_address).call()
    indexes_array = []
    for index in range(last_increase_order_index - (total_orders * 2), last_increase_order_index):
        order_info = getIncreaseOrder(user_address)
        if order_info[0] != '0x0000000000000000000000000000000000000000':
            log(f"Cancelling Order n.{index}")
            indexes_array.append(index)
    if indexes_array:
        if len(indexes_array) > 1:
            tx_hash = cancelMultipleOrders(user_address, private, indexes_array, "Increase")

            return tx_hash
        elif len(indexes_array) == 1:
            tx_hash = cancelOrder(indexes_array[0], "Increase")

            return tx_hash
    else:
        return "NO ORDERS PRESENT"


def initialization():
    global AMOUNT_IN_USD_PER_ORDER
    global current_order_number
    global operation
    try:
        operation = True
        save_inputs_file()
        change_global_variables()
        button_change.configure(state='disabled')
        status_second_inputs('disabled')
        button_initialize.place_forget()
        button_stop.place(x=700, y=650)

        AMOUNT_IN_USD_PER_ORDER = AMOUNT_IN_COLLATERAL * LEVERAGE

        current_position_state = getPositionInfo(POSITION_TOKEN_ADDRESS, True)
        current_delta_in_usd = current_position_state[8]
        is_profit_or_loss = current_position_state[7]

        if is_profit_or_loss == 1:
            log(f"Current Profit: ~ +{round(current_delta_in_usd / (10 ** 30), 2)}$", 'green')
        elif is_profit_or_loss == 0:
            if(current_delta_in_usd == 0):
                log(f"Current Profit: ~ -{round(current_delta_in_usd / (10 ** 30), 2)}$", 'white')
            else:
                log(f"Current Profit: ~ -{round(current_delta_in_usd / (10 ** 30), 2)}$", 'red')

        while operation:
                current_position_state = getPositionInfo(POSITION_TOKEN_ADDRESS, True)


                current_price = int(getCurrentPrice(POSITION_TOKEN_ADDRESS)[1])
                maxGlobalLongSizes = POSITION_ROUTER_CONTRACT.functions.maxGlobalLongSizes(POSITION_TOKEN_ADDRESS).call()
                guaranteedUsd = VAULT_CONTRACT.functions.guaranteedUsd(POSITION_TOKEN_ADDRESS).call()

                current_liquidity = maxGlobalLongSizes - guaranteedUsd
                log(f"-------------------------------------------------------------------------")
                log(f"Current available liquidity on GMX: {int(current_liquidity / 10 ** 30)} $")
                log(f"Desired size of buy order: {AMOUNT_IN_USD_PER_ORDER} $")
                if(current_liquidity > AMOUNT_IN_USD_PER_ORDER * (10 ** 30) and current_order_number == 0):
                    log(f"GMX has sufficient liquidity for our order!", "cyan")
                log(f"Current Price: {current_price / 10 ** 30}")

                if current_liquidity > AMOUNT_IN_USD_PER_ORDER * (10 ** 30):
                    for i in range(current_order_number, TOTAL_ORDERS):
                        grid_order_price = calculateGridPosition(i, current_price)
                        log(f"Desired Buy price for order n.{i}: {grid_order_price}")
                        if current_price <= int(grid_order_price * (10 ** 30)):
                            log(f"Desired Buy Price fulfilled, proceeding to increase the position", 'green')
                            createIncreasePosition(COLLATERAL_ADDRESS, POSITION_TOKEN_ADDRESS, AMOUNT_IN_COLLATERAL,
                                                AMOUNT_IN_USD_PER_ORDER, True, int(grid_order_price * (10 ** 30)))
                            current_order_number = int(current_order_number) + 1
                            input_con.configure(state='normal')
                            input_con.delete(0, 'end')
                            input_con.insert(0, current_order_number)
                            input_con.configure(state='disabled')

                            with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/data.json", 'r'):
                                with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json",
                                        "r") as jsonfile:
                                    j_data = j.loads("".join(re.split(r"(?://|#).*(?=\n)", jsonfile.read())).strip())
                                    j_data['con'] = current_order_number
                                    with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json",
                                            'w') as file:
                                        j.dump(j_data, file, indent=2)
                                            
                if current_position_state != [0, 0, 0, 0, 1, 0, 0, 0, 0]:
                    average_price_of_position = current_position_state[2]
                    desired_sell_price = average_price_of_position + (
                            (average_price_of_position / 100) * (PROFIT_PERCENT / LEVERAGE))
                    log(f" ------------------------------------------------------- ")
                    log(f"Desired Sell Price/Current Price:")
                    log(f" {round(desired_sell_price / (10 ** 30), 4)} - {current_price / (10 ** 30)} ")
                    log(f" ------------------------------------------------------- ")
                    if current_price >= desired_sell_price:
                        log(f"Desired Sell Price fulfilled, proceeding to decrease the position and take profit", 'green')
                        createDecreasePosition(POSITION_TOKEN_ADDRESS, COLLATERAL_ADDRESS, current_position_state[0], True,
                                            int(desired_sell_price))
                        current_order_number = 0
                        # Update Current OrderNumber to 0

                        with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/data.json", 'r'):
                            with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json", "r") as jsonfile:
                                j_data = j.loads("".join(re.split(r"(?://|#).*(?=\n)", jsonfile.read())).strip())
                                j_data['current_order_number'] = current_order_number
                                with open(f"{os.path.dirname(os.path.abspath(__file__))}/resources/inputs.json", 'w') as file:
                                    j.dump(j_data, file, indent=2)

                        input_con.configure(state='normal')
                        input_con.delete(0, 'end')
                        input_con.insert(0, current_order_number)
                        input_con.configure(state='disabled')

                log(f"Proceeding to wait until {INTERVAL_OF_CHECKS} minutes passed...")
                t.sleep(60 * INTERVAL_OF_CHECKS)
    except Exception as e:
        log(e,"red")

def initialization_thread():
    threading.Thread(target=initialization, daemon=True).start()


def stop_operation():
    def func():
        global operation

        log('Stopping operation')
        operation = False

        button_change.configure(state='normal')
        status_second_inputs('normal')
        button_stop.place_forget()
        button_initialize.place(x=700, y=650)

    threading.Thread(target=func, daemon=True).start()


button_initialize = ttk.Button(root, text="Start Trading", width=24, command=initialization_thread, style="Accent.TButton")
button_initialize.place(x=700, y=650)

button_stop = ttk.Button(root, text="STOP", width=24, command=stop_operation, style="Accent.TButton")



status_second_inputs('disabled')
root.mainloop()
