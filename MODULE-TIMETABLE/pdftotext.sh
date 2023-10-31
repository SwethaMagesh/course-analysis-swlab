#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_pdf> <course_match>"
    exit 1
fi

input_pdf="$1"
time_table="time_table.txt"
csv_file="tt_record.csv"
without_lab_data_file="only_timetable.txt"

rm -f "$time_table" "$csv_file" "$without_lab_data_file"
touch $csv_file

if [ ! -f "$time_table" ]; then
    pdftotext "$input_pdf" "$time_table"
fi

if [ ! -f "$without_lab_data_file" ]; then
    without_lab_data=$(mktemp)
    sed '/Lab:/,$d' "$time_table" > "$without_lab_data"
    mv "$without_lab_data" "$without_lab_data_file"
fi

current_record=""
found_record=false

# Loop through the file
while IFS= read -r line; do
    if [[ "$line" == "CS"* ]]; then
        if [ -n "$current_record" ]; then
            # Format the CSV record and append to the CSV file
            formatted_record=$(echo "$current_record" | sed -e ':a;N;$!ba;s/\n\{1,\}/, /g; s/, ,/, /g')
            echo "$formatted_record" >> "$csv_file"
        fi
        current_record="$line"
    else
        current_record="$current_record, $line"
    fi
done < "$without_lab_data_file"

sed -i '1s/.*/Course Code, Slot, Venue, Course Title, Instructor/' "$csv_file"
sed -i 's/, ,/,/g;' "$csv_file"
sed -i 's/, $//' "$csv_file"
echo "Course records have been appended to $csv_file"
