import boto3
import pandas as pd

# Criar um client para interagir com o S3
s3_client = boto3.client('s3')

s3_client.download_file("datalake-thiago-igti-edc",
                        "data/Teste.csv",
                        "data/Teste.csv")

df = pd.read_csv("data/Teste.csv")
print(df)

s3_client.upload_file("data/Teste_upload.csv", #nome do arquivo original
                      "datalake-thiago-igti-edc", #bucket
                      "data/Teste_upload.csv") #nome do arquivo no destino