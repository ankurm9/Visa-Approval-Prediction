# US Visa Approval Prediction Using MLOps

This project aims to predict the approval of US visa applications using machine learning and deploy the model using MLOps practices. The MLOps pipeline ensures seamless development, deployment, and monitoring of the machine learning model, ensuring continuous integration and delivery (CI/CD) for robust and scalable production-ready models.

## Table of Contents

- Project Overview
- Workflow
- Technologies Used
- Data
- Installation
- Usage
- Results
- License

## Project Overview

Visa approval is a critical process that involves several factors. This project applies machine learning models to predict the approval of US visa applications based on applicant information. Using MLOps, we automate model training, deployment, monitoring, and retraining to streamline and enhance the prediction process.

## Workflow:

1. constants
2. entity
3. components
4. pipeline
5. Main file

## Technologies Used:

- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- Flowchart: https://whimsical.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login

## Data
Download the dataset from [here](https://www.kaggle.com/datasets/moro23/easyvisa-dataset).

The data contains the different attributes of the employee and the employer. The detailed data dictionary is given below.

- <span style="color:blue">case_id:</span> ID of each visa application
- <span style="color:blue">continent:</span> Information of continent the employee
- <span style="color:blue">education_of_employee:</span> Information of education of the employee
- <span style="color:blue">has_job_experience:</span> Does the employee has any job experience? Y= Yes; N = No
- <span style="color:blue">requires_job_training:</span> Does the employee require any job training? Y = Yes; N = No
- <span style="color:blue">no_of_employees:</span> Number of employees in the employer's company
- <span style="color:blue">yr_of_estab:</span> Year in which the employer's company was established
- <span style="color:blue">region_of_employment:</span> Information of foreign worker's intended region of employment in the US.
- <span style="color:blue">prevailing_wage:</span> Average wage paid to similarly employed workers in a specific occupation in the area of intended employment. The purpose of the prevailing wage is to ensure that the foreign worker is not underpaid compared to other workers offering the same or similar service in the same area of employment.
- <span style="color:blue">unit_of_wage:</span> Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly.
- <span style="color:blue">full_time_position:</span> Is the position of work full-time? Y = Full Time Position; N = Part Time Position
- <span style="color:blue">case_status:</span> Flag indicating if the Visa was certified or denied

## Modeling
<span style="color:red">case_id:</span> 

## Evaluation Metrics:



## Setup
1. Clone the repository:

    ```bash
    git clone https://github.com/YourUsername/visa-approval-mlops.git
    ```
    ```bash
    cd visa-approval-mlops
    ```

2. Create a virtual environment and activate it:

    ``` bash
    conda create -n visa-approval python=3.8
    ```
    ```bash
    conda activate visa-approval
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up DVC for data versioning:

    dvc init
    dvc remote add -d myremote <remote-url>
    dvc pull

5. Set up MLflow for experiment tracking:

    mlflow ui

6. Start the local Flask or FastAPI server for deployment:

    python app.py

## Usage
1. To train the model:

    ```bash
    python train.py
    ```

2. To test the model locally:

    ```bash
    python test.py
    ```

3. To deploy the model (Docker):

    ```bash
    docker build -t visa-approval-app .
    ```
    ```bash
    docker run -p 5000:5000 visa-approval-app
    ```

4. To monitor the model in production, visit the Prometheus or Grafana dashboards set up in your cloud infrastructure.

## Results



## License
This project is licensed under the Apache License - see the LICENSE file for details.

