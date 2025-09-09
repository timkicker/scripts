#!/bin/bash

# Get the name of the active monitor (connected output)
active_monitor=$(xrandr --listmonitors | grep "+" | awk '{print $4}')

# Get the name of the disconnected output(s)
disconnected_monitors=$(xrandr | grep "disconnected" | awk '{print $1}')

# Iterate over each disconnected monitor
for disconnected in $disconnected_monitors; do
    # Find workspaces on the disconnected display and move them to the active monitor
    for ws in $(i3-msg -t get_workspaces | jq -r --arg disconnected "$disconnected" '.[] | select(.output == $disconnected) | .name'); do
        i3-msg workspace $ws
        i3-msg move workspace to output $active_monitor
    done
done

