# Comentário para alterar o arquivo
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = {
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
}

# Ler os dados do enem 2020
enem = {
    spark
    .read
    .format("csv")
    .option("header",True)
    .option("inferSchema",True)
    .option("delimiter",";")
    .load("s3://datalake-thiago-186050745142/consumer-zone/enem/")
}

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("NU_ANO")
    .save("s3://datalake-thiago-186050745142/consumer-zone/enem/")
)