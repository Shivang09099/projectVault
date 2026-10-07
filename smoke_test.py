import sqlite3
from pathlib import Path

from app import app, DB_PATH

assert app.title == "ProjectVault"
assert DB_PATH.exists()
with sqlite3.connect(DB_PATH) as conn:
    assert conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0] >= 6
    assert conn.execute("SELECT COUNT(*) FROM projects WHERE status='approved'").fetchone()[0] >= 5
print("ProjectVault smoke test passed")
