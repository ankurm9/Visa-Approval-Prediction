# US Visa Approval Prediction Using MLOps

This project aims to predict the approval of US visa applications using machine learning and deploy the model using MLOps practices. The MLOps pipeline ensures seamless development, deployment, and monitoring of the machine learning model, ensuring continuous integration and delivery (CI/CD) for robust and scalable production-ready models.

## Table of Contents
Project Overview
Features
Technologies Used
Data
Modeling
MLOps Workflow
Installation
Usage
Results
Contributing
License

## Project Overview
Visa approval is a critical process that involves several factors. This project applies machine learning models to predict the approval of US visa applications based on applicant information. Using MLOps, we automate model training, deployment, monitoring, and retraining to streamline and enhance the prediction process.

## The project workflow includes:

Data ingestion and preprocessing.
Feature selection and engineering.
Model training and evaluation.
Model deployment using CI/CD pipelines.
Monitoring model performance in production.
Automated retraining based on feedback and data drift.
Features
Automated data ingestion and preprocessing pipeline.
Continuous integration with automated model testing and validation.
Containerized model deployment using Docker.
Real-time monitoring of model performance (accuracy, drift, etc.).
Automated retraining when performance drops below a threshold.
Version control for datasets and models.
Technologies Used
Machine Learning: scikit-learn, XGBoost
MLOps: MLflow, DVC, Docker, Kubernetes
Deployment: Flask, FastAPI, AWS EC2/S3, or Google Cloud
CI/CD: GitHub Actions, Jenkins, or CircleCI
Monitoring: Prometheus, Grafana, or Seldon Core
Version Control: Git, DVC (Data Version Control)
Containerization: Docker
Orchestration: Kubernetes

## Data
The dataset used for this project includes various features related to visa applicants, such as:

Applicant's country of origin
Job classification
Wage information
Employer details
Visa category
The dataset can be found here or any other visa-related dataset that fits the project.

## Modeling
The machine learning models used in the project include:

Logistic Regression
Decision Trees
Random Forest
XGBoost
The best model is selected based on cross-validation performance, and hyperparameter tuning is performed using GridSearchCV.

## Evaluation Metrics:
Accuracy
Precision, Recall, F1-score
ROC-AUC score
MLOps Workflow
Data Ingestion: Automatically pull the latest data from a source (e.g., database or API).
Data Preprocessing: Clean and preprocess the data using a scheduled pipeline.
Model Training: Automated training pipeline, including hyperparameter tuning.
Versioning: Use DVC for dataset and model versioning.
Containerization: The model is containerized using Docker for easy deployment.
Deployment: Deployed on cloud infrastructure (e.g., AWS/GCP) using Kubernetes for scaling.
Monitoring: Real-time monitoring with Prometheus and Grafana to track performance metrics.
Retraining: Automatically trigger retraining pipelines if model performance degrades.
Installation
Prerequisites
Python 3.8+
Conda/Miniconda (Optional)
Docker
Git
DVC
MLflow
## Setup
1. Clone the repository:

git clone https://github.com/YourUsername/visa-approval-mlops.git
cd visa-approval-mlops

2. Create a virtual environment and activate it:

conda create -n visa-approval python=3.8
conda activate visa-approval

3. Install the dependencies:

bash
Copy code
pip install -r requirements.txt

4. Set up DVC for data versioning:

dvc init
dvc remote add -d myremote <remote-url>
dvc pull

5. Set up MLflow for experiment tracking:

mlflow ui

6. Start the local Flask or FastAPI server for deployment:

python app.py

#### Usage
1. To train the model:

python train.py

2. To test the model locally:

python test.py

3. To deploy the model (Docker):

docker build -t visa-approval-app .
docker run -p 5000:5000 visa-approval-app

4. To monitor the model in production, visit the Prometheus or Grafana dashboards set up in your cloud infrastructure.

## Results
The best-performing model was XGBoost, which achieved an accuracy of 90%, with a recall of 88% and an AUC-ROC score of 0.92. These results demonstrate the ability of the model to predict visa approval outcomes based on applicant data.

## Contributing
We welcome contributions! If you would like to contribute to the project, please follow these steps:

Fork the repository.
Create a new feature branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add a new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

## License
This project is licensed under the Apache License - see the LICENSE file for details.

