

CREATE TABLE IF NOT EXISTS products (
    ware_id TEXT PRIMARY KEY,
    weight_kg REAL,
    sales_per_month INTEGER,
    picks_per_month INTEGER,
    length_cm REAL,
    width_cm REAL,
    height_cm REAL
);


CREATE TABLE IF NOT EXISTS shelves (
    shelf_id TEXT PRIMARY KEY,
    x REAL NOT NULL,
    y REAL NOT NULL,
    width REAL NOT NULL,
    height REAL NOT NULL,
    rotation REAL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS locations (
    location_id TEXT PRIMARY KEY,
    shelf_id TEXT NOT NULL,
    position INTEGER NOT NULL,
    max_weight_kg REAL,
    warehouse_id TEXT NOT NULL,

    FOREIGN KEY (shelf_id)
        REFERENCES shelves(shelf_id)
        ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS optimization_runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    alpha REAL,
    beta REAL,
    total_cost REAL
);


CREATE TABLE IF NOT EXISTS recommended_assignments (
    run_id INTEGER NOT NULL,
    ware_id TEXT NOT NULL,
    location_id TEXT NOT NULL,
    assignment_cost REAL,

    PRIMARY KEY (run_id, ware_id),

    FOREIGN KEY (run_id)
        REFERENCES optimization_runs(run_id),

    FOREIGN KEY (ware_id)
        REFERENCES products(ware_id),

    FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);