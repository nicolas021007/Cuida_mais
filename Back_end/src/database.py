TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3"

}, 
    "apps": {
        "models": {
            "models": ["models.doutores", "models.pacientes", "aerich.models"],
            "default_connection": "default",
        }
    },
}