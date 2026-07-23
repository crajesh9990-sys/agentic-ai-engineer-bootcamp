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