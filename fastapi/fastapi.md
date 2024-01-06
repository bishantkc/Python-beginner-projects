# FastAPI

* Like any web framework, FastAPI helps us build web applications.
* It targets development of web APIs.

### **Table Of Contents**

1. [Parameters]
    * Path Parameter
    * Query Parameter
1. [HTTP]
    * A. [HTTP Requests]
        * i. [GET]
        * ii. [POST]
        * iii. [PUT]
        * iv. [PATCH]
        * v. [DELETE]
    * B. [HTTP Responses]
        * i. [Status Codes]
1. [REST(ful)]
1. [Python Generators]
    * A. [Yield]
1. [Asynchronous Programming]
    * A. [async]
    * B. [await]
    * C. [asyncio]
1. [Pydantic]
1. [Dependencies]
1. [Object-Relational Mapping (ORM)]
    * [SQLAlchemy]

## Parameters

| Aspect                  | Path Parameters                                   | Query Parameters                                  |
|-------------------------|---------------------------------------------------|---------------------------------------------------|
| **Location in URL**     | Included in the URL path segment.                 | Appended to the URL after the "?" character.     |
| **Syntax in URL**       | `/resource/{pathParam}`                           | `/resource?queryParam=value`                      |
| **Definition in Code**  | Defined in the route decorator or endpoint path.  | Defined in the route decorator or as function arguments. |
| **Example in URL**      | `/users/123`                                      | `/users?filter=active&sort=name`                  |
| **Visibility in URL**   | Visible in the URL path.                          | Visible in the URL query string.                  |
| **Use Case**            | i. Used for identifying a specific resource or entity in the URL. | i. Used for filtering, sorting, or providing additional information to the server. |
| | ii. Use path parameters for crucial data that is necessary for the endpoint to function. | ii. Use query parameter for optional or additional data that refines the result. |

Here's a simple example:
#### Path parameter example:
```py
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id}: item_id"}
```
#### Query Parameter example:
```py
@app.get("/items/")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```


## HTTP

* HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. 
* It is a protocol used to request and transmit data between a client (such as a web browser) and a server. 

## A. HTTP Requests

* HTTP requests are the actions, clients take to communicate with a server.
* They are the messages sent by a client to a server to initiate a specific action.
* HTTP requests are typically initiated when a user interacts with a web page, such as clicking a link or submitting a form.
* HTTP defines several request methods, also known as HTTP verbs, that indicate the desired action to be performed on a resource. 

Here are some common HTTP methods:

### i. GET

* The `GET` method is used to retrieve information from the server or specified resource.
* The `@app.get` decorator is used to define a handler for `GET` requests.

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

### ii. POST

* The `POST` method is used to submit data to be processed to a specified resource.
* The `@app.post` decorator is used to define handler for `POST` requests.

```py
@app.post("/create")
def create_item(item: dict):
    return {"item_created": item}
```

### iii. PUT

* The PUT method is used to update a resource or create a new resource if it does not exist.
* The `@app.put` decorator is used to define a handler for `PUT` requests.

```py

@app.put("/update/{item_id}")
def update_item(item_id: int, updated_item: dict):
    return {"item_id": item_id, "updated_item": updated_item}
```

### iv. PATCH

* The PATCH method is used to apply partial modifications to a resource.
* The `@app.patch` decorator is used to define a handler for `PATCH` requests.

```py
@app.patch("/modify/{item_id}")
def modify_item(item_id: int, modifications: dict):
    return {"item_id": item_id, "modifications": modifications}

```

### v. DELETE

* The DELETE method is used to request the removal of a resource.
* The `@app.delete` decorator is used to define a handler for `DELETE` requests
```py
@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```