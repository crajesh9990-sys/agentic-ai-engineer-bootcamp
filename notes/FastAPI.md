# FastAPI Technical Guide

FastAPI speed comes down to two main ideas: **runtime performance** (how fast the code executes) and **developer velocity** (how fast you can build and maintain it).

Rather than reinventing the wheel, FastAPI combines two powerful Python tools under the hood:
1. **Starlette** — Handles high-performance web routing, `async/await`, and ASGI concurrency.
2. **Pydantic** — Handles lightning-fast data parsing, type validation, and serialization using standard Python type hints.

---

## 1. Minimal Code, Maximum Output

With traditional Python frameworks, setting up route validation, JSON parsing, and documentation requires extra configuration and external plugins. FastAPI handles all three using standard Python types.

Here is a full working API endpoint in just a few lines:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define your data structure using type hints
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

# 2. Define your endpoint
@app.post("/items/")
async def create_item(item: Item):
    # 'item' is already parsed and validated into a Python object
    return {"status": "success", "data": item}
```

---

## 2. The 4 Engines Driving Its Speed

| Engine | What It Does | Why It Speeds Things Up |
| :--- | :--- | :--- |
| **Pydantic Validation** | Enforces input schemas automatically. | Rejects invalid requests (e.g., passing `"abc"` for a `float`) before your core logic even runs. |
| **Native `async/await`** | Uses asynchronous non-blocking I/O. | The server processes other incoming requests while waiting for database calls or external APIs. |
| **Automatic OpenAPI Docs** | Generates live interactive documentation (`/docs` using Swagger UI). | Zero time spent writing or updating API documentation manually; test endpoints directly in the browser. |
| **Type Hint Integration** | Integrates directly with modern IDEs. | Enables instant autocompletion and catches syntax bugs in your editor before you even run the code. |

---

## 3. How Data Flows in FastAPI

When a request arrives at a FastAPI application, it follows an automated pipeline:

```
Incoming HTTP Request
       │
       ▼
   [ Starlette ] ──► Handles ASGI server routing & connections
       │
       ▼
   [ Pydantic ]  ──► Validates payload types & deserializes JSON
       │
       ▼
  [ Your Function ] ──► Executes clean, business-logic code
       │
       ▼
[ JSON Response ] ──► Automatically serializes return data & sets headers
```

---

## 4. Key Advantages Summary

1. **High Performance**: Performance on par with **NodeJS** and **Go** thanks to Starlette and ASGI.
2. **Fast to Code**: Increases feature velocity by 200% to 300%.
3. **Fewer Bugs**: Reduces human-induced errors by up to 40% with deep IDE type checking.
4. **Intuitive**: Great editor support with autocompletion everywhere.
5. **Standards-Based**: Based on open API standards: OpenAPI (formerly Swagger) and JSON Schema.

---

## 5. Why FastAPI instead of Flask?

Choosing **FastAPI** over **Flask** usually comes down to **modern features**, **type safety**, and **performance**. While Flask has been a reliable staple for over a decade, FastAPI was built specifically to solve many of Flask's long-standing pain points.

### Feature Comparison

| Feature | **FastAPI** | **Flask** |
| :--- | :--- | :--- |
| **Performance** | High (on par with NodeJS & Go) | Moderate (synchronous by default) |
| **Asynchronous (async/await)** | Native (built on ASGI via Starlette) | Secondary (WSGI focus; limited async support) |
| **Data Validation** | Automatic via Pydantic & type hints | Manual or via external extensions (e.g., Marshmallow) |
| **API Documentation** | Automatic (Swagger UI & ReDoc out of the box) | Requires setup via plugins (e.g., `flasgger`) |
| **Developer Experience** | Autocomplete & type checking in IDEs | Minimal typing integration |

### Key Differences

1. **Automatic Validation vs. Manual Parsing**
   * **Flask:** You have to extract incoming JSON payloads manually and write validation logic or install external packages to verify data types.
   * **FastAPI:** You declare request models using standard Python type hints. FastAPI parses, validates, and throws friendly `422 Unprocessable Entity` errors automatically if the types don't match.

2. **Built-in `async/await` Concurrency**
   * **Flask:** Originally built for WSGI (synchronous web servers). Handling high-concurrency non-blocking tasks requires additional threading or extensions.
   * **FastAPI:** Built from the ground up on **ASGI** (via Starlette). It can handle thousands of concurrent requests natively while waiting for slow database queries or third-party webhooks.

3. **Zero-Config Interactive Docs**
   * **Flask:** To get Swagger/OpenAPI documentation, you have to write custom spec files or integrate third-party libraries.
   * **FastAPI:** Navigating to `/docs` automatically gives you a live, interactive **Swagger UI** generated directly from your code's type definitions.

4. **Better IDE Support & Typing**
   * **Flask:** Uses standard dynamic Python patterns, which means IDEs often can't predict what properties exist on request objects.
   * **FastAPI:** Relies heavily on type hints. This gives your code editor superpowers like deep autocomplete, inline documentation, and instant syntax error detection before you even run the code.

### When Should You Still Use Flask?

* **Simple Server-Rendered Apps:** If you are building traditional HTML websites using Jinja templates rather than REST/JSON APIs, Flask's ecosystem is heavily optimized for it.
* **Legacy Codebases & Extensions:** Flask has a massive legacy ecosystem of micro-extensions for nearly every conceivable use case.
* **Absolute Simplicity:** For ultra-tiny scripts or single-file tools that don't need data validation or docs, Flask's footprint is marginally smaller.

---

## 6. What is Pydantic?

**Pydantic** is the data validation and settings management library used under the hood by FastAPI (and many modern Python frameworks). It leverages standard **Python type annotations** to validate, parse, and serialize data.

### Core Features of Pydantic

1. **Data Parsing Over Validation**:
   * Pydantic doesn't just validate raw input; it **coerces/parses** it into pythonic objects.
   * If a field expects an `int` and receives `"42"` (as a string), Pydantic automatically converts it into integer `42`.

2. **Speed (Powered by Rust)**:
   * Since Pydantic V2, the core validation engine (`pydantic-core`) is written in **Rust**, making data parsing extremely fast.

3. **Schema Generation**:
   * Pydantic automatically exports data models to **JSON Schema**, which allows FastAPI to auto-generate OpenAPI / Swagger documentation seamlessly.

4. **IDE & Type Check Support**:
   * Because model definitions are plain Python classes inheriting from `BaseModel`, IDEs like PyCharm and VS Code offer instant auto-completion and static type checking (`mypy`).

### Code Example

```python
from pydantic import BaseModel, EmailStr, Field

class UserProfile(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int = Field(gt=0, lt=120)  # Constraint: 0 < age < 120

# Parsing raw JSON/dict into a validated Python object
raw_data = {"id": "101", "name": "Alice", "email": "alice@example.com", "age": 28}
user = UserProfile(**raw_data)

print(user.id)   # Output: 101 (Automatically converted from string to int)
print(type(user.id)) # <class 'int'>
```

---

## 7. FastAPI Dependency Injection (`Depends`)

FastAPI comes with a built-in **Dependency Injection (DI)** system using `Depends()`. It allows you to inject shared logic, database sessions, authentication handlers, or query parameters directly into path operation functions.

### Why Use Dependency Injection?
* **Code Reuse**: Avoid repeating code across multiple endpoints (e.g., pagination, auth checks).
* **Database Connection Management**: Automatically open connections before handling requests and safely close them afterward (yield dependencies).
* **Easy Testing & Mocking**: Easily override dependencies during automated testing.

### 1. Basic Dependency Example (Shared Query Parameters)

```python
from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

# 1. Dependency Function
def common_parameters(q: str | None = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}

# 2. Injecting into Route Functions using Annotated
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Fetching items", "params": commons}

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return {"message": "Fetching users", "params": commons}
```

### 2. Advanced: Cleanup with `yield` (Database Sessions)

You can use `yield` instead of `return` to create teardown steps (e.g., closing a database session after the response is sent).

```python
from typing import Generator, Annotated
from fastapi import FastAPI, Depends

def get_db() -> Generator:
    db = "DB_SESSION_CONNECTED"  # Simulate DB Connection
    try:
        yield db
    finally:
        print("Closing DB connection...")  # Executes after response is sent

@app.get("/data/")
async def read_data(db: Annotated[str, Depends(get_db)]):
    return {"db_status": db}
```

---

## 8. Understanding `Annotated` and `Generator` in FastAPI

Both `Annotated` and `Generator` are standard Python typing tools that play a major role in modern FastAPI development.

### A. `typing.Annotated`

Introduced in **Python 3.9** (PEP 593), `Annotated` lets you attach framework-specific metadata to standard type hints without altering the type itself.

#### Syntax Structure
`Annotated[BaseType, Metadata]`

#### Why FastAPI prefers `Annotated`:
1. **DRY Defaults**: You can define reusable types with pre-built dependencies or validations.
2. **Standard Python Compliance**: IDEs recognize the variable's primary type (`int`, `str`, `dict`), enabling full autocompletion and static type checking (`mypy`).

#### Examples of `Annotated` Usage:

```python
from typing import Annotated
from fastapi import FastAPI, Depends, Query, Header

app = FastAPI()

# 1. Custom Metadata / Validation
# Here `q` is a string, but FastAPI validates min_length=3
@app.get("/search/")
async def search(q: Annotated[str, Query(min_length=3, max_length=50)]):
    return {"query": q}

# 2. Dependency Injection Alias
# Define once, reuse everywhere cleanly
DbDep = Annotated[str, Depends(get_db)]

@app.get("/users/")
async def get_users(db: DbDep):
    return {"db": db}

# 3. Request Header Extraction
@app.get("/user-agent/")
async def get_agent(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}
```

---

### B. `typing.Generator` (and `AsyncGenerator`)

In Python typing, `Generator` describes functions that use `yield`. In FastAPI, generator dependencies are used for resource management (context managers, database connections, file handles).

#### Syntax Structure
`Generator[YieldType, SendType, ReturnType]`
* **`YieldType`**: What the dependency yields to the route function (e.g., `Session`).
* **`SendType`**: What can be sent into the generator (usually `None`).
* **`ReturnType`**: What the generator returns when complete (usually `None`).

#### Sync vs. Async Generator Examples:

```python
from typing import Generator, AsyncGenerator, Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

# Synchronous Resource Generator
def get_sync_resource() -> Generator[str, None, None]:
    resource = "SYNC_CONNECTION_OPEN"
    try:
        yield resource  # Yield control to the path operation
    finally:
        print("Sync Resource Closed")

# Asynchronous Resource Generator
async def get_async_resource() -> AsyncGenerator[str, None]:
    resource = "ASYNC_CONNECTION_OPEN"
    try:
        yield resource  # Yield control to async path operation
    finally:
        print("Async Resource Closed")

@app.get("/sync-test")
def test_sync(res: Annotated[str, Depends(get_sync_resource)]):
    return {"resource": res}

@app.get("/async-test")
async def test_async(res: Annotated[str, Depends(get_async_resource)]):
    return {"resource": res}
```

---

## 9. Deep Dive into Pydantic Models

In FastAPI, **Pydantic Models** are classes that define the structure, validation rules, and default values of your request and response payloads. They inherit from `pydantic.BaseModel`.

### Core Features & Patterns

#### 1. Field Validation (`Field`)
The `Field` function allows setting constraints like length, numerical boundaries, regex patterns, or default values:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Name of product")
    price: float = Field(..., gt=0, description="Price must be strictly positive")
    quantity: int = Field(default=1, ge=1, le=50)
```

#### 2. Custom Field Validators (`@field_validator`)
You can define custom validation rules for individual attributes:

```python
from pydantic import BaseModel, field_validator

class UserRegistration(BaseModel):
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        return v
```

#### 3. Nested Models
Models can be nested inside other models to represent complex, hierarchical JSON schemas:

```python
from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class UserProfile(BaseModel):
    id: int
    email: EmailStr
    address: Address  # Nested model definition
```

#### 4. Serializing & Exporting Data (`model_dump` & `model_dump_json`)
* `model.model_dump()`: Converts a Pydantic model into a native Python dictionary.
* `model.model_dump_json()`: Converts a Pydantic model directly into a JSON string.

```python
user = UserProfile(
    id=1,
    email="dev@example.com",
    address=Address(street="123 Main St", city="TechCity", postal_code="600001")
)

dict_data = user.model_dump()
json_string = user.model_dump_json()
```

---

*Updated FastAPI Technical Reference Guide.*


---

## 10. Python Requests Library Integration

The `requests` library is the standard Python library for making synchronous HTTP requests to external REST APIs or web services.

### Core HTTP Methods & Usage

```python
import requests

# 1. GET Request with Query Parameters
response = requests.get(
    "https://api.example.com/items",
    params={"category": "electronics", "page": 1},
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)

if response.status_code == 200:
    data = response.json()  # Automatically parses JSON response
    print("Fetched Data:", data)

# 2. POST Request with JSON Payload
payload = {"name": "Laptop", "price": 999.99}
res_post = requests.post("https://api.example.com/items", json=payload)

# 3. Handling Responses & Errors
try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx codes
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error occurred: {err}")
except requests.exceptions.RequestException as e:
    print(f"An unexpected error occurred: {e}")
```

### Key Differences: `requests` (Sync) vs. `httpx` (Async in FastAPI)

While `requests` is standard for synchronous Python scripts, FastAPI applications performing external API calls often use **`httpx`** or **`aiohttp`** to avoid blocking the ASGI event loop.

| Feature | `requests` | `httpx` |
| :--- | :--- | :--- |
| **Execution Mode** | Synchronous (Blocking) | Sync + Asynchronous (`async`/`await`) |
| **FastAPI Integration** | Great for background workers/celery | Preferred inside `async def` endpoints |
| **API Syntax** | Industry Standard (`requests.get`) | Heavily modeled after `requests` |
