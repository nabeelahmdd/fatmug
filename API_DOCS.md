# Vendor Management API

## Authentication Endpoint

### Obtain access and refresh tokens
**Endpoint:** `POST /login/`

**Description:** Authenticates a user and obtains access and refresh tokens for making authenticated requests.

**Request Body:**
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:** Returns an object containing the access and refresh tokens.

```json
{
    "access": "access_token_string",
    "refresh": "refresh_token_string"
}
```

**Note:** Include the access token in the `Authorization` header as `Bearer <access_token>` for authenticated requests.

## Vendor Endpoints

### Create a new vendor
**Endpoint:** `POST /api/vendors/`

**Description:** Creates a new vendor.

**Request Body:**
```json
{
    "name": "Vendor Name",
    "contact_details": "Contact information",
    "address": "Vendor address"
}
```

**Response:** Returns the created vendor object.

### List all vendors
**Endpoint:** `GET /api/vendors/`

**Description:** Retrieves a list of all vendors.

**Response:** Returns an array of vendor objects.

### Retrieve a specific vendor
**Endpoint:** `GET /api/vendors/{vendor_id}/`

**Description:** Retrieves the details of a specific vendor.

**Response:** Returns the vendor object.

### Update a vendor
**Endpoint:** `PUT /api/vendors/{vendor_id}/`

**Request Body:**
```json
{
    "name": "Updated Vendor Name",
    "contact_details": "Updated contact information",
    "address": "Updated vendor address"
}
```

**Description:** Updates the details of a specific vendor.

**Response:** Returns the updated vendor object.

### Delete a vendor
**Endpoint:** `DELETE /api/vendors/{vendor_id}/`

**Description:** Deletes a specific vendor.

**Response:** Returns a success message.

## Purchase Order Endpoints

### Create a purchase order
**Endpoint:** `POST /api/purchase_orders/`

**Request Body:**
```json
{
    "vendor": 1,
    "order_date": "2023-05-01T12:00:00Z",
    "delivery_date": "2023-05-15T12:00:00Z",
    "items": [
        {
            "name": "Item 1",
            "quantity": 10
        },
        {
            "name": "Item 2",
            "quantity": 5
        }
    ],
    "quantity": 15,
    "status": "pending",
    "issue_date": "2023-05-01T12:00:00Z"
}
```

**Description:** Creates a new purchase order.

**Response:** Returns the created purchase order object.

### List all purchase orders
**Endpoint:** `GET /api/purchase_orders/`

**Description:** Retrieves a list of all purchase orders. Supports filtering by vendor name using the `search` query parameter.

**Response:** Returns an array of purchase order objects.

### Retrieve a specific purchase order
**Endpoint:** `GET /api/purchase_orders/{po_number}/`

**Description:** Retrieves the details of a specific purchase order.

**Response:** Returns the purchase order object.

### Update a purchase order
**Endpoint:** `PUT /api/purchase_orders/{po_number}/`

**Request Body:**
```json
{
    "vendor": 1,
    "order_date": "2023-05-01T12:00:00Z",
    "delivery_date": "2023-05-20T12:00:00Z",
    "items": [
        {
            "name": "Updated Item 1",
            "quantity": 8
        },
        {
            "name": "Item 2",
            "quantity": 5
        }
    ],
    "quantity": 13,
    "status": "pending",
    "issue_date": "2023-05-01T12:00:00Z"
}
```

**Description:** Updates the details of a specific purchase order.

**Response:** Returns the updated purchase order object.

### Delete a purchase order
**Endpoint:** `DELETE /api/purchase_orders/{po_number}/`

**Description:** Deletes a specific purchase order.

**Response:** Returns a success message.

## Vendor Performance Endpoint

### Retrieve vendor performance metrics
**Endpoint:** `GET /api/vendors/{vendor_id}/performance`

**Description:** Retrieves the performance metrics for a specific vendor.

**Response:** Returns an object containing the vendor's performance metrics (on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate).

## Purchase Order Acknowledgment Endpoint

### Acknowledge a purchase order
**Endpoint:** `POST /api/purchase_orders/{po_id}/acknowledge`

**Description:** Allows vendors to acknowledge a purchase order.

**Response:** Returns a success message.

Note: Replace `{vendor_id}`, `{po_number}`, and `{po_id}` with the respective IDs or numbers in the URLs.