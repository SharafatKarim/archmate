# Arch Mate - Arch Linux management and configuration tool
# A simple, user-friendly tool for managing and configuring Arch Linux systems
# If it's installed just run 'amate' in your terminal!

# Description: "Arch Mate is a Python script designed to make it easier for users to manage and configure their Arch Linux systems. It provides a range of features, including package management, system configuration, and more, all within a user-friendly interface. With Arch Mate, you can easily maintain and optimize your Arch Linux system, saving time and effort."

# TODO LIST
# 1) make a function for input error check
# 2) check if a update is needed using a VERSION file in the repository

import os
from time import sleep #FIXME unusual

__CURRENT_VERSION__ = "1.0"



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
            sleep(0.5) #FIXME: sleep is kinda unsual
        
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
            sleep(0.5) #FIXME: sleep is kinda unsual
        
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
            sleep(0.5) #FIXME: sleep is kinda unsual
        
        #finally run the chosen command
        else:
            print(information_center_commands[user_choice][1])
            os.system(information_center_commands[user_choice][1])
            print()





def update_amate():
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





def welcome_screen():
    print("""
    Welcome to ArchMate!
    It'll help you to configure and manage
    your system easily and efficiently!\n""")
    

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

'''
Prints the menu name and its choices
then asks for the user input and returns it.
'''
def prompt_menu(menu_name, choices_list):
    # You cant go any backwards of main menu
    back_choice = ""
    if menu_name == "Main Menu":
        back_choice = "Exit"
    else:
        back_choice = "Back"
    
    #Printing choices
    print(menu_name)
    print("------")
    for i in range(len(choices_list)):
        print(f"{i+1}) {choices_list[i][0]}")
    print("------")
    print(f"0) {back_choice}\n")

    #asking for input and reduce of 1 because of natural counting
    choice = int(input("Your Choice -> "))
    return choice-1




if __name__ == "__main__":
    welcome_screen()
    while True:
        primary_menu()
        break


