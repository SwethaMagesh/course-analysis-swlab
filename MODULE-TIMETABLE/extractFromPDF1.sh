#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_pdf>"
    exit 1
fi

input_pdf="$1"
time_table=$1"_tt_raw.txt" 
just_tt2=$1"_tt.txt"

rm -f "$time_table" "$just_tt2"
if [ ! -f "$time_table" ]; then
    pdftotext -layout "$input_pdf" "$time_table"
fi

echo "$time_table"
if [ ! -f "$just_tt2" ]; then
    just_tt=$(mktemp)
     sed '/Lab:/,$d' "$time_table" > "$just_tt"
    mv "$just_tt" "$just_tt2"
fi

sed -i 's/CS /\nCS/g'  "$just_tt2" 
sed -i 's/^\(CS[0-9]*\) M/\1/' "$just_tt2" 
grep -v '^[[:space:]]*$' "$just_tt2" > output.txt
tail -n +3 output.txt > output_file.txt
awk '{printf "%s,%s,%s,%s\n", $1, $2, $3, substr($0, index($0,$4))}' output_file.txt > $1".csv"

