import matplotlib.pyplot as plt
import pandas as pd
x=pd.read_csv('dataset_hate_speech.csv')
plt.pie(x['class'].value_counts().values, # type: ignore
       labels=x['class'].value_counts().index, # type: ignore
       autopct="%3f%%")
plt.show()
