# Week 7 (Outline)***:hurtrealbad::hurtrealbad:</br>
## 7.1 What you've learned so far  

        - Kafka, Kafka streams (Native), MQTT, Mobile sensors, Spark streaming (Micro-batch)

## 7.2 Spark Streaming (Continue from week 6)
        - Continue https://spark.apache.org/docs/latest/streaming-programming-guide.html  
        - RDD: (https://stackoverflow.com/a/36441528/)
        - https://sparkbyexamples.com/pyspark/different-ways-to-create-dataframe-in-pyspark/
        

## 7.3 Spark Machine Learning
        - Introduce MLlib
        - Example: Twitter sentiment analysis https://github.com/lakshay-arora/PySpark/tree/master/spark_streaming
        - Run this example "Week7-twitter.ipynb" on colab
        

## 7.4 Scikit-learn Multiflow (https://scikit-multiflow.github.io/)
        - Batch Learning VS Stream Learning
        - Concept drift
        - Decision tree
        - Evaluation
        - Paper: https://jmlr.org/papers/volume19/18-251/18-251.pdf
        
## Note
The modeling algorithms in Spark MLlib will only accept a vectorized column as input. This is done for reasons of efficiency and scaling. The vector assembler will express the features efficiently using techniques like spark vector, which allow a larger amount of data to be handled with less memory. This helps the modeling algorithms run efficiently even on large data columns.
https://towardsdatascience.com/your-first-apache-spark-ml-model-d2bb82b599dd
        
## TBD
https://melmeric.files.wordpress.com/2010/05/efficient-online-evaluation-of-big-data-stream-classifiers.pdf
