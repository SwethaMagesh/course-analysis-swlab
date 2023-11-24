#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_pdf> <course_match>"
    exit 1
fi

input_pdf="$1"
time_table=$1"time_table.txt" 
without_lab_data_file=$1"only_timetable.txt"

rm -f "$time_table" "$without_lab_data_file"
if [ ! -f "$time_table" ]; then
    pdftotext -layout "$input_pdf" "$time_table"
fi

echo "$time_table"
if [ ! -f "$without_lab_data_file" ]; then
    without_lab_data=$(mktemp)
     sed '/Lab:/,$d' "$time_table" > "$without_lab_data"
    mv "$without_lab_data" "$without_lab_data_file"
fi

sed -i 's/CS /\nCS/g'  "$without_lab_data_file" 
sed -i 's/\n//g' "$without_lab_data_file"


