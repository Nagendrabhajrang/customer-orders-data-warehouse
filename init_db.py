import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_DIR = BASE_DIR / "database"
DB_DIR.mkdir(exist_ok=True)

db_path = DB_DIR / "customer_orders.db"

conn = sqlite3.connect(db_path)

schema = (BASE_DIR / "database" / "schema.sql").read_text(encoding="utf-8")
seed = (BASE_DIR / "database" / "seed.sql").read_text(encoding="utf-8")

conn.executescript(schema)
conn.executescript(seed)
conn.commit()
conn.close()

print("Database created successfully:")
print(db_path)
