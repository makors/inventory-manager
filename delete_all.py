# imports
import gspread
from colorama import just_fix_windows_console, Fore, Back, Style

# fix colorama and init google service acc
just_fix_windows_console()
gc = gspread.service_account(filename='tokens/credentials.json')

# confirmation
confirm = input(f"{Fore.RED}Are you sure you would like to delete {Style.BRIGHT}ALL{Style.RESET_ALL}{Fore.RED} spreadsheets?\nIf so, type {Style.BRIGHT}'makors is cool'{Style.RESET_ALL}{Fore.RED} in the box below.{Style.RESET_ALL}\n{Fore.BLUE}")
print(Style.RESET_ALL)

# if confirmation, delete files and print "action completed" 
if confirm == "makors is cool":
    try:
        for sh in gc.openall():
            gc.del_spreadsheet(sh.id)
        raise Exception("DTB")
    except:
        print(Back.GREEN + Fore.WHITE + "Action completed." + Style.RESET_ALL)

# if the confirmation is not "makors is cool", dont do anything
else:
    print(Back.RED + "Please rerun the file and type 'makors is so cool' to delete your spreadsheet if you would like to proceed." + Style.RESET_ALL)