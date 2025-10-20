from jsonschema import validate, ValidationError

# Define the schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["name", "age", "email"]
}

# Example JSON input
data = {
    "name": "Muntasir Rahman Saikat",
    "age": 22,
    "email": "u1902078@student.cuet.ac.bd"
}

# Validate the data
try:
    validate(instance=data, schema=schema)
    print(" JSON is valid! Proceed to insert into database.")
except ValidationError as e:
    print("❌ JSON validation failed:", e.message)
