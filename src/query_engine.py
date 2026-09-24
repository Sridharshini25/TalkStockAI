import polars as pl
import datafusion
import pyarrow.dataset as ds
from src.rules import RULES

def init_engine(df, config_dict):
    """
    Initializes DataFusion engine with:
    - cleaned dataframe column names
    - cleaned config column mappings
    """

    cleaned_cols = [col.lower().replace(" ", "_") for col in df.columns]
    df = df.rename({old: new for old, new in zip(df.columns, cleaned_cols)})

    def clean(col):
        if not col:
            return None
        return col.lower().replace(" ", "_")

    config = {
        "sku": clean(config_dict.get("sku_name")),
        "price": clean(config_dict.get("price_column")),
        "qty": clean(config_dict.get("qty_sold_column")),
        "revenue": clean(config_dict.get("revenue_column")),
        "supplier": clean(config_dict.get("supplier_name")),
    }

    ctx = datafusion.SessionContext()
    arrow_df = df.to_arrow()
    dataset = ds.dataset(arrow_df)
    ctx.register_dataset("supply_chain", dataset)
    return {"ctx": ctx, "config": config}


def text_to_sql(question, config):
    """
    Converts the user's natural language question into an SQL query
    by checking which rule matches the text. Uses the column names
    defined in the config to dynamically build the SQL.
    """
    q = question.lower()

    for rule in RULES:
        if any(t in q for t in rule["trigger"]):
            return rule["sql"](config)

    return "SELECT * FROM supply_chain LIMIT 10"


def ask(question, engine):
    """
    Takes a user question, converts it to SQL, runs it on the
    DataFusion engine, and returns the result as a Polars DataFrame.
    Shows SQL errors if the query is invalid.
    """
    ctx = engine["ctx"]
    config = engine["config"]

    sql = text_to_sql(question, config)
    print(f"\nGenerated SQL:\n{sql}\n")

    try:
        result = ctx.sql(sql).to_polars()
        return result
    except Exception as e:
        return f"SQL Error: {e}"