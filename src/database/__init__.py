
def get_db() -> Database:
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)
    if db is None:
        if mongo.cx is None:
            raise ValueError("Cannot create mongodb client instance")

        db = g._database = mongo.cx.get_database(ENV.DATABASE_NAME)
        if db is None:
            raise ValueError(
                f"Cannot get mongodb database, Name: {ENV.DATABASE_NAME}"
            )

    if not isinstance(db, Database):
        raise TypeError(
            "DB (_database) instance in app global context is not instance of pymongo.database.Database"
        )

    return db


# Use LocalProxy to read the global db instance with just `db`
db: Database = LocalProxy(get_db)  # type: ignore
