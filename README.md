<img src="https://github.com/LinhQuach13/readme_files/blob/master/NLP%20Project%20Predicting%20READMEs.gif">

#### Project Goals
> - The goal will be to build a model that can predict what programming language a repository is given the text of the README file.


#### Project Deliverables
> - A well-documented jupyter notebook that contains your analysis
> - One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.


#### Data Dictionary
    
- This is a data dictionary as a reference for the variables used within in the data set. 
![img](https://user-images.githubusercontent.com/80718476/127890072-0875c03d-713f-40c4-b387-9c0e9784ea96.png)




<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
<b>Findings:</b>

- It was difficult to find one main feature that would predict the language of the readme contents due to many words being similar between languages.

- Through exploration we were able to find correlation between a list of unique words with unique combinations to be able predict language of the readme contents.

- The reduction of noise by removing stop words significantly increased the accuracy score of our models.

- All models performed similarly with KNN had the highest accuracy score.

- When comparing train and validate datasets in all the models we see none of the models are overfit.

- KNN model is better than baseline but with more time we would continue to work with this model to improve the accuracy score by adjusting hyperparameters and adding more readme contents.

- The models we created were a Decision tree, KNNeighbors, and Naive Bayes. To reiterate the model we chose was the KNNeighbors as our best model with a 82.86% accuracy rate for predicting the programming language of readme contents from Github.

- The K-Nearest Neighbors Model (82.86%) outperformed our baseline score of 26.80 % thus it has value.

 
  
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Data Acquisition
> - Data Preparation
> - Exploration 
> - Modeling and Evaluation


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [x] Read this README.md
- [ ] Download data2.json file
- [ ] Download the aquire.py, prepare.py, explore.py and Final_notebook.ipynb files into your working directory
- [ ] Run the Final_notebook.ipynb notebook
