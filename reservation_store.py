import sqlite3
from typing import Any, Dict, List, Optional


class ReservationStore:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        connection = sqlite3.connect(self.db_path)
        
        # Create reservations table
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                country TEXT NOT NULL,
                vehicle TEXT NOT NULL,
                usage TEXT,
                timeline TEXT,
                quantity TEXT,
                consent INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        
        # Create inquiries table for business partners
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS inquiries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                inquiry_type TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                country TEXT,
                company_name TEXT,
                contact_name TEXT,
                message TEXT,
                additional_data TEXT,
                consent INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        
        # Add missing columns to reservations table
        for column_sql in [
            "ALTER TABLE reservations ADD COLUMN usage TEXT",
            "ALTER TABLE reservations ADD COLUMN timeline TEXT",
            "ALTER TABLE reservations ADD COLUMN quantity TEXT",
            "ALTER TABLE reservations ADD COLUMN consent INTEGER NOT NULL DEFAULT 0",
        ]:
            try:
                connection.execute(column_sql)
            except sqlite3.OperationalError:
                pass
        
        connection.commit()
        connection.close()

    def save(self, reservation: Dict[str, Any]) -> Optional[int]:
        connection = sqlite3.connect(self.db_path)
        cursor = connection.execute(
            """
            INSERT INTO reservations (name, email, phone, country, vehicle, usage, timeline, quantity, consent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                reservation.get("name", ""),
                reservation.get("email", ""),
                reservation.get("phone", ""),
                reservation.get("country", ""),
                reservation.get("vehicle", ""),
                reservation.get("usage", ""),
                reservation.get("timeline", ""),
                reservation.get("quantity", ""),
                1 if reservation.get("consent") else 0,
            ),
        )
        connection.commit()
        reservation_id = cursor.lastrowid
        connection.close()
        return reservation_id

    def save_inquiry(self, inquiry: Dict[str, Any]) -> Optional[int]:
        """Save business inquiry (manufacturer, distributor, investor)"""
        connection = sqlite3.connect(self.db_path)
        
        # Extract common fields
        inquiry_type = inquiry.get("type", "unknown")
        email = inquiry.get("email", "")
        phone = inquiry.get("phone", "")
        country = inquiry.get("country", "")
        company_name = inquiry.get("company_name", inquiry.get("full_name", ""))
        contact_name = inquiry.get("contact_name", inquiry.get("full_name", ""))
        message = inquiry.get("message", "")
        consent = 1 if inquiry.get("consent") else 0
        
        # Serialize additional data as JSON
        import json
        additional_data = json.dumps(inquiry)
        
        cursor = connection.execute(
            """
            INSERT INTO inquiries (inquiry_type, email, phone, country, company_name, contact_name, message, additional_data, consent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (inquiry_type, email, phone, country, company_name, contact_name, message, additional_data, consent),
        )
        connection.commit()
        inquiry_id = cursor.lastrowid
        connection.close()
        return inquiry_id

    def list_reservations(self) -> List[Dict[str, Any]]:
        connection = sqlite3.connect(self.db_path)
        rows = connection.execute(
            "SELECT id, name, email, phone, country, vehicle, usage, timeline, quantity, consent, created_at FROM reservations ORDER BY id DESC"
        ).fetchall()
        connection.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "phone": row[3],
                "country": row[4],
                "vehicle": row[5],
                "usage": row[6],
                "timeline": row[7],
                "quantity": row[8],
                "consent": bool(row[9]),
                "created_at": row[10],
            }
            for row in rows
        ]

    def list_inquiries(self, inquiry_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """List business inquiries, optionally filtered by type"""
        connection = sqlite3.connect(self.db_path)
        
        if inquiry_type:
            rows = connection.execute(
                "SELECT id, inquiry_type, email, phone, country, company_name, contact_name, message, created_at FROM inquiries WHERE inquiry_type = ? ORDER BY id DESC",
                (inquiry_type,)
            ).fetchall()
        else:
            rows = connection.execute(
                "SELECT id, inquiry_type, email, phone, country, company_name, contact_name, message, created_at FROM inquiries ORDER BY id DESC"
            ).fetchall()
        
        connection.close()

        return [
            {
                "id": row[0],
                "inquiry_type": row[1],
                "email": row[2],
                "phone": row[3],
                "country": row[4],
                "company_name": row[5],
                "contact_name": row[6],
                "message": row[7],
                "created_at": row[8],
            }
            for row in rows
        ]
