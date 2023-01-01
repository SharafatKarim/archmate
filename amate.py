# Arch Mate - Arch Linux management and configuration tool
# A simple, user-friendly tool for managing and configuring Arch Linux systems
# If it's installed just run 'amate' in your terminal!

# Description: "Arch Mate is a Python script designed to make it easier for users to manage and configure their Arch Linux systems. It provides a range of features, including package management, system configuration, and more, all within a user-friendly interface. With Arch Mate, you can easily maintain and optimize your Arch Linux system, saving time and effort."

import os
from time import sleep

def show_troubleshooting():
    print("""
        Troubleshooting
        ------
        1) Uninstall this script (if installed)
        2) Manjaro Bangla font issue
        ------
        0) Main Menu
""")

def troubleshooting():
    show_troubleshooting()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                user = os.getenv('USER')
                if os.path.isfile(f'/home/{user}/amate.py'):
                    os.system(f"rm ~/amate.py")
                with open(f'/home/{user}/.zshrc','r') as f:
                    with open(f'/home/{user}/.zshrccopy','w') as w:
                        for i in f:
                            if i == 'alias amate="python $HOME/amate.py"\n':
                                continue
                            w.write(i)
                os.system("mv ~/.zshrccopy ~/.zshrc")
                with open(f'/home/{user}/.bashrc','r') as f:
                    with open(f'/home/{user}/.bashrccopy','w') as w:
                        for i in f:
                            if i == 'alias amate="python $HOME/amate.py"\n':
                                continue
                            w.write(i)
                os.system("mv ~/.bashrccopy ~/.bashrc")
            case 2:
                os.system(f"curl -s https://raw.githubusercontent.com/SharafatKarim/Manjaro-Bangla-Font-Fix/main/main.sh | bash")
                troubleshooting()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                troubleshooting()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        troubleshooting()

def show_information_center():
    print("""
        Information Center
        ------
        1) Operating System and Kernel
        2) CPU
        3) Disks and Partitions
        4) PCI devices and USB
        5) Partition and File System
        6) DMI table
        7) IP address
        ------
        0) Main Menu
""")

def information_center():
    show_information_center()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"uname -a")
                os.system(f"cat /etc/os-release")
                information_center()
            case 2:
                os.system(f"lscpu")
                information_center()
            case 3:
                os.system(f"lsblk -a")
                information_center()
            case 4:
                os.system(f"lspci")
                information_center()
            case 5:
                os.system(f"sudo fsdisk -l")
                information_center()
            case 6:
                os.system(f"sudo dmidecode")
                information_center()
            case 7:
                os.system(f"ip addr")
                information_center()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                information_center()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        information_center()

def show_user_management():
    print("""
        User Management
        ------
        1) List Users
        2) List Active Users
        3) Add User (wheel)
        4) Add User without group
        5) Remove User including home data
        6) Remove User keeping home data
        7) VISUDO - users permission
        ------
        0) Main Menu
        9) Current Text Editor
""")

def user_management():
    show_user_management()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"cat /etc/passwd | grep /home/")
                user_management()
            case 2:
                os.system(f"who")
                user_management()
            case 3:
                name = input("Enter your username -> ")
                os.system(f"sudo useradd -m -G wheel {user}")
                user_management()
            case 4:
                name = input("Enter your username -> ")
                os.system(f"sudo useradd -m {user}")
                user_management()
            case 5:
                name = input("Enter your username -> ")
                os.system(f"sudo userdel -r {user}")
                user_management()
            case 6:
                name = input("Enter your username -> ")
                os.system(f"sudo userdel {user}")
                user_management()
            case 7:
                os.system(f"sudo EDITOR=$EDITOR visudo")
                user_management()
            case 9:
                os.system("echo 'Your current text editor is -> '$EDITOR")
                print("-----")
                print("If you want to change your editor,")
                print("set with your Environment Variable,")
                print("for example, 'export EDITOR=vim'")
                sleep(0.5)
                mirror_and_repository_management()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                user_management()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        user_management()

def show_system_configuration():
    print("""
        System Configuration
        ------
        1) GRUB Configuration
        2) GRUB Update
        3) locale-gen file
        4) locale-gen update
        ------
        0) Main Menu
        9) Current Text Editor
""")

def system_configuration():
    show_system_configuration()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"sudo $EDITOR /etc/default/grub")
                system_configuration()
            case 2:
                os.system(f"grub-mkconfig -o /boot/grub/grub.cfg")
                system_configuration()
            case 3:
                os.system(f"sudo $EDITOR /etc/locale.gen")
                system_configuration()
            case 4:
                os.system(f"sudo locale-gen")
                system_configuration()
            case 9:
                os.system("echo 'Your current text editor is -> '$EDITOR")
                print("-----")
                print("If you want to change your editor,")
                print("set with your Environment Variable,")
                print("for example, 'export EDITOR=vim'")
                sleep(0.5)
                mirror_and_repository_management()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                system_configuration()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        system_configuration()

def show_system_cleaning():
    print("""
        System Cleanups
        ------
        1) Remove orphan packages
        2) Pacman Cache Cleanup
        3) Home directory cache Size
        4) Home directory cache Clean
        5) Systemd jounal Cleanup
        6) Filelight install/ update
        ------
        0) Main Menu
""")

def system_cleaning():
    show_system_cleaning()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"sudo -S pacman -R --noconfirm $(pacman -Qdtq)")
                system_cleaning()
            case 2:
                os.system(f"sudo pacman -Scc")
                system_cleaning()
            case 3:
                os.system(f"du -sh ~/.cache/")
                system_cleaning()
            case 4:
                os.system(f"rm -rf ~/.cache/*")
                system_cleaning()
            case 5:
                os.system(f"sudo journalctl --vacuum-size=50M")
                system_cleaning()
            case 6:
                os.system(f"pacman -S --noconfirm --needed filelight")
                system_cleaning()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                system_cleaning()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        system_cleaning()

def show_package_management():
    print("""
        Package Management
        ------
        1) Install packages
        2) Install packages as dependency
        3) Uninstall packages
        4) Search packages
        5) DB lock remove
        6) List system + explicit + dependency packages
        7) List system packages
        8) List explicit packages
        9) List orphan packages
        ------
        0) Main Menu
""")

def package_management():
    show_package_management()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                package = input("Enter your package names (for multiple value, separate with space)\n-> ")
                os.system(f"sudo pacman -S --needed --noconfirm {package}")
                package_management()
            case 2:
                package = input("Enter your package names (for multiple value, separate with space)\n-> ")
                os.system(f"sudo pacman -S --needed --noconfirm --asdeps {package}")
                package_management()
            case 3:
                package = input("Enter your package names (for multiple value, separate with space)\n-> ")
                os.system(f"sudo pacman -Rns {package}")
                package_management()
            case 4:
                package = input("Enter your package name\n-> ")
                os.system(f"sudo pacman -Ss {package}")
                package_management()
            case 5:
                os.system(f"sudo rm /var/lib/pacman/db.lck")
                package_management()
            case 6:
                os.system(f"pacman -Q")
                package_management()
            case 7:
                os.system(f"pacman -Qet")
                package_management()
            case 9:
                os.system(f"pacman -Qdt")
                print("-----")
                print("To clean it, you can head over to")
                print("System Cleanups section!")
                sleep(0.5)
                package_management()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                package_management()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        package_management()

def show_mirror_and_repository_management():
    print("""
        Mirror and Repository Management
        ------
        1) Print current mirrors
        2) Mirrorlist Edit
        3) Reflector Install or Update
        4) Reflector Mirror Setup for Specific Country
        5) List all Repository
        6) Pacman Configuration
        7) Chaotic AUR Installer
        ------
        0) Main Menu
        9) Current Text Editor
""")

def mirror_and_repository_management():
    show_mirror_and_repository_management()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"cat /etc/pacman.d/mirrorlist")
                mirror_and_repository_management()
            case 2:
                os.system(f"sudo $EDITOR /etc/pacman.d/mirrorlist")
                mirror_and_repository_management()
            case 3:
                os.system(f"sudo pacman -S --needed --noconfirm reflector")
                mirror_and_repository_management()
            case 4:
                country = input("Your country name or code -> ")
                os.system(f"sudo reflector -c {country} --save /etc/pacman.d/mirrorlist")
                mirror_and_repository_management()
            case 5:
                os.system(f"grep '^\[.*\]' /etc/pacman.conf | grep -v 'options' | sed 's/\[//g' | sed 's/\]//g'")
                mirror_and_repository_management()
            case 6:
                os.system(f"sudo $EDITOR /etc/pacman.conf")
                mirror_and_repository_management()
            case 7:
                os.system(f"wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash")
                mirror_and_repository_management()
            case 9:
                os.system("echo 'Your current text editor is -> '$EDITOR")
                print("-----")
                print("If you want to change your editor,")
                print("set with your Environment Variable,")
                print("for example, 'export EDITOR=vim'")
                sleep(0.5)
                mirror_and_repository_management()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                mirror_and_repository_management()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        mirror_and_repository_management()

def show_setup_and_updates():
    print("""
        Setup and Updates
        ------
        1) Package Data Sync Only
        2) Full System Update
        3) Refresh Keys
        4) Keyring Update/ Installation
        5) Base Package Ensure
        6) Noto Sans (full dependency)
        7) Chaotic AUR Installer
        ------
        0) Main Menu
""")


def setup_and_updates():
    show_setup_and_updates()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                primary_choice()
            case 1:
                os.system(f"sudo pacman -Syy")
                setup_and_updates()
            case 2:
                os.system(f"sudo pacman -Syyu")
                setup_and_updates()
            case 3:
                os.system(f"sudo pacman-key --refresh-keys")
                setup_and_updates()
            case 4:
                os.system(f"sudo pacman -Sy archlinux-keyring")
                setup_and_updates()
            case 5:
                os.system(f"sudo pacman -S --needed --noconfirm base base-devel wget man")
                setup_and_updates()
            case 6:
                os.system(f"sudo pacman -S --needed --noconfirm noto-fonts")
                os.system(f"sudo pacman -S --needed --noconfirm --asdeps noto-fonts-cjk  noto-fonts-emoji noto-fonts-extra")
                setup_and_updates()
            case 7:
                os.system(f"wget -q -O chaotic-AUR-installer.bash https://raw.githubusercontent.com/SharafatKarim/chaotic-AUR-installer/main/install.bash && sudo bash chaotic-AUR-installer.bash && rm chaotic-AUR-installer.bash")
                setup_and_updates()
            case _:
                print("""
        Invalid choice!
        Please try again...
    """)
                sleep(0.5)
                setup_and_updates()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
    """)
        sleep(0.5)
        setup_and_updates()

def autoupdate_hook():
    from filecmp import cmp
    if os.getcwd() == os.getenv("HOME"):
        os.system('curl -s --output "$PWD/amate_updated.py" "https://raw.githubusercontent.com/redwan-hossain/amate/main/amate.py"')
        if not cmp("amate.py", "amate_updated.py"):
            os.system("mv amate_updated.py amate.py")
            print("Script has been updated!")
        else:
            os.system("rm amate_updated.py")

def show_main_menu():
    print("""
        Main Menu
        ------
        1) Setup and Updates
        2) Mirror and Repository Management
        3) Package Management
        4) System Cleanups
        5) System Configuration
        6) User Management
        7) Information Center
        8) Troubleshooting
        ------
        0) Update and Exit
""")

def primary_choice():
    show_main_menu()
    try:
        match eval(input("Your Choice -> ")):
            case 0:
                print("exiting...")
                autoupdate_hook()
                exit()
            case 1:
                setup_and_updates()
            case 2:
                mirror_and_repository_management()
            case 3:
                package_management()
            case 4:
                system_cleaning()
            case 5:
                system_configuration()
            case 6:
                user_management()
            case 7:
                information_center()
            case 8:
                troubleshooting()
            case _:
                print("""
        Invalid choice!
        Please try again...
        -----
        Tip: To exit press 0 and enter
    """)
                sleep(0.5)
                primary_choice()
    except (SyntaxError, NameError):
        print("""
        Invalid choice!
        Please try again...
        -----
        Tip: To exit press 0 and enter
    """)
        sleep(0.5)
        primary_choice()

def primary_menu():
    print("""
    Welcome to ArchMate!
    It'll help you to configure and manage
    your system easily and efficiently!""")
    primary_choice()

if __name__ == "__main__":
    primary_menu()
