from database import get_db

def checkout_logic():
    db = get_db()
    db.row_factory = None  

    events = db.execute("SELECT fee FROM events").fetchall()

    # The crash line remains commented out
    # 1 / 0

    # OPTIMIZED LOGIC:
    total = 0
    for e in events:
        total += e[0]  # Directly add the fee instead of incrementing by 1
        
    return total