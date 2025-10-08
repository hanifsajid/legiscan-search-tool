from datetime import datetime

current_year = datetime.now().year

STATE_OPTIONS = {
    "ALL": "All States (Default)", "US": "Federal (U.S. Congress)", "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona",
    "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois", "IN": "Indiana",
    "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri",
    "MT": "Montana", "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio",
    "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia",
    "WA": "Washington", "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming"
}

YEAR_OPTIONS = {
    1: "All Years",
    2: "Current Year (Default)",
    3: "Most Recent Year",
    4: "Prior Year",
    9999: "Exact Year (Enter Below)",
}

STATUS_MAP = {
    "All (Default)": "", "Introduced": "introduced", "Engrossed": "engrossed",
    "Enrolled": "enrolled", "Passed": "passed", "Failed": "failed", "Vetoed": "vetoed"
}

CHAMBER_MAP = {
    "All (Default)": "", "Senate": "S", "House": "H", "Assembly": "A"
}

TYPE_MAP = {
    "All (Default)": "", "Bill": "B", "Resolution": "R", "Concurrent Resolution": "CR",
    "Joint Resolution": "JR", "Constitutional Amendment": "CA"
}