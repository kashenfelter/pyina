#!/usr/bin/env python

__doc__ = """
# print rank - hostname info
# To run:

alias mpython='mpirun -np [#nodes] `which mpipython.exe`'
mpython machines_raw.py
"""

def host(id):
    import socket
    return "Rank: %d -- %s" % (id, socket.gethostname())


if __name__ == '__main__':

    try:
        from pyina.parallel_map2 import parallel_map
        import mpi, pyina
        world = mpi.world()

        hostnames = parallel_map(host, range(world.size))

        if world.rank == 0:
            print '\n'.join(hostnames)
    except:
        print __doc__
        

# end of file
