# Talk Stock AI

Talk Stock AI is a rule-based Natural Language to SQL engine for supply chain analytics.

It allows users to ask questions about supply chain data using natural language. The system identifies predefined query patterns, generates SQL queries dynamically, executes them using Apache DataFusion, and displays the results through a Streamlit interface.

## Features

- Natural language querying of supply chain data
- Rule-based Natural Language Processing (NLP) to SQL conversion
- Dynamic SQL query generation
- Supply chain revenue and product analysis
- Supplier performance analysis
- Data processing using Polars
- SQL execution using Apache DataFusion
- Data handling using PyArrow
- Interactive Streamlit web interface
- Automated testing using pytest

## Architecture

```text
User
  |
  v
Streamlit UI
  |
  v
Rule-based NLP Processor
  |
  v
SQL Query
  |
  v
Apache DataFusion
  |
  v
Polars / PyArrow
  |
  v
Result
```

## Technologies Used

- Python
- Polars
- Apache DataFusion
- PyArrow
- Streamlit
- Plotly
- Pytest

## Project Structure

```text
TalkStockAI/
|
├── data/
│   └── supply_chain_data.csv
|
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── query_engine.py
│   └── rules.py
|
├── tests/
│   └── test_queries.py
|
├── app.py
├── README.md
├── .gitignore
└── TalkStockAI.iml
```

## Supported Queries

The application supports natural language questions such as:

- Show total revenue
- Show maximum revenue
- Show minimum revenue
- Show average revenue
- Show top 5 products
- Show bottom products
- Show total quantity
- Show average price
- Show maximum price
- Show minimum price
- Show supplier revenue
- Show top supplier
- Show bottom supplier
- Show revenue by SKU
- Show quantity by supplier
- Show highest priced SKU
- Show cheapest SKU
- Show revenue contribution
- Show supplier count

## Dataset

The project uses a supply chain dataset containing information about:

- Products
- SKUs
- Prices
- Product availability
- Products sold
- Revenue
- Stock levels
- Lead times
- Order quantities
- Shipping information
- Suppliers
- Locations
- Production volumes
- Manufacturing costs
- Inspection results
- Defect rates
- Transportation modes

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sridharshini25/TalkStockAI.git
```

Move into the project directory:

```bash
cd TalkStockAI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Required Libraries

```bash
pip install polars pyarrow datafusion streamlit plotly pytest
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

You can then enter questions such as:

```text
Show total revenue
```

or:

```text
Show supplier revenue
```

and click **Analyze** to view the results.

## Run Tests

To run the automated tests:

```bash
python -m pytest
```

The project contains tests for:

- Total revenue
- Average price
- Total quantity
- Top products
- Supplier revenue

## How It Works

1. The user enters a question in the Streamlit interface.
2. The question is processed by the rule-based NLP engine.
3. The system identifies a matching predefined rule.
4. The corresponding SQL query is generated dynamically.
5. Apache DataFusion executes the SQL query.
6. The result is converted into a Polars DataFrame.
7. Streamlit displays the result to the user.

## Project Purpose

This project demonstrates how rule-based Natural Language Processing can be used to convert natural language questions into SQL queries and perform analytics on structured supply chain data.

## Author

**Sridharshini**