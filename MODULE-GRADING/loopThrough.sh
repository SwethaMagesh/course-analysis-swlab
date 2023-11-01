 cd ../ASC-Grading/SingleFile
 for file in $(ls *html) ;
 do  
 python3 ../../MODULE-GRADING/getTable.py $file;
  done

# python3 ../MODULE-GRADING/getTable.py cs601.html