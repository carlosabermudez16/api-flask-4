instructions = [
    """CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            title TEXT NOT NULL,
            created_date TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        );
    """]