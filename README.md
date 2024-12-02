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

- case_id: ID of each visa application
- continent: Information of continent the employee
- education_of_employee: Information of education of the employee
- has_job_experience: Does the employee has any job experience? Y= Yes; N = No
- requires_job_training: Does the employee require any job training? Y = Yes; N = No
- no_of_employees: Number of employees in the employer's company
- yr_of_estab: Year in which the employer's company was established
- region_of_employment: Information of foreign worker's intended region of employment in the US.
- prevailing_wage: Average wage paid to similarly employed workers in a specific occupation in the area of intended employment. The purpose of the - prevailing wage is to ensure that the foreign worker is not underpaid compared to other workers offering the same or similar service in the same - area of employment.
- unit_of_wage: Unit of prevailing wage. Values include Hourly, Weekly, Monthly, and Yearly.
- full_time_position: Is the position of work full-time? Y = Full Time Position; N = Part Time Position
- case_status: Flag indicating if the Visa was certified or denied

## Modeling


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

# AWS CI/CD Deployment with GitHub Actions


## License
This project is licensed under the Apache License - see the LICENSE file for details.

