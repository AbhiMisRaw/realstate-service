## Property Listing REST APIs

### Tech Stack


- **Backend**: FastAPI
- **ORM**: SQLAlcehmy - Async
- **Database**: MySQL - Async MySQL-Driver
- **Cache**: Redis
- **Tools**: Swagger & Postman


### How to Run Project


#### Local Installation

1. create a directory and move to newwly created directory

```shell
mkdir realstate-service
cd realstate-service
```

2. Make an virtual environment and enable the virtual environment

```shell
# for windows
# creating virtual environment
python -m venv venv

# for linux or unix machine
# creating virtual environment
python3 -m venv venv
```

3. Clone the project

```bash
  git clone git@github.com:AbhiMisRaw/realstate-service.git
```

4. Activate virtual environment.

```shell
# activating virtual environment for Windows
venv\Script\activate

# activating virtual environment for Unix-like Systems
source venv/bin/activate
```

5. Go to the cloned project directory

```bash
  cd realstate-service
```

6. Install dependencies

```bash
  pip install -r requirements.txt
```

7. Create `.env` file with following Values

```env
SECRET_KEY="5b4bb4e6fe7862a28986e67b7087f0a61385f28e32ce9284295a3ce2781afc97"
JWT_SECRET_KEY="7862a28986e67b7087f0a61385f28e32ce9284295a3re23ady34m65ad23e"
DB_USER="<DB_USER>"
DB_PASSWORD="<DB_PASSWORD>"
DB_PORT=3308
DB_NAME="<DB_NAME>"
ACCESS_TOKEN_EXP_MIN=30
ALGORITHM="HS256"

```

8. Start the server

```bash
    uvicorn app.main:app
```

### API Endpoints


- If you are using _POSTMAN_ add **Authorization** header in **Headers** section for each request except `register` and `login` endpoints

```json
  KEY : "Authorization",
  Value : "Bearer <TOKEN STRING>"
```
- If you are using `curl`
```
curl -X GET http://127.0.0.1:8000/profile/1 -H 'Authorization: Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

### For Registration
- Endpoints

 >   POST /register

- Body
```json
{
    "name":"USER_NAME",
    "email": "user@example.com",
    "password": "PASSWORD"
}
```
### For Signin
- Endpoints
 
> POST /api/auth/signin/

- Body
```json
{
    "email": "user@example.com",
    "password": "PASSWORD"
}
```
