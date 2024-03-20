git add -A
git commit -m new
git push -f -u origin
ssh 192.168.1.105 './sync.sh'
