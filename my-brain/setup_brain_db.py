import sqlite3
from datetime import datetime


DB_NAME = "brain.db"


def create_tables(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            createdat TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS business (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            createdat TEXT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS brandvoice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            createdat TEXT NOT NULL
        )
        """
    )


def seed_data(cursor: sqlite3.Cursor) -> None:
    now = datetime.now().isoformat(timespec="seconds")

    knowledge_rows = [
        ("Quy luat 80/20", "Tap trung 20% hanh dong tao ra 80% ket qua.", now),
        ("Insight khach hang", "Khach mua loi ich, khong mua tinh nang.", now),
    ]

    business_rows = [
        ("San pham chu luc", "Goi tu van chuyen doi so cho doanh nghiep nho.", now),
        ("Khach hang muc tieu", "Chu shop online doanh thu 100-500 trieu/thang.", now),
    ]

    brandvoice_rows = [
        ("Tone chu dao", "Than thien, thuc te, huong den hanh dong.", now),
        ("Style viet", "Cau ngan gon, ro rang, uu tien vi du cu the.", now),
    ]

    cursor.executemany(
        "INSERT INTO knowledge (title, content, createdat) VALUES (?, ?, ?)",
        knowledge_rows,
    )
    cursor.executemany(
        "INSERT INTO business (title, content, createdat) VALUES (?, ?, ?)",
        business_rows,
    )
    cursor.executemany(
        "INSERT INTO brandvoice (title, content, createdat) VALUES (?, ?, ?)",
        brandvoice_rows,
    )


def main() -> None:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    create_tables(cursor)
    seed_data(cursor)

    connection.commit()
    connection.close()

    print(f"Da tao xong database '{DB_NAME}' va chen du lieu mau.")


if __name__ == "__main__":
    main()
