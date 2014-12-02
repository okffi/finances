finances
========

OKF Finland finances, scripts and data

These scripts maybe be useful to anyone who wants to aggregate data
from several Holvi accounts. You first need an API key that is connected
to all the Holvi accounts you wish to process.

1. Change the list of Holvi IDs in holvilist.txt to match your own.
2. Load budget information by calling "./loadholvibudgets.sh holvilist.txt" and enter your Holvi API key when prompted.
3. Enjoy your fresh json files!
4. Run "python ./createbudgettables.py" to create budget.csv that combines all Holvi accounts into one table.

