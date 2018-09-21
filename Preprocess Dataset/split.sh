#!/bin/bash
cd images/
array="Abyssinian:1 Bengal:2 Birman:3 Bombay:4 British_shorthair:5 Egyptian_mau:6 Maine_coon:7 Persian:8 Ragdoll:9 Russian_blue:10 Siamese:11 Sphynx:12 Burmese:13 Manx:14"

oldIFS=$IFS
IFS=' '
for data in $array
do
    i=1
    name=`echo $data | awk -F":" '{print $1}'`
    category=`echo $data | awk -F":" '{print $2}'`
    ls $name* | while read file
    do
        line=`echo $file | awk -v awk_catg=$category -F"." '{print $1" "awk_catg}'`
        if [ $(( $i % 10 )) -le 7 ];
        then 
            echo $line >> ../train.txt
            
        else
            echo $line >> ../val.txt
        fi

        i=$(($i+1))    
    done
done
IFS=$oldIFS

