POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"},
    },
    "required": ["id"]
}
