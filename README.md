# Information-Retrieval 2022-2023

A web-based search engine of the Greek Parliament proceedings that runs locally, developed with Python, Flask and HTML. This is a project for the Information Retrieval course @ AUTh 

<p align="center">
  <img src="report\demo.gif" alt="animated" />
</p>

## Installation
In order to run the app you need to run to install all the necessary modules
```
pip install -r requirements.txt
```

## Run
The app runs from the **app.py** file
```
python app.py
```
When it is ready go to: http://127.0.0.1:5000/

## Important Notes
In order to run the app you need to **change the .csv file** in the initialize.py.
```
Data_temp = pd.read_csv('Greek_Parliament_Proceedings_1989_2020_DataSample.csv')
```
The original file (Greek_Parliament_Proceedings_1989_2020.csv) cannot be uploaded in github due to its size. You can get the file from https://github.com/iMEdD-Lab/Greek_Parliament_Proceedings
