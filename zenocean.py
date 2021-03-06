import os
from web3 import Web3
from ocean_lib.ocean.ocean import Ocean
from ocean_lib.config import Config
from ocean_lib.config import Config
from ocean_lib.config_provider import ConfigProvider
from ocean_lib.ocean.util import get_web3_connection_provider
from ocean_lib.web3_internal.web3_provider import Web3Provider, CustomHTTPProvider
from ocean_lib.data_provider.data_service_provider import DataServiceProvider
from ocean_utils.agreements.service_factory import ServiceDescriptor
from ocean_lib.web3_internal.contract_handler import ContractHandler
from ocean_lib.web3_internal.wallet import Wallet

def run_scenario():
    config = Config('config.ini')
    ocean = Ocean(config)
    wallet = Wallet(ocean.web3, 0x376e05899a4ae00463a3a607c774069b7d6a647860dba723f39b735c91238ddf, None, "EARLYTOBEDANDEARLYTORISE")
    ConfigProvider.set_config(config)
    Web3Provider.init_web3(provider=get_web3_connection_provider(config.network_url))
    ContractHandler.set_artifacts_path(config.artifacts_path)
    print(dir(wallet))
    print(wallet.address)
    print(config.network_url)
    print(config.provider_url)
    print(config.network_url)
    print(config.artifacts_path)
    
    
    data_token = ocean.create_data_token('S1Seven', 'S1SV', from_wallet=wallet)
    print(f'created new datatoken with address {data_token.address}')
    token_address = data_token.address
    print(token_address)

    '''
    date_created = "2020-12-01T10:55:11Z"
    service_attributes = {
            "main": {
            "name": "dataAssetAccessServiceAgreement",
            "creator": wallet.address,
            "timeout": 3600 * 24,
            "datePublished": date_created,
            "cost": 1.0, # <don't change, this is obsolete>
        }
    }
    service_endpoint = DataServiceProvider.get_url(ocean.config)
    download_service = ServiceDescriptor.access_service_descriptor(service_attributes, service_endpoint)
    metadata =  {
        "main": {
            "type": "dataset", "name": "S1Seven", "author": "Hannes", 
            "license": "CC0: Public Domain", "dateCreated": date_created, 
            "files": [
                { "index": 0, "contentType": "application/zip", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/training.zip"},
                { "index": 1, "contentType": "text/text", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/monkey_labels.txt"},
                { "index": 2, "contentType": "application/zip", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/validation.zip"}]}
    }
    
    
    asset = ocean.assets.create(metadata, wallet, service_descriptors=[download_service], data_token_address=token_address)
    assert token_address == asset.data_token_address
    did = asset.did  
    print(did) 
    
    data_token.mint_tokens(wallet.address, 100.0, wallet)
    print(data_token.address)

    pool = ocean.pool.create(
        token_address,
        data_token_amount=20.0,
        OCEAN_amount=2.0,
        from_wallet=wallet
    )
    pool_address = pool.address
    print(f'DataToken @{data_token.address} has a `pool` available @{pool_address}')
    
    '''