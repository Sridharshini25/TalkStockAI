# Talk Stock AI

Talk Stock AI is a rule-based Natural Language to SQL engine for supply chain analytics.

It allows users to ask questions about supply chain data using natural language. The system identifies predefined query patterns, generates SQL dynamically, executes the SQL using Apache DataFusion, and displays the results through a Streamlit interface.

## Features

- Natural language querying of supply chain data
- Rule-based NLP to SQL conversion
- Dynamic SQL generation using dataset column mappings
- SQL execution using Apache DataFusion
- High-performance data processing using Polars and PyArrow
- Interactive Streamlit interface
- Automated tests using pytest

## Architecture

```text
User
  ↓
Streamlit UI
  ↓
Rule-based NLP Processor
  ↓
SQL Query
  ↓
Apache DataFusion
  ↓
Polars / PyArrow
  ↓
Result

## Technologies Used

- Python
- Polars
- Apache DataFusion
- PyArrow
- Streamlit
- Pytest

Project Structure
TalkStockAI/
│
├── data/
│   └── supply_chain_data.csv
│
├── src/
│   ├── data_loader.py
│   ├── query_engine.py
│   ├── rules.py
│   └── __init__.py
│
├── tests/
│   └── test_queries.py
│
├── app.py
├── README.md
└── .gitignore

Example Queries

The application supports questions such as:

Show total revenue
Show average price
Show top 5
Show supplier revenue
Show total quantity
Show maximum revenue
Show minimum revenue
Show average revenue
Show top supplier
Show bottom supplier

Installation

Clone the repository:

git clone https://github.com/Sridharshini25/TalkStockAI.git
cd TalkStockAI

Create a virtual environment:

python -m venv .venv

Activate the virtual environment on Windows:

.venv\Scripts\Activate.ps1

Install the required packages:

pip install polars pyarrow datafusion streamlit plotly pytest
Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

Run Tests

Run the test suite using:

python -m pytest

Project Purpose

This project demonstrates how natural language queries can be mapped to SQL using rule-based NLP techniques and then executed efficiently on structured supply chain data.