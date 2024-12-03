from us_visa.cloud_storage.aws_storage import AWSOperation
from us_visa.exception import CustomException
from us_visa.logger import logging
import sys

def deploy_to_ecr():
    try:
        aws_op = AWSOperation()
        # Create repository
        aws_op.create_ecr_repository('visarepo')
        # Get login token
        token = aws_op.get_ecr_login()
        # Add your deployment logic here
    except Exception as e:
        raise CustomException(e, sys) 