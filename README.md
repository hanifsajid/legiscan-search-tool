# 📜 [LegiScan Search Tool](https://legiscansearch.streamlit.app)

A Streamlit web app that allows users to search, filter, and download U.S. legislative data via the [LegiScan API](https://legiscan.com/). Search across states and US Congress, filter by status, chamber, type, dates, and export results in CSV or JSON.

## Features

- Full-text search with Boolean operators (`AND`, `OR`, `NOT`, etc.)
- Search by U.S. state or federal level
- Filter by:
  - Bill status
  - Chamber (Senate, House, etc.)
  - Bill type (Bill, Resolution, etc.)
  - Intro/action date ranges
- Fetch multiple pages of results
- Export results as `.csv` or `.json`
- Built-in help and usage guide

## Live Demo

You can run this app locally using Streamlit (instructions below) or [click here](https://legiscansearch.streamlit.app) to open it in your browser.

## Folder Structure

```bash
legiscan-search-app/
├── main.py           # Main entry point
├── api.py            # API fetch and result handling
├── ui.py             # Streamlit UI components
├── utils.py          # Query builder and download logic
├── constants.py      # Static data and dropdown mappings
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Installation

1. **Clone the repo**

```bash
git clone https://github.com/hanifsajid/legiscan-search-tool.git
cd legiscan-search-tool
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run main.py
```

## API Key Required

You need a valid [LegiScan API Key](https://legiscan.com/legiscan) to use this app.

* Enter your API key in the app sidebar on first run.
* The key is stored in session memory only and not saved permanently.

## Usage Tips

* Use exact phrases in quotes: `"climate change"`
* Use advanced syntax: `(election OR voting) AND (security NOT fraud)`
* Use filters like `status:introduced`, `chamber:S`, `intro:today`, `action:20230101..20230131`

See the **Help** section in the app for full query examples.

## Disclaimer

This project is for demonstration and research purposes only. Data is provided via LegiScan’s public API and subject to their availability and rate limits.

## Contributions

Pull requests, feature suggestions, and issue reports are welcome!
