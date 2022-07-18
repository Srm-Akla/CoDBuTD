#!/usr/bin/bash

v4l2-ctl --list-devices | grep -A 2 "Pure" | awk -F '/' 'FNR == 2 {print $3}'
