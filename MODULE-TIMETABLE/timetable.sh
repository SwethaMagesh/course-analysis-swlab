for file in *.pdf; do
    ./extractFromPDF1.sh "$file"
done
for file in *.csv; do
    python3 generateCSV.py "$file"
done
make clean