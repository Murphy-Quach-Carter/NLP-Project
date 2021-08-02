import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def show_counts_and_ratios(df, column):
    """
    Takes in a dataframe and a string of a single column
    Returns a dataframe with absolute value counts and percentage value counts
    """
    labels = pd.concat([df[column].value_counts(),
                    df[column].value_counts(normalize=True)], axis=1)
    labels.columns = ['n', 'percent']
    labels
    return labels


def show_scatter_plot(df, x, y, hue=None):
    '''
    Shows scatter plot for 2 given points
    '''
    plt.figure(figsize=(12,6))
    plt.title("{} vs {}".format(x,y))
    sns.scatterplot(data=df, x=df[x], y=df[y], hue=hue)
    plt.show()
    

def show_distributions(word_table, orderby='All'):
    plt.rc('figure', figsize=(12,6))
    (word_table
 .assign(java = word_table.java / word_table['All'],
         javascript =word_table.javascript/ word_table['All'],
         r = word_table.r / word_table['All'],
         python =word_table.python / word_table['All'])
 .sort_values(by='All')
 [['java', 'javascript','r','python']]
 .tail(20)
 .sort_values(orderby)
 .plot.barh(stacked=True))
    

#function to create word clouds
def word_cloud(word_string, name):
    from wordcloud import WordCloud
    img = WordCloud(background_color='white', width=800, height=600).generate(word_string)
    print('-------------------')
    print(f'{name}')
    print('-------------------')
    plt.imshow(img)
    plt.axis('off')
    
    
def df_to_wordcloud(df, language = None):
    if language: 
        df = df[df.language_cleaned == language]
    else:
        language = 'all_language'
    to_list = ''
    for readme in df.readme_contents_cleaned:
        to_list += readme
    word_cloud(to_list,language)
    
    
def bigrams_wordclouds(thelist):
    data = {k[0] + ' ' + k[1]: v for k, v in thelist.to_dict().items()}
    img = WordCloud(background_color='white', width=800, height=400).generate_from_frequencies(data)
    plt.figure(figsize=(8,4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def trigrams_wordclouds(thelist):
    data = {k[0] + ' ' + k[1] + ' '+ k[2]: v for k, v in thelist.to_dict().items()}
    img = WordCloud(background_color='white', width=800, height=400).generate_from_frequencies(data)
    plt.figure(figsize=(8,4))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
