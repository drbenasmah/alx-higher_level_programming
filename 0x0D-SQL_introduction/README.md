SQL - Introduction
This repository contains the solutions for the tasks related to the "0x0D. SQL - Introduction" project. It covers the fundamental concepts of SQL and MySQL. By completing this project, you will gain a solid understanding of databases, relational databases, SQL syntax, and essential SQL operations.

Concepts
During this project, we expect you to become familiar with the following concepts:

Databases
Databases
Resources
To successfully complete this project, it is recommended to review the following resources:

What is Database & SQL?
A Basic MySQL Tutorial
Basic SQL statements: DDL and DML (no need to read the chapter "Privileges")
Basic queries: SQL and RA
SQL technique: functions
SQL technique: subqueries
What makes the big difference between a backtick and an apostrophe?
MySQL Cheat Sheet
MySQL 8.0 SQL Statement Syntax
Installing MySQL in Ubuntu 20.04
Learning Objectives
By the end of this project, you are expected to be able to explain the following concepts to anyone, without the help of Google:

What a database is
What a relational database is
What SQL stands for
What MySQL is
How to create a database in MySQL
What DDL and DML stand for
How to create or alter a table
How to select data from a table
How to insert, update, or delete data
What subqueries are
How to use MySQL functions
Requirements
General requirements for this project:

Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e., syntax above)
All your files should start with a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE...)
A README.md file, at the root of the project folder, is mandatory
The length of your files will be tested using wc
Getting Started
To get started with this project, follow these steps:

Install MySQL 8.0 on Ubuntu 20.04 LTS:
ruby
Copy code
$ sudo apt update
$ sudo apt install mysql-server
Connect to your MySQL server:
ruby
Copy code
$ sudo mysql
Usage
You can execute the SQL files using the MySQL command-line client. Here's an example:

shell
Copy code
$ cat my_script.sql | mysql -uroot -p
Replace my_script.sql with the name of the