# Project: Environmental Monitoring
This project uses MQTT to monitor environmental sensors . MQTT is a lightweight messaging protocol for publishing and subscribing messages in IoT applications and real-time data exchange.

# Project Overview
My goal with this project is to demonstrate how you can retrieve data from environmental sensors and publish them or subscribe in order to recieve the sensor information wether its temperature,air or Co2 sensor.

# Main Feautures
1-It connects to a MQTT broker in order to exchange information.
2-Publishes messages with the infomation of the sensors.
3-Subscribes to the MQTT server and actively listens for messages.
4-Different data are saved into different databases using SQLITE3 , MONGOPY , NEO4J based on their sensor types.
5-After some information are inserted into the databases, the data could be viewed on the according platform for instance neo4j data can be viewed on neo4j desktop.


# Librarries Used 
Paho-mqtt library is used in order to connect to the mqtt server.
sqlite3 library is used for the sql database and its queries.
mongopy is used to connect and maintain the information related to air sensors.
graphdatabase is imported from neo4j library in order to connect to the database and execute beo4j queries



# Prerequisites
1-MQTT Broker:
for local developent mosquitto broker is recommended https://mosquitto.org/download/
2-Python 3+
make sure you have python3+ installed on your device
3-Python Libraries
you need to install paho-mqtt , mongopy , neo4j libraries using pip install command . (sqlite library is often included)
make sure you have installed mongopy and neo4j servers and started them befor implementation.


# Project Files 
1-Subscriber.py:
  Subscriber file subscribes to the MQTT server in order to recieve the published    information and it should be ran first to start listening.
  
2-Publisher.py:
  This send data to the mqtt server and sleeps 5 seconds before repeating the        publishment.

3-Mongodb.py:
  This files saves the information related to air sensors to the mongodb database    via tbe function save_to_mongo() imported to subscriber.py.

4-Sqlite:
  This files saves the information related to temperature sensors to the sql         database via tbe function save_to_sqlite() imported to subscriber.py.

5-neo4j:
  This files saves the information related to Co2 sensors to the neo4j database      using tbe function save_to_neo4j() imported to subscriber.py.



# HOW TO RUN THE APPLICATION 

1- Run the subscriber file so it starts listening for information.
2- Then you can run the publisher.py to actually publish sensors data.
3-in each database file there is a function commented out for printing out the results saved in them.in order to see the results you would have to remove the commenting code and run the file.

