## Note: This is a fork of Balancer Lab's Balpy software.  This repo includes the configuration files for the BeethovenX deployments on Fantom.  

Balpy has the ability to import custom configuration files where you can define the contract addresses for your Balancer v2 deployment.  
Add the following to the script using balpy while having the fantom.json (beetx/fantom.json)
```bash
	network = "fantom";
	customConfigFile = "./fantom.json";

	bal = balpy.balpy.balpy(network, customConfigFile=customConfigFile);
```
If the subgraph is used, it must be replaced with Beethovenx's subgraph link
https://graph.beethovenx.io/subgraphs/name/beethovenx
(beetx/runSamples.sh)

If you are looking to deploy a pool, use beetx/poolCreationSample.py.
Usage:

```bash
export BALPY_CUSTOM_RPC="https://rpc.ftm.tools/"

python3 poolCreationSample.py ./link/to/pool.json 
```
export KEY_PRIVATE=[your key]
# balpy
Python tools for interacting with Balancer Protocol V2 in Python. 

DISCLAIMER: While balpy is intended to be a useful tool to simplify interacting with Balancer V2 Smart Contracts, this package is an ALPHA-build and should be considered as such. Use at your own risk! This package is capable of sending Ethereum tokens controlled by whatever private key you provide. User assumes all liability for using this software; contributors to this package are not liable for any undesirable results. Users are STRONGLY encouraged to experiment with this package on testnets before using it on mainnet with valuable assets.

## Usage
balpy has been tested on:
- MacOS using Python 3.9.0
- Linux using Python 3.9-dev
- Windows using Python 3.9.5

### Install
I recommend using a virtual environment:
```bash
python3 -m venv ./venv
source ./venv/bin/activate
python3 -m pip install balpy
```
See release on PyPI: https://pypi.org/project/balpy/

### Build from source
```bash
git clone https://github.com/gerrrg/balpy.git
cd balpy
python3 -m build
python3 -m pip install dist/<your_build>.whl
```

### Environment Variables
You must set these two environment variables in order to use the balpy module
- KEY_API_ETHERSCAN: 	API key for Etherscan for gas prices
- KEY_PRIVATE: 			Plain text private key for signing transactions

You also must set AT LEAST one of these environment variables to connect to the network
- KEY_API_INFURA: 		API key for Infura for sending transactions
- BALPY_CUSTOM_RPC:   Custom RPC URL (like localhost or Polygon RPC)


## Samples
See README.md in samples/ for more information.
