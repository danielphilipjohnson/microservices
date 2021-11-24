Admin Authentication Endpoints

POST /api/admin/register
POST /api/admin/login
GET /api/admin/user
POST /api/admin/logout
PUT /api/admin/users/info
PUT /api/admin/users/password


Ambassador Authentication Endpoints

POST /api/ambassadors/register
POST /api/ambassadors/login
GET /api/ambassadors/user
POST /api/ambassadors/logout
PUT /api/ambassadors/users/info
PUT /api/ambassadors/users/password

GET /api/ambassadors/products/frontend
GET /api/ambassadors/products/backends
POST /api/ambassadors/links
GET /api/ambassadors/stats
GET /api/ambassadors/rankings


Product endpoints

GET/POST /api/admin/products
GET/PUT/Delete /api/admin/products/{product_id}
GET /api/admin/users/{user_id}/links
GET /api/admin/orders
Get /api/admin/ambassadors

Checkout endpoints

GET /api/checkout/links/{code}
POST /api/checkout/orders
POST /api/checkout/orders/confirm