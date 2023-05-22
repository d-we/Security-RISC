#! /usr/bin/env python3

import subprocess
from pathlib import Path

LIBPATH = "./libmbedtls.so.8"
OFFSET_HEADERFILE = "./attack_offsets.h"

def execute_cmd(s):
    return subprocess.run(s, shell=True)


def generate_headerfile(headerfname, mpi_exp_mod_offset, one_offset):
    template = """// generated by build.py
#ifndef ATTACK_OFFSETS_H
#define ATTACK_OFFSETS_H

#define MPI_EXP_MOD_OFFSET 0x{mpi_offset:x}
#define ONE_OFFSET 0x{one_offset:x}

#endif /* !ATTACK_OFFSETS_H */
"""
    header_content = template.format(mpi_offset=mpi_exp_mod_offset,
                    one_offset=one_offset)

    with open(headerfname, "w") as fd:
        fd.write(header_content)


def build_library():
    execute_cmd("make lib -C mbedtls")
    

def main():
    # create default header for first build
    if not Path(OFFSET_HEADERFILE).is_file():
        print("Generating default header (actual offsets still required)")
        generate_headerfile(OFFSET_HEADERFILE, 0, 0)

    # always force recompilation of the important file
    execute_cmd("touch ./mbedtls/library/bignum.c")
    # build to generate binary
    build_library()


if __name__ == "__main__":
    main()