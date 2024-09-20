High Level overview

# API Documentation

## Overview

The Human Digital Twin API allows you to interact with the simulation data, including cells, tissues, and organs.

## Endpoints

### Cells

- **GET** `/api/simulation/cells/`  
  Retrieve a list of all cells.

- **POST** `/api/simulation/cells/`  
  Create a new cell.

- **GET** `/api/simulation/cells/{id}/`  
  Retrieve details of a specific cell.

- **PUT** `/api/simulation/cells/{id}/`  
  Update a specific cell.

- **DELETE** `/api/simulation/cells/{id}/`  
  Delete a specific cell.

## Authentication

[Describe your authentication method here, e.g., Token-based, OAuth2.]

## Examples

### Fetching All Cells

**Request:**

```bash
curl -X GET http://localhost:8000/api/simulation/cells/
