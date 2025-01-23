import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os
import logging
import json

# Initialize the Cosmos DB client
COSMOS_DB_URL = os.getenv("CosmosDbUrl")
COSMOS_DB_KEY = os.getenv("CosmosDbKey")
DATABASE_NAME = "AzureResume"  # Replace with your database name
CONTAINER_NAME = "Counter"  # The container you've created

client = CosmosClient(COSMOS_DB_URL, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetResumeCounter")
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Retrieve the document with id = 1
        item = container.read_item(item="1", partition_key="1")
        count = item.get("count", 0)  # Fallback to 0 if "count" is missing

        # Increment the count
        item["count"] = count + 1

        # Update the document in Cosmos DB
        container.replace_item(item=item["id"], body=item)

        # Return the updated count in the response
        response = {"count": item["count"]}
        return func.HttpResponse(
            body=json.dumps(response),  # Serialize dictionary to JSON
            mimetype="application/json",
            status_code=200
        )
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occurred: {e}")
        return func.HttpResponse(
            body="Error retrieving or updating data from Cosmos DB.",
            status_code=500
        )


@app.route(route="GetResumeCounter1", auth_level=func.AuthLevel.FUNCTION)
def GetResumeCounter1(req: func.HttpRequest) -> func.HttpResponse:
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

@app.route(route="GetResumeCounter2", auth_level=func.AuthLevel.FUNCTION)
def GetResumeCounter2(req: func.HttpRequest) -> func.HttpResponse:
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