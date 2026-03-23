Verify the integrity of the main datasets.

Steps:
1. Read `config.py` to get the clean/ data paths.
2. For each dataset found in clean/, run a Python snippet to check:
   - Number of rows and columns
   - Column names
   - Number of missing values per column
   - Date range (if a date column exists)
   - Duplicate rows
3. Display a summary table per dataset.
4. Flag any anomalies: empty files, excessive missing values (>20%), unexpected row counts.
5. If no clean data exists yet, report that and show what raw data is available.
