#!/bin/bash


git log -n 1 -- -- bst.c
sed s/\$Log/"\$Log `cat .gitlognolines`"/g test
sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g' .gitlog > .gitlognolines

