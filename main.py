# import libraries
import gspread
from colorama import just_fix_windows_console, Fore, Back, Style
import configparser
from gspread_formatting import *
import gspread_formatting as gsf
from flask import Flask, request
import json
import logging

# flask logging errors - remove for development
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# config
config = configparser.ConfigParser()
config.read('the.config')

# read config and def vars
user_email = config['USER']['email']
sh_title = config['SHEET']['title']

# colorama fix
just_fix_windows_console()

# define acc
gc = gspread.service_account(filename='tokens/credentials.json')

# color formatter for simplified coloring
def colr(r, g, b):
    red = r/255
    green = g/255
    blue = b/255
    return red, green, blue

# create if not exists (cine)
def initalize(title):
    if title not in [sh.title for sh in gc.openall()]:
        # create and share
        sh = gc.create(title)
        sh.share(user_email, perm_type='user', role='writer')
        # make template
        ss = gc.open(title).sheet1
        # colors in google sheets format
        green = colr(50, 168, 82)
        yellow = colr(162, 184, 37)
        blue = colr(74, 134, 232)
        hotpink = colr(181, 63, 158)
        orange = colr(201, 71, 38)
        red = colr(194, 29, 29)
        # column formatting
        col1 = gsf.cellFormat(
            backgroundColor=gsf.color(green[0], green[1], green[2]),
            horizontalAlignment='LEFT'
        )
        col2 = gsf.cellFormat(
            backgroundColor=gsf.color(blue[0], blue[1], blue[2]),
            horizontalAlignment='LEFT'
        )
        col3 = gsf.cellFormat(
            backgroundColor=gsf.color(yellow[0], yellow[1], yellow[2]),
            horizontalAlignment='LEFT'
        )
        col4 = gsf.cellFormat(
            backgroundColor=gsf.color(hotpink[0], hotpink[1], hotpink[2]),
            horizontalAlignment='LEFT'
        )
        col5 = gsf.cellFormat(
            backgroundColor=gsf.color(orange[0], orange[1], orange[2]),
            horizontalAlignment='LEFT'
        )
        col6 = gsf.cellFormat(
            backgroundColor=gsf.color(red[0], red[1], red[2]),
            horizontalAlignment='LEFT'
        )
        # apply formatting and styles
        format_cell_range(ss, 'A1:A10000', col1)
        format_cell_range(ss, 'B1:B10000', col2)
        format_cell_range(ss, 'C1:C10000', col3)
        format_cell_range(ss, 'D1:D10000', col4)
        format_cell_range(ss, 'E1:E10000', col5)
        format_cell_range(ss, 'F1:F10000', col6)
        gsf.set_column_width(ss, 'A', 400)
        gsf.set_column_width(ss, 'C', 120)
        gsf.set_column_width(ss, 'E', 320)
        # final format
        row1a = gsf.cellFormat(
            textFormat=gsf.textFormat(bold=True, fontSize=12),
            horizontalAlignment='CENTER'
        )
        format_cell_range(ss, 'A1:F1', row1a)
        # add text to rows
        ss.update('A1', [["Product", "Price Paid", "Original Price", "Discount", "Amazon Account", "Task Mode"]])
        # print output
        print(Fore.GREEN + f"Google Spreadsheet Created!{Fore.CYAN}\nURL: {sh.url}" + Style.RESET_ALL)
    else:
        sh = gc.open(title)
        print(Fore.RED + f"Spreadsheet Already Exists!\n{Fore.LIGHTBLUE_EX}URL: {sh.url}" + Style.RESET_ALL)

# create spreadsheet named "inventory manager", if it does not exist
initalize(sh_title)

# open spreadsheet
ss = gc.open(sh_title).sheet1

# next row
def next_available_row(sheet):
    str_list = list(filter(None, sheet.col_values(1)))
    return str(len(str_list)+1)

def neww(jsoa):
    data2 = json.dumps(jsoa)
    # Parse the JSON string into a Python dictionary
    data = json.loads(data2)

    # Access the "title" field of the first element in the "embeds" list
    title = data['embeds'][0]['description']
    url = data['embeds'][0]['url']
    orig = data['embeds'][0]['fields'][0]['value']
    paid = data['embeds'][0]['fields'][1]['value']
    discount = data['embeds'][0]['fields'][2]['value']
    mode = data['embeds'][0]['fields'][4]['value']
    email = data['embeds'][0]['fields'][5]['value'][2:-2]
    next_row = next_available_row(ss)
    ss.update_acell(f"A{next_row}", f'=HYPERLINK("{url}", "{title}")')
    ss.update_acell(f"B{next_row}", paid)
    ss.update_acell(f"C{next_row}", orig)
    ss.update_acell(f"D{next_row}", discount)
    ss.update_acell(f"E{next_row}", email)
    ss.update_acell(f"F{next_row}", mode)

# flask app
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_json():
    # Get the JSON data from the request
    data = request.get_json()
    # Do something with the data
    neww(data)
    print(Fore.GREEN + f"Added item to spreadsheet! 🎉" + Style.RESET_ALL)
    return 'Success 🎉'

if __name__ == '__main__':
    app.run(port=8080)