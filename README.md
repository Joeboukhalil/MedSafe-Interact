# MedSafe-Interact
#  Drug Interaction Checker (OpenFDA Enhanced)

A Python program that helps users find **drug interaction risks** and **warnings** using the official [OpenFDA Drug Label API](https://open.fda.gov/apis/drug/label/).

##  Features
- Type one or multiple medicines (e.g. `aspirin, ibuprofen`)
- Shows known drug interactions and FDA warnings
- Clean colored table output (using `rich`)
- 100% free and open-source

##  Installation
```bash pip install requests rich```

## Usage

Run the script:

```bash python drug_interactions.py```


Then type a drug name (or multiple, separated by commas).


## API Used

OpenFDA Drug Label API — public FDA database of approved drugs and their safety information.


## License

MIT License © Joe Bou Khalil
