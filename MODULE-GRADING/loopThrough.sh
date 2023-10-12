 for file in $(ls ../ASC-Grading/*html) ;
 do  echo $file;
 python3 getTable.py $file;
  done