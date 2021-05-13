import pandas as pd


JOBS_FILENAME = 'jobs.xlsx'
COLUMNS = ['Company', 'Position Name', 'Date Applied', 'Last Contact',
           'Via', 'Status', 'Job Posting URL']
df = None

def setup_function():
    global df
    if df is not None: return # only load it once
    try:
        df = pd.read_excel(JOBS_FILENAME)
    except FileNotFoundError:
        print(f"Jobs file {JOBS_FILENAME} is not found in the root of this repository")

def test_column_names():
    '''
    Test that the sheet includes the necessary columns
    '''
    assert(df is not None)
    assert(set(COLUMNS).issubset(df.columns))
    # assert(set(df.columns) == set(COLUMNS))

def test_missing_companies():
    '''
    Test that every row has info for Company column
    '''
    assert(df is not None)
    nmissing_companies = sum(df['Company'].isna()) if 'Company' in df.columns else 0
    assert(nmissing_companies == 0)

def test_missing_date_applied():
    '''
    Test that every row has info for Data Applied column
    '''
    assert(df is not None)
    nmissing_date_applied = sum(df['Date Applied'].isna()) if 'Date Applied' in df.columns else 0
    assert(nmissing_date_applied == 0)

def test_missing_status():
    '''
    Test that every row has info for Status column
    '''
    assert(df is not None)
    nmissing_status = sum(df['Status'].isna()) if 'Status' in df.columns else 0
    assert(nmissing_status == 0)
