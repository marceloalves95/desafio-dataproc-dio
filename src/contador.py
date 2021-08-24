from pyspark import SparkContext

if __name__ == "__main__":
    sc = SparkContext("local", "PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("gs://{SEU_BUCKET}/livro.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).sortBy(lambda a: a[1],
                                                                                          ascending=False)
    wordCounts.saveAsTextFile("gs://{SEU_BUCKET}/resultado")
