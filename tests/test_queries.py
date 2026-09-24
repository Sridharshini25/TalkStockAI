from src.data_loader import load_data
from src.query_engine import init_engine, ask


def create_engine():
    df = load_data()

    config = {
        "sku_name": "SKU",
        "price_column": "Price",
        "qty_sold_column": "Number of products sold",
        "revenue_column": "Revenue generated",
        "supplier_name": "Supplier name"
    }

    return init_engine(df, config)


def test_total_revenue():
    engine = create_engine()

    result = ask("Show total revenue", engine)

    assert result.shape == (1, 1)
    assert result.columns == ["total_revenue"]


def test_average_price():
    engine = create_engine()

    result = ask("Show average price", engine)

    assert result.shape == (1, 1)
    assert result.columns == ["avg_price"]


def test_total_quantity():
    engine = create_engine()

    result = ask("Show total quantity", engine)

    assert result.shape == (1, 1)
    assert result.columns == ["total_qty"]


def test_top_products():
    engine = create_engine()

    result = ask("Show top 5", engine)

    assert result.shape[0] <= 5
    assert "sku" in result.columns


def test_supplier_revenue():
    engine = create_engine()

    result = ask("Show supplier revenue", engine)

    assert "supplier_name" in result.columns
    assert "revenue" in result.columns