#  Awk can treat the data in exactly the same way, as long as
#  you specify which character it should use as the field separa-
#  tor in your command. Use the --field-separator (or just -F for
#  short) option to define the delimiter:

awk -F',' '$2=="yellow" {print $1}' colours.csv