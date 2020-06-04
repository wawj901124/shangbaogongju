#!/bin/sh 
echo "############ Welcome to wanwei-tech  ############"
echo "############ Version: 2014-05-08(WQ) ############"

if [ $# -ne 1 ];
then
    echo "Usage: $0 protocol_name"
    exit -1
fi 

echo "===>step 0. killall main and his children!"
# get ID of main 
ID=`ps | grep main | grep -v "grep" | awk '{print $1}'`
echo "main(ID): $ID" 

pstree -p $ID > tree.txt 
egrep -o '\([[:digit:]]+\)' tree.txt | while read LINE

do 
	ID=`echo $LINE  | tr -d '\(' | tr -d '\)'`
	echo "ID: $ID"
	kill -9 $ID
done 

rm tree.txt 

echo "===>step 1. up main again................."

export RUNMODE=standalone

cd /usr/app_install/main/bin
./main&

sleep 10
killall $1



