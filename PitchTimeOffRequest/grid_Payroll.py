ax.query = f"""
    SELECT {ax.db_fields}
    FROM "{ax.db_table}"
    WHERE "axState"='Payroll Processing';
"""