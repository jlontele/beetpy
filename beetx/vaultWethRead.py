import balpy

def main():
	
	network = "fantom";
	customConfigFile = "./fantom.json";

	bal = balpy.balpy.balpy(network, customConfigFile=customConfigFile);
	weth = bal.balVaultWeth();
	print("Wrapped ETH Address:", weth);
		
if __name__ == '__main__':
	main();