git add -A
git commit -m New
git push -u -f origin
#ssh 192.168.1.105 'rm -r -f ~/Minesweeper'
ssh 192.168.1.105 git fetch --all 
