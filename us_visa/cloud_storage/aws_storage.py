import os
import sys
from us_visa.exception import CustomException
from us_visa.logger import logging
import boto3

class AWSOperation:
    def __init__(self):
        self.client = boto3.client('ecr')
    
    def create_ecr_repository(self, repository_name: str):
        try:
            response = self.client.create_repository(
                repositoryName=repository_name
            )
            logging.info(f"Successfully created ECR repository: {repository_name}")
            return response
        except Exception as e:
            raise CustomException(e, sys)
    
    def get_ecr_login(self):
        try:
            token = self.client.get_authorization_token()
            logging.info("Successfully retrieved ECR authorization token")
            return token
        except Exception as e:
            raise CustomException(e, sys)