# Arch Mate - Arch Linux management and configuration tool
# A simple, user-friendly tool for managing and configuring Arch Linux systems
# If it's installed just run 'amate' in your terminal!

# Description: "Arch Mate is a Python script designed to make it easier for users to manage and configure their Arch Linux systems. It provides a range of features, including package management, system configuration, and more, all within a user-friendly interface. With Arch Mate, you can easily maintain and optimize your Arch Linux system, saving time and effort."

# TODO LIST
# 1) make a function for input error check
# 2) adjust the \n at the end between menu


import os
import re # regular expressions

# for internet connection
import urllib.request
import urllib.error

from time import sleep

# File location in the repository
__SCRIPT_URL__ = "https://raw.githubusercontent.com/Pasqualecoder/archmate/main/amate.py" 
__CURRENT_VERSION__ = "2.0"



# Feel free to delete me. I'm not really useful
def cowsay(message):
    lines = message.split('\n')
    width = max(len(line) for line in lines)
    cow = r'''
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
    '''
    result = []
    result.append(' ' + '_' * width)
    for line in lines:
        result.append('< ' + line.ljust(width) + ' >')
    result.append(' ' + '-' * width)
    result.append(cow)
    return '\n'.join(result)
# -----------------------------------



# -------------------------- UPDATE MODULE -----------------------------------

# Compares version numbers
# for example: 1.1 and 2.4
def compare_versions(version1, version2):
    components1 = version1.split('.')
    components2 = version2.split('.')

    for i in range(min(len(components1), len(components2))):
        if int(components1[i]) < int(components2[i]):
            return -1
        elif int(components1[i]) > int(components2[i]):
            return 1

    if len(components1) < len(components2):
        return -1
    elif len(components1) > len(components2):
        return 1
    else:
        return 0


# Makes an HTTP request to the __URL_VERSION__ (the VERSION file in the repository) and return its content
def fetch_newer_version():
    try:
        with urllib.request.urlopen(__SCRIPT_URL__) as response:
            status = int(response.status)
            if status == 200:
                server_file = response.read()
                # CLEANUP the file
                server_file = server_file.decode('utf-8')

                # find the version in the new file
                new_file = server_file.split('\n') # whole file
                new_version = ""
                for i in new_file:
                    if i[0:19] == "__CURRENT_VERSION__":
                        new_version = i.split('"')[1] # gets the string
                        break # once found there's no need to keep seearching 
                return {'file': server_file, 'version': new_version} 
            else:
                return -1
    except (urllib.error.HTTPError, urllib.error.URLError):
        return -1


# Effectly downloads the script from repository
def run_update(contents):
    # location of this file
    script_directory = os.path.dirname(os.path.realpath(__file__))
    script_file = os.path.basename(__file__)
    script_path = os.path.join(script_directory, script_file)
    absolute_path = os.path.abspath(script_path)
    
    with open(absolute_path,'w') as f:
        for i in contents:
            f.write(i)
    print("Update finished. Restart the app")


# Shows the current version, grabs from the web the new version, then choose if run the update or no
def update_amate():
    print(f"Current version: {__CURRENT_VERSION__}")
    fetched = fetch_newer_version()
    if (fetched['version']) == -1:
        print(f"Can't fetch the version from the server! (Probably a network error) {__SCRIPT_URL__}")
    else:
        print(f"Fetched version: {fetched['version']}")

        comparisone_result = compare_versions(__CURRENT_VERSION__, fetched['version'])

        # currently is older
        if comparisone_result == -1:
            run_update(fetched['file'])
            exit()
            
        # currently is newer (WEIRD CASE)
        elif comparisone_result == 1:
            print("Ops... This is kinda weird. You are currently running a newer version of Arch Mate. Probably you made some changes to the program")
            print("The update is up to you. You will lose the changes you have done")
            print("Are you sure you want to download the version from the repository?")
            response = input("(y/N)>")
            if response.lower() in ['y', 'yes', 'YES', 'Yes']:
                run_update(fetched['file'])
                exit()

        # currently is up-to-date'
        elif comparisone_result == 0:
            print("You are already up-to-date")
            print("There is nothing to do")


# ----------------------------------------------------------------------------


# -------------------------- CATEGORIES --------------------------------------


def setup_and_update():
    menu_name = "Setup and Updates"
    setup_and_updates_commands = [
        ["Package Data Sync Only", "sudo pacman -Syy"],
        ["Full System Update", "sudo pacman -Syyu"],
        ["Refresh Keys", "sudo pacman-key --refresh-keys"],
        ["Keyring Update/ Installation", "sudo pacman -Sy archlinux-keyring"],
        ["Base Package Ensure", "sudo pacman -S --needed --noconfirm base base-devel wget man"],
        ["Noto Sans (full dependency)", "sudo pacman -S --needed --noconfirm noto-fonts && sudo pacman -S --needed --noconfirm --asdeps noto-fonts-cjk  noto-fonts-emoji noto-fonts-extra"],
        ["Chaotic AUR Installer", "wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash"]
    ]

    #TODO 1)
    # do while user choice != -1 (so he want to go back)
    while True:
        user_choice = prompt_menu(menu_name, setup_and_updates_commands)
        if user_choice == -1:
            break

        #choice out of range
        elif user_choice < 0 or user_choice > len(setup_and_updates_commands):
            print("Invalid choice!\nPlease try again ...")
            sleep(0.5)
        
        #finally run the chosen command
        else:
            print(setup_and_updates_commands[user_choice][1])
            os.system(setup_and_updates_commands[user_choice][1])
            print()


def system_cleanups():
    menu_name = "System Cleanups"
    system_cleanups_commands = [
        ["Remove orphan packages", "sudo -S pacman -R --noconfirm $(pacman -Qdtq)"],
        ["Pacman Cache Cleanup", "sudo pacman -Scc"],
        ["Home directory cache Size", "du -sh ~/.cache/"],
        ["Home directory cache Clean", "rm -rf ~/.cache/*"],
        ["Systemd jounal Cleanup", "sudo journalctl --vacuum-size=50M"],
        ["Filelight install/update", "pacman -S --noconfirm --needed filelight"]
    ]

    #TODO 1)
    # do while user choice != -1 (so he want to go back)
    while True:
        user_choice = prompt_menu(menu_name, system_cleanups_commands)
        if user_choice == -1:
            break

        #choice out of range
        elif user_choice < 0 or user_choice > len(system_cleanups_commands):
            print("Invalid choice!\nPlease try again ...")
            sleep(0.5)
        
        #finally run the chosen command
        else:
            print(system_cleanups_commands[user_choice][1])
            os.system(system_cleanups_commands[user_choice][1])
            print()


def information_center():
    menu_name = "Information Center"
    information_center_commands = [
        ["Operating System and Kernel", "uname -a && cat /etc/os-release"],
        ["CPU", "lscpu"],
        ["Disks and Partitions", "lsblk -a"],
        ["PCI devices and USB", "lspci"],
        ["Partition and File System", "sudo fsdisk -l"],
        ["DMI table", "sudo dmidecode"],
        ["IP address", "ip addr"]
    ]

    #TODO 1)
    # do while user choice != -1 (so he want to go back)
    while True:
        user_choice = prompt_menu(menu_name, information_center_commands)
        if user_choice == -1:
            break

        #choice out of range
        elif user_choice < 0 or user_choice > len(information_center_commands):
            print("Invalid choice!\nPlease try again ...")
            sleep(0.5)
        
        #finally run the chosen command
        else:
            print(information_center_commands[user_choice][1])
            os.system(information_center_commands[user_choice][1])
            print()


categories = [
    ["Setup and Updates", setup_and_update],
    #["Mirror and Repository Management", mirror_and_repository_management],
    #["Package Management", package_management],
    ["System Cleanups", system_cleanups],
    #["System Configuration", system_configuration],
    #["User Management", user_management],
    ["Information Center", information_center],
    #["Troubleshooting", troubleshooting]
    ["Update Arch Mate", update_amate]
]

# Category | Description | Command | requires input
command_argument = ""
all_commands = [
    ["Setup and Updates", "Package Data Sync Only", "sudo pacman -Syy", False],
    ["Setup and Updates", "Full System Update", "sudo pacman -Syyu", False],
    ["Setup and Updates", "Refresh Keys", "sudo pacman-key --refresh-keys", False],
    ["Setup and Updates", "Keyring Update/ Installation", "sudo pacman -Sy archlinux-keyring", False],
    ["Setup and Updates", "Base Package Ensure", "sudo pacman -S --needed --noconfirm base base-devel wget man", False],
    ["Setup and Updates", "Noto Sans (full dependency)", "sudo pacman -S --needed --noconfirm noto-fonts && sudo pacman -S --needed --noconfirm --asdeps noto-fonts-cjk  noto-fonts-emoji noto-fonts-extra", False],
    ["Setup and Updates", "Chaotic AUR Installer", "wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash", False],
    ["System Cleanups", "Remove orphan packages", "sudo -S pacman -R --noconfirm $(pacman -Qdtq)", False],
    ["System Cleanups", "Pacman Cache Cleanup", "sudo pacman -Scc", False],
    ["System Cleanups", "Home directory cache Size", "du -sh ~/.cache/", False],
    ["System Cleanups", "Home directory cache Clean", "rm -rf ~/.cache/*", False],
    ["System Cleanups", "Systemd jounal Cleanup", "sudo journalctl --vacuum-size=50M", False],
    ["System Cleanups", "Filelight install/update", "pacman -S --noconfirm --needed filelight", False],
    ["Information Center", "Operating System and Kernel", "uname -a && cat /etc/os-release", False],
    ["Information Center", "CPU", "lscpu", False],
    ["Information Center", "Disks and Partitions", "lsblk -a", False],
    ["Information Center", "PCI devices and USB", "lspci", False],
    ["Information Center", "Partition and File System", "sudo fsdisk -l", False],
    ["Information Center", "DMI table", "sudo dmidecode", False],
    ["Information Center", "IP address", "ip addr", False],
]

# ----------------------------------------------------------------------------


def welcome_screen():
    message = "Welcome to ArchMate!\nIt'll help you to configure and manage\nyour system easily and efficiently!"
    print(cowsay(message))
    

def primary_menu():
    #TODO 1)
    while True:
        category_choice = prompt_menu("Main Menu", categories)
        # TODO: do the "out of range check"
        if category_choice == -1:
            break
        elif False:
            print()
        else: 
            categories[category_choice][1]()

    # Close the program


# Prints the menu name and its choices
# then asks for the user input and returns it.
def prompt_menu(menu_name, choices_list):
    # You cant go any backwards of main menu
    back_choice = ""
    if menu_name == "Main Menu":
        back_choice = "Exit"
    else:
        back_choice = "Back"
    
    # printing choices
    print(menu_name)
    print("------")
    for i in range(len(choices_list)):
        print(f"{i+1}) {choices_list[i][0]}")
    print("------")
    print(f"0) {back_choice}\n")

    # asking for input and reduce of 1 because of natural counting
    choice = int(input("Your Choice -> "))
    return choice-1


def secure_input_int(prompt, range):
    value = 0
    while True:
        try:
            value = int(input(prompt))
            if not (0 <= value <= range+1):
                print('Invalid input. Please try again.')
            else:
                break
        except ValueError:
            print('Invalid input. Please try again.')
    return value


def secure_input_string(prompt):
    value = ""
    while True:
        try:
            value = input(prompt)
            if value != '':
                break
            else:
                print('Invalid input. Please try again')
        except ValueError:
                print('Invalid input. Please try again')
    return value


    
def sub_menu(category: str):
    category_command = [row for row in all_commands if row[0] == category]
    print(category_command)
    

def main_menu():
    # take categories
    categories = list([line[0] for line in all_commands])
    unique_elements = []
    for element in categories:
        if element not in unique_elements:
            unique_elements.append(element)
    categories = unique_elements
    print(categories)
    n_categories = len(categories)
    updater_index = n_categories+1
    
    while True:
        menu_formatter("Main Menu", categories, True)
        chosen_category = secure_input_int("Your choice ->", n_categories)
        if chosen_category == 0:
            break
        elif chosen_category == updater_index:
            # TODO run update
            # RUN UPDATE
            print("RUN UPDATE")
        else:
            sub_menu(categories[chosen_category-1])


        


def menu_formatter(title, list, exit: bool):
    print(title)
    print("------")
    for i in range(len(list)):
        print(f"{i+1}) {list[i]}")
    print("------")
    if exit:
        print(f"{len(list)+1}) Update Arch Mate")
        print("0) Exit")
    else:
        print("0) Back")


if __name__ == "__main__":
    welcome_screen()
    main_menu()

