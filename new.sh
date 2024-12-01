#!/bin/bash

year=$1
day=$2

if [ -z $year ] || [ -z $day ]; then
  echo "You forgot to supply all the params!"
  echo ""
  echo "    Usage:"
  echo "      new.sh <year> <day>"
  echo ""
  exit 1
fi

echo "Creating a new day..."
folder=$year/"day${day}"

# create folder and make files
mkdir -p $folder
touch $folder/input.txt $folder/test_1.txt $folder/part_1_test_1_result.txt
cp solution.py.template $folder/solution.py

# nice replace in file the year and day for the link
sed -i "s/<YEAR>/${year}/g" $folder/solution.py
sed -i "s/<DAY>/${day}/g" $folder/solution.py

echo "Created!"
