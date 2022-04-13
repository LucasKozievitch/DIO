import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("D:\Documentos\Cursos\DIO\BootCamp Cognizant Cloud Data Engineer #2\28 - Criando um Ecossistema Hadoop Totalmente Gerenciado com Google\dio-desafio-dataproc-main/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    wordCounts.saveAsTextFile("D:\Documentos\Cursos\DIO\BootCamp Cognizant Cloud Data Engineer #2\28 - Criando um Ecossistema Hadoop Totalmente Gerenciado com Google\dio-desafio-dataproc-main/resultado")