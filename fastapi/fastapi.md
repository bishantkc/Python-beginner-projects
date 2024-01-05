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
| **Use Case**            | Used for identifying a specific resource or entity in the URL. | Used for filtering, sorting, or providing additional information to the server. |


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

* Retrieves data from the server
