# read raw csv file and generate a new csv file

import csv
import sys

# get fname from args
fname = sys.argv[1]
# open the file
processed_rows = []
with open(fname, 'r', newline='') as infile:
    reader = csv.reader(infile)
    processed_codes = []
    for row in reader:
        # Task 1: Check if the row has 4 columns  and starts with 'cs' in the 1st column
        if len(row) == 4 and row[0].lower().startswith('cs') and row[0] not in processed_codes:
            if(len(row[2])) == 1:
                row[2] = '-'
            try:
                row[1] = int(row[1])
            except:
                row[1] = 0
                continue

            # Task 2: Split the last column where 'Prof' begins
            row[-1] = ' '.join(row[-1].split())
            last_column_parts = row[-1].split('Prof.')
            title = last_column_parts[0].strip()
            row = row[:-1]

            # Write the processed row to the output file
            if len(title) == 0:
                continue
            row.append(title)
            row.append('Prof. ' + last_column_parts[-1].strip() )
            processed_codes.append(row[0])
            processed_rows.append(row)


with open(fname, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Task 3: Write the header row
    writer.writerow(['Course Code','Slot', 'Venue', 'Course Title', 'Instructor'])
    
    # Task 4: Write the processed rows
    writer.writerows(processed_rows)

print("Processing completed. Output written to", fname)