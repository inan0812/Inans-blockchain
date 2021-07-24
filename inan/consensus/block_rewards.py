from inan.util.ints import uint32, uint64

# 1 Inan coin = 100,000,000 = 100 trillion mojo.
_mojo_per_inan = 100000000
_blocks_per_year = 6727680  # (32 * 6 * 24 * 365) * 4


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    return 3
    # if height == 0:
        # return uint64(int((7 / 8) * 100000000 * _mojo_per_inan))
    # elif height < 3 * _blocks_per_year:
        # return uint64(int((7 / 8) * 1024 * _mojo_per_inan))
    # elif height < 6 * _blocks_per_year:
        # return uint64(int((7 / 8) * 512 * _mojo_per_inan))
    # elif height < 9 * _blocks_per_year:
        # return uint64(int((7 / 8) * 256 * _mojo_per_inan))
    # elif height < 12 * _blocks_per_year:
        # return uint64(int((7 / 8) * 128 * _mojo_per_inan))
    # else:
        # return uint64(int((7 / 8) * 64 * _mojo_per_inan))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
         return uint64(int(2 * _mojo_per_inan))
    elif height < 3 * _blocks_per_year:
         return uint64(int(1024 * _mojo_per_inan))
    elif height < 6 * _blocks_per_year:
         return uint64(int(2 * _mojo_per_inan))
    elif height < 9 * _blocks_per_year:
         return uint64(int(2 * _mojo_per_inan))
    elif height < 12 * _blocks_per_year:
         return uint64(int(2 * _mojo_per_inan))
    else:
         return uint64(int( 2 * _mojo_per_inan))
    
    # if height == 0:
        # return uint64(int((1 / 8) * 100000000 * _mojo_per_inan))
    # elif height < 3 * _blocks_per_year:
        # return uint64(int((1 / 8) * 1024 * _mojo_per_inan))
    # elif height < 6 * _blocks_per_year:
        # return uint64(int((1 / 8) * 512 * _mojo_per_inan))
    # elif height < 9 * _blocks_per_year:
        # return uint64(int((1 / 8) * 256 * _mojo_per_inan))
    # elif height < 12 * _blocks_per_year:
        # return uint64(int((1 / 8) * 128 * _mojo_per_inan))
    # else:
        # return uint64(int((1 / 8) * 64 * _mojo_per_inan))
