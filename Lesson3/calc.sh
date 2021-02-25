#!/bin/bash
Help()
{
	echo "write: a b -"
}
while getopts ":h" option; do
   case $option in
      h) # display Help
         Help
         exit;;
   esac
done
a=$1
b=$2
c=$3
if [[ $c == '+' ]]
then
	echo $(($a+$b))
elif [[ $c == '-' ]]
then
	echo $(($a-$b))
elif [[ $c == '/' ]]
then
        echo $(($a/$b))
elif [[ $c == '.' ]]
then
        echo $(( $a * $b ))
fi
