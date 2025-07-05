#!/usr/bin/env python3

import os

os.environ["ORT_DISABLE_AFFINITY"] = "1"
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
os.environ["ONNXRUNTIME_INTRA_OP_NUM_THREADS"] = "4"
os.environ["ONNXRUNTIME_INTER_OP_NUM_THREADS"] = "1"
os.environ["OMP_PROC_BIND"] = "false"
os.environ["OMP_PLACES"] = "cores"

from facefusion import core

if __name__ == '__main__':
	core.cli()
