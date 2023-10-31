# pip install demoji

# Convert emoji into text

import demoji

text = "🍎👩‍🦰💩🌭🇧🇷"

foo = demoji.findall(text)

print(foo)