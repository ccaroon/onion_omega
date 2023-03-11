DIR=$(dirname $0)
# echo $DIR
nohup micropython $DIR/../main.py >> $DIR/../ws-panel.log &
