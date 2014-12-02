#!/bin/bash
echo -n "Enter Token: "
read -s password
for line in $(cat $1);
do
echo "Loading $line..."
curl https://holvi.com/api/pool/$line/openbudget/ -H "Authorization: Token $password" -o "$line.json"
done
