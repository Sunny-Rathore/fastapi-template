## **What is SQLAlchemy?**

**SQLAlchemy** is one of the oldest and most widely used **ORM (Object Relational Mapping)** and SQL toolkits in Python. It provides everything you need to interact with relational databases, including schema definitions, queries, transactions, and advanced relationship handling.

You can work with SQLAlchemy in two ways:

*   **Core**: Use raw SQL expressions with Python objects.
*   **ORM**: Define models as Python classes mapped to database tables.

Example:

from sqlalchemy import Column, Integer, String, create\_engine  
from sqlalchemy.orm import declarative\_base, sessionmaker

```
Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
engine = create_engine("sqlite:///example.db")
SessionLocal = sessionmaker(bind=engine)
```

**Pros of SQLAlchemy:**

*   Mature and stable (used in thousands of production systems).
*   Extremely flexible and powerful.
*   Supports complex queries and advanced use cases.

**Cons:**

*   Verbose and requires boilerplate code.
*   If you’re using FastAPI, you’ll often end up writing **separate Pydantic models** for data validation.