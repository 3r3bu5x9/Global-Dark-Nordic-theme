#!/bin/bash

# options to be displayed
option0="screen"
option1="area"
option2="window"

# options to be displyed
options="$option0\n$option1\n$option2"

selected="$(echo -e "$options" | rofi -lines 3 -dmenu -p "scrot")"
case $selected in
    $option0)
        cd ~/Pictures/scrots/ && sleep 1 && scrot -q 100;;
    $option1)
        cd ~/Pictures/scrots/ && scrot -s -q 100;;
    $option2)
        cd ~/Pictures/scrots/ && sleep 1 && scrot -u -q 100;;
esac
