import sqlite3
import pandas as pd


conn = sqlite3.connect("data.sqlite")


df_first_five = pd.read_sql(""" SELECT employeeNumber, lastName FROM employees""", conn)


df_five_reverse = pd.read_sql(""" SELECT lastName, employeeNumber FROM employees""", conn)



df_alias = pd.read_sql(""" SELECT lastName, employeeNumber AS Id FROM employees""",conn)


df_executive = pd.read_sql(""" 
    SELECt *, 
        CASE 
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' 
            Then 'Executive' 
            ELSE 'Not Executive'
        END AS role
     FROM employees 
""",conn)
                                    
                            
df_name_length = pd.read_sql(""" SELECT LENGTH(lastName) AS name_length FROM employees """,conn).iloc[0, 0]


df_short_title = pd.read_sql(""" SELECT SUBSTR(jobTitle, 1. 2) AS short_title FROM employees """, conn) 


sum_total_price = pd.read_sql("""SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total FROM orderDetails""", conn).iloc[0, 0]



df_day_month_year = d.read_sql("""
    SELECT orderDate,
        SUBSTR(orderDate, 9, 2) AS day,
        SUBSTR(orderDate, 6, 2) AS month,
        SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)