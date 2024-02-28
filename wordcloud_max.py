from wordcloud import WordCloud
import pandas as pd 
import matplotlib.pyplot as plt
def plotting(data,typ):
    
    tweet_corp=" ".join(data['tweet'])
    plt.figure(figsize=(10,10))
    wc=WordCloud(max_words=100,width=200,height=100,collocations=False).generate(tweet_corp)
    plt.title(f'Wordcloud for {typ} tweet',fontsize=15)
    plt.axis('off')
    plt.imshow(wc)
    plt.show()
    print()


df=pd.read_csv('dataset_hate_speech.csv')
plotting(df[df['class']==1],"neither")