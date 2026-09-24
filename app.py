import streamlit as st

from src.data_loader import load_data
from src.query_engine import init_engine, ask


st.set_page_config(
    page_title="Talk Stock AI",
    page_icon="📊"
)

st.title("📊 Talk Stock AI")

st.write(
    "Ask questions about your supply chain data using natural language."
)


# Load the data
df = load_data()

# Configuration from the original dataset
config = {
    "sku_name": "SKU",
    "price_column": "Price",
    "qty_sold_column": "Number of products sold",
    "revenue_column": "Revenue generated",
    "supplier_name": "Supplier name"
}

# Initialize the query engine
engine = init_engine(df, config)


question = st.text_input(
    "Ask a question",
    placeholder="Example: Show total revenue"
)


if st.button("Analyze"):
    if question:
        result = ask(question, engine)

        if isinstance(result, str):
            st.error(result)
        else:
            st.subheader("Result")
            st.dataframe(result)
    else:
        st.warning("Please enter a question.")