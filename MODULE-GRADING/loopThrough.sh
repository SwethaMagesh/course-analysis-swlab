
 cd ../ASC-Grading/$1
#  $1 is year of grading stats
rm ../../MODULE-GRADING/$1grades.json
 for file in $(ls *html) ;
 do  
 touch ../../MODULE-GRADING/$1grades.json
 python3 ../../MODULE-GRADING/getTable.py $file $1;
  done

# python3 ../MODULE-GRADING/getTable.py cs601.html