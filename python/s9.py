# WordClouds
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Open the text file
with open('wordcloud.txt', 'r') as f:
    text = f.read()

# Generate the word cloud
wordcloud = WordCloud().generate(text)

# Display the word cloud
"""
supported values are 'none', 'sinc', 'blackman', 'antialiased', 'nearest', 'bicubic', 'quadric', 'spline36', 'bessel', 
'bilinear', 'spline16', 'hermite', 'catrom', 'mitchell', 'gaussian', 'lanczos', 'kaiser', 'hamming', 'hanning'
"""
plt.imshow(wordcloud, interpolation='mitchell')
plt.axis("off")
plt.show()