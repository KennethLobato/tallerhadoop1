# Taller Hadoop 1
***

Download the code from this repository:
```Bash
git clone https://github.com/KennethLobato/tallerhadoop1.git
```

Launch vagrant:
```Bash
vagrant up
```

Wait for vagrant to finish the setup of this small cluster, and connect to both machines "ubuntu1" and "ubuntu2" in two separate command shells:
```Bash
vagrant ssh ubuntu1
```
```Bash
vagrant ssh ubuntu2
```

Verify that the /etc/hosts has the following information (otherwise edit it with vim or nano):
```Bash
vagrant@ubuntu1:~$ cat /etc/hosts
127.0.0.1 localhost

10.0.0.10 ubuntu1.tallerhadoop1.org ubuntu1
10.0.0.11 ubuntu2.tallerhadoop1.org ubuntu2
```

Connect to the following machines with SSH to accept their fingerprint:
```Bash
vagrant@ubuntu1:~$ ssh ubuntu1
vagrant@ubuntu1:~$ ssh ubuntu2
vagrant@ubuntu1:~$ ssh localhost
vagrant@ubuntu1:~$ ssh 0.0.0.0
```

Ask to format the HDFS's NameNode:
```Bash
vagrant@ubuntu1:~$ hdfs namenode -format
```

Start the HDFS:
```Bash
vagrant@ubuntu1:~$ cd /usr/local/hadoop/
vagrant@ubuntu1:~$ ./sbin/start-dfs.sh
```
Verify that the namenode, datanode and snamenode are started properly:
```Bash
vagrant@ubuntu1:/usr/local/hadoop$ jps
4260 SecondaryNameNode
4039 DataNode
4376 Jps
3852 NameNode
```

```Bash
vagrant@ubuntu2:~$ jps
3625 Jps
3550 DataNode
```

Create the folders /user/vagrant in the HDFS:
```Bash
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -mkdir -p /user/vagrant/
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /
Found 1 items
drwxr-xr-x   - vagrant supergroup          0 2016-10-12 17:02 /user
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /user/
Found 1 items
drwxr-xr-x   - vagrant supergroup          0 2016-10-12 17:02 /user/vagrant
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /user/vagrant/
```

Start YARN Resource Manager:
```Bash
vagrant@ubuntu1:/usr/local/hadoop$ ./sbin/start-yarn.sh
starting yarn daemons
starting resourcemanager, logging to /usr/local/hadoop-2.7.3/logs/yarn-vagrant-resourcemanager-ubuntu1.out
ubuntu2: starting nodemanager, logging to /usr/local/hadoop-2.7.3/logs/yarn-vagrant-nodemanager-ubuntu2.out
ubuntu1: starting nodemanager, logging to /usr/local/hadoop-2.7.3/logs/yarn-vagrant-nodemanager-ubuntu1.out
```
Verify that the following processes are running (ResourceManager and NodeManager):
```Bash
vagrant@ubuntu1:/usr/local/hadoop$ jps
4592 ResourceManager
4756 NodeManager
4260 SecondaryNameNode
4039 DataNode
5049 Jps
3852 NameNode
```
```Bash
vagrant@ubuntu2:~$ jps
3729 NodeManager
3833 Jps
3550 DataNode
```

## Exercise 1
Introduce NCDC samples in the HDFS:
```Bash
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -put /vagrant/inputfiles/ncdc/sample/ /user/vagrant/ncdc-input
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /user/vagrant/ncdc-input/
Found 10 items
-rw-r--r--   2 vagrant supergroup     148476 2016-10-12 17:09 /user/vagrant/ncdc-input/1901
-rw-r--r--   2 vagrant supergroup     148113 2016-10-12 17:09 /user/vagrant/ncdc-input/1902
-rw-r--r--   2 vagrant supergroup     146745 2016-10-12 17:09 /user/vagrant/ncdc-input/1903
-rw-r--r--   2 vagrant supergroup     148533 2016-10-12 17:09 /user/vagrant/ncdc-input/1904
-rw-r--r--   2 vagrant supergroup     147651 2016-10-12 17:09 /user/vagrant/ncdc-input/1905
-rw-r--r--   2 vagrant supergroup     148659 2016-10-12 17:09 /user/vagrant/ncdc-input/1906
-rw-r--r--   2 vagrant supergroup     148733 2016-10-12 17:09 /user/vagrant/ncdc-input/1907
-rw-r--r--   2 vagrant supergroup     148846 2016-10-12 17:09 /user/vagrant/ncdc-input/1908
-rw-r--r--   2 vagrant supergroup     148727 2016-10-12 17:09 /user/vagrant/ncdc-input/1909
-rw-r--r--   2 vagrant supergroup     148288 2016-10-12 17:09 /user/vagrant/ncdc-input/1910
```

Out of the machines ubuntu1 and/or ubuntu2, compile and generate the JAR for the introductory MapReduce Intro:
```
$ cd src/java/mapreduce-intro
$ mvn compile
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building MapReduceIntro 1.0
[INFO] ------------------------------------------------------------------------
[INFO]
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 2.311 s
[INFO] Finished at: 2016-10-12T19:11:58+02:00
[INFO] Final Memory: 22M/277M
[INFO] ------------------------------------------------------------------------

$ mvn package
[INFO] Scanning for projects...
[INFO]                                                                         
[INFO] ------------------------------------------------------------------------
[INFO] Building MapReduceIntro 1.0
[INFO] ------------------------------------------------------------------------
(...)
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1.760 s
[INFO] Finished at: 2016-10-12T19:12:06+02:00
[INFO] Final Memory: 16M/309M
[INFO] ------------------------------------------------------------------------
```

Launch the MapReduce Intro in the cluster:
```
vagrant@ubuntu1:/usr/local/hadoop$ hadoop jar /vagrant/src/java/mapreduce-intro/target/mapreduce-intro-1.0.jar \
  MaxTemperature /user/vagrant/ncdc-input /user/vagrant/ncdc-output
```

Verify the output:
```
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /user/vagrant/ncdc-output/
Found 2 items
-rw-r--r--   2 vagrant supergroup          0 2016-10-12 17:21 /user/vagrant/ncdc-output/_SUCCESS
-rw-r--r--   2 vagrant supergroup         90 2016-10-12 17:21 /user/vagrant/ncdc-output/part-r-00000
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -cat /user/vagrant/ncdc-output/part-r-00000
1901	239
1902	156
1903	172
1904	172
1905	178
1906	278
1907	256
1908	283
1909	278
1910	294
```

##Exercise 2
Using the streaming functionalities distributed with Hadoop, we can launch other languages using stdin and stdout. For example, some python programs:
```
vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -put /vagrant/src/python/wordcount/cervantes/ /user/vagrant/cervantes-input

vagrant@ubuntu1:/usr/local/hadoop$ hadoop jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
> -file /vagrant/src/python/wordcount/mapper.py -mapper /vagrant/src/python/wordcount/mapper.py \
> -file /vagrant/src/python/wordcount/reducer.py -reducer /vagrant/src/python/wordcount/reducer.py \
> -input /user/vagrant/cervantes-input \
> -output /user/vagrant/cervantes-output

vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -ls /user/vagrant/cervantes-output/
Found 2 items
-rw-r--r--   2 vagrant supergroup          0 2016-10-12 17:31 /user/vagrant/cervantes-output/_SUCCESS
-rw-r--r--   2 vagrant supergroup     275669 2016-10-12 17:31 /user/vagrant/cervantes-output/part-00000

vagrant@ubuntu1:/usr/local/hadoop$ hdfs dfs -cat /user/vagrant/cervantes-output/part-00000
$1 	1
$5,000 	1
*** 	2
(...)
últimamente 	4
últimas 	4
último 	26
últimos 	3
única 	7
único 	11
únicos 	1
útil 	3
útiles 	1
```
There are more examples in the python folder that could be tested with this environment: distgrep, inverted, sampling, sentiment, stats and topN.
