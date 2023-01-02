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


class Command:
    def __init__(self, category: str, description: str, command: str, needs_input: bool, prompt: str) -> None:
        self.category = category
        self.description = description
        self.command = command
        self.needs_input = needs_input
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

    def get_needs_input(self) -> bool:
        return self.needs_input

    def set_needs_input(self, needs_input: bool) -> None:
        self.needs_input = needs_input

    def get_prompt(self) -> str:
        return self.prompt

    def set_prompt(self, prompt: str) -> None:
        self.prompt = prompt

command_argument = ""
all_commands = [
    Command("Setup and Updates", "Package Data Sync Only", "sudo pacman -Syy", False, ""),
    Command("Setup and Updates", "Full System Update", "sudo pacman -Syyu", False, ""),
    Command("Setup and Updates", "Refresh Keys", "sudo pacman-key --refresh-keys", False, ""),
    Command("Setup and Updates", "Keyring Update/ Installation", "sudo pacman -Sy archlinux-keyring", False, ""),
    Command("Setup and Updates", "Base Package Ensure", "sudo pacman -S --needed --noconfirm base base-devel wget man", False, ""),
    Command("Setup and Updates", "Noto Sans (full dependency)", "sudo pacman -S --needed --noconfirm noto-fonts && sudo pacman -S --needed --noconfirm --asdeps noto-fonts-cjk  noto-fonts-emoji noto-fonts-extra", False, ""),
    Command("Setup and Updates", "Chaotic AUR Installer", "wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash", False, ""),
    Command("System Cleanups", "Remove orphan packages", "sudo -S pacman -R --noconfirm $(pacman -Qdtq)", False, ""),
    Command("System Cleanups", "Pacman Cache Cleanup", "sudo pacman -Scc", False, ""),
    Command("System Cleanups", "Home directory cache Size", "du -sh ~/.cache/", False, ""),
    Command("System Cleanups", "Home directory cache Clean", "rm -rf ~/.cache/*", False, ""),
    Command("System Cleanups", "Systemd jounal Cleanup", "sudo journalctl --vacuum-size=50M", False, ""),
    Command("System Cleanups", "Filelight install/update", "pacman -S --noconfirm --needed filelight", False, ""),
    Command("Information Center", "Operating System and Kernel", "uname -a && cat /etc/os-release", False, ""),
    Command("Information Center", "CPU", "lscpu", False, ""),
    Command("Information Center", "Disks and Partitions", "lsblk -a", False, ""),
    Command("Information Center", "PCI devices and USB", "lspci", False, ""),
    Command("Information Center", "Partition and File System", "sudo fsdisk -l", False, ""),
    Command("Information Center", "DMI table", "sudo dmidecode", False, ""),
    Command("Information Center", "IP address", "ip addr", False, "")
]

classic_ask = "Your Choice -> "


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
    category_commands = [cmd for cmd in all_commands if cmd.category == category]
    while True:
        menu_formatter(category, category_commands, False)
        selected_command = secure_input_int(classic_ask, len(category_commands))
        if selected_command == -1:
            break
        if category_commands[selected_command].needs_input:
            command_argument = secure_input_string(category_commands[selected_command].prompt)
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

