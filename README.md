<img src="https://github.com/LinhQuach13/readme_files/blob/master/NLP%20Project%20Predicting%20READMEs.gif">

#### Project Goals
> - The goal will be to build a model that can predict what programming language a repository is given the text of the README file.


#### Project Deliverables
> - A well-documented jupyter notebook that contains your analysis
> - One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.


#### Data Dictionary
    
- This is a data dictionary as a reference for the variables used within in the data set. 



![img](https://user-images.githubusercontent.com/80718476/127921008-719bd63c-4afd-4ded-a3fc-79fae5b1f735.png)





<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>
<b>Findings:</b>

- It was difficult to find one main feature that would predict the language of the readme contents due to many words being similar between languages.

- Through exploration we were able to find correlation between a list of unique words with unique combinations to be able predict language of the readme contents.

- All of our models were overfit to some degree with the exception of our KNN model.

- The models we created were a Decision tree, KNNeighbors, Logistic Regression, Random Forest, Linear SVC and Naive Bayes. The model we chose as our best model for the test dataset was the KNNeighbors model with a 83% accuracy rate for predicting the programming language of readme contents from Github.

- The K-Nearest Neighbors Model (83%) outperformed our baseline score of 27 % thus it has value.

- With more time we would continue to work with our models to improve the accuracy score by adjusting hyperparameters and adding more data by adding more readme contents from github.

 
  
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
