# awk [options] 'pattern {action}' file

# Printing a column
awk '{print $1}' colours.txt

# Conditionally selecting columns
awk '$2=="purple"{print $1}' colours.txt

