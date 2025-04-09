# 🎉 Online Party Booking System  

## 📌 Overview  
This project is an **online party booking system** that allows users to book venues, make payments, and leave reviews. Organizers can manage venue listings, while admins oversee the platform.

---

## 🛠 Features & Functions  

### 1️⃣ User Authentication & Management  
#### Authentication
- `POST /api/token/`: Get JWT access and refresh tokens
- `POST /api/token/refresh/`: Refresh JWT token

#### User Management
- `POST /api/register/`: Register a new user
- `GET /api/users/`: List users (admin sees all, others see only themselves)
- `GET /api/me/`: Get current user data
- `GET /api/users/{id}/`: Get specific user (if owner or admin)
- `PUT /api/users/{id}/`: Update user (if owner or admin)
- `DELETE /api/users/{id}/`: Delete user (admin only)

## Usage Examples

### Register a new user
```
POST /api/register/
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword",
    "password_confirm": "securepassword",
    "first_name": "John",
    "last_name": "Doe",
    "role": "user",
    "bio": "Regular user"
}
```

### Login to get JWT tokens
```
POST /api/token/
{
    "email": "john@example.com",
    "password": "securepassword"
}
```

### Access protected resources
Include the access token in the Authorization header:
```
GET /api/users/
Authorization: Bearer <your_access_token>
```

### 2️⃣ Venue Management (For Organizers)  
- **Add Venue** (`POST /api/venues/add`) 
    ```ex: {
    "name": "Party_12",
    "location": "Bangalore",
    "capacity": 15,
    "price_per_hour": "1500.00",
    "description": "DJ",
    "image_url": null
    }```
    
- **Edit Venue Details** (`PUT /api/venues/update/{venue_id}`)  
- **Delete Venue** (`DELETE /api/venues/delete/{venue_id}`)  
- **List All Venues** (`GET /api/venues`)  
- **Get Venue Details** (`GET /api/venues/{venue_id}`)  

### 3️⃣ Party Booking (For Users)  
- **Book a Party** (`POST /api/parties/book`)  
- **Cancel a Booking** (`DELETE /api/parties/cancel/{party_id}`)  
- **View My Bookings** (`GET /api/parties/my-bookings`)  

### 4️⃣ Payment Processing  
- **Make Payment** (`POST /api/payments/process`)  
- **Check Payment Status** (`GET /api/payments/status/{payment_id}`)  

### 5️⃣ Reviews & Ratings  
- **Submit Review** (`POST /api/reviews/add`)  
- **Update Review** (`PUT /api/reviews/update/{review_id}`)  
- **Delete Review** (`DELETE /api/reviews/delete/{review_id}`)  

### 6️⃣ Admin Panel  
- **Approve or Reject Venues** (`PUT /api/admin/approve-venue/{venue_id}`)  
- **Manage Users & Organizers** (`GET /api/admin/manage-users`)  
- **View System Reports** (`GET /api/admin/reports`)  

### 7️⃣ Government ID Proof Validation  
- **Validate Aadhaar, PAN, SSN, or Passport** (`POST /api/id/validate`)  
  - Uses **Government API** or **Third-Party API (ID Analyzer, Shufti Pro)**.  
  - Returns **name, date of birth, address, and verification status**.  

---

## 🗃 Database Schema  

### Tables & Columns  
#### 1️⃣ Users (`users`)  
| Column Name      | Data Type  | Description            |  
|-----------------|-----------|------------------------|  
| `user_id`       | UUID      | Primary Key            |  
| `full_name`     | VARCHAR   | User’s full name       |  
| `email`         | VARCHAR   | Unique email           |  
| `phone`         | VARCHAR   | Contact number         |  
| `password_hash` | VARCHAR   | Encrypted password     |  
| `created_at`    | TIMESTAMP | Account creation date  |  

#### 2️⃣ Admins (`admins`)  
| Column Name  | Data Type | Description           |  
|-------------|----------|-----------------------|  
| `admin_id`  | UUID     | Primary Key           |  
| `user_id`   | UUID     | Foreign Key to Users  |  
| `role`      | VARCHAR  | Admin Role            |  

#### 3️⃣ Organizers (`organizers`)  
| Column Name    | Data Type  | Description           |  
|---------------|-----------|-----------------------|  
| `organizer_id`| UUID      | Primary Key           |  
| `name`        | VARCHAR   | Organizer Name        |  
| `email`       | VARCHAR   | Contact Email         |  
| `phone`       | VARCHAR   | Contact Number       |  
| `password_hash` | VARCHAR | Encrypted password    |  
| `created_at`  | TIMESTAMP | Account creation date |  

#### 4️⃣ Venues (`venues`)  
| Column Name        | Data Type | Description               |  
|-------------------|-----------|---------------------------|  
| `venue_id`       | UUID      | Primary Key               |  
| `organizer_id`   | UUID      | Foreign Key to Organizers |  
| `name`           | VARCHAR   | Venue Name                |  
| `location`       | TEXT      | Venue Location            |  
| `capacity`       | INT       | Maximum Capacity          |  
| `price_per_hour` | FLOAT     | Hourly Price              |  
| `description`    | TEXT      | Venue Details             |  
| `image_url`      | TEXT      | Image URL                 |  

#### 5️⃣ Parties (`parties`)  
| Column Name    | Data Type | Description               |  
|---------------|-----------|---------------------------|  
| `party_id`    | UUID      | Primary Key               |  
| `user_id`     | UUID      | Foreign Key to Users      |  
| `venue_id`    | UUID      | Foreign Key to Venues     |  
| `event_date`  | DATE      | Party Date                |  
| `start_time`  | TIME      | Start Time                |  
| `end_time`    | TIME      | End Time                  |  
| `status`      | VARCHAR   | Booking Status            |  
| `total_price` | FLOAT     | Total Cost                |  
| `created_at`  | TIMESTAMP | Booking Time              |  

#### 6️⃣ Payments (`payments`)  
| Column Name      | Data Type | Description            |  
|-----------------|-----------|------------------------|  
| `payment_id`    | UUID      | Primary Key            |  
| `party_id`      | UUID      | Foreign Key to Parties |  
| `user_id`       | UUID      | Foreign Key to Users   |  
| `amount`        | FLOAT     | Payment Amount         |  
| `payment_method`| VARCHAR   | Payment Type           |  
| `status`        | VARCHAR   | Payment Status         |  
| `transaction_id`| VARCHAR   | Payment Gateway ID     |  
| `payment_date`  | TIMESTAMP | Payment Date           |  

#### 7️⃣ Reviews (`reviews`)  
| Column Name   | Data Type | Description            |  
|--------------|-----------|------------------------|  
| `review_id`  | UUID      | Primary Key            |  
| `user_id`    | UUID      | Foreign Key to Users   |  
| `venue_id`   | UUID      | Foreign Key to Venues  |  
| `rating`     | INT       | Rating (1-5)           |  
| `review_text`| TEXT      | User Review            |  
| `created_at` | TIMESTAMP | Review Date            |  

---

## 🚀 How to Set Up the Project  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/tarun18032002/patry_booking.git
cd patry_booking
