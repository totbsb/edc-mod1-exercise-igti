# HCL - Hashicorp Configuration Languagem
# Linguagem declarativa

resource "aws_s3_bucket" "datalake" {
  # parametros de configuração do recurso disponível
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}" #datalake-thiago-igti-edc-tf
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    IES   = "IGTI"
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_object" "codigo_spark" {
  # id é um parâmetro do recurso criado, vendo a documentação
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl    = "private"
  source = "../job_spark.py"
  etag   = filemd5("../job_spark.py")
}

provider "aws" {
  region = "us-east-1"
}