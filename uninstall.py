import os

# system's username grab
user = os.getenv('USER')

# if ~/amate.py exists, it'll delete it
if os.path.isfile(f'/home/{user}/amate.py'):
    os.system(f"rm ~/amate.py")

# zshrc alias remove
with open(f'/home/{user}/.zshrc','r') as f:
    with open(f'/home/{user}/.zshrccopy','w') as w:
        for i in f:
            if i == 'alias amate="python $HOME/amate.py"\n':
                continue
            w.write(i)
os.system("mv ~/.zshrccopy ~/.zshrc")

# bashrc alias remove
with open(f'/home/{user}/.bashrc','r') as f:
    with open(f'/home/{user}/.bashrccopy','w') as w:
        for i in f:
            if i == 'alias amate="python $HOME/amate.py"\n':
                continue
            w.write(i)
os.system("mv ~/.bashrccopy ~/.bashrc")

# exit
exit()
