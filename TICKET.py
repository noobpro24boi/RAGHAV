import mysql.connector
from mysql.connector import Error

# Function to connect to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',         # Replace with your MySQL host
            database='railway_ticket_system',  
            user='raghav',              
            password='password'       # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to create a new ticket
def create_ticket(connection, ticket_data):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO tickets (name, phone_no, gender, nationality, date, catering_service, email, train_no, arrival, departure, class)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, ticket_data)
        connection.commit()
        print("Ticket created successfully")
    except Error as e:
        print(f"Error: {e}")

# Function to fetch ticket details by PNR
def get_ticket_by_pnr(connection, pnr):
    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM tickets WHERE pnr = %s"
        cursor.execute(query, (pnr,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            print("No ticket found with the given PNR")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

# Main execution
if __name__ == "__main__":
    conn = create_connection()
    
    if conn:
        # Example ticket data
        ticket_data = (
            'John Doe', 1234567890, 'Male', 'American', '2024-09-17', 'Veg', 'john.doe@example.com', 1234, 'New York', 'Los Angeles', 'First Class'
        )
        
        create_ticket(conn, ticket_data)
        
        # Fetch and print ticket by PNR
        pnr = 1  # Change this to a valid PNR value
        ticket = get_ticket_by_pnr(conn, pnr)
        if ticket:
            print(ticket)
        
        conn.close()
