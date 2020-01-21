ax.query = f"""
    SELECT {ax.db_fields}
    FROM "{ax.db_table}"
    WHERE "employee"='{ax.user_email}';
"""