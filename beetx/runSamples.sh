python3 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install balpy

source fantom.env

python3 getPools.py
python3 vaultWethRead.py

deactivate
