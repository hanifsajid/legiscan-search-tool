import streamlit as st
from constants import STATE_OPTIONS, STATUS_MAP, CHAMBER_MAP, TYPE_MAP, YEAR_OPTIONS, current_year

def show_help_section():
        with st.expander("Help and detail about query and input information"):
            st.markdown("""
            ### 1. Basic Query (Full Text Search)
            - Enter keywords or phrases to search bill texts.
            - Example: `vaccination`

            ### 2. Boolean Operators
            - Use `AND`, `OR`, `NOT` and parentheses `( )` for complex logic.
            - Examples:
            - `election AND ballot`
            - `(climate OR environment) AND policy`

            ### 3. Phrase Search
            - Use double quotes for exact phrases.
            - Example: `"National Popular Vote"`

            ### 4. Proximity Operators
            - `ADJ`: terms adjacent in order.
            - `NEAR`: terms near each other in any order.
            - Examples:
            - `personal ADJ property ADJ tax`
            - `abortion OR (pregnancy NEAR termination)`

            ### 5. Meta Filters (Select from dropdowns)
            - **State:** Select one or ALL.
            - **Status:** introduced, engrossed, enrolled, passed, failed, vetoed.
            - **Chamber:** S (Senate), H (House), A (Assembly).
            - **Type:** B (Bill), R (Resolution), CR, JR, CA.
            - **Intro Date / Action Date:** today, yesterday, week, month, year, or `YYYYMMDD..YYYYMMDD` range.

            ### 6. Combining Queries and Filters
            - Example: Query = `(alternative ADJ fuel)`, Status = `introduced`, Chamber = `S`  
            Searches for introduced Senate bills about alternative fuels.

            ### 7. Date Filters
            - `intro:today` - Bills introduced today.
            - `action:20220101..20220115` - Actions in date range.""")


# def show_sidebar():
#     with st.sidebar:
#         st.header("🔐 API Key")
#         api_key = st.text_input("Enter LegiScan API Key", type="password", key="api_key_input")
#         if api_key:
#             st.session_state.api_key = api_key
#             st.success("API key stored in session.")
#         show_help_section()
#         return api_key


def footer():
    st.sidebar.markdown("""---""")
    st.sidebar.markdown("""
                        ## 📜 LegiScan Search Tool 
**Disclaimer**: This project is for demonstration and research purposes only. Data is provided via LegiScan’s public API and subject to their availability and rate limits.

Built by [Hanif Ullah Sajid](https://hanifsajid.github.io)  
Developed at SPaD Lab   
Powered by [LegiScan API](https://legiscan.com)  
[GitHub Repository](https://github.com/hanifsajid/legiscan-search-tool.git)
    """)

def show_sidebar():
    with st.sidebar:
        st.header("🔐 API Key")
        st.caption("Your API key is stored only in this session and never sent anywhere else.")
        st.caption("If you do not have an API key, please [register here on LegiScan](https://legiscan.com/user/register) to obtain one.")

        # If an API key is already stored, show status and reset button
        if "api_key" in st.session_state:
            st.success("✅ API key is set.")

            if st.button("🔁 Reset API Key"):
                st.session_state.pop("api_key", None)
                st.session_state.pop("api_key_input", None)
                st.experimental_rerun()

        else:
            # Show input box if no key is stored
            api_key = st.text_input("Enter LegiScan API Key",
                                    type="password", key="api_key_input",)
                                    #help= 'If you do not have an API key, please [register here on LegiScan](https://legiscan.com/user/register) to obtain one.')
            if api_key:
                st.session_state.api_key = api_key
                st.success("✅ API key stored in session.")

        show_help_section()

        st.info("If you encounter any issue(s), please [create an issue on GitHub](https://github.com/hanifsajid/legiscan-search-tool/issues).", icon="🐞")
        footer()

        return st.session_state.get("api_key")



def get_main_inputs():
    query = st.text_input("Search Query", help="Enter keywords or Boolean expressions. See the help section in the sidebar for details.")
    state = st.selectbox("State", options=list(STATE_OPTIONS), format_func=lambda x: STATE_OPTIONS[x], index=0, help="Any US state, All states, or US Congress")
    selected_year_option = st.selectbox("Year", options=list(YEAR_OPTIONS),
                                        format_func=lambda x: YEAR_OPTIONS[x],
                                        index=1,
                                        help="Choose a general year option or enter an exact year after 1900 (no future years).")

    if selected_year_option == 9999:
        exact_year = st.number_input("Enter Exact Year", min_value=1900,
                               max_value=current_year, value=current_year,
                               step=1, help="Enter a year greater than 1900 and no later than the current year.")
        year = int(exact_year)
    
    else:
        year = selected_year_option

    return query, state, year

def get_optional_filters():
    status = STATUS_MAP[st.selectbox("Bill Status", STATUS_MAP, index=0, help="Filter by bill status (or select All to include any status).")]
    chamber = CHAMBER_MAP[st.selectbox("Chamber", CHAMBER_MAP, index=0, help="Filter by chamber (or select All to include any chamber).")]
    bill_type = TYPE_MAP[st.selectbox("Bill Type", TYPE_MAP, index=0, help="Filter by bill type (or select All to include all types).")]
    intro_date = st.text_input("Intro Date Filter", placeholder="e.g. today, yesterday, YYYYMMDD..YYYYMMDD", help="Use 'today', 'yesterday', 'week', 'month', 'year' or static format like 20230101 or 20230101..20230131")
    action_date = st.text_input("Action Date Filter", placeholder="e.g. today, yesterday, YYYYMMDD..YYYYMMDD", help="Use 'today', 'yesterday', 'week', 'month', 'year' or static format like 20230101 or 20230101..20230131")
    return status, chamber, bill_type, intro_date, action_date

def validate_inputs(api_key, query) -> bool:
    if not api_key:
        st.warning("Please enter your API key.")
        return False
    if not query or not query.strip():
        st.warning("Please enter a search query.")
        return False
    return True