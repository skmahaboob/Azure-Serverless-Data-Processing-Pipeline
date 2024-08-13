import json
import azure.functions as func
import logging
import pyodbc
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Parse incoming JSON data
    req_body = req.get_json()
    
    
    # Process the data (e.g., extract needed fields)
    # For example:
    processed_data = {
        "product": req_body.get("product"),
        "price": req_body.get("price")
    }
    
    # Return processed data
    insert_into_sql(processed_data)
    
    return func.HttpResponse(f"Data inserted successfully", status_code=200)


def insert_into_sql(processed_data):
    # Set up the SQL Server connection
    conn_str = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=tcp:test-server-18.database.windows.net,1433;"
        "Database=testdb;"
        "Uid=myadmin;"
        "Pwd=admin@123;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Insert data into SQL Database
    cursor.execute("""
        INSERT INTO dbo.JsonOutput (product, price)
        VALUES (?, ?)
    """, processed_data["product"], processed_data["price"])
    
    conn.commit()
    cursor.close()
    conn.close()


@app.route(route="ingest_json", auth_level=func.AuthLevel.FUNCTION)
def ingest_json(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )