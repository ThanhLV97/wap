Here is a sample README.md I would create for this Django REST API project:

# API Project

This project implements a REST API for models, data ingestion, and actions using Django REST Framework.

## Features

- CRUD endpoints for Models, DataIngestion, and Actions
- Serializers to convert model instances to JSON
- Custom model managers for querying
- Containerized using Docker and Docker Compose
- GRPC for action api
- Integrate Oauth server and create client for testing

## Usage

### Environment Setup

- Python 3.9.6
- Django 4.2.7
- Install dependencies: `pip install -r requirements.txt`

### Run Locally

```
$ git clone https://github.com/user/project.git
$ cd project
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

The API will be available at http://localhost:8000/

### Docker

```
$ docker-compose up
```

### Endpoints

The API includes the following endpoints:

**Models**

- `GET /models/` - List all models
- `POST /models/` - Create a new model
- `GET /models/:id` - Get a model by id
- `PUT /models/:id` - Update a model
- `DELETE /models/:id` - Delete a model

**Data Ingestion**

- `GET /data/` - List all data ingestion jobs
- `POST /data/` - Create a new data ingestion job
- `GET /data/:id` - Get a job by id
- `PUT /data/:id` - Update a job
- `DELETE /data/:id` - Delete a job

**Actions**

- `GET /actions/` - List all actions
- `POST /actions/` - Create a new action
- `GET /actions/:id` - Get an action by id
- `PUT /actions/:id` - Update an action
- `DELETE /actions/:id` - Delete an action

## Documentation

## Todo

- [ ] Integrate oauth server and create client for testing
- [ ] Implement action api with GRPC protocal and create stub for testing api
- [ ] Add more docs about flow digram

## Autho

Created by: Thanhlv97
Updated at: 10/11/2023
