from brownie import network, AdvancedCollectible
import time
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_contract, get_account
from scripts.advanced_collectible.deploy_and_create import deploy_and_create

def test_can_create_advanced_collectible_integration():
    # deploy the contract
    # create and NFT
    # get a random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
    # original_tokencounter = advanced_collectible.tokenCounter()
    # assert advanced_collectible.tokenCounter() == original_tokencounter + 1
