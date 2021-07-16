# SQL-Assignments
### Assignment 1 (schema)
Here is the MySQL assignment  Create a Database for an eCommerce company to record the following info 
- Customer info like name, email, phone, status 
- Product info like name, price, description, image, status 
- Order details like date, cost, status 
- Customer can purchase one or more quantities of different products in a single order    

### Assignment 2(Trigger):
Create a user table, which will have id, name, password, create_date, status 
- Insert 10 rows in the table 
- Create a trigger that will record user_id, old_password, new_password, date in a different table when the user password is changed 
- Create one more trigger to store deleted user records when we are deleting a user from the user table.

### Assignment 3(Indexing):
Create a table named product(Fields: id, product_name, product_code, product_description) 
- Create a table named order(id, order_id) 
- Create a table named order item(id, product_id, order_id)  (From product to order relationship is 1 to many. From order_item to product relationship is 1 to many)
- Insert some data into these tables. 
- Every table must have a primary key.  
- Apply unique index on product_code and order_id column of product and order table. 
- Apply fulltext search on product_description.  
- Apply the composite index on product_code and product_description.
- Test with various select queries and check the query execution plan with EXPLAIN command
