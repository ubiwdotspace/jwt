
# JWT Authentication for Web3

This project provides JWT authentication for Web3 applications. It includes a Python-based back-end service utilizing FastAPI to handle the authentication flow.

## Requirements

Before starting, ensure you have Docker installed on your machine. The provided `Dockerfile` is configured to create a containerized environment for the application.

## Getting Started

Clone the repository to your local machine:

```
git clone [repository-url]
```

Navigate to the project directory:

```
cd [local-repository-path]
```

## Configuration

Create an `.env` file in the root directory of the project to store environment variables:

```
`cp ex.env .env`
```

Edit the `.env` file to set your specific variables like database URI, secret keys for JWT, and other required configurations.

## Building the Docker Image

To build the Docker image for the application, run:

```
docker build -t jwt-web3-auth .
```

This command reads the `Dockerfile` in the current directory and builds an image named `jwt-web3-auth`.

## Running the Container

Once the image is built, you can run a container with:

```
docker run -d -p 8000:8000 --name jwt_auth_container jwt-web3-auth
```

This will start a container named `jwt_auth_container` running your FastAPI application, and it will bind the container's port 8000 to port 8000 on your host machine.

## Interacting with the Application

The application will be accessible at `http://localhost:8000`.

You can now use the provided API endpoints to register users, log in, and perform actions that require JWT authentication within your Web3 application.

## Documentation

Swagger UI documentation is available at `http://localhost:8000/docs`, where you can test and interact with the API endpoints.

## Stopping the Container

To stop and remove the container, run:

```
docker stop jwt_auth_container && docker rm jwt_auth_container
```

## Contributing

Contributions are welcome. Please open a pull request to contribute.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
  


