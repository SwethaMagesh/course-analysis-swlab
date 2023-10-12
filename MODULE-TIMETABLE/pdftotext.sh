#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_pdf>"
    exit 1
fi

input_pdf="$1"
time_table="time_table.txt"
csv_file="tt_record.csv"

# Check if the input PDF file exists
if [ ! -f "$input_pdf" ]; then
    echo "Input PDF file '$input_pdf' not found."
    exit 1
fi

# Check if the temporary text file already exists, and if not, convert the PDF to text
if [ ! -f "$time_table" ]; then
    pdftotext "$input_pdf" "$time_table"
fi

# Find the line with "Lab" and extract the text before it
# lab_line=$(grep -n "Lab" "$time_table" | cut -d ":" -f 1)
# head -n "$lab_line" "$time_table" > "$csv_file"

# Initialize variables for storing records
current_record=""
found_record=false

# Loop through the file
while IFS= read -r line; do
    if [[ "$line" == "CS "* ]]; then
        if [ -n "$current_record" ]; then
            # Format the CSV record and append to the CSV file
            formatted_record=$(echo "$current_record" | sed -e ':a;N;$!ba;s/\n\{1,\}/, /g')
            echo "$formatted_record" >> "$csv_file"
        fi
        current_record="$line"
    else
        current_record="$current_record, $line"
    fi
done < "$csv_file"

echo "Course records have been appended to $csv_file"








# #!/bin/bash

# if [ "$#" -ne 2 ]; then
#     echo "Usage: $0 <input_pdf> <course_match>"
#     exit 1
# fi

# input_pdf="$1"
# course_match="$2"
# time_table="time_table.txt"
# csv_file="tt_record.csv"

# if [ ! -f "$time_table" ]; then
#     pdftotext "$input_pdf" "$time_table"
# fi

# ans=$(sed -n "/$course_match/,/CS/{/$course_match/b;/CS/b;p}" "$time_table")

# if [ -n "$ans" ]; then
#     ans="$course_match, $ans"
    
#     echo "$ans" | sed -e ':a;N;$!ba;s/\n\{1,\}/, /g' >> "$csv_file"
# else
#     echo "No data found for $course_match"
# fi

