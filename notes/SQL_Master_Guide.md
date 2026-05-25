# 📘 SQL MASTER GUIDE
### From Beginner to Advanced — A Complete Textbook + Bootcamp + Interview Prep

> **How to use this guide:** Read it top to bottom for the full learning journey, or jump to any section for reference. Every concept includes theory, syntax, real examples, outputs, common mistakes, and practice questions.

---

## 📋 TABLE OF CONTENTS

1. [Introduction to Databases](#section-1--introduction-to-databases)
2. [Installation & Setup](#section-2--installation--setup)
3. [SQL Fundamentals](#section-3--sql-fundamentals)
4. [Table Operations](#section-4--table-operations)
5. [CRUD Operations](#section-5--crud-operations)
6. [Constraints](#section-6--constraints)
7. [Joins](#section-7--joins)
8. [Aggregate Functions](#section-8--aggregate-functions)
9. [Advanced SQL](#section-9--advanced-sql)
10. [Database Design](#section-10--database-design)
11. [Performance Optimization](#section-11--performance-optimization)
12. [SQL Security](#section-12--sql-security)
13. [Real-World Projects](#section-13--real-world-projects)
14. [Interview Preparation](#section-14--interview-preparation)
15. [Practice Sets](#section-15--practice-sets)
16. [SQL Cheatsheet](#section-16--sql-cheatsheet)
17. [30-Day Learning Roadmap](#section-17--30-day-learning-roadmap)

---

# SECTION 1 — INTRODUCTION TO DATABASES

## 1.1 What is Data?

**Data** is raw, unprocessed facts. It can be:
- Numbers: `42`, `3.14`
- Text: `"Alice"`, `"Indore"`
- Dates: `2024-01-15`
- Images, audio, video (binary)

**Analogy:** Data is like individual puzzle pieces — on their own, not very useful. When organized, they become a picture (information).

---

## 1.2 What is a Database?

A **database** is an organized collection of structured data stored electronically. It allows you to store, retrieve, update, and delete data efficiently.

**Analogy:** Think of a database like a school filing cabinet:
- Each **drawer** = a table (e.g., Students, Teachers)
- Each **folder** = a row (one student's record)
- Each **item in the folder** = a column (name, age, grade)

Without a database, imagine managing 10,000 students in Excel files scattered across folders — a nightmare!

---

## 1.3 Why Are Databases Used?

| Problem Without DB | Solution With DB |
|--------------------|------------------|
| Data stored in files, hard to search | Instant search with queries |
| Duplicate data everywhere | Normalization prevents redundancy |
| No security control | Roles & permissions |
| Hard to share data across apps | Multiple apps connect to one DB |
| Manual updates prone to errors | Transactions ensure accuracy |

**Real-world examples:**
- Amazon: stores millions of products, orders, users
- Facebook: stores posts, friendships, messages
- Banks: stores accounts, transactions, balances
- Hospitals: stores patient records, prescriptions

---

## 1.4 Types of Databases

### Relational Databases (RDBMS)
- Data stored in **tables** (rows and columns)
- Tables relate to each other via **keys**
- Use **SQL** (Structured Query Language)
- Examples: MySQL, PostgreSQL, Oracle, SQL Server, SQLite

### Non-Relational Databases (NoSQL)
- Data stored in documents, key-value pairs, graphs, or columns
- No fixed schema
- Examples: MongoDB (documents), Redis (key-value), Cassandra (wide-column), Neo4j (graph)

### Comparison Table

| Feature | RDBMS | NoSQL |
|---------|-------|-------|
| Structure | Fixed tables | Flexible |
| Query language | SQL | Varies |
| ACID compliance | Yes | Partial |
| Scaling | Vertical | Horizontal |
| Best for | Structured data | Unstructured/Big data |
| Examples | MySQL, PostgreSQL | MongoDB, Redis |

---

## 1.5 What is SQL?

**SQL** = **S**tructured **Q**uery **L**anguage

SQL is the standard language used to communicate with relational databases. It lets you:
- **Create** databases and tables
- **Insert** data
- **Read** data with queries
- **Update** existing data
- **Delete** data
- **Control** access and permissions

**Pronunciation:** "S-Q-L" or "sequel" — both are accepted.

---

## 1.6 History of SQL

| Year | Event |
|------|-------|
| 1970 | Edgar F. Codd publishes relational model theory |
| 1974 | IBM develops SEQUEL (Structured English Query Language) |
| 1979 | Oracle releases first commercial SQL RDBMS |
| 1986 | ANSI standardizes SQL |
| 1992 | SQL-92 (major standard update) |
| 2003 | SQL:2003 introduces window functions |
| Today | SQL is used in virtually every industry |

---

## 1.7 Popular Database Systems

### MySQL
- Open-source, owned by Oracle
- Most popular for web applications
- Used by: Facebook, Twitter, Wikipedia
- Best for: Web apps, CMS systems

### PostgreSQL
- Open-source, highly feature-rich
- Supports advanced data types (JSON, arrays, geographic)
- Used by: Instagram, Twitch, Apple
- Best for: Complex queries, analytics, enterprise apps

### SQLite
- File-based, no server needed
- Embedded in apps (Android, iOS, browsers)
- Best for: Mobile apps, small projects, testing

### Oracle Database
- Enterprise-grade, expensive
- Extremely powerful and scalable
- Used by: Banks, governments, large enterprises
- Best for: Mission-critical enterprise applications

### Microsoft SQL Server
- Microsoft's RDBMS
- Tight integration with .NET and Azure
- Used by: Many Windows-based enterprise apps
- Best for: Microsoft ecosystem projects

---

## 1.8 Core Database Concepts

### Tables
A **table** is the fundamental storage unit in a relational database. It looks exactly like a spreadsheet.

```
students table:
+----+----------+-----+------------------+
| id | name     | age | email            |
+----+----------+-----+------------------+
|  1 | Alice    |  20 | alice@email.com  |
|  2 | Bob      |  22 | bob@email.com    |
|  3 | Charlie  |  19 | charlie@email.com|
+----+----------+-----+------------------+
```

### Rows (Records)
Each **row** represents one complete record. In the table above, `1 | Alice | 20 | alice@email.com` is one row.

### Columns (Fields)
Each **column** represents one attribute. `name`, `age`, `email` are columns. Every value in a column has the same data type.

### Schema
A **schema** is the blueprint of the database — it defines what tables exist and what columns each table has. Think of it as the architecture plan.

### Primary Key
A **primary key** is a column (or combination) that **uniquely identifies** each row.
- Must be unique
- Cannot be NULL
- Example: `id` in the students table

### Foreign Key
A **foreign key** is a column that **references the primary key** of another table. It creates a link between two tables.

```
orders table:
+----------+------------+-------------+
| order_id | student_id | total_price |   ← student_id is a FK referencing students.id
+----------+------------+-------------+
|     101  |     1      |    250.00   |
|     102  |     2      |    180.00   |
+----------+------------+-------------+
```

---

## 1.9 Mini Quiz — Section 1

1. What does SQL stand for?
2. Name 3 differences between RDBMS and NoSQL.
3. What is a primary key? Why is it important?
4. What is the purpose of a foreign key?
5. Name 2 real-world applications that use databases.

> **Answers:** (1) Structured Query Language (2) Fixed vs flexible schema, SQL vs no SQL, ACID vs partial (3) Uniquely identifies each row, ensures no duplicates (4) Links tables together (5) Amazon, Facebook, any valid example

---

# SECTION 2 — INSTALLATION & SETUP

## 2.1 Installing MySQL

### Windows
1. Download MySQL Installer from: `https://dev.mysql.com/downloads/installer/`
2. Choose "MySQL Server" + "MySQL Workbench" during setup
3. Set root password (remember it!)
4. Choose "Development Computer" for local use
5. Complete installation

### macOS
```bash
# Using Homebrew
brew install mysql
brew services start mysql
mysql_secure_installation
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
```

### Verify Installation
```bash
mysql -u root -p
# Enter your password
# You should see the MySQL prompt: mysql>
```

---

## 2.2 Installing PostgreSQL

### Windows
1. Download from: `https://www.postgresql.org/download/windows/`
2. Install with pgAdmin (GUI tool included)
3. Set password for `postgres` superuser

### macOS
```bash
brew install postgresql@16
brew services start postgresql@16
```

### Linux
```bash
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo -u postgres psql  # connect as postgres user
```

---

## 2.3 Using SQLite (No Installation!)

SQLite requires no server — just download the CLI:
```bash
# Linux/macOS
sudo apt install sqlite3   # or brew install sqlite

# Start SQLite
sqlite3 mydatabase.db
```

For Python users:
```python
import sqlite3
conn = sqlite3.connect('mydatabase.db')
```

---

## 2.4 GUI Tools

| Tool | Works With | Free? | Notes |
|------|-----------|-------|-------|
| MySQL Workbench | MySQL | Yes | Official MySQL GUI |
| pgAdmin | PostgreSQL | Yes | Official PostgreSQL GUI |
| DBeaver | All databases | Yes | Most popular universal GUI |
| TablePlus | All databases | Freemium | Beautiful macOS/Windows GUI |
| DB Browser for SQLite | SQLite | Yes | Simple and lightweight |

**Recommendation for beginners:** Install **DBeaver** — it works with all database types and has an intuitive interface.

---

## 2.5 Creating Your First Database

### MySQL
```sql
-- Connect via command line:
mysql -u root -p

-- Create database
CREATE DATABASE my_first_db;

-- Use it
USE my_first_db;

-- Confirm
SHOW DATABASES;
```

### PostgreSQL
```sql
-- Connect via psql
psql -U postgres

-- Create database
CREATE DATABASE my_first_db;

-- Connect to it
\c my_first_db

-- List databases
\l
```

---

## 2.6 Common Setup Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Can't connect to MySQL | Service not running | `sudo systemctl start mysql` |
| Access denied for root | Wrong password | Reset root password via safe mode |
| Port 3306 in use | Another service using it | Change port in `my.cnf` |
| psql command not found | PATH not set | Add PostgreSQL bin to PATH |

---

# SECTION 3 — SQL FUNDAMENTALS

## 3.1 SQL Syntax Basics

SQL is made up of **statements**. Each statement performs one action.

```sql
-- Basic structure:
KEYWORD column_name(s) FROM table_name WHERE condition;

-- Example:
SELECT name, age FROM students WHERE age > 18;
```

**Rules:**
- SQL is **case-insensitive** for keywords (`SELECT` = `select` = `Select`)
- Statements end with a **semicolon** `;`
- String values use **single quotes** `'Alice'` (not double quotes in standard SQL)
- Table and column names are **case-sensitive** on Linux/macOS

**Best practice:** Write SQL keywords in UPPERCASE for readability. It's a widely accepted convention.

---

## 3.2 Comments in SQL

```sql
-- This is a single-line comment

/*
   This is a
   multi-line comment
*/

SELECT name  -- inline comment
FROM students;
```

---

## 3.3 SQL Data Types

Understanding data types is critical — choosing the wrong type wastes storage and causes bugs.

### Numeric Types

| Type | Range | Storage | Use When |
|------|-------|---------|----------|
| `TINYINT` | -128 to 127 | 1 byte | Age, boolean flags |
| `SMALLINT` | -32,768 to 32,767 | 2 bytes | Small counters |
| `INT` / `INTEGER` | -2.1B to 2.1B | 4 bytes | IDs, quantities, counts |
| `BIGINT` | ±9.2 quintillion | 8 bytes | Large IDs, timestamps as numbers |
| `DECIMAL(p,s)` | Exact precision | Variable | Money, financial data |
| `FLOAT` | ~7 decimal digits | 4 bytes | Scientific data (approximate) |
| `DOUBLE` | ~15 decimal digits | 8 bytes | Higher precision floats |

> **⚠️ Never use FLOAT for money!** Use `DECIMAL(10,2)` instead. Float arithmetic can cause rounding errors: `0.1 + 0.2 = 0.30000000000000004`

### String/Text Types

| Type | Max Size | Use When |
|------|----------|----------|
| `CHAR(n)` | 255 chars (fixed) | Fixed-length strings like country codes `'US'`, `'IN'` |
| `VARCHAR(n)` | 65,535 chars (variable) | Names, emails, addresses |
| `TEXT` | 65,535 chars | Long descriptions, comments |
| `MEDIUMTEXT` | 16 MB | Articles, blog posts |
| `LONGTEXT` | 4 GB | Very large text data |

> `CHAR(10)` always uses 10 bytes even if you store 3 chars. `VARCHAR(10)` only uses what you need plus 1-2 overhead bytes.

### Date and Time Types

| Type | Format | Example |
|------|--------|---------|
| `DATE` | YYYY-MM-DD | `2024-01-15` |
| `TIME` | HH:MM:SS | `14:30:00` |
| `DATETIME` | YYYY-MM-DD HH:MM:SS | `2024-01-15 14:30:00` |
| `TIMESTAMP` | YYYY-MM-DD HH:MM:SS | `2024-01-15 14:30:00` (auto-updates) |
| `YEAR` | YYYY | `2024` |

> **TIMESTAMP vs DATETIME:** TIMESTAMP stores UTC and converts to the server timezone. DATETIME stores exactly what you give it. Use TIMESTAMP for audit fields (`created_at`, `updated_at`).

### Other Types

| Type | Use |
|------|-----|
| `BOOLEAN` / `TINYINT(1)` | True/false values (MySQL stores as 0/1) |
| `BLOB` | Binary data (images, files — but store files on disk!) |
| `JSON` | JSON documents (PostgreSQL, MySQL 5.7+) |
| `ENUM('v1','v2')` | Column that can only hold predefined values |

---

## 3.4 Creating Your First Table

```sql
-- Syntax:
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);

-- Real example:
CREATE TABLE students (
    id         INT           PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(100)  NOT NULL,
    age        TINYINT       NOT NULL,
    email      VARCHAR(255)  UNIQUE NOT NULL,
    gpa        DECIMAL(3,2),
    enrolled   DATE,
    created_at TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);
```

**Explanation of each column:**
- `id` — auto-increments, uniquely identifies each student
- `name` — up to 100 characters, cannot be empty
- `age` — small number, mandatory
- `email` — must be unique across all students
- `gpa` — 3 total digits, 2 after decimal (e.g., 3.85)
- `enrolled` — date of enrollment
- `created_at` — automatically set when row is inserted

---

## 3.5 Inserting Data

```sql
-- Syntax (specify columns):
INSERT INTO table_name (col1, col2, col3)
VALUES (val1, val2, val3);

-- Insert one student:
INSERT INTO students (name, age, email, gpa, enrolled)
VALUES ('Alice Johnson', 20, 'alice@university.edu', 3.85, '2023-09-01');

-- Insert multiple rows at once:
INSERT INTO students (name, age, email, gpa, enrolled)
VALUES
    ('Bob Smith',    22, 'bob@university.edu',     3.20, '2022-09-01'),
    ('Charlie Brown',19, 'charlie@university.edu', 3.95, '2024-01-15'),
    ('Diana Prince', 21, 'diana@university.edu',   3.60, '2022-09-01');
```

> **Common Mistake:** Inserting without specifying columns works only if you provide ALL values in exact column order. Always specify column names — it's safer and more readable.

---

## 3.6 Selecting Data (READ)

```sql
-- Select all columns:
SELECT * FROM students;

-- Select specific columns:
SELECT name, age, gpa FROM students;

-- Output:
-- +--------------+-----+------+
-- | name         | age | gpa  |
-- +--------------+-----+------+
-- | Alice Johnson|  20 | 3.85 |
-- | Bob Smith    |  22 | 3.20 |
-- | Charlie Brown|  19 | 3.95 |
-- | Diana Prince |  21 | 3.60 |
-- +--------------+-----+------+
```

---

## 3.7 WHERE Clause

Filter rows that match a condition.

```sql
-- Students older than 20:
SELECT * FROM students WHERE age > 20;

-- Students with GPA >= 3.5:
SELECT name, gpa FROM students WHERE gpa >= 3.50;

-- Exact match:
SELECT * FROM students WHERE name = 'Alice Johnson';

-- Output (age > 20):
-- +----+--------------+-----+---------------------+------+
-- | id | name         | age | email               | gpa  |
-- +----+--------------+-----+---------------------+------+
-- |  2 | Bob Smith    |  22 | bob@university.edu  | 3.20 |
-- |  4 | Diana Prince |  21 | diana@university.edu| 3.60 |
-- +----+--------------+-----+---------------------+------+
```

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal | `age = 20` |
| `!=` or `<>` | Not equal | `age != 20` |
| `>` | Greater than | `age > 18` |
| `<` | Less than | `gpa < 3.0` |
| `>=` | Greater or equal | `age >= 21` |
| `<=` | Less or equal | `gpa <= 3.5` |
| `BETWEEN` | Within range (inclusive) | `age BETWEEN 18 AND 25` |
| `LIKE` | Pattern match | `name LIKE 'A%'` |
| `IN` | Match a list | `age IN (19, 20, 21)` |
| `IS NULL` | Check for null | `gpa IS NULL` |
| `IS NOT NULL` | Check not null | `email IS NOT NULL` |

### LIKE Wildcards

```sql
-- Names starting with 'A':
SELECT * FROM students WHERE name LIKE 'A%';

-- Names ending with 'n':
SELECT * FROM students WHERE name LIKE '%n';

-- Names containing 'ob':
SELECT * FROM students WHERE name LIKE '%ob%';

-- Exactly 5 characters:
SELECT * FROM students WHERE name LIKE '_____';

-- % = any number of characters
-- _ = exactly one character
```

### Logical Operators

```sql
-- AND: both conditions must be true
SELECT * FROM students WHERE age > 18 AND gpa >= 3.5;

-- OR: at least one condition must be true
SELECT * FROM students WHERE age < 20 OR gpa > 3.8;

-- NOT: negates the condition
SELECT * FROM students WHERE NOT age = 19;

-- Combine them:
SELECT * FROM students
WHERE (age BETWEEN 19 AND 21) AND (gpa >= 3.5 OR name LIKE 'A%');
```

---

## 3.8 ORDER BY

Sort results by one or more columns.

```sql
-- Sort by GPA descending (highest first):
SELECT name, gpa FROM students ORDER BY gpa DESC;

-- Sort by age ascending (youngest first):
SELECT name, age FROM students ORDER BY age ASC;

-- Sort by multiple columns (primary sort by age, secondary by name):
SELECT name, age, gpa FROM students ORDER BY age ASC, name ASC;

-- Output (ORDER BY gpa DESC):
-- +--------------+------+
-- | name         | gpa  |
-- +--------------+------+
-- | Charlie Brown| 3.95 |
-- | Alice Johnson| 3.85 |
-- | Diana Prince | 3.60 |
-- | Bob Smith    | 3.20 |
-- +--------------+------+
```

> **Note:** `ASC` (ascending) is the default. You only need to specify it for clarity.

---

## 3.9 DISTINCT

Remove duplicate values from results.

```sql
-- Without DISTINCT:
SELECT age FROM students;
-- Returns: 20, 22, 19, 21

-- With DISTINCT (if there were duplicates):
SELECT DISTINCT age FROM students;
-- Returns only unique ages

-- Real use case — unique departments:
SELECT DISTINCT department FROM employees;
```

---

## 3.10 LIMIT (and OFFSET)

Control how many rows are returned.

```sql
-- Get top 3 rows:
SELECT * FROM students LIMIT 3;

-- Get rows 4-6 (skip first 3, take next 3):
SELECT * FROM students LIMIT 3 OFFSET 3;

-- Top 2 highest GPA students:
SELECT name, gpa FROM students
ORDER BY gpa DESC
LIMIT 2;

-- Output:
-- +--------------+------+
-- | name         | gpa  |
-- +--------------+------+
-- | Charlie Brown| 3.95 |
-- | Alice Johnson| 3.85 |
-- +--------------+------+
```

> **Pagination formula:** For page N with P rows per page: `LIMIT P OFFSET (N-1)*P`

---

## 3.11 Aliases (AS)

Give columns or tables a temporary name for readability.

```sql
-- Column aliases:
SELECT
    name        AS student_name,
    age         AS student_age,
    gpa * 25    AS gpa_percentage
FROM students;

-- Table aliases:
SELECT s.name, s.gpa
FROM students AS s
WHERE s.age > 19;

-- Aliases are REQUIRED for expressions:
SELECT name, (age * 12) AS age_in_months FROM students;
```

---

## 3.12 Arithmetic Operators

```sql
SELECT
    name,
    gpa,
    gpa * 25          AS gpa_percent,
    gpa + 0.5         AS adjusted_gpa,
    age * 12          AS age_months,
    100 / age         AS inverse_age
FROM students;
```

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `price + tax` |
| `-` | Subtraction | `total - discount` |
| `*` | Multiplication | `quantity * price` |
| `/` | Division | `total / count` |
| `%` | Modulo (remainder) | `id % 2` |

---

## 3.13 Section 3 Practice Questions

**Beginner:**
1. Select all students sorted by name alphabetically.
2. Find all students with GPA between 3.0 and 3.9.
3. Find students whose name starts with 'B' or 'C'.
4. Select the top 2 youngest students.
5. Show all unique GPAs in the students table.

**Solutions:**
```sql
-- 1
SELECT * FROM students ORDER BY name ASC;

-- 2
SELECT * FROM students WHERE gpa BETWEEN 3.0 AND 3.9;

-- 3
SELECT * FROM students WHERE name LIKE 'B%' OR name LIKE 'C%';

-- 4
SELECT name, age FROM students ORDER BY age ASC LIMIT 2;

-- 5
SELECT DISTINCT gpa FROM students ORDER BY gpa DESC;
```

---

# SECTION 4 — TABLE OPERATIONS

## 4.1 CREATE TABLE (Review + Advanced)

```sql
-- With all constraint types:
CREATE TABLE employees (
    emp_id      INT             PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50)     NOT NULL,
    last_name   VARCHAR(50)     NOT NULL,
    email       VARCHAR(255)    UNIQUE NOT NULL,
    phone       CHAR(15),
    department  VARCHAR(100)    DEFAULT 'General',
    salary      DECIMAL(10,2)   CHECK (salary > 0),
    hire_date   DATE            NOT NULL,
    is_active   BOOLEAN         DEFAULT TRUE,
    manager_id  INT,            -- FK to self (for hierarchy)
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);
```

---

## 4.2 ALTER TABLE

Modify an existing table without losing data.

### Add a Column
```sql
-- Add phone column to students:
ALTER TABLE students ADD COLUMN phone VARCHAR(20);

-- Add column at a specific position:
ALTER TABLE students ADD COLUMN phone VARCHAR(20) AFTER email;

-- Add column with default:
ALTER TABLE students ADD COLUMN is_active BOOLEAN DEFAULT TRUE;
```

### Modify a Column
```sql
-- Change data type or constraint:
ALTER TABLE students MODIFY COLUMN name VARCHAR(200) NOT NULL;

-- PostgreSQL syntax:
ALTER TABLE students ALTER COLUMN name TYPE VARCHAR(200);
```

### Rename a Column
```sql
-- MySQL 8.0+:
ALTER TABLE students RENAME COLUMN name TO full_name;

-- Older MySQL:
ALTER TABLE students CHANGE name full_name VARCHAR(100);
```

### Drop a Column
```sql
-- ⚠️ This permanently deletes all data in that column!
ALTER TABLE students DROP COLUMN phone;
```

### Add a Constraint
```sql
ALTER TABLE students ADD CONSTRAINT chk_age CHECK (age >= 16 AND age <= 100);
ALTER TABLE students ADD CONSTRAINT uq_email UNIQUE (email);
```

### Drop a Constraint
```sql
ALTER TABLE students DROP CONSTRAINT chk_age;      -- PostgreSQL
ALTER TABLE students DROP CHECK chk_age;           -- MySQL
ALTER TABLE students DROP INDEX uq_email;          -- MySQL unique
```

---

## 4.3 RENAME TABLE

```sql
-- MySQL:
RENAME TABLE students TO learners;

-- Alternative:
ALTER TABLE students RENAME TO learners;
```

---

## 4.4 TRUNCATE TABLE

Deletes **all rows** but keeps the table structure.

```sql
TRUNCATE TABLE students;
-- students table still exists, but it's empty
-- AUTO_INCREMENT counter resets to 1
```

**TRUNCATE vs DELETE vs DROP:**

| Feature | TRUNCATE | DELETE | DROP |
|---------|----------|--------|------|
| Removes rows | Yes | Yes | Yes |
| Keeps structure | Yes | Yes | No |
| WHERE clause | No | Yes | No |
| Resets AUTO_INCREMENT | Yes | No | Yes |
| Can rollback | Sometimes | Yes | No |
| Speed | Fast | Slower | Fast |

---

## 4.5 DROP TABLE

Permanently removes the table AND all its data.

```sql
-- ⚠️ IRREVERSIBLE! Always backup first!
DROP TABLE students;

-- Safe version (no error if table doesn't exist):
DROP TABLE IF EXISTS students;
```

---

## 4.6 Checking Table Structure

```sql
-- MySQL:
DESCRIBE students;
-- or:
SHOW COLUMNS FROM students;

-- PostgreSQL:
\d students

-- Shows: column name, type, nullable, key, default, extra
```

---

## 4.7 Common Mistakes in Table Operations

1. **Dropping a table with foreign key references** — other tables depend on it; drop child tables first
2. **Forgetting IF EXISTS** — causes error if table doesn't exist
3. **TRUNCATE when you need WHERE** — use DELETE instead
4. **Modifying column type** — can cause data loss if incompatible (e.g., VARCHAR to INT)

---

## 4.8 Practice — Section 4

1. Add a `graduation_year` INT column to the students table.
2. Change the `phone` column from `VARCHAR(15)` to `VARCHAR(20)`.
3. Rename the `students` table to `university_students`.
4. Add a CHECK constraint ensuring `graduation_year >= 2000`.
5. Drop the `gpa` column.

```sql
-- Solutions:
-- 1
ALTER TABLE students ADD COLUMN graduation_year INT;

-- 2
ALTER TABLE students MODIFY COLUMN phone VARCHAR(20);

-- 3
RENAME TABLE students TO university_students;

-- 4
ALTER TABLE university_students
ADD CONSTRAINT chk_grad_year CHECK (graduation_year >= 2000);

-- 5
ALTER TABLE university_students DROP COLUMN gpa;
```

---

# SECTION 5 — CRUD OPERATIONS

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete — the four fundamental database operations.

## 5.1 CREATE — INSERT INTO

```sql
-- Sample tables for this section:
CREATE TABLE products (
    product_id   INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(200) NOT NULL,
    price        DECIMAL(10,2) NOT NULL,
    stock        INT DEFAULT 0,
    category     VARCHAR(100),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert one product:
INSERT INTO products (name, price, stock, category)
VALUES ('Laptop Pro 15', 89999.00, 25, 'Electronics');

-- Insert multiple products:
INSERT INTO products (name, price, stock, category)
VALUES
    ('Wireless Mouse',    799.00, 150, 'Accessories'),
    ('USB-C Hub',        1499.00,  80, 'Accessories'),
    ('4K Monitor',      24999.00,  15, 'Electronics'),
    ('Mechanical Keyboard', 3999.00, 60, 'Accessories'),
    ('Webcam HD',        5999.00,  40, 'Electronics');
```

### INSERT with SELECT (Copy data)
```sql
-- Copy rows from one table to another:
INSERT INTO products_archive (name, price, category)
SELECT name, price, category
FROM products
WHERE stock = 0;
```

---

## 5.2 READ — SELECT (Advanced)

```sql
-- Basic select with all filters:
SELECT
    product_id,
    name,
    price,
    stock,
    category
FROM products
WHERE category = 'Electronics'
    AND price < 50000
ORDER BY price DESC
LIMIT 5;

-- Output:
-- +------------+---------------+----------+-------+-------------+
-- | product_id | name          | price    | stock | category    |
-- +------------+---------------+----------+-------+-------------+
-- |          4 | 4K Monitor    | 24999.00 |    15 | Electronics |
-- |          6 | Webcam HD     |  5999.00 |    40 | Electronics |
-- |          1 | Laptop Pro 15 | 89999.00 |    25 | Electronics |
-- +------------+---------------+----------+-------+-------------+
```

---

## 5.3 UPDATE

Modify existing records.

```sql
-- Syntax:
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;

-- Update price of one product:
UPDATE products
SET price = 85999.00
WHERE product_id = 1;

-- Update multiple columns:
UPDATE products
SET price = 799.00, stock = 200
WHERE name = 'Wireless Mouse';

-- Update based on condition:
UPDATE products
SET stock = stock - 1
WHERE product_id = 4;

-- Apply 10% discount to all Electronics:
UPDATE products
SET price = price * 0.90
WHERE category = 'Electronics';
```

> **⚠️ DANGER:** `UPDATE products SET price = 0;` — No WHERE clause! This updates EVERY row!
> Always test with `SELECT` using the same WHERE clause before running UPDATE.

### Safe Update Mode (MySQL)
```sql
-- Enable safe mode to prevent accidental full-table updates:
SET SQL_SAFE_UPDATES = 1;
-- Now UPDATE without WHERE using a key column will error
```

---

## 5.4 DELETE

Remove records from a table.

```sql
-- Delete one specific product:
DELETE FROM products WHERE product_id = 3;

-- Delete all out-of-stock products:
DELETE FROM products WHERE stock = 0;

-- Delete based on price:
DELETE FROM products WHERE price > 100000;
```

> **⚠️ NEVER do this accidentally:** `DELETE FROM products;` — deletes ALL rows!
> Always include a WHERE clause. Always verify with SELECT first.

### DELETE with LIMIT (Safety net)
```sql
-- Delete maximum 5 rows at a time (safer for large deletes):
DELETE FROM products WHERE stock = 0 LIMIT 5;
```

---

## 5.5 CRUD Summary Table

| Operation | SQL Command | Description |
|-----------|-------------|-------------|
| Create | `INSERT INTO` | Add new records |
| Read | `SELECT` | Retrieve records |
| Update | `UPDATE SET` | Modify existing records |
| Delete | `DELETE FROM` | Remove records |

---

## 5.6 Best Practices for CRUD

1. **Always use WHERE** in UPDATE and DELETE
2. **Test with SELECT** before destructive operations
3. **Use transactions** for multi-step operations
4. **Backup before bulk updates/deletes**
5. **Use LIMIT** when deleting/updating large datasets

---

## 5.7 Practice — Section 5

**Setup:**
```sql
CREATE TABLE orders (
    order_id    INT PRIMARY KEY AUTO_INCREMENT,
    customer    VARCHAR(100),
    product     VARCHAR(100),
    quantity    INT,
    total_price DECIMAL(10,2),
    status      VARCHAR(20) DEFAULT 'pending',
    order_date  DATE
);

INSERT INTO orders (customer, product, quantity, total_price, order_date)
VALUES
    ('Alice', 'Laptop', 1, 89999.00, '2024-01-15'),
    ('Bob', 'Mouse', 2, 1598.00, '2024-01-16'),
    ('Charlie', 'Monitor', 1, 24999.00, '2024-01-17'),
    ('Alice', 'Keyboard', 1, 3999.00, '2024-01-18'),
    ('Diana', 'Webcam', 1, 5999.00, '2024-01-19');
```

**Questions:**
1. Select all orders placed by Alice.
2. Update Charlie's order status to 'shipped'.
3. Add a new order for Eve buying 2 USB-C Hubs at 2998.00.
4. Delete all orders where total_price < 2000.
5. Increase all prices by 5%.

```sql
-- Solutions:
-- 1
SELECT * FROM orders WHERE customer = 'Alice';

-- 2
UPDATE orders SET status = 'shipped' WHERE customer = 'Charlie';

-- 3
INSERT INTO orders (customer, product, quantity, total_price, order_date)
VALUES ('Eve', 'USB-C Hub', 2, 2998.00, '2024-01-20');

-- 4
DELETE FROM orders WHERE total_price < 2000;

-- 5
UPDATE orders SET total_price = total_price * 1.05;
```

---

# SECTION 6 — CONSTRAINTS

Constraints enforce **rules** on the data in a table, maintaining accuracy and integrity.

## 6.1 PRIMARY KEY

- Uniquely identifies each row
- Cannot be NULL
- Only ONE per table (but can be composite)

```sql
-- Single column primary key:
CREATE TABLE departments (
    dept_id   INT PRIMARY KEY,
    dept_name VARCHAR(100)
);

-- Composite primary key (combination must be unique):
CREATE TABLE course_enrollments (
    student_id  INT,
    course_id   INT,
    enrolled_on DATE,
    PRIMARY KEY (student_id, course_id)  -- Each student can enroll in a course only once
);
```

---

## 6.2 FOREIGN KEY

Enforces referential integrity between tables.

```sql
CREATE TABLE courses (
    course_id   INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(200) NOT NULL,
    dept_id     INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE CASCADE      -- If dept is deleted, delete its courses too
        ON UPDATE CASCADE      -- If dept_id changes, update here too
);
```

### ON DELETE / ON UPDATE Options

| Option | Behavior |
|--------|----------|
| `CASCADE` | Automatically delete/update child rows |
| `SET NULL` | Set FK column to NULL |
| `RESTRICT` | Prevent deletion if children exist |
| `NO ACTION` | Same as RESTRICT (default) |
| `SET DEFAULT` | Set FK to default value |

---

## 6.3 UNIQUE

Ensures no duplicate values in a column (NULLs are allowed in most databases).

```sql
CREATE TABLE users (
    user_id  INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    email    VARCHAR(255),
    -- Multi-column unique constraint:
    CONSTRAINT uq_user_email UNIQUE (username, email)
);
```

---

## 6.4 NOT NULL

Column must always have a value — cannot be left empty.

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(200) NOT NULL,  -- Must provide a name
    price      DECIMAL(10,2) NOT NULL, -- Must provide a price
    description TEXT                   -- Optional (can be NULL)
);
```

---

## 6.5 DEFAULT

Provides an automatic value when no value is specified.

```sql
CREATE TABLE posts (
    post_id    INT PRIMARY KEY AUTO_INCREMENT,
    title      VARCHAR(200) NOT NULL,
    views      INT DEFAULT 0,
    status     VARCHAR(20) DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert without specifying views/status/created_at:
INSERT INTO posts (title) VALUES ('My First Post');
-- views = 0, status = 'draft', created_at = now()
```

---

## 6.6 CHECK

Validates data against a condition before insertion or update.

```sql
CREATE TABLE employees (
    emp_id   INT PRIMARY KEY AUTO_INCREMENT,
    name     VARCHAR(100) NOT NULL,
    age      INT CHECK (age >= 18 AND age <= 65),
    salary   DECIMAL(10,2) CHECK (salary > 0),
    gender   CHAR(1) CHECK (gender IN ('M', 'F', 'O'))
);

-- This will FAIL:
INSERT INTO employees (name, age, salary, gender)
VALUES ('John', 15, 50000, 'M');  -- age 15 violates CHECK
```

---

## 6.7 AUTO_INCREMENT

Automatically generates a sequential unique number (usually for primary keys).

```sql
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    subject   VARCHAR(200)
);

INSERT INTO tickets (subject) VALUES ('Login issue');  -- ticket_id = 1
INSERT INTO tickets (subject) VALUES ('Payment bug');  -- ticket_id = 2
INSERT INTO tickets (subject) VALUES ('UI glitch');    -- ticket_id = 3

-- Start from a specific value:
ALTER TABLE tickets AUTO_INCREMENT = 1000;
-- Next insert will get ticket_id = 1000
```

---

## 6.8 Constraints Summary

| Constraint | Purpose | NULL Allowed? |
|------------|---------|---------------|
| `PRIMARY KEY` | Unique row identifier | No |
| `FOREIGN KEY` | Link to another table | Yes |
| `UNIQUE` | No duplicates | Yes (usually) |
| `NOT NULL` | Must have value | No |
| `DEFAULT` | Auto-fill value | N/A |
| `CHECK` | Validate condition | N/A |
| `AUTO_INCREMENT` | Auto-generate numbers | No |

---

## 6.9 Practice — Section 6

Design a `library` database with these rules:
- Books must have a title and ISBN
- ISBN must be unique
- Available copies cannot be negative
- Member age must be between 5 and 120

```sql
CREATE TABLE members (
    member_id   INT PRIMARY KEY AUTO_INCREMENT,
    full_name   VARCHAR(150) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    age         INT CHECK (age BETWEEN 5 AND 120),
    joined_date DATE DEFAULT (CURRENT_DATE)
);

CREATE TABLE books (
    book_id     INT PRIMARY KEY AUTO_INCREMENT,
    title       VARCHAR(300) NOT NULL,
    isbn        CHAR(13) UNIQUE NOT NULL,
    author      VARCHAR(150),
    available   INT DEFAULT 1 CHECK (available >= 0),
    total       INT NOT NULL CHECK (total > 0)
);

CREATE TABLE loans (
    loan_id     INT PRIMARY KEY AUTO_INCREMENT,
    member_id   INT NOT NULL,
    book_id     INT NOT NULL,
    loan_date   DATE DEFAULT (CURRENT_DATE),
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE RESTRICT,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE RESTRICT
);
```

---

# SECTION 7 — JOINS

Joins combine rows from **two or more tables** based on a related column. This is one of the most important SQL concepts.

## Setup for Join Examples

```sql
-- We'll use employees and departments:
CREATE TABLE departments (
    dept_id   INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    emp_id    INT PRIMARY KEY AUTO_INCREMENT,
    name      VARCHAR(100) NOT NULL,
    dept_id   INT,    -- Can be NULL (unassigned employees)
    salary    DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

INSERT INTO departments VALUES (1,'Engineering'), (2,'Marketing'), (3,'HR'), (4,'Finance');

INSERT INTO employees (name, dept_id, salary) VALUES
    ('Alice',  1, 95000),
    ('Bob',    1, 88000),
    ('Charlie',2, 72000),
    ('Diana',  NULL, 65000),   -- No department yet
    ('Eve',    2, 78000),
    ('Frank',  3, 68000);

-- departments with NO employees: Finance (dept_id=4)
-- employees with NO dept: Diana
```

---

## 7.1 INNER JOIN

Returns only rows where there is a **match in BOTH tables**.

```sql
SELECT
    e.name        AS employee,
    d.dept_name   AS department,
    e.salary
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- Output (Diana excluded — no dept; Finance excluded — no employees):
-- +----------+-------------+----------+
-- | employee | department  | salary   |
-- +----------+-------------+----------+
-- | Alice    | Engineering | 95000.00 |
-- | Bob      | Engineering | 88000.00 |
-- | Charlie  | Marketing   | 72000.00 |
-- | Eve      | Marketing   | 78000.00 |
-- | Frank    | HR          | 68000.00 |
-- +----------+-------------+----------+
```

**Venn Diagram:** Only the overlapping intersection is returned.

**Use when:** You only want records that exist in BOTH tables.

---

## 7.2 LEFT JOIN (LEFT OUTER JOIN)

Returns **all rows from the LEFT table** plus matching rows from the right. Non-matching right rows show NULL.

```sql
SELECT
    e.name        AS employee,
    d.dept_name   AS department
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Output (Diana included with NULL department):
-- +----------+-------------+
-- | employee | department  |
-- +----------+-------------+
-- | Alice    | Engineering |
-- | Bob      | Engineering |
-- | Charlie  | Marketing   |
-- | Diana    | NULL        |  ← Diana included, no department
-- | Eve      | Marketing   |
-- | Frank    | HR          |
-- +----------+-------------+
```

**Find employees WITHOUT a department:**
```sql
SELECT e.name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
-- Returns: Diana
```

---

## 7.3 RIGHT JOIN (RIGHT OUTER JOIN)

Returns **all rows from the RIGHT table** plus matching rows from the left. Non-matching left rows show NULL.

```sql
SELECT
    e.name        AS employee,
    d.dept_name   AS department
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- Output (Finance included with NULL employee):
-- +----------+-------------+
-- | employee | department  |
-- +----------+-------------+
-- | Alice    | Engineering |
-- | Bob      | Engineering |
-- | Charlie  | Marketing   |
-- | Eve      | Marketing   |
-- | Frank    | HR          |
-- | NULL     | Finance     |  ← Finance included, no employees
-- +----------+-------------+
```

> **Pro Tip:** You can always rewrite a RIGHT JOIN as a LEFT JOIN by swapping the table order. Most developers prefer LEFT JOINs for consistency.

---

## 7.4 FULL OUTER JOIN

Returns **all rows from BOTH tables**, with NULL where there's no match.

```sql
SELECT
    e.name        AS employee,
    d.dept_name   AS department
FROM employees e
FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;

-- Output (both Diana and Finance included):
-- +----------+-------------+
-- | employee | department  |
-- +----------+-------------+
-- | Alice    | Engineering |
-- | Bob      | Engineering |
-- | Charlie  | Marketing   |
-- | Diana    | NULL        |
-- | Eve      | Marketing   |
-- | Frank    | HR          |
-- | NULL     | Finance     |
-- +----------+-------------+
```

> **MySQL Note:** MySQL doesn't support FULL OUTER JOIN directly. Emulate with:
```sql
SELECT * FROM employees e LEFT JOIN departments d ON e.dept_id = d.dept_id
UNION
SELECT * FROM employees e RIGHT JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 7.5 SELF JOIN

A table **joins with itself**. Useful for hierarchies (manager-employee relationships).

```sql
-- Add managers to employees table:
ALTER TABLE employees ADD COLUMN manager_id INT;
UPDATE employees SET manager_id = 1 WHERE emp_id IN (2,3);  -- Alice manages Bob and Charlie
UPDATE employees SET manager_id = 3 WHERE emp_id = 6;       -- Charlie manages Frank

-- Self join to show employee and their manager:
SELECT
    e.name    AS employee,
    m.name    AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- Output:
-- +----------+----------+
-- | employee | manager  |
-- +----------+----------+
-- | Alice    | NULL     |  ← Top level, no manager
-- | Bob      | Alice    |
-- | Charlie  | Alice    |
-- | Diana    | NULL     |
-- | Eve      | NULL     |
-- | Frank    | Charlie  |
-- +----------+----------+
```

---

## 7.6 CROSS JOIN

Returns the **Cartesian product** — every row from Table A combined with every row from Table B.

```sql
-- All possible size-color combinations:
SELECT sizes.size, colors.color
FROM sizes
CROSS JOIN colors;

-- If sizes has 3 rows and colors has 4 rows: 3×4 = 12 result rows
```

**Use cases:** Generating all combinations (inventory matrices, scheduling, test data).

---

## 7.7 Joining Multiple Tables

```sql
-- 3-table join:
CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(200),
    dept_id    INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

SELECT
    e.name          AS employee,
    d.dept_name     AS department,
    p.name          AS project
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN projects p ON d.dept_id = p.dept_id
ORDER BY e.name;
```

---

## 7.8 Join Types Visual Summary

```
Table A (Employees)     Table B (Departments)

INNER JOIN:     [  ●●●●  ]  (intersection only)
LEFT JOIN:      [●●●●●●●●]  (all A, matching B or NULL)
RIGHT JOIN:     [  ●●●●●●●] (all B, matching A or NULL)
FULL JOIN:      [●●●●●●●●●] (everything from both)
```

---

## 7.9 Practice — Section 7

Using the employees/departments tables:
1. List all employees with their department names (show unassigned employees too).
2. Find departments that have no employees.
3. Show all employee pairs from the same department.
4. List employees who earn more than the average salary in their department.

```sql
-- 1
SELECT e.name, COALESCE(d.dept_name, 'Unassigned') AS department
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- 2
SELECT d.dept_name
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- 3 (Self join)
SELECT a.name AS employee1, b.name AS employee2, d.dept_name
FROM employees a
JOIN employees b ON a.dept_id = b.dept_id AND a.emp_id < b.emp_id
JOIN departments d ON a.dept_id = d.dept_id;

-- 4 (Subquery + join)
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > (
    SELECT AVG(salary) FROM employees WHERE dept_id = e.dept_id
);
```

---

# SECTION 8 — AGGREGATE FUNCTIONS

Aggregate functions perform calculations on **sets of rows** and return a single value.

## 8.1 COUNT

Count the number of rows.

```sql
-- Count all rows:
SELECT COUNT(*) AS total_employees FROM employees;
-- Result: 6

-- Count non-NULL values in a column:
SELECT COUNT(dept_id) AS assigned_employees FROM employees;
-- Result: 5 (Diana with NULL dept_id is excluded)

-- Count distinct values:
SELECT COUNT(DISTINCT dept_id) AS departments_used FROM employees;
-- Result: 3
```

---

## 8.2 SUM

Calculate the total of numeric values.

```sql
-- Total salary expense:
SELECT SUM(salary) AS total_salary FROM employees;
-- Result: 466000.00

-- Total salary by department:
SELECT d.dept_name, SUM(e.salary) AS dept_salary_total
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

---

## 8.3 AVG

Calculate the arithmetic mean.

```sql
-- Average salary:
SELECT AVG(salary) AS avg_salary FROM employees;
-- Result: 77666.67

-- Average by department:
SELECT d.dept_name, ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY avg_salary DESC;

-- Output:
-- +-------------+------------+
-- | dept_name   | avg_salary |
-- +-------------+------------+
-- | Engineering | 91500.00   |
-- | Marketing   | 75000.00   |
-- | HR          | 68000.00   |
-- +-------------+------------+
```

---

## 8.4 MIN and MAX

```sql
-- Lowest and highest salary:
SELECT
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary,
    MAX(salary) - MIN(salary) AS salary_range
FROM employees;

-- Earliest and latest hire per department:
SELECT
    d.dept_name,
    MIN(e.hire_date) AS first_hire,
    MAX(e.hire_date) AS latest_hire
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
```

---

## 8.5 GROUP BY

Groups rows that share a value and applies aggregate functions to each group.

```sql
-- Count employees per department:
SELECT dept_id, COUNT(*) AS headcount
FROM employees
GROUP BY dept_id;

-- Multiple grouping columns:
SELECT
    d.dept_name,
    YEAR(e.hire_date) AS hire_year,
    COUNT(*) AS hires_that_year
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name, YEAR(e.hire_date)
ORDER BY d.dept_name, hire_year;
```

> **Rule:** Every column in SELECT must either be in GROUP BY or inside an aggregate function.

---

## 8.6 HAVING

Like WHERE, but for **aggregate results**. Filters groups after aggregation.

```sql
-- Departments with more than 1 employee:
SELECT dept_id, COUNT(*) AS headcount
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1;

-- Departments with average salary above 75000:
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING AVG(e.salary) > 75000
ORDER BY avg_salary DESC;
```

### WHERE vs HAVING

| Feature | WHERE | HAVING |
|---------|-------|--------|
| Filters | Individual rows | Groups |
| Works with aggregates? | No | Yes |
| Runs | Before GROUP BY | After GROUP BY |
| Example | `WHERE salary > 60000` | `HAVING AVG(salary) > 60000` |

---

## 8.7 Query Execution Order

Understanding this prevents many SQL errors:

```
1. FROM       → Which tables?
2. JOIN       → How to combine?
3. WHERE      → Filter rows
4. GROUP BY   → Group remaining rows
5. HAVING     → Filter groups
6. SELECT     → Choose columns
7. DISTINCT   → Remove duplicates
8. ORDER BY   → Sort results
9. LIMIT      → Restrict output
```

---

## 8.8 Practice — Section 8

Using the employees/departments tables:
1. Count the number of employees in each department.
2. Find the highest-paid employee in each department.
3. List departments where total salary exceeds 100,000.
4. Show the average salary for each department, only for departments with more than 1 employee.

```sql
-- 1
SELECT d.dept_name, COUNT(e.emp_id) AS headcount
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- 2
SELECT d.dept_name, e.name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary = (
    SELECT MAX(salary) FROM employees WHERE dept_id = e.dept_id
);

-- 3
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING SUM(e.salary) > 100000;

-- 4
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 1;
```

---

# SECTION 9 — ADVANCED SQL

## 9.1 Subqueries

A **subquery** is a query nested inside another query.

```sql
-- Find employees who earn more than the company average:
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Find products more expensive than the average product price:
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);

-- Subquery in FROM (derived table):
SELECT dept_summary.dept_id, dept_summary.avg_sal
FROM (
    SELECT dept_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept_id
) AS dept_summary
WHERE dept_summary.avg_sal > 80000;
```

### Types of Subqueries

| Type | Returns | Example |
|------|---------|---------|
| Scalar | Single value | `WHERE salary > (SELECT AVG(salary) FROM ...)` |
| Row | Single row | `WHERE (a,b) = (SELECT a,b FROM ...)` |
| Column | Single column | `WHERE id IN (SELECT id FROM ...)` |
| Table | Multiple rows/cols | `FROM (SELECT ...) AS alias` |

---

## 9.2 Correlated Subqueries

The subquery **references the outer query** — it runs once per row.

```sql
-- Find employees whose salary is higher than the average of their OWN department:
SELECT e.name, e.salary, e.dept_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE dept_id = e.dept_id  -- References outer query's dept_id
);

-- For each employee, show how many others earn more:
SELECT
    e.name,
    e.salary,
    (SELECT COUNT(*) FROM employees WHERE salary > e.salary) AS employees_earning_more
FROM employees e
ORDER BY e.salary DESC;
```

> **Performance Note:** Correlated subqueries can be slow on large tables. Often rewritable as JOINs for better performance.

---

## 9.3 CTEs (Common Table Expressions)

CTEs create **named temporary result sets** that you can reference in the main query. Makes complex queries readable.

```sql
-- Basic CTE syntax:
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;

-- Example — find top earner per department:
WITH dept_max_salary AS (
    SELECT dept_id, MAX(salary) AS max_sal
    FROM employees
    GROUP BY dept_id
)
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN dept_max_salary dms ON e.dept_id = dms.dept_id AND e.salary = dms.max_sal;

-- Multiple CTEs:
WITH
dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id
),
dept_headcount AS (
    SELECT dept_id, COUNT(*) AS headcount FROM employees GROUP BY dept_id
)
SELECT
    d.dept_name,
    da.avg_sal,
    dh.headcount
FROM departments d
JOIN dept_avg da ON d.dept_id = da.dept_id
JOIN dept_headcount dh ON d.dept_id = dh.dept_id;
```

### Recursive CTE

```sql
-- Generate numbers 1-10:
WITH RECURSIVE numbers AS (
    SELECT 1 AS n          -- Base case
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 10  -- Recursive case
)
SELECT * FROM numbers;

-- Traverse employee hierarchy:
WITH RECURSIVE org_chart AS (
    SELECT emp_id, name, manager_id, 0 AS level
    FROM employees WHERE manager_id IS NULL     -- Top-level managers
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.emp_id
)
SELECT REPEAT('  ', level) || name AS hierarchy, level
FROM org_chart
ORDER BY level, name;
```

---

## 9.4 Window Functions

Window functions perform calculations **across a set of related rows** without collapsing them into one row (unlike GROUP BY).

```sql
-- Syntax:
function_name() OVER (
    PARTITION BY column   -- Group by this (like GROUP BY but keeps all rows)
    ORDER BY column       -- Order within each partition
    ROWS/RANGE ...        -- Window frame (optional)
)
```

### ROW_NUMBER, RANK, DENSE_RANK

```sql
SELECT
    name,
    salary,
    dept_id,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num,
    RANK()       OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_val,
    DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank
FROM employees;

-- Difference between RANK and DENSE_RANK when tied:
-- Salaries: 95000, 95000, 88000
-- ROW_NUMBER: 1, 2, 3  (always unique)
-- RANK:       1, 1, 3  (gap after tie)
-- DENSE_RANK: 1, 1, 2  (no gap)
```

### LAG and LEAD

```sql
-- Compare current and previous month sales:
SELECT
    month,
    sales,
    LAG(sales, 1) OVER (ORDER BY month) AS prev_month_sales,
    sales - LAG(sales, 1) OVER (ORDER BY month) AS month_change
FROM monthly_sales;
```

### Running Totals and Moving Averages

```sql
-- Running total of salary by hire date:
SELECT
    name,
    hire_date,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) AS running_total,
    AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3
FROM employees;
```

### NTILE (Percentile Buckets)

```sql
-- Divide employees into 4 salary quartiles:
SELECT
    name,
    salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

---

## 9.5 CASE Statements

Conditional logic inside SQL queries.

```sql
-- Simple CASE (exact match):
SELECT name, salary,
    CASE
        WHEN salary >= 90000 THEN 'Senior'
        WHEN salary >= 75000 THEN 'Mid-Level'
        WHEN salary >= 60000 THEN 'Junior'
        ELSE 'Entry Level'
    END AS seniority_level
FROM employees;

-- CASE in aggregate (conditional count):
SELECT
    dept_id,
    COUNT(*) AS total,
    COUNT(CASE WHEN salary >= 80000 THEN 1 END) AS high_earners,
    COUNT(CASE WHEN salary < 80000 THEN 1 END) AS others
FROM employees
GROUP BY dept_id;
```

---

## 9.6 Views

A **view** is a saved SQL query that acts like a virtual table.

```sql
-- Create a view:
CREATE VIEW high_earning_employees AS
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 75000;

-- Use view like a table:
SELECT * FROM high_earning_employees;
SELECT dept_name, COUNT(*) FROM high_earning_employees GROUP BY dept_name;

-- Update view:
CREATE OR REPLACE VIEW high_earning_employees AS
SELECT e.name, e.salary, d.dept_name, e.hire_date
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 80000;

-- Drop view:
DROP VIEW IF EXISTS high_earning_employees;
```

**Benefits of Views:**
- Security: hide sensitive columns
- Simplification: complex queries become simple table reads
- Consistency: one definition used everywhere

---

## 9.7 Indexes

Indexes speed up queries by creating a data structure (like a book index) that allows faster lookups.

```sql
-- Create index:
CREATE INDEX idx_employees_dept ON employees(dept_id);
CREATE INDEX idx_employees_salary ON employees(salary);

-- Composite index (covers multiple columns):
CREATE INDEX idx_emp_dept_salary ON employees(dept_id, salary);

-- Unique index:
CREATE UNIQUE INDEX idx_users_email ON users(email);

-- Drop index:
DROP INDEX idx_employees_dept ON employees;  -- MySQL
DROP INDEX idx_employees_dept;               -- PostgreSQL

-- Show indexes:
SHOW INDEX FROM employees;  -- MySQL
\d employees                -- PostgreSQL
```

**When to add indexes:**
- Columns frequently used in WHERE clauses
- Columns used in JOIN conditions
- Columns used in ORDER BY

**When NOT to add indexes:**
- Tables with very few rows
- Columns with low cardinality (few distinct values, like boolean)
- Columns rarely queried

---

## 9.8 Stored Procedures

Reusable blocks of SQL code stored in the database.

```sql
-- Create procedure:
DELIMITER //
CREATE PROCEDURE get_employees_by_dept(IN dept_name_param VARCHAR(100))
BEGIN
    SELECT e.name, e.salary
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    WHERE d.dept_name = dept_name_param
    ORDER BY e.salary DESC;
END //
DELIMITER ;

-- Call procedure:
CALL get_employees_by_dept('Engineering');

-- Procedure with OUT parameter:
DELIMITER //
CREATE PROCEDURE get_dept_avg_salary(
    IN dept_id_param INT,
    OUT avg_sal DECIMAL(10,2)
)
BEGIN
    SELECT AVG(salary) INTO avg_sal
    FROM employees
    WHERE dept_id = dept_id_param;
END //
DELIMITER ;

-- Use OUT parameter:
CALL get_dept_avg_salary(1, @result);
SELECT @result AS engineering_avg;
```

---

## 9.9 Triggers

Automatically execute SQL when a table event occurs.

```sql
-- Audit log table:
CREATE TABLE employee_audit (
    audit_id    INT PRIMARY KEY AUTO_INCREMENT,
    emp_id      INT,
    old_salary  DECIMAL(10,2),
    new_salary  DECIMAL(10,2),
    changed_by  VARCHAR(100),
    changed_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Trigger: log salary changes:
DELIMITER //
CREATE TRIGGER log_salary_change
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary != NEW.salary THEN
        INSERT INTO employee_audit(emp_id, old_salary, new_salary, changed_by)
        VALUES (NEW.emp_id, OLD.salary, NEW.salary, USER());
    END IF;
END //
DELIMITER ;

-- Now every salary update is logged automatically!
UPDATE employees SET salary = 100000 WHERE emp_id = 1;
SELECT * FROM employee_audit;
```

---

## 9.10 Transactions and ACID

A **transaction** is a group of SQL operations treated as a single unit — either ALL succeed or ALL fail.

```sql
-- Start transaction:
START TRANSACTION;  -- or BEGIN;

-- Bank transfer example:
START TRANSACTION;

UPDATE accounts SET balance = balance - 5000 WHERE account_id = 101;  -- Debit
UPDATE accounts SET balance = balance + 5000 WHERE account_id = 202;  -- Credit

-- If everything is OK:
COMMIT;

-- If something went wrong:
ROLLBACK;
```

### ACID Properties

| Property | Meaning | Example |
|----------|---------|---------|
| **Atomicity** | All or nothing | Transfer either completes fully or not at all |
| **Consistency** | Data stays valid | Account balances can't go negative |
| **Isolation** | Transactions don't interfere | Two transfers don't corrupt each other |
| **Durability** | Committed data persists | Power outage won't lose committed transactions |

### SAVEPOINT

```sql
START TRANSACTION;

INSERT INTO orders VALUES (...);          -- Step 1
SAVEPOINT step1;

INSERT INTO order_items VALUES (...);     -- Step 2
-- Something fails here!
ROLLBACK TO SAVEPOINT step1;             -- Roll back only to step 1

COMMIT;
```

---

# SECTION 10 — DATABASE DESIGN

## 10.1 Entity-Relationship (ER) Diagrams

An ER diagram visually represents entities (tables) and their relationships.

**Key elements:**
- **Entity** = Table (rectangle)
- **Attribute** = Column (oval)
- **Relationship** = Connection (diamond)
- **Primary Key** = Underlined attribute

---

## 10.2 Types of Relationships

### One-to-One (1:1)
Each row in Table A corresponds to exactly one row in Table B.

```
users ←——→ user_profiles
  (one user has one profile)

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50)
);

CREATE TABLE user_profiles (
    profile_id INT PRIMARY KEY,
    user_id    INT UNIQUE,  -- UNIQUE enforces 1:1
    bio        TEXT,
    avatar_url VARCHAR(500),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

### One-to-Many (1:N)
One row in Table A corresponds to many rows in Table B.

```
departments ←——→ employees (many)
  (one department has many employees)

-- Department's dept_id is the FK in employees table
-- (Already designed this in Section 7)
```

### Many-to-Many (M:N)
Many rows in Table A correspond to many rows in Table B. **Requires a junction table.**

```
students ←——→ courses (students enroll in many courses; courses have many students)

CREATE TABLE students (student_id INT PRIMARY KEY, name VARCHAR(100));
CREATE TABLE courses  (course_id  INT PRIMARY KEY, title VARCHAR(200));

-- Junction table:
CREATE TABLE enrollments (
    student_id INT,
    course_id  INT,
    grade      CHAR(2),
    enrolled_at DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)
);
```

---

## 10.3 Normalization

Normalization organizes data to **reduce redundancy** and **improve integrity**.

### Problem — Unnormalized Table

```
+----+--------+------------------+-----------+-----------+
| id | name   | email            | course1   | course2   |
+----+--------+------------------+-----------+-----------+
|  1 | Alice  | alice@uni.edu   | Math 101  | CS 201    |
|  2 | Bob    | bob@uni.edu     | Math 101  | NULL      |
+----+--------+------------------+-----------+-----------+
```

Problems:
- Adding a 3rd course requires altering the schema
- "Math 101" duplicated — update anomaly
- Deleting Alice deletes Math 101 data — delete anomaly

---

### First Normal Form (1NF)

**Rule:** Each column contains atomic (indivisible) values. No repeating groups.

```sql
-- Instead of course1, course2 columns:
CREATE TABLE student_courses (
    student_id INT,
    course     VARCHAR(200)
);

-- Now:
-- student_id=1, course='Math 101'
-- student_id=1, course='CS 201'
-- student_id=2, course='Math 101'
```

---

### Second Normal Form (2NF)

**Rule:** 1NF + every non-key column depends on the ENTIRE primary key (no partial dependency). Applies only when composite PK exists.

```sql
-- Problem: composite PK is (student_id, course_id)
-- course_name depends only on course_id, not on student_id → partial dependency!

-- Violation:
CREATE TABLE enrollments_bad (
    student_id  INT,
    course_id   INT,
    course_name VARCHAR(200),  -- Depends only on course_id!
    grade       CHAR(2),
    PRIMARY KEY (student_id, course_id)
);

-- Solution: move course_name to courses table:
CREATE TABLE courses (
    course_id   INT PRIMARY KEY,
    course_name VARCHAR(200)
);

CREATE TABLE enrollments (
    student_id INT,
    course_id  INT,
    grade      CHAR(2),
    PRIMARY KEY (student_id, course_id)
);
```

---

### Third Normal Form (3NF)

**Rule:** 2NF + no transitive dependencies (non-key columns don't depend on other non-key columns).

```sql
-- Problem: emp_id → dept_id → dept_name
-- dept_name depends on dept_id (non-key), not on emp_id

-- Violation:
CREATE TABLE employees_bad (
    emp_id    INT PRIMARY KEY,
    name      VARCHAR(100),
    dept_id   INT,
    dept_name VARCHAR(100)  -- Depends on dept_id, not emp_id (transitive!)
);

-- Solution: separate tables (already done earlier!):
CREATE TABLE departments (dept_id INT PRIMARY KEY, dept_name VARCHAR(100));
CREATE TABLE employees   (emp_id INT PRIMARY KEY, name VARCHAR(100), dept_id INT REFERENCES departments);
```

---

### BCNF (Boyce-Codd Normal Form)

A stricter version of 3NF: for every functional dependency X → Y, X must be a superkey.

---

### Normalization Summary

| Normal Form | Key Rule |
|-------------|----------|
| 1NF | Atomic values, no repeating groups |
| 2NF | No partial dependencies (full PK dependency) |
| 3NF | No transitive dependencies |
| BCNF | Every determinant is a superkey |

> **Practical advice:** Design to 3NF for most applications. Don't over-normalize — sometimes controlled denormalization improves performance.

---

# SECTION 11 — PERFORMANCE OPTIMIZATION

## 11.1 Indexing Strategy

```sql
-- Check if a query uses an index:
EXPLAIN SELECT * FROM employees WHERE dept_id = 1;

-- Output shows:
-- type: ALL (full table scan) → BAD
-- type: ref or index → GOOD
-- rows: 6 vs rows: 2 (shows how many rows scanned)

-- Add the right index:
CREATE INDEX idx_dept_id ON employees(dept_id);

-- After adding index, EXPLAIN shows fewer rows scanned
```

---

## 11.2 Bad Queries vs Optimized Queries

### Full Table Scan (Bad)
```sql
-- ❌ SLOW: Function on indexed column disables the index
SELECT * FROM employees WHERE YEAR(hire_date) = 2023;

-- ✅ FAST: Use range instead
SELECT * FROM employees
WHERE hire_date >= '2023-01-01' AND hire_date < '2024-01-01';
```

### Using SELECT *
```sql
-- ❌ BAD: Fetches all columns, even unused ones
SELECT * FROM employees WHERE dept_id = 1;

-- ✅ GOOD: Fetch only needed columns
SELECT emp_id, name, salary FROM employees WHERE dept_id = 1;
```

### Implicit Type Conversion
```sql
-- ❌ BAD: phone is VARCHAR, comparing to INT causes full scan
SELECT * FROM users WHERE phone = 9876543210;

-- ✅ GOOD: Match types
SELECT * FROM users WHERE phone = '9876543210';
```

### N+1 Query Problem
```sql
-- ❌ BAD: Running 1 query per employee to get department (N+1)
-- In application code:
-- for each employee: SELECT dept_name FROM departments WHERE dept_id = ?

-- ✅ GOOD: One JOIN query
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;
```

---

## 11.3 EXPLAIN and EXPLAIN ANALYZE

```sql
-- Basic EXPLAIN:
EXPLAIN SELECT * FROM employees WHERE salary > 80000;

-- More detail (MySQL 8.0+):
EXPLAIN FORMAT=JSON SELECT * FROM employees WHERE salary > 80000;

-- Run the query and get actual stats (PostgreSQL):
EXPLAIN ANALYZE SELECT * FROM employees WHERE salary > 80000;
```

**Key fields to watch:**
- `type`: ALL (bad) → range/ref/const (good)
- `rows`: estimate of rows scanned
- `Extra`: "Using filesort", "Using temporary" = potential issues

---

## 11.4 Query Optimization Checklist

- [ ] Use indexes on WHERE, JOIN, and ORDER BY columns
- [ ] Avoid SELECT *
- [ ] Use LIMIT when only a few rows needed
- [ ] Avoid functions on indexed columns in WHERE
- [ ] Use JOINs instead of correlated subqueries
- [ ] Check for missing indexes with EXPLAIN
- [ ] Use connection pooling in applications
- [ ] Partition large tables
- [ ] Cache frequently accessed, rarely changing data
- [ ] Avoid `LIKE '%term'` (leading wildcard disables index)

---

# SECTION 12 — SQL SECURITY

## 12.1 SQL Injection

**SQL injection** is a critical security vulnerability where an attacker manipulates a query by injecting malicious SQL.

### Vulnerable Code (Never do this)
```python
# Python example — DANGEROUS:
user_input = "' OR '1'='1"
query = f"SELECT * FROM users WHERE username = '{user_input}'"
# Becomes: SELECT * FROM users WHERE username = '' OR '1'='1'
# This returns ALL users!
```

### Prevention — Parameterized Queries
```python
# SAFE: Use parameterized queries
cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
```

```sql
-- SAFE in stored procedures with parameters:
PREPARE stmt FROM 'SELECT * FROM users WHERE username = ?';
EXECUTE stmt USING @username;
```

---

## 12.2 User Roles and Permissions

```sql
-- Create a read-only user:
CREATE USER 'app_reader'@'localhost' IDENTIFIED BY 'SecurePass123!';
GRANT SELECT ON my_database.* TO 'app_reader'@'localhost';

-- Create an app user (no DROP/ALTER):
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'AnotherSecurePass!';
GRANT SELECT, INSERT, UPDATE, DELETE ON my_database.* TO 'app_user'@'localhost';

-- Create a full admin:
GRANT ALL PRIVILEGES ON *.* TO 'admin_user'@'localhost' WITH GRANT OPTION;

-- Revoke permissions:
REVOKE DELETE ON my_database.* FROM 'app_user'@'localhost';

-- Show user privileges:
SHOW GRANTS FOR 'app_user'@'localhost';
```

---

## 12.3 Backups and Recovery

```bash
# MySQL backup:
mysqldump -u root -p my_database > backup_2024_01_15.sql

# Restore:
mysql -u root -p my_database < backup_2024_01_15.sql

# Backup all databases:
mysqldump -u root -p --all-databases > full_backup.sql

# PostgreSQL backup:
pg_dump my_database > backup.sql
pg_restore -d my_database backup.sql
```

---

# SECTION 13 — REAL-WORLD PROJECTS

## Project 1: Student Management System

```sql
-- Schema Design:
CREATE DATABASE student_management;
USE student_management;

CREATE TABLE departments (
    dept_id   INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL,
    head_name VARCHAR(100)
);

CREATE TABLE students (
    student_id  INT PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    phone       VARCHAR(20),
    dept_id     INT,
    dob         DATE,
    enrollment  DATE DEFAULT (CURRENT_DATE),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE courses (
    course_id   INT PRIMARY KEY AUTO_INCREMENT,
    code        VARCHAR(20) UNIQUE NOT NULL,
    title       VARCHAR(200) NOT NULL,
    dept_id     INT,
    credits     TINYINT DEFAULT 3,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id    INT,
    course_id     INT,
    semester      VARCHAR(20),
    grade         DECIMAL(4,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id)  REFERENCES courses(course_id),
    UNIQUE(student_id, course_id, semester)
);

-- Sample Data:
INSERT INTO departments VALUES (1,'Computer Science','Dr. Kumar'), (2,'Mathematics','Dr. Sharma');

INSERT INTO students (first_name, last_name, email, dept_id, dob)
VALUES
    ('Priya',   'Verma',  'priya@uni.edu',   1, '2002-05-15'),
    ('Rahul',   'Singh',  'rahul@uni.edu',   1, '2001-11-22'),
    ('Ananya',  'Joshi',  'ananya@uni.edu',  2, '2003-01-08');

INSERT INTO courses (code, title, dept_id, credits)
VALUES ('CS101','Intro to Programming',1,4), ('MATH201','Linear Algebra',2,3);

INSERT INTO enrollments (student_id, course_id, semester, grade)
VALUES (1,1,'2024-Spring',8.5), (2,1,'2024-Spring',7.2), (1,2,'2024-Spring',9.0);

-- Useful Queries:
-- Student report card:
SELECT s.first_name, s.last_name, c.code, c.title, e.grade
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE e.student_id = 1;

-- Top students:
SELECT s.first_name, s.last_name, AVG(e.grade) AS cgpa
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id
ORDER BY cgpa DESC;
```

---

## Project 2: E-Commerce Database

```sql
CREATE DATABASE ecommerce;
USE ecommerce;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(150) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    phone       VARCHAR(20),
    address     TEXT,
    city        VARCHAR(100),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    parent_id   INT,  -- Self-referencing for subcategories
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
);

CREATE TABLE products (
    product_id  INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(300) NOT NULL,
    description TEXT,
    price       DECIMAL(10,2) NOT NULL,
    stock       INT DEFAULT 0,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status      ENUM('pending','processing','shipped','delivered','cancelled') DEFAULT 'pending',
    total       DECIMAL(12,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    item_id    INT PRIMARY KEY AUTO_INCREMENT,
    order_id   INT NOT NULL,
    product_id INT NOT NULL,
    quantity   INT NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,  -- Price at time of purchase (snapshot)
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Key analytics queries:

-- Monthly revenue:
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    COUNT(*) AS order_count,
    SUM(total) AS revenue
FROM orders
WHERE status != 'cancelled'
GROUP BY month
ORDER BY month;

-- Best-selling products:
SELECT
    p.name,
    SUM(oi.quantity) AS units_sold,
    SUM(oi.quantity * oi.unit_price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY units_sold DESC
LIMIT 10;

-- Customer lifetime value:
SELECT
    c.name,
    COUNT(o.order_id) AS order_count,
    SUM(o.total) AS lifetime_value
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status != 'cancelled'
GROUP BY c.customer_id
ORDER BY lifetime_value DESC;
```

---

# SECTION 14 — INTERVIEW PREPARATION

## Beginner Questions

**Q1: What is the difference between DELETE, TRUNCATE, and DROP?**

| Feature | DELETE | TRUNCATE | DROP |
|---------|--------|----------|------|
| Removes data | Yes | Yes | Yes |
| Removes structure | No | No | Yes |
| WHERE clause | Yes | No | No |
| Rollback | Yes | No* | No |
| Resets auto-increment | No | Yes | Yes |

**Q2: What is a PRIMARY KEY vs UNIQUE KEY?**
- Primary Key: one per table, cannot be NULL, uniquely identifies rows
- Unique Key: multiple allowed, one NULL allowed, ensures no duplicates

**Q3: What is normalization? Why is it needed?**
Normalization organizes tables to reduce redundancy and improve data integrity. It prevents insertion, update, and deletion anomalies.

---

## Intermediate Questions

**Q4: What is the difference between WHERE and HAVING?**
- WHERE filters individual rows before grouping
- HAVING filters groups after GROUP BY
- HAVING can use aggregate functions; WHERE cannot

**Q5: What are window functions? Give an example.**
Window functions perform calculations across a partition of rows without collapsing them. Example: `RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC)` ranks employees within each department.

**Q6: Explain INNER JOIN vs LEFT JOIN.**
- INNER JOIN: returns only rows with matches in BOTH tables
- LEFT JOIN: returns all rows from the left table, with NULL for non-matching right rows

---

## Advanced Questions

**Q7: What are ACID properties?**
- Atomicity: all or nothing
- Consistency: data remains valid
- Isolation: concurrent transactions don't interfere
- Durability: committed data persists

**Q8: What is an index? What are its pros and cons?**
An index is a data structure that speeds up data retrieval.
- Pros: Faster SELECT queries, faster JOINs
- Cons: Slows INSERT/UPDATE/DELETE, uses extra storage

**Q9: Write a query to find the second highest salary.**
```sql
-- Method 1: Subquery
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 2: LIMIT/OFFSET
SELECT DISTINCT salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Method 3: Window function (Nth highest)
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk = 2;
```

**Q10: What is a correlated subquery? How is it different from a regular subquery?**
A correlated subquery references a column from the outer query and is evaluated once per row. A regular subquery runs once and its result is used by the outer query.

---

## SQL Query Challenges

**Challenge 1:** Find all employees who have never placed an order.
```sql
SELECT e.name FROM employees e
LEFT JOIN orders o ON e.emp_id = o.customer_id
WHERE o.order_id IS NULL;
```

**Challenge 2:** Find the department with the highest total salary.
```sql
SELECT d.dept_name, SUM(e.salary) AS total
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total DESC
LIMIT 1;
```

**Challenge 3:** Find all customers who placed orders in every month of 2023.
```sql
SELECT customer_id
FROM orders
WHERE YEAR(order_date) = 2023
GROUP BY customer_id
HAVING COUNT(DISTINCT MONTH(order_date)) = 12;
```

---

# SECTION 15 — PRACTICE SETS

## Beginner Exercises

**Dataset:**
```sql
CREATE TABLE sales (
    sale_id   INT PRIMARY KEY AUTO_INCREMENT,
    rep_name  VARCHAR(100),
    region    VARCHAR(50),
    product   VARCHAR(100),
    amount    DECIMAL(10,2),
    sale_date DATE
);

INSERT INTO sales (rep_name, region, product, amount, sale_date) VALUES
('Rahul', 'North', 'Laptop', 85000, '2024-01-05'),
('Priya', 'South', 'Phone', 45000, '2024-01-12'),
('Amit',  'East',  'Tablet', 35000, '2024-01-18'),
('Rahul', 'North', 'Phone', 52000, '2024-02-03'),
('Priya', 'South', 'Laptop', 92000, '2024-02-15'),
('Neha',  'West',  'Tablet', 28000, '2024-02-22'),
('Amit',  'East',  'Laptop', 78000, '2024-03-01'),
('Neha',  'West',  'Phone', 61000, '2024-03-19');
```

**Questions:**
1. Show all sales from the 'North' region.
2. Find the total sales amount per region.
3. Which sales rep has the highest total sales?
4. Show all sales in February 2024.
5. Find sales where the amount is between 40,000 and 80,000.
6. Show the top 3 highest individual sales.
7. Count sales per product type.
8. Find all reps who have made more than 1 sale.

**Solutions:**
```sql
-- 1
SELECT * FROM sales WHERE region = 'North';

-- 2
SELECT region, SUM(amount) AS total FROM sales GROUP BY region ORDER BY total DESC;

-- 3
SELECT rep_name, SUM(amount) AS total
FROM sales GROUP BY rep_name ORDER BY total DESC LIMIT 1;

-- 4
SELECT * FROM sales WHERE sale_date BETWEEN '2024-02-01' AND '2024-02-29';

-- 5
SELECT * FROM sales WHERE amount BETWEEN 40000 AND 80000;

-- 6
SELECT * FROM sales ORDER BY amount DESC LIMIT 3;

-- 7
SELECT product, COUNT(*) AS sale_count FROM sales GROUP BY product;

-- 8
SELECT rep_name, COUNT(*) AS sales
FROM sales GROUP BY rep_name HAVING COUNT(*) > 1;
```

---

## Advanced Exercises

**Questions:**
1. Rank sales reps by their total sales using window functions.
2. Calculate a running total of sales ordered by date.
3. Find months where sales exceeded the overall monthly average.
4. Identify which product had the highest sales in each region.

```sql
-- 1 (Window function ranking)
SELECT rep_name,
       SUM(amount) AS total,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS rank_position
FROM sales
GROUP BY rep_name;

-- 2 (Running total)
SELECT sale_date, amount,
       SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM sales;

-- 3 (Months above average)
WITH monthly AS (
    SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month, SUM(amount) AS total
    FROM sales GROUP BY month
)
SELECT month, total
FROM monthly
WHERE total > (SELECT AVG(total) FROM monthly);

-- 4 (Best product per region)
WITH ranked AS (
    SELECT region, product, SUM(amount) AS total,
           RANK() OVER (PARTITION BY region ORDER BY SUM(amount) DESC) AS rnk
    FROM sales GROUP BY region, product
)
SELECT region, product, total FROM ranked WHERE rnk = 1;
```

---

# SECTION 16 — SQL CHEATSHEET

## DDL Commands

```sql
CREATE DATABASE db_name;
USE db_name;
DROP DATABASE db_name;

CREATE TABLE table_name (col type constraints, ...);
ALTER TABLE t ADD COLUMN col type;
ALTER TABLE t MODIFY COLUMN col newtype;
ALTER TABLE t DROP COLUMN col;
ALTER TABLE t RENAME TO new_name;
DROP TABLE IF EXISTS table_name;
TRUNCATE TABLE table_name;
```

## DML Commands

```sql
INSERT INTO t (c1, c2) VALUES (v1, v2);
INSERT INTO t (c1, c2) SELECT c1, c2 FROM t2;
UPDATE t SET c1=v1 WHERE condition;
DELETE FROM t WHERE condition;
SELECT c1, c2 FROM t WHERE condition
    ORDER BY c1 DESC LIMIT 10 OFFSET 5;
```

## Clauses

```sql
WHERE col = val AND col2 > val2
WHERE col LIKE 'A%'          -- starts with A
WHERE col IN (1, 2, 3)
WHERE col BETWEEN 10 AND 20
WHERE col IS NULL / IS NOT NULL
GROUP BY col HAVING COUNT(*) > 1
ORDER BY col ASC / DESC
```

## Joins

```sql
INNER JOIN t2 ON t1.id = t2.fk_id
LEFT JOIN  t2 ON t1.id = t2.fk_id
RIGHT JOIN t2 ON t1.id = t2.fk_id
CROSS JOIN t2
```

## Aggregate Functions

```sql
COUNT(*), COUNT(col), COUNT(DISTINCT col)
SUM(col), AVG(col), MIN(col), MAX(col)
ROUND(val, decimals), FLOOR(val), CEIL(val)
```

## String Functions

```sql
CONCAT(str1, str2)
LENGTH(str) / CHAR_LENGTH(str)
UPPER(str), LOWER(str)
TRIM(str), LTRIM(str), RTRIM(str)
SUBSTRING(str, start, length)
REPLACE(str, from, to)
```

## Date Functions

```sql
NOW(), CURRENT_DATE, CURRENT_TIME
DATE_FORMAT(date, '%Y-%m-%d')
YEAR(date), MONTH(date), DAY(date)
DATEDIFF(date1, date2)
DATE_ADD(date, INTERVAL 30 DAY)
```

## Window Functions

```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY col2)
RANK()        OVER (PARTITION BY col ORDER BY col2)
DENSE_RANK()  OVER (ORDER BY col)
LAG(col, n)   OVER (ORDER BY col)
LEAD(col, n)  OVER (ORDER BY col)
SUM(col)      OVER (PARTITION BY col ORDER BY col2)
```

## Most Used Patterns

```sql
-- Nth highest value:
SELECT salary FROM employees
ORDER BY salary DESC LIMIT 1 OFFSET N-1;

-- Duplicates:
SELECT col, COUNT(*) FROM t GROUP BY col HAVING COUNT(*) > 1;

-- Delete duplicates (keep lowest id):
DELETE FROM t WHERE id NOT IN (SELECT MIN(id) FROM t GROUP BY col);

-- Pagination:
SELECT * FROM t ORDER BY id LIMIT page_size OFFSET (page-1)*page_size;

-- Conditional count:
SELECT COUNT(CASE WHEN condition THEN 1 END) AS count FROM t;
```

---

# SECTION 17 — 30-DAY LEARNING ROADMAP

## Week 1 — Foundations (Days 1-7)

| Day | Topic | Practice |
|-----|-------|----------|
| 1 | What is a DB, SQL intro, install MySQL | Set up environment |
| 2 | CREATE DATABASE, CREATE TABLE, data types | Create a students table |
| 3 | INSERT INTO, SELECT, WHERE basics | Add 10 students, query them |
| 4 | ORDER BY, LIMIT, DISTINCT, LIKE | Sort and filter queries |
| 5 | UPDATE, DELETE, safe practices | Modify and remove records |
| 6 | Constraints: PK, FK, UNIQUE, NOT NULL | Design a proper schema |
| 7 | Review + mini project: simple address book | Build address book DB |

## Week 2 — Intermediate (Days 8-14)

| Day | Topic | Practice |
|-----|-------|----------|
| 8 | INNER JOIN, LEFT JOIN | Join employees to departments |
| 9 | RIGHT JOIN, FULL JOIN, SELF JOIN | Complete join practice |
| 10 | Aggregate: COUNT, SUM, AVG, MIN, MAX | Sales analytics |
| 11 | GROUP BY and HAVING | Group and filter aggregates |
| 12 | Subqueries (scalar, IN, EXISTS) | Complex filtering |
| 13 | ALTER TABLE, DDL deep dive | Schema evolution |
| 14 | Review + mini project: e-commerce schema | Design and query |

## Week 3 — Advanced (Days 15-21)

| Day | Topic | Practice |
|-----|-------|----------|
| 15 | CTEs (WITH clause) | Refactor complex queries |
| 16 | Window functions: ROW_NUMBER, RANK | Rankings and analytics |
| 17 | Window functions: LAG, LEAD, running totals | Time series analysis |
| 18 | CASE statements | Conditional logic |
| 19 | Views and virtual tables | Create analytics views |
| 20 | Indexes and EXPLAIN | Optimize slow queries |
| 21 | Transactions and ACID | Bank transfer simulation |

## Week 4 — Expert & Interview Prep (Days 22-30)

| Day | Topic | Practice |
|-----|-------|----------|
| 22 | Stored procedures | Reusable query modules |
| 23 | Triggers | Audit logging |
| 24 | Database normalization (1NF-3NF) | Normalize a bad schema |
| 25 | SQL security and injection prevention | Secure a database |
| 26 | Performance tuning deep dive | Optimize 5 slow queries |
| 27 | Full project: Student Management System | Build complete DB |
| 28 | Full project: E-commerce Database | Build complete DB |
| 29 | Interview question practice (50 questions) | Mock interview |
| 30 | Final review + cheatsheet internalization | Revise everything |

---

## Best Projects to Build

1. **Student Management System** — tests JOIN, FK, aggregate
2. **E-Commerce Database** — complex relationships, reporting
3. **Hospital Management** — scheduling, hierarchies
4. **Bank Account System** — transactions, ACID, security
5. **Blog/CMS Backend** — categories, tags, many-to-many
6. **Inventory System** — stock tracking, triggers

## Recommended Practice Strategy

1. **Code daily** — even 30 minutes beats 4-hour weekend sessions
2. **Read then write** — don't copy solutions; read the concept, close the book, write from memory
3. **Use real datasets** — Kaggle has free CSV datasets to import
4. **Read EXPLAIN** — understand every query you write
5. **Study others' code** — read open-source SQL schemas on GitHub
6. **Practice on LeetCode/HackerRank** — both have SQL problem sets

---

> 📌 **Final Tip:** SQL is a skill built through repetition. The concepts are simple, but mastery comes from writing thousands of queries. Every query teaches you something new. Keep practicing!

---

*Guide Version 1.0 — Covers MySQL & PostgreSQL — Suitable for Beginners to Advanced*
