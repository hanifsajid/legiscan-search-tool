import streamlit as st
import time

from constants import STATE_OPTIONS
from ui import show_help_section, show_sidebar, get_main_inputs, get_optional_filters, validate_inputs
from api import fetch_page, flatten_results
from utils import build_full_query, prepare_download

def main():
    st.set_page_config(page_title="LegiScan Legislative Search", layout="wide")
    # st.title("LegiScan Search Tool")

    st.markdown("""
    <h1 style='font-family:Montserrat, sans-serif; font-size: 36px; font-weight:700; color:#004466;  text-align: center;'>
        📜 LegiScan Search Tool
    </h1> """, unsafe_allow_html=True)

    api_key = show_sidebar()

    query, state, year = get_main_inputs()


    with st.expander("⚙️ Optional Filters"):
        status, chamber, bill_type, intro_date, action_date = get_optional_filters()

    if not validate_inputs(st.session_state.get("api_key"), query):
        st.stop()

    full_query = build_full_query(query, status, chamber, bill_type, intro_date, action_date)

    # Initial fetch
    try:
        first_response = fetch_page(st.session_state.api_key, full_query, year, 1, state)
        if first_response.get('status') != 'OK':
            raise ValueError("Invalid API response: " + str(first_response))
        summary = first_response.get('searchresult', {}).get('summary', {})
        page_total = summary.get('page_total', 0)
        result_count = summary.get('count', 0)
        if not page_total or result_count == 0:
            st.warning("No results found for your query.")
            st.stop()
    except Exception as e:
        st.error(f"API call failed: {e}")
        st.stop()

    delay = st.slider("⏱️ Delay between API requests (sec)", 0.0, 2.0, 0.5, step=0.1)
    file_format = st.radio("📄 Output format", ["csv", "json"], index=0)
    st.success(f"✅ Found {result_count} record(s) across {page_total} page(s).")

    if st.button("📥 Fetch Records"):
        all_results = flatten_results(first_response['searchresult'])
        progress = st.progress(1 / page_total)

        for page in range(2, page_total + 1):
            try:
                response = fetch_page(st.session_state.api_key, full_query, year, page, state)
                if response.get('status') != 'OK':
                    st.warning(f"API error on page {page}: {response}")
                    break
                results = flatten_results(response['searchresult'])
                all_results.extend(results)
                progress.progress(page / page_total)
                time.sleep(delay)
            except Exception as e:
                st.error(f"Failed on page {page}: {e}")
                break

        st.success(f"✅ Fetched {len(all_results)} record(s) from {page_total} page(s).")
        st.dataframe(all_results)

        file_bytes, ext, mime = prepare_download(all_results, file_format)
        st.download_button(
            label=f"⬇️ Download as {ext.upper()}",
            data=file_bytes,
            file_name=f"legiscan_results.{ext}",
            mime=mime
        )

     



if __name__ == "__main__":
    main()