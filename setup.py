from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "inanvdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.3",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the inan processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="inan-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@chia.net",
    description="Inan blockchain full node, farmer, timelord, and wallet.",
    url="https://chia.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="inan blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "inan",
        "inan.cmds",
        "inan.clvm",
        "inan.consensus",
        "inan.daemon",
        "inan.full_node",
        "inan.timelord",
        "inan.farmer",
        "inan.harvester",
        "inan.introducer",
        "inan.plotting",
        "inan.pools",
        "inan.protocols",
        "inan.rpc",
        "inan.server",
        "inan.simulator",
        "inan.types.blockchain_format",
        "inan.types",
        "inan.util",
        "inan.wallet",
        "inan.wallet.puzzles",
        "inan.wallet.rl_wallet",
        "inan.wallet.cc_wallet",
        "inan.wallet.did_wallet",
        "inan.wallet.settings",
        "inan.wallet.trading",
        "inan.wallet.util",
        "inan.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "inan = inan.cmds.inan:main",
            "inan_wallet = inan.server.start_wallet:main",
            "inan_full_node = inan.server.start_full_node:main",
            "inan_harvester = inan.server.start_harvester:main",
            "inan_farmer = inan.server.start_farmer:main",
            "inan_introducer = inan.server.start_introducer:main",
            "inan_timelord = inan.server.start_timelord:main",
            "inan_timelord_launcher = inan.timelord.timelord_launcher:main",
            "inan_full_node_simulator = inan.simulator.start_simulator:main",
        ]
    },
    package_data={
        "inan": ["pyinstaller.spec"],
        "inan.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "inan.util": ["initial-*.yaml", "english.txt"],
        "inan.ssl": ["inan_ca.crt", "inan_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
