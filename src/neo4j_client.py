"""Neo4j connectivity client for GraphRAG project."""
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Neo4jClient:
    """Simple Neo4j database client."""
    
    def __init__(
        self,
        uri: str = None,
        username: str = None,
        password: str = None
    ):
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.username = username or os.getenv("NEO4J_USERNAME", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "password123")
        self.driver = None
    
    def connect(self):
        """Establish connection to Neo4j."""
        self.driver = GraphDatabase.driver(
            self.uri,
            auth=(self.username, self.password)
        )
        return self
    
    def close(self):
        """Close the connection."""
        if self.driver:
            self.driver.close()
    
    def verify_connectivity(self):
        """Verify database connection."""
        with self.driver.session() as session:
            result = session.run("RETURN 1 AS num")
            record = result.single()
            return record["num"] == 1
    
    def __enter__(self):
        """Context manager entry."""
        return self.connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


if __name__ == "__main__":
    # Quick connectivity test
    try:
        with Neo4jClient() as client:
            if client.verify_connectivity():
                print("✅ Neo4j connectivity verified!")
            else:
                print("❌ Neo4j connectivity failed!")
    except Exception as e:
        print(f"❌ Error connecting to Neo4j: {e}")
