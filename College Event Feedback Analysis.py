!pip install textblob wordcloud seaborn

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from google.colab import files

# Upload the CSV file
uploaded = files.upload()

# Read it
import io
df = pd.read_csv(io.BytesIO(uploaded[list(uploaded.keys())[0]]), encoding='cp1252')


# Display first few rows
df.head()
