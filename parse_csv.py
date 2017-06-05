import csv
import sys

def strip_prefix(input_string, prefix):
    if input_string.startswith(prefix):
        return input_string[len(prefix):]
    return input_string

def add_to_output(export_output, row, prefix):
    if row['URL'].startswith(prefix):
        endurl = strip_prefix(row['URL'], prefix)
        if endurl in export_output:
            old_row = export_output[endurl]
            for col in row.keys():
                if col == "URL":
                    row[col] = "https://www.parse.ly" + endurl
                    continue
                try:
                    if old_row[col] != "":
                        old_val = float(old_row[col])
                    else:
                        old_val = 0.0
                    if row[col] != "":
                        new_val = float(row[col])
                    else:
                        new_val = 0.0
                    row[col] = str( old_val + new_val )
                except ValueError:
                    if row[col] == "":
                        row[col] = old_row[col]
                    elif old_row[col] == "":
                        pass
                    elif row[col] != old_row[col]:
                        row[col] = old_row[col] + " / " + row[col]
            export_output[endurl] = row
        else:
            row['URL'] = "https://www.parse.ly" + endurl
            export_output[endurl] = row
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Watch out! You need to add in input and output filenames!")
    export_output = {}
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    with open(input_filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        trashed_domains = ['https://www-alpha.parsely.com/', 'http://2015.parse.ly', 'https://www-beta.parsely.com', 'http://www-alpha.parsely.com/', 'http://localhost', 'https://beta.parse.ly/', 'https://alpha.parse.ly', 'https://2014.parse.ly/']
        for row in reader:
            if add_to_output(export_output, row, 'https://www.parsely.com'):
                pass
            elif add_to_output(export_output, row, 'https://www.parse.ly'):
                pass
            elif add_to_output(export_output, row, 'http://www.parsely.com'):
                pass
            elif add_to_output(export_output, row, 'https://parse.ly'):
                pass
            else:
                trash = False
                for domain in trashed_domains:
                    if row['URL'].startswith(domain):
                        trash = True
                        break
                if not trash:
                    export_output[row['URL']] = row

    with open(output_filename, 'wb') as outfile:
        writer = csv.DictWriter(outfile, reader.fieldnames)
        writer.writeheader()
        for url, row in export_output.iteritems():
            writer.writerow(row)
