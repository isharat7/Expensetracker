import sqlite3
def get_connection(database):
	try:
		conn = sqlite3.connect(database)

	except Exception as e:
		print(e)
		conn = None

	return conn


def create_tables(database):
	conn = get_connection(database)	   
	spend_create_query = """
	CREATE TABLE IF NOT EXISTS EXPENDITURE(ID INTEGER PRIMARY KEY,
	                                                                  AMOUNT INT NOT NULL,
									  CATEGORY VARCHAR(50),
									  DATE  DATE NOT NULL UNIQUE
                                      
									  
									)
 						   """
 						  
	range_create_query = """
	CREATE TABLE IF NOT EXISTS RANG(ID INTEGER PRIMARY KEY,
	                                                                 STARTDATE DATE NOT NULL,
							                 ENDDATE DATE NOT NULL,
							                 FOREIGN KEY(STARTDATE) REFERENCES EXPENDITURE(ID),
							                 FOREIGN KEY(ENDDATE) REFERENCES EXPENDITURE(ID)
							                 )			
 						   """
	if conn is not None:
		conn.execute(spend_create_query)
		conn.commit()    
		conn.execute(range_create_query)
		conn.commit()
		conn.close()

	return "SUCCESS"	
	
def add_expenses(amount,category,date):
        #from datetime import datetime
        #date=str(datetime.now())
        print(create_tables("expense.db"))
        conn = get_connection("expense.db")
        add_expenses_query = """
		INSERT INTO EXPENDITURE(AMOUNT,CATEGORY,DATE) VALUES(?,?,?)
	                          """
        if conn is not None:
            try:
                conn.execute(add_expenses_query,(amount,category,date))
                conn.commit()		
                status = "SUCCESS"
                
            except Exception as e: 
                print(e)
                status = "FAILURE"
            
            finally:
                conn.close()

        return status
    
        
def add_range(startdate,enddate):
        #from datetime import datetime
        #date=str(datetime.now())
        print(create_tables("expense.db"))
        conn = get_connection("expense.db")
        add_expenses_query = """
		INSERT INTO RANG(STARTDATE,ENDDATE) VALUES(?,?)
	                          """
        if conn is not None:
            try:
                conn.execute(add_expenses_query,(startdate,enddate))
                conn.commit()		
                status = "SUCCESS"
                
            except Exception as e:
                print(e)
                status = "FAILURE"
            
            finally:
                conn.close()

        return status	
	
def view_expenses():
       conn=get_connection("expense.db")
       sql='''
       select * from expenditure
           '''
       if conn is not None:
           try:
                    expenses=conn.execute(sql).fetchall()
                  
           except Exception as e:
               print(e) 
               expenses=[] 
              
           finally:
               conn.close()    
       return expenses

	
def amnt_range():
	query = "SELECT RANG.ID,RANG.STARTDATE AS STARTDATE,RANG.ENDDATE AS ENDDATE,sum(AMOUNT) FROM EXPENDITURE,RANG WHERE EXPENDITURE.DATE BETWEEN STARTDATE AND ENDDATE group by RANG.ID order by RANG.ID desc limit 1"
	conn = get_connection("expense.db")
	if conn is not None:
		try:
			range_amnts = conn.execute(query).fetchall()
			print(range_amnts)
		except Exception as e:
			print(e)
			range_amnts=[]
		
		finally:
			conn.close()

	return range_amnts	
	
def total_expenses():
        query = "SELECT sum(amount) FROM EXPENDITURE"
        conn = get_connection("expense.db")
        if conn is not None:
            try:
                       total_amnts = conn.execute(query).fetchone()[0]
            except Exception as e:
                        print(e)
                        total_amnts=[]
            finally:
                        conn.close()
            return total_amnts							
				
if __name__ == "__main__":
    print(create_tables("expense.db"))
 
   
    #print(total_expenses())
 
   # print(amnt_range())    
	
	
	
   
	   
	
	
	
   
	
   		   				   
				   				   			   				   			   				   