#  Regular expressions work as well. This conditional looks
#  at $2 for approximate matches to the letter p followed by
#  any number of (one or more) characters, which are in turn
#  followed by the letter p:

awk '$2 ~ /p.+p/ {print $0}' colours.txt

#  Numbers are interpreted naturally by awk. For instance,
#  to print any row with a third column containing an integer
#  greater than 8:

awk '$3>8 {print $1, $2}' colours.txt
