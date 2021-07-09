from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "inan_harvester inan_timelord_launcher inan_timelord inan_farmer inan_full_node inan_wallet".split(),
    "node": "inan_full_node".split(),
    "harvester": "inan_harvester".split(),
    "farmer": "inan_harvester inan_farmer inan_full_node inan_wallet".split(),
    "farmer-no-wallet": "inan_harvester inan_farmer inan_full_node".split(),
    "farmer-only": "inan_farmer".split(),
    "timelord": "inan_timelord_launcher inan_timelord inan_full_node".split(),
    "timelord-only": "inan_timelord".split(),
    "timelord-launcher-only": "inan_timelord_launcher".split(),
    "wallet": "inan_wallet inan_full_node".split(),
    "wallet-only": "inan_wallet".split(),
    "introducer": "inan_introducer".split(),
    "simulator": "inan_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
