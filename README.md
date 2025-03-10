# Arch Mate

A simple, lightweight, user-friendly tool for managing and configuring Arch Linux systems, written in python.

Arch Mate is a Python script designed to make it easier for users to manage and configure their Arch Linux systems. It provides a range of features, including package management, system configuration, and more, all within a user-friendly interface. With Arch Mate, you can easily maintain and optimize your Arch Linux system, saving time and effort.

![archmate](https://socialify.git.ci/SharafatKarim/archmate/image?description=1&descriptionEditable=A%20simple%20tool%20for%20managing%20Arch%20Linux%20systems%2C%20with%20python&font=Bitter&forks=1&issues=1&language=1&name=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Auto)

> If it's installed just run 'amate' in your terminal to access!


## Screenshots

![](https://res.cloudinary.com/dte603aka/image/upload/v1672566584/2023/arch%20mate/amate_w6o7g2.png)


## Installation

> If you install it, the script will be placed to your home directory and an entry to your `.bashrc`. So that you can access it from anywhere in your system, just by running `amate`!

To install, simply run,

```
curl -s https://raw.githubusercontent.com/SharafatKarim/archmate/main/install.bash > installer.bash && bash installer.bash && rm installer.bash
```

While installation, you can both install it into your system (pacman pacakge) or, your user (`~/`). If you later want to uninstall from your system, you can do it with,

```bash
sudo pacman -R archmate
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/SharafatKarim/archmate
```

Go to the project directory

```bash
  cd archmate
```

Make sure python is installed. For most systems it comes out of the box.

> `python-pip` or any third party modules not required! We also love as minimal as possible!

Then execute with,

```bash
  python amate.py
```

If you want to install on your system, try,
```bash
makepkg -si --clean
```
`--clean` flag will get rid of unnecessary files.

## Support

For support, feel free to text me,
- [Sharafat Karim | Contacts](https://sharafat.pages.dev/about/)


## Features

You'll easily understand if you open the script. Besides this script can be updated from inside(if you are inside home directory)!

Some features are,
- Setup and Updates - basic packages, system's base and fonts updating tool.
- Mirror and Repository Management - easily use reflector and install chaotic AUR and pacman configs.
- Package Management - List, install or manager your pacman database.
- System Cleanups - Orphans, cache and other cleanups.
- System Configuration - Easily access config files inside your root directory.
- User Management - simply add or, remove users to save time.
- Information Center - learn about your system!
- Troubleshooting - this script uninstaller and other quick fixes.

## Contribution
It's lightweight, no third party modules, and you can understand easily with just basic python knowledge! Feel free to send me merge request or, directory knock me!

Special thanks to,

[![PasqualeMuraca's Profilator](https://profilator.deno.dev/PasqualeMuraca?v=1.0.0.alpha.4)](https://github.com/PasqualeMuraca)

## Troubleshooting

### Both `.bashrc` and `.zshrc` exists?

If you're using both `bash` and `zsh` then, while Installation it'll ask you to set one (bash or zsh). You can set bash to import the alias in `bashrc` and later in the `.zshrc` you can source your `.bashrc` from your `.zshcrc` in this way,
```
source ~/.bashrc
```
or vice versa!

## License

[MIT](https://choosealicense.com/licenses/mit/) - feel free to fork, clone or send me a pull request!


## Acknowledgements

All thanks to [Md. Redwan Hossain](https://github.com/redwan-hossain/) for inspiring me. His tool to easily use pacman package manger, [lazypac](https://github.com/redwan-hossain/lazypac) really inspired me and gave a lot of ideas!


