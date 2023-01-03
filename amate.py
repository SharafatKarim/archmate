# Arch Mate - Arch Linux management and configuration tool
# A simple, user-friendly tool for managing and configuring Arch Linux systems
# If it's installed just run 'amate' in your terminal!

# Description: "Arch Mate is a Python script designed to make it easier for users to manage and configure their Arch Linux systems. It provides a range of features, including package management, system configuration, and more, all within a user-friendly interface. With Arch Mate, you can easily maintain and optimize your Arch Linux system, saving time and effort."

# TODO LIST
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

# Insert this in the command string. It will be replaced with the actual argument
argument_identifier = "__AMATE_ARGUMENT__"

class Command:
    def __init__(self, category: str, description: str, command: str, prompt: str) -> None:
        self.category = category
        self.description = description
        self.command = command
        self.prompt = prompt

    def get_category(self) -> str:
        return self.category

    def set_category(self, category: str) -> None:
        self.category = category

    def get_description(self) -> str:
        return self.description

    def set_description(self, description: str) -> None:
        self.description = description

    def get_command(self) -> str:
        return self.command

    def set_command(self, command: str) -> None:
        self.command = command

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, prompt: str) -> None:
        self.prompt = prompt

        
classic_ask = "Your Choice -> "

all_commands = [
    Command("Setup and Updates", "Package Data Sync Only", "sudo pacman -Syy", ""),
    Command("Setup and Updates", "Full System Update", "sudo pacman -Syyu", ""),
    Command("Setup and Updates", "Refresh Keys", "sudo pacman-key --refresh-keys", ""),
    Command("Setup and Updates", "Keyring Update/ Installation", "sudo pacman -Sy archlinux-keyring", ""),
    Command("Setup and Updates", "Base Package Ensure", "sudo pacman -S --needed --noconfirm base base-devel wget man", ""),
    Command("Setup and Updates", "Noto Sans (full dependency)", "sudo pacman -S --needed --noconfirm noto-fonts && sudo pacman -S --needed --noconfirm --asdeps noto-fonts-cjk  noto-fonts-emoji noto-fonts-extra", ""),
    Command("Setup and Updates", "Chaotic AUR Installer", "wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash", ""),

    Command("Mirror and Repository Management", "Print current mirrors", "cat /etc/pacman.d/mirrorlist", ""),
    Command("Mirror and Repository Management", "Mirrorlist Edit", "sudo ${EDITOR:-nano} /etc/pacman.d/mirrorlist", ""),
    Command("Mirror and Repository Management", "Reflector Install or Update", "sudo pacman -S --needed --noconfirm reflector", ""),
    Command("Mirror and Repository Management", "Reflector Mirror Setup for Specific Country", f"sudo reflector -c {argument_identifier} --save /etc/pacman.d/mirrorlist", "Your country name or code -> "),
    Command("Mirror and Repository Management", "List all Repository", "grep '^\[.*\]' /etc/pacman.conf | grep -v 'options' | sed 's/\[//g' | sed 's/\]//g'", ""),
    Command("Mirror and Repository Management", "Pacman Configuration", "sudo ${EDITOR:-nano} /etc/pacman.conf", ""),
    Command("Mirror and Repository Management", "Chaotic AUR Installer", "wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash", ""), # FIXME: AGAIN?!
    
    Command("Package Management", "Install packages", f"sudo pacman -S --needed --noconfirm {argument_identifier}", "Enter your package names (for multiple value, separate with space)\n-> "),
    Command("Package Management", "Install packages as dependency", f"sudo pacman -S --needed --noconfirm --asdeps {argument_identifier}", "Enter your package names (for multiple value, separate with space)\n-> "),
    Command("Package Management", "Uninstall packages", f"sudo pacman -Rns {argument_identifier}", "Enter your package names (for multiple value, separate with space)\n-> "),
    Command("Package Management", "Search packages", f"sudo pacman -Ss {argument_identifier}", "Enter your package name\n-> "),
    Command("Package Management", "DB lock remove", "sudo rm /var/lib/pacman/db.lck", ""),
    Command("Package Management", "List system + explicit + dependency packages", "pacman -Q", ""),
    Command("Package Management", "List system packages", "pacman -Qet", ""),
    Command("Package Management", "List explicit packages", "pacman -Qe", ""),
    Command("Package Management", "List orphan packages", "pacman -Qdt", ""),
    
    Command("System Cleanups", "Remove orphan packages", "sudo -S pacman -R --noconfirm $(pacman -Qdtq)", ""),
    Command("System Cleanups", "Pacman Cache Cleanup", "sudo pacman -Scc", ""),
    Command("System Cleanups", "Home directory cache Size", "du -sh ~/.cache/", ""),
    Command("System Cleanups", "Home directory cache Clean", "rm -rf ~/.cache/*", ""),
    Command("System Cleanups", "Systemd jounal Cleanup", "sudo journalctl --vacuum-size=50M", ""),
    Command("System Cleanups", "Filelight install/update", "pacman -S --noconfirm --needed filelight", ""),

    Command("Information Center", "Operating System and Kernel", "uname -a && cat /etc/os-release", ""),
    Command("Information Center", "CPU", "lscpu", ""),
    Command("Information Center", "Disks and Partitions", "lsblk -a", ""),
    Command("Information Center", "PCI devices and USB", "lspci", ""),
    Command("Information Center", "Partition and File System", "sudo fsdisk -l", ""),
    Command("Information Center", "DMI table", "sudo dmidecode", ""),
    Command("Information Center", "IP address", "ip addr", "")
]



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

def welcome_screen():
    message = "Welcome to ArchMate!\nIt'll help you to configure and manage\nyour system easily and efficiently!"
    print(cowsay(message))


def menu_formatter(title, list, exit: bool):
    are_commands = True if type(list[0]) == Command else False
    
    print(title)
    print("------")
    for i in range(len(list)):
        if are_commands:
            print(f"{i+1}) {list[i].description}")
        else:
            print(f"{i+1}) {list[i]}")
    print("------")
    if exit:
        print(f"{len(list)+1}) Update Arch Mate")
        print("0) Exit")
    else:
        print("0) Back")


def secure_input_int(prompt, range):
    value = 0
    while True:
        try:
            value = int(input(prompt)) - 1
            if -1 <= value < range:
                break
            else:
                print('Invalid input. Please try again.')
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
    # grab all commands of the chosen category
    category_commands = [cmd for cmd in all_commands if cmd.category == category]
    while True:
        menu_formatter(category, category_commands, False)
        selected_command = secure_input_int(classic_ask, len(category_commands))
        if selected_command == -1:
            break
        if category_commands[selected_command].prompt != "":
            # Asks the user for the additional input
            command_argument = secure_input_string(category_commands[selected_command].prompt)
            # Compose the command using the new input
            category_commands[selected_command].command = category_commands[selected_command].command.replace(argument_identifier, command_argument)
        os.system(category_commands[selected_command].command)
        print()
    

def main_menu():
    # take categories
    categories = [cmd.category for cmd in all_commands]
    unique_elements = []
    for element in categories:
        if element not in unique_elements:
            unique_elements.append(element)
    categories = unique_elements
    n_categories = len(categories)
    updater_index = n_categories
    
    while True:
        menu_formatter("Main Menu", categories, True)
        chosen_category = secure_input_int(classic_ask, n_categories+1)
        if chosen_category == -1:
            break
        elif chosen_category == updater_index:
            # TODO run update
            # RUN UPDATE
            print("RUN UPDATE")
        else:
            sub_menu(categories[chosen_category])


if __name__ == "__main__":
    welcome_screen()
    main_menu()

