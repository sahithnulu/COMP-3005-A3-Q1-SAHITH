Sahith Nulu
101257609

Youtube Link : https://youtu.be/xk9u-dA9OCU

STEPS TO RUN

(1) Install the module using the below command in your directory in the terminal
pip install psycopg2

(2) Create a table in PostgreSQL using the following SQL query 

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

(3) To insert data, uncomment the below lines of code (line 68 - 71)

    #Initial addition of data into students
    #addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
    #addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
    #addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

(4) Update the data connection parameters (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT) to match with your Postgres Database (line 5 - 9)

(5) There are no compilation steps. You can simply run the program by typing "python app.py" or by clicking the run button if you are using Visual Studio Code

(6) You can change the queries you want to execute in the main function of the program to test the program however you want. The operations you can test are adding new record, updating new record, deleting a record and printing a record. 

(7) While testing the update and delete functions, change the id to match with your database
