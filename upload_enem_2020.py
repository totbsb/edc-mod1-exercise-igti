import boto3
import pandas as pd
#import pprint
#from botocore.exceptions import ClientError

# Criar um client para interagir com o S3
s3_client = boto3.client('s3')

# s3_client.download_file("datalake-thiago-igti-edc",
#                         "data/Teste.csv",
#                         "data/Teste.csv")

# df = pd.read_csv("data/Teste.csv")
# print(df)


# def create_bucket(bucket_name, region):
#     try:
#         s3_client = boto3.client('s3', region_name=region)
#         location = {'LocationConstraint': region}
#         pprint.pprint(s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)) #Usamos o pprint para uma saída mais amigável do resultado.
#     except ClientError as e:
#         print(e)

# create_bucket("datalake-thiago-186050745142", "us-east-1")

s3_client.upload_file("data/MICRODADOS_ENEM_2020.csv", #nome do arquivo original
                      "datalake-thiago-186050745142", #bucket
                      "data/MICRODADOS_ENEM_2020.csv") #nome do arquivo no destino

df = pd.read_csv("data/MICRODADOS_ENEM_2020.csv")
print(df)                      