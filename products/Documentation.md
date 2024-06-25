# API Documentation

## Introduction
The Product API allows for managing products in the store. The base URL for the API is `http://127.0.0.1:8000/api/`.

## Authentication
All requests must include an API key in the headers.


## Endpoints Overview
- **GET api/v1/products/**: Retrieve a list of all products.
- **GET /api/v1//products/{id}/**: Retrieve a single product by ID.
- **POST /api/v1/products/**: Create a new product.
- **PATCH /api/v1/products/{id}/**: Partially update an existing product by ID.
- **DELETE /products/{id}/**: Delete an existing product by ID.

## GET /products/

### Description
Retrieve a list of all products.

### Request
- **Method**: GET
- **URL**: `/api/v1/products/`

### Response

#### Success Response
- **Status Code**: 200 OK
- **Content**: JSON array of products

```json
[
    {
        "id": 1,
        "name": "Product 1",
        "category": "Category 1",
        "price": 100.00,
        "description": "Description of Product 1",
        "stars": 5,
        "image": "image1.jpg"
    }
]
```
#### Error Response
- **Status Code**: 401 Unauthorized
- **Content**: JSON object with error message

```
{
    "error": "Unauthorized"
}
```
# GET /api/v1/products/{id}/
## Description
Retrieve a single product by ID.

## Request
- **Method**: GET
- **URL**: /products/{id}/
## Parameters:
id (integer): ID of the product to retrieve (required)
### Response
### Success Response
- **Status Code**: 200 OK
- **Content**: JSON object of the product

## Error Response
- **Status Code**: 404 Not Found
- **Content**: JSON object with error message

# POST /api/v1/products/

## Description
Create a new product.

## Request

- **Method**: POST
- **URL**: `/products/`
- **Content-Type**: `application/json`

### Body
```json
{
    "name": "Product 1",
    "category": "Category 1",
    "price": 100.00,
    "description": "Description of Product 1",
    "stars": 5,
    "image": "http://example.com/image1.jpg"
}
```
### Response
### Success Response
- **Status Code**: 201 created
- **Content**: JSON object of the product

## Error Response
- **Status Code**: 400 Bad Request
- **Content**: JSON object with error message

# PATCH /products/{id}/
## Description
Partially update an existing product by ID.

## Request
**Method**: PATCH
**URL**: /api/v1/products/{id}/
## Parameters:
id (integer): ID of the product to partially update (required)
**Content-Type**: application/json

```
{
    "price": 120.00,
    "stars": 5
}
```
### Response
### Success Response
- **Status Code**: 200 OK
- **Content**: JSON object of the partially updated product
```
{
    "id": 1,
    "name": "Product 1",
    "category": "Category 1",
    "price": 120.00,
    "description": "Description of Product 1",
    "stars": 5,
    "image": "http://example.com/image1.jpg"
}
```
## Error Response
- **Status Code**: 400 Bad Request
- **Content**: JSON object with error message 'invalid data'

# DELETE /api/v1/products/{id}/
## Description
Delete an existing product by ID.

## Request
**Method**: DELETE
**URL**: /api/v1/products/{id}/
## Parameters:
id (integer): ID of the product to delete (required)

### Response
### Success Response
- **Status Code**: 204 No content
- **Content**: None

## Error Response
- **Status Code**: 404 Not Found
- **Content**: JSON object with error message 'product not found'


