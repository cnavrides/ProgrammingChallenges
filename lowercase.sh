#!/bin/bash

for file in *
do
    lowercase=`echo $file | tr '[A-Z]*' '[a-z]*'`
    echo $lowercase
#    mv "$file" "$lowercase"
done
