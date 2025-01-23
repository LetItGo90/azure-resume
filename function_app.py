import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os
import json

COSMOS_DB_URL = os.getenv("CosmosDbUrl")
COSMOS_DB_KEY = os.getenv("CosmosDbKey")
DATABASE_NAME = "AzureResume"
CONTAINER_NAME = "Counter"

client = CosmosClient(COSMOS_DB_URL, COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetResumeCounter1")
def GetResumeCounter1(req: func.HttpRequest) -> func.HttpResponse:
    try:
        item = container.read_item(item="1", partition_key="1")
        count = item.get("count", 0)
        item["count"] = count + 1
        container.replace_item(item, item)
        return func.HttpResponse(json.dumps({"count": item["count"]}), mimetype="application/json", status_code=200)
    except exceptions.CosmosHttpResponseError as e:
        return func.HttpResponse("Error accessing Cosmos DB.", status_code=500)
