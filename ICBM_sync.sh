 git add -A
git commit -m New
git push -u -f origin

ssh 192.168.1.105 'rm -r -f tmp & git clone https://github.com/Raidfire-SDR/Minesweeper.git tmp & cp -f ~/tmp/*.* ~/Minesweeper/*.*'
