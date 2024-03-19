import psycopg2
from psycopg2 import Error

# Database connection parameters
DB_NAME = "University"
DB_USER = "postgres"
DB_PASSWORD = "Nulah_300"
DB_HOST = "localhost"
DB_PORT = "5432"

# Function to connect to PostgreSQL database
def connect():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL:", e)

# Function to retrieve all students
def getAllStudents():
    connection = connect() # Connect to the database
    cursor = connection.cursor() # Create a cursor object
    cursor.execute("SELECT * FROM students;") # Execute the SQL query
    students = cursor.fetchall() # Fetch all the records
    cursor.close() # Close the cursor
    connection.close() # Close the connection
    return students # Return the records

# Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    connection = connect() # Connect to the database
    cursor = connection.cursor() # Create a cursor object
    cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date)) # Execute the SQL query
    connection.commit() # Commit the transaction
    print("Student added successfully.")
    cursor.close() # Close the cursor
    connection.close() # Close the connection

# Function to update student's email
def updateStudentEmail(student_id, new_email):
    connection = connect() # Connect to the database
    cursor = connection.cursor() # Create a cursor object
    cursor.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id)) # Execute the SQL query
    connection.commit() # Commit the transaction 
    print("Email updated successfully.")    
    cursor.close() # Close the cursor
    connection.close() # Close the connection

# Function to delete a student
def deleteStudent(student_id):
        connection = connect() # Connect to the database
        cursor = connection.cursor() # Create a cursor object
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,)) # Execute the SQL query
        connection.commit() # Commit the transaction
        print("Student deleted successfully.")
        cursor.close() # Close the cursor
        connection.close() # Close the connection

# Main function to demonstrate CRUD operations
if __name__ == "__main__":

    #Initial addition of data into students
    #addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
    #addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
    #addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

    #print("1. Fetching all students:")
    #print(getAllStudents())
    
    #print("\n2. Adding a new student:")
    #addStudent("Emily", "Brown", "emily.brown@example.com", "2024-03-15")    
    #print(getAllStudents())
    
    #print("\n3. Updating email of student with ID 9:")
    #updateStudentEmail(9, "john.doe.updated@example.com")
    #print(getAllStudents())
    
    print("\n4. Deleting student with ID 10:")
    deleteStudent(10)
    print(getAllStudents())
