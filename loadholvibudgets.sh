#!/bin/bash
echo -n "Enter Token: "
read -s password
for line in $(cat $1);
do
echo "Loading $line..."
holvi=$(echo $line | cut -d'#' -f1)
echo "Holvi: $holvi"
curl https://holvi.com/api/pool/$holvi/openbudget/ -H "Authorization: Token $password" -o "$holvi.json"
done
