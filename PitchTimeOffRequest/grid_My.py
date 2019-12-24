ax.query = f"""
    SELECT <ax_fields> 
    FROM "<ax_table>"
    WHERE "employee"="{ax.user_email}";
"""