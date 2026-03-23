List all notebooks in the project and flag any issues.

Steps:
1. Search for all `.ipynb` files under `code/`.
2. For each notebook, show:
   - File path
   - Last modified date
   - Number of cells
   - Whether it has been executed (any output cells?)
3. Flag notebooks that:
   - Have no output (never run or cleared)
   - Have error outputs in any cell
   - Are in the root of a build folder (should be in a `notebooks/` subfolder)
4. Suggest which notebooks should be converted to `.py` scripts.
