# QMENTA 1000 Brains Challenge 2018

<img src="assets/qmenta_logo.png" alt="QMENTA" style="width: 50%">

----------------

This challenge is presented in the context of the **Hackathon Nacional de Salud 2018** happening the **15th and 16th June** in the **Centro Nacional de Investigaciones Cardiovasculares (CNIC), Madrid.** 

<div style="width: 100%; overflow: hidden;">
  <div style="float: left; width: 45%; padding: 20px">
    <img src="assets/hackaton_salud_logo.png" alt="Hackaton Salud" style="width: 100%">
  </div>
  <div style="float: left; width: 45%;">
    
  </div>
</div>

## Goal

In the 1000 Brains Challenge, participants will have to **predict the age** of healthy individuals based on **structural Magnetic Resonance images** of their **brains**.

_Bonus_

Among the healthy subjects there is a subset of patients diagnosed with Alzheimer's Disease, but these are not labeled. The bonus goal consists in identifying those subjects with Alzheimer's Disease in the database in an unsupervised manner.

## Evaluation

A team will be considered eligible for evaluation if the following conditions are met:

- A CSV with the predicted ages for the **test** set is produced, named *TeamID_age_predictions.csv*, where *TeamID* is a unique identifier of each team participating in the challenge. It should have the following structure:

SubjectID | Predicted Age
--------- | -------------
28751 | 95
29003 | 12
(...) | (...)
33828 | 57

- An SDK tool is produced and deployed to the QMENTA platform, following the guidelines and recommendations shown in this repository.

- The tool is shown to run and finish succesfully in the QMENTA platform, giving a prediction of the age for at least 2 test subjects.

*Bonus objective: Unsupervised AD detection*

If your team has prepared an unsupervised model that identifies the subjects in the database (both in **train** and **test** set), you will have to provide a CSV file in which, for each subject, you indicate with a boolean variable if such subject has AD or not. The structure should be the following:

SubjectID | AD
--------- | --
28329 | True
28330 | False
28338 | False
(...) |
34119 | True
34123 | False

Among all elligible entries the winner will be chosen according to the following criteria:
- Technical presentation
- Methodology
- [Mean Squared Error](http://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error) of the predictions of the test data 
- (Bonus objective) [F1-score](http://scikit-learn.org/stable/modules/model_evaluation.html#precision-recall-f-measure-metrics) of the AD classification model.

## Resources

- **Database**: 1000 healthy individuals with T1-weighted Magnetic Resonance images and their associated age in years.

<img src="assets/t1_w.jpg" alt="T1-Weighted" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

- **Volumetric and Morphometric analyses**: all the T1-weighted images have been processed with a standard volumetric and morphometric analysis tool available in the QMENTA platform.

<img src="assets/vol_morph_analysis.png" alt="Volumetric and Morphometric Analysis" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

- **Getting started material**: this GitHub repository contains introductory Jupyter notebooks to get started with the QMENTA Python client, training a simple regression model and packaging your predictive model in a Docker image with the QMENTA SDK.

<img src="assets/getting_started.png" alt="Getting started material" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

## Preparing the Python environment

_NOTE_: _The Jupyter notebooks in this repository have been written and tested with **Python 2.7**. 
Our libraries will soon support the latest versions of Python, however their compatibility is not guaranteed as of now._

At QMENTA we extensively use Conda for managing Python packages and environments. It is especially useful because it allows having different environments with different Python versions without needing to change to another environment management system. 

After [installing Miniconda for your platform](https://conda.io/docs/user-guide/install/index.html) (Windows, macOS or Linux), you can create a replica of the environment used to create these notebooks by executing the following commands:
```s
conda create env -f environment.yml
```

When the environment creation process finishes you can activate your environment in order to run Jupyter Lab and inspect the provided code:
```s
conda activate qmenta_1000_brains
jupyter lab
```

## Contents of the repository

File | Description
---- | -------------
1.qmenta_client_download_data.ipynb | How to download large amounts of data from the QMENTA platform using the QMENTA client. 
2.train_simple_regression_model.ipynb | Example Scikit-Learn regression model trained on the 1000 brains volumetric data.
3.create_tool_qmenta_sdk.ipynb | Create a model artifact to use for inference, create a tool with the QMENTA SDK and package it in a Docker container image. 
Dockerfile | Set of instructions interpreted by the Docker Engine that specify how the Docker image is built.
environment.yml | Conda environment file
predict_age.py | Python script that implements the age prediction tool using the QMENTA SDK
predict_age_settings.json | Settings specification in JSON format that has to be introduced when registering the tool in the QMENTA platform
