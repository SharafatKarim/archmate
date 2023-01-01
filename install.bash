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
echo "Please set an alias for your shell!"
echo "You can run the Script like this way:"
echo -e "${Green}python ~/amate.py${NC} or, ${Green}python3 ~/amate.py${NC}"
echo -e "So your alias will be,${Green}"
echo -e 'alias amate="python $HOME/amate.py"'
echo -e "${NC}-----"
}

bashrc_search()
{
if [ -f ~/.bashrc ]
    then
        if [ -f ~/.zshrc ]
            then
                echo "bash + zsh"
            else
                echo 'alias amate="python $HOME/amate.py"' >> ~/.bashrc
        fi
    else
        if [ -f ~/.zshrc ]
            then
                echo 'alias amate="python $HOME/amate.py"' >> ~/.zshrc
                echo -e "Alias set to - ${Green}.zshrc${NC}"
                echo -e "Please restart your terminal,"
                echo -e "and run, ${Green}amate${NC}"
            else
                ask_to_set_manually
        fi
fi
}

install_script
echo -e "Script download - ${Green}Success${NC}"
bashrc_search

