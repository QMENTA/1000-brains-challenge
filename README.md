# QMENTA 1000 Brains Challenge


<div class="row" style="box-sizing: border-box">
  <div style="float:left; width=50%; padding=20px">
    <img src="assets/hackaton_salud_logo.png" alt="Hackaton Salud" style="width: 100%">
  </div>
  <div style="float:left; width=50%; padding=20px">
    <img src="assets/qmenta_logo.png"" alt="QMENTA" style="width: 100%">
  </div>
</div>

### Goal

The 1000 Brains Challenge participants will have to predict the age of healthy individuals based on structural Magnetic Resonance images of their brains.

_Bonus_

Among the healthy subjects there is subset of patients diagnosed with Alzheimer's Disease, but these are not labeled. The bonus goal consists in identifying those subjects with Alzheimer's Disease in the database in an unsupervised manner.

### Evaluation

_WORK IN PROGRESS_

### Resources

- **Database**: 1000 healthy individuals with T1-weighted Magnetic Resonance images and their associated age in years.

<img src="assets/t1_w.jpg" alt="T1-Weighted" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

- **Volumetric and Morphometric analyses**: all the T1-weighted images have been processed with a standard volumetric and morphometric analysis tool available in the QMENTA platform.

<img src="assets/vol_morph_analysis.png" alt="Volumetric and Morphometric Analysis" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

- **Getting started material**: this GitHub repository contains introductory Jupyter notebooks to get started with the QMENTA Python client, training a simple regression model and packaging your predictive model in a Docker image with the QMENTA SDK.

<img src="assets/getting_started.png" alt="Getting started material" style="display: block; margin-left: auto; margin-right: auto; width: 50%">

### Preparing the Python environment

_NOTE_: _The Jupyter notebooks in this repository have been written and tested with **Python 3.6**. 
**Python 2.7** support is not guaranteed._

At QMENTA we extensively use Conda for managing Python packages and environments. It is specially useful because it allows having different environments with different Python versions without needing to change to another environment management system. 

After [installing Miniconda for your platform](https://conda.io/docs/user-guide/install/index.html) (Windows, macOS or Linux), you can create a replica of the environment used to create these notebooks by executing the following commands:
```s
user@hostname $ conda create env -f environment.yml
```

When the environment creation process finishes you can activate your environment in order to run Jupyter Lab and inspect the provided code:
```s
user@hostname $ conda activate qmenta_1000_brains
user@hostname $ jupyter lab
```

### Contents

File | Description
---- | -------------
1.qmenta_client_download_data.ipynb | How to download large amounts of data from the QMENTA platform using the QMENTA client. 
2.train_simple_regression_model.ipynb | Example Scikit-Learn regression model trained on the 1000 brains volumetric data.
3.create_tool_qmenta_sdk.ipynb | Create a model artifact to use for inference, create a tool with the QMENTA SDK and package it in a Docker container image. 
Dockerfile | Set of instructions interpreted by the Docker Engine that specify how the Docker image is built.
