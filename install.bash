#!/bin/bash

#color
Green='\033[0;32m'        # Green
NC='\033[0m'              # No Color

install_script()
{
    curl https://raw.githubusercontent.com/SharafatKarim/archmate/main/amate.py > ~/amate.py
}

ask_to_set_manually()
{
echo "-----"
echo "You can run the Script like this way:"
echo -e "${Green}python ~/amate.py${NC} or, ${Green}python3 ~/amate.py${NC}"
echo -e "So your alias will be,${Green}"
echo -e 'alias amate="python $HOME/amate.py"'
echo -e "${NC}Please set an alias for your convenience! (recommended)"
echo -e "-----"
}

bashrc_alias()
{
echo 'alias amate="python $HOME/amate.py"' >> ~/.bashrc
echo -e "Alias set to - ${Green}.bashrc${NC}"
echo -e "Please restart your terminal,"
echo -e "and run, ${Green}amate${NC}"
}

zshrc_alias()
{
echo 'alias amate="python $HOME/amate.py"' >> ~/.zshrc
echo -e "Alias set to - ${Green}.zshrc${NC}"
echo -e "Please restart your terminal,"
echo -e "and run, ${Green}amate${NC}"
}

both_bash_zsh()
{
echo ""
while true; do
    read -p "Where do you want to set alias?(Bash or zsh) " bz
    case $bz in
        [Bb]* ) bashrc_alias; exit;;
        [Zz]* ) zshrc_alias; exit;;
        * ) echo -e "Please answer bash or zsh. Or, b or z is fine!";;
    esac
done
}

bashrc_search()
{
if [ -f ~/.bashrc ]
    then
        if [ -f ~/.zshrc ]
            then
                both_bash_zsh
            else
                bashrc_alias
        fi
    else
        if [ -f ~/.zshrc ]
            then
                zshrc_alias
            else
                ask_to_set_manually
        fi
fi
}

install_script
echo ""
echo -e "Script download - ${Green}Success${NC}"

echo ""
while true; do
    read -p "Do you want to set alias?(yes or no) " yn
    case $yn in
        [Yy]* ) bashrc_search; exit;;
        [Nn]* ) ask_to_set_manually; exit;;
        * ) echo -e "Please answer yes or no. Press y for yes or n for no. ";;
    esac
done
