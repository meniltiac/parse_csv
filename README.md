# parse_csv
## Quick csv combining script for analytics data for a website with multiple domain names

Combines rows in a csv if they are related to the same page. So for instance, if you have two domain names, one at http and one at https, and a csv that treats those two as separate entities, this script can combine them into one domain name with both of the row values added together. 

To run from the command line, download the code, navigate to its directory, and type 

```
python parse_csv.py path/to/current_csv.csv path/to/csv_to_export.csv
```
