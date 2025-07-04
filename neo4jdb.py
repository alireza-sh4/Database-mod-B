from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def save_to_neo4j(payload):
    try:
        with driver.session() as session:
            session.write_transaction(_create_sensor_and_reading, payload)
        print("Data saved successfully")
    except Exception as e:
        print(f"Error saving to Neo4j: {e}")

def _create_sensor_and_reading(tx, payload):
    sensor_id = int(payload.get("sensor_id"))
    sensor_type = payload["type"]
    value = payload["value"]
    unit = payload["unit"]
    timestamp = payload["timestamp"]

    
    sensor_name = f"Sensor {sensor_id}"

    tx.run("""
        MERGE (s:Sensor {id: $sensor_id})
        ON CREATE SET 
            s.name = $sensor_name,
            s.type = $sensor_type
        ON MATCH SET 
            s.last_value = $value,
            s.last_unit = $unit,
            s.last_timestamp = $timestamp

        CREATE (r:Reading {
            name: toString($value)+" "+$unit ,
            value: $value,
            unit: $unit,
            timestamp: $timestamp,
            type: $sensor_type
        })

        MERGE (s)-[:REPORTED]->(r)
    """, 
    sensor_id=sensor_id,
    sensor_name=sensor_name,
    sensor_type=sensor_type,
    value=value,
    unit=unit,
    timestamp=timestamp
    )

def reset_neo4j():
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    driver.close()
    print("Neo4j reset complete.")

def test_db():
    try:
        with driver.session() as session:
            result = session.run("RETURN 1 AS test")
            for record in result:
                print("Neo4j test OK:", record["test"])
    except Exception as e:
        print("Neo4j error:", e)

def test_insert_data():
    test_payload = {
        "sensor_id": "co2_sensor_1",
        "value": 420,
        "unit": "ppm",
        "timestamp": "2023-11-15T12:00:00",
        "type": "CO2"
    }
    save_to_neo4j(test_payload)
    print("Test data inserted successfully")


#test_db()
#test_insert_data()


#reset_neo4j()