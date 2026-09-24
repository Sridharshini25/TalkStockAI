RULES = [
    {
    "trigger": ["average stock", "avg stock", "average stock level"],"sql": lambda c: f"""SELECT AVG(stock_levels) AS avg_stockFROM supply_chain"""},

    {"trigger": ["total revenue", "overall revenue"], "sql": lambda c: f"""SELECT SUM({c['revenue']}) AS total_revenue FROM supply_chain"""},

    {"trigger": ["max revenue", "highest revenue"], "sql": lambda c: f"""SELECT MAX({c['revenue']}) AS max_revenue FROM supply_chain"""},

    {"trigger": ["min revenue", "lowest revenue"], "sql": lambda c: f"""SELECT MIN({c['revenue']}) AS min_revenue FROM supply_chain"""},

    {"trigger": ["avg revenue", "average revenue"], "sql": lambda c: f"""SELECT AVG({c['revenue']}) AS avg_revenue FROM supply_chain"""},

    {"trigger": ["top sku", "top product", "top 5"], "sql": lambda c: f"""SELECT {c['sku']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['sku']} ORDER BY revenue DESC LIMIT 5"""},

    {"trigger": ["bottom sku", "worst product", "least selling"], "sql": lambda c: f"""SELECT {c['sku']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['sku']} ORDER BY revenue ASC LIMIT 5"""},

    {"trigger": ["total qty", "total quantity", "qty sold"], "sql": lambda c: f"""SELECT SUM({c['qty']}) AS total_qty FROM supply_chain"""},

    {"trigger": ["avg price", "average price"], "sql": lambda c: f"""SELECT AVG({c['price']}) AS avg_price FROM supply_chain"""},

    {"trigger": ["max price", "highest price"], "sql": lambda c: f"""SELECT MAX({c['price']}) AS max_price FROM supply_chain"""},

    {"trigger": ["min price", "lowest price"], "sql": lambda c: f"""SELECT MIN({c['price']}) AS min_price FROM supply_chain"""},

    {"trigger": ["supplier revenue", "supplier performance"], "sql": lambda c: f"""SELECT {c['supplier']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['supplier']} ORDER BY revenue DESC"""},

    {"trigger": ["top supplier", "best supplier"], "sql": lambda c: f"""SELECT {c['supplier']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['supplier']} ORDER BY revenue DESC LIMIT 1"""},

    {"trigger": ["bottom supplier", "worst supplier"], "sql": lambda c: f"""SELECT {c['supplier']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['supplier']} ORDER BY revenue ASC LIMIT 1"""},

    {"trigger": ["revenue by sku", "sku revenue"], "sql": lambda c: f"""SELECT {c['sku']}, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY {c['sku']} ORDER BY revenue DESC"""},

    {"trigger": ["revenue by price bucket", "price bucket"], "sql": lambda c: f"""SELECT FLOOR({c['price']} / 100) * 100 AS price_bucket, SUM({c['revenue']}) AS revenue FROM supply_chain GROUP BY price_bucket ORDER BY price_bucket"""},

    {"trigger": ["qty by supplier", "supplier qty"], "sql": lambda c: f"""SELECT {c['supplier']}, SUM({c['qty']}) AS total_qty FROM supply_chain GROUP BY {c['supplier']} ORDER BY total_qty DESC"""},

    {"trigger": ["top expensive sku", "highest priced sku"], "sql": lambda c: f"""SELECT {c['sku']}, {c['price']} FROM supply_chain ORDER BY {c['price']} DESC LIMIT 5"""},

    {"trigger": ["cheapest sku", "lowest priced sku"], "sql": lambda c: f"""SELECT {c['sku']}, {c['price']} FROM supply_chain ORDER BY {c['price']} ASC LIMIT 5"""},

    {"trigger": ["revenue contribution", "sku contribution"], "sql": lambda c: f"""SELECT {c['sku']}, SUM({c['revenue']}) AS revenue, SUM({c['revenue']}) * 100.0 / (SELECT SUM({c['revenue']}) FROM supply_chain) AS contribution_pct FROM supply_chain GROUP BY {c['sku']} ORDER BY contribution_pct DESC"""},

    {"trigger": ["supplier count", "number of suppliers"], "sql": lambda c: f"""SELECT COUNT(DISTINCT {c['supplier']}) AS supplier_count FROM supply_chain"""},
]