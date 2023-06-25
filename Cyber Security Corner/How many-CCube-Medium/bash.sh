#! /bin/bash
sum=0
while read -r line; do
  field3=$(echo "$line" | cut -d' ' -f3)
  if [[ "$field3" =~ ^(553|828|723|698)$ ]]; then
    field5=$(echo "$line" | cut -d' ' -f5)
    sum=$((sum + field5))
  fi
done < users.txt

echo "Total count of USER IDs are: $sum"
