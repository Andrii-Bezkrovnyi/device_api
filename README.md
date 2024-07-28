# API for CRUD devices data

This is a simple app to manage IoT devices in Python

## Description

This project is a web application built using Python, Aiohttp, and Peewee ORM for managing data about IoT devices. The application interfaces with a PostgreSQL database and provides APIs for managing users, locations, and devices. The setup uses Docker and Docker Compose for containerization and ease of deployment.

The code consists endpoints:

1. `/`: Check is the server started.
2. `/devices/`: This endpoint for get and post data about devices.
3. `/devices/{id}/`: This endpoint for get, put, patch, delete data about devices by id.


## How to Use the code

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/Andrii-Bezkrovnyi/device_api.git
    ```

2. Navigate to the project directory:

    ```bash
    cd device_api
    ```
3. Run app via Docker:

    ```bash
    docker-compose up --build -d
    ```
4. You can see app`s logs via Docker command:

    ```bash
    docker-compose logs -f
    ```

5. You can check app work via Postman.
6. Or You can check app work via scripts in direction `methods`.
   - 6.1. Open app`s directory in another console:
       ```bash
       cd device_api
       ```
   - 6.2. Create virtual environment:
       ```bash
       python -m venv venv
       ```
   - 6.3. Enter in virtual environment in Linux:

       ```bash
       source venv/bin/activate
       ```
     - in Windows
      ```bash
      venv\Scripts\activate
      ```
   - 6.4. Install the required dependencies:

        ```bash
        pip install -r requirements_test.txt
        ```
   - 6.5. Run script for checking app work (for Windows):

        ```bash
         python methods\get_req.py
        ```
        ```bash
         python methods\post_req.py
        ```
        ```bash
         python methods\put_req.py
        ```
        ```bash
         python methods\del_req.py
        ```
7. You can stop run app via Docker command:
    ```bash
    docker-compose down
    ```



## How to Test the code

1. Start the app via Docker.

2. Open app`s directory in another console:

    ```bash
    cd device_api
    ```
3. Create virtual environment (if it does not exist):
       ```bash
       python -m venv venv
       ```
4. Enter in virtual environment in Linux:

    ```bash
    source venv/bin/activate
    ```
     - in Windows
      ```bash
      venv\Scripts\activate
      ```
5. Install the required dependencies:

    ```bash
    pip install -r requirements_test.txt
    ```
6. Run script for test app's endpoints (for Windows):
    
    ```bash
    pytest -v
    ```

## Project structure
```
device_api/
├── methods/
    ├── del_req.py
    ├── get_req.py
    ├── post_req.py
    └── put_req.py
├── tests/
    ├── test_delete_method.py
    ├── test_get_method.py
    ├── test_patch_method.py
    ├── test_post_method.py
    └── test_put_method.py
├── app.py
├── config.py
├── db_setup.py
├── models.py
├── routes.py
├── .env.dist
└── .env
```