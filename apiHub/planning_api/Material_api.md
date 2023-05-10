## Material API

### Retrieve Material (GET)
Retrieves a material object by ID.

#### URL
```
localhost/api/planning/Material_api/<int:pk>/
```

#### Method
```
GET
```

#### Parameters
- `pk` (integer, required): The ID of the material to retrieve.

#### Responses
- 200 OK: Successfully retrieved the material.
- 404 Not Found: The material with the specified ID does not exist.

### List Materials (GET)
Retrieves a list of all materials.

#### URL
```
localhost/api/planning/Material_api/
```

#### Method
```
GET
```

#### Parameters
None

#### Responses
- 200 OK: Successfully retrieved the list of materials.
- 404 Not Found: No materials found.

### Create Material (POST)
Creates a new material.

#### URL
```
localhost/api/planning/Material_api/
```

#### Method
```
POST
```

#### Parameters
- `matcode` (string, required): The material code.
- `title` (string, required): The title of the material.
- `ref` (string, required): The reference of the material.
- `au` (string): The AU value of the material.
- `safstk` (float): The safe stock value of the material.
- `reorder` (float): The reorder value of the material.
- `ar` (float): The AR value of the material.
- `desk` (string, required): The desk of the material.
- `ordcst` (float): The order cost of the material.
- `eoq` (float): The EOQ value of the material.
- `lt` (float): The lead time of the material.
- `safty` (float): The safety value of the material.
- `auamt` (float): The AU amount of the material.
- `spare` (float): The spare value of the material.
- `gr` (float): The GR value of the material.
- `nm` (float): The NM value of the material.
- `pstock` (float): The Pstock value of the material.
- `ind` (float): The IND value of the material.
- `nsaftystk` (float): The NSaftyStk value of the material.
- `specno` (string, required): The specification number of the material.
- `matgroup` (string, required): The material group of the material.
- `section` (string, required): The section of the material.
- `group_b` (float): The group B value of the material.
- `group_c` (float): The group C value of the material.
- `group_a` (float): The group A value of the material.
- `abc` (string, required): The ABC value of the material.
- `reordqty` (float): The reorder quantity of the material.
- `unitrate` (float): The unit rate of the material.
- `dwgno` (string, required): The drawing number of the material.

#### Responses
- 200 OK: Successfully created the material.
- 400 Bad Request: Invalid input data.

