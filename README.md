# VLSI learning examples

Small SystemVerilog examples accompanying the LinkedIn learning series.

## Examples

- [Post 001: A 2-to-1 multiplexer](post-001-mux/README.md)

Each post folder contains its RTL, self-checking testbench, file list, run instructions and expected results. New lessons can be added alongside existing examples.

## Requirements

Install Python 3 and Icarus Verilog with `iverilog` and `vvp` available on PATH. Run commands from the repository root. Other SystemVerilog simulators may also be used with the supplied source files.

```text
python run.py
```

Simulation outputs go under `build/`, which is ignored by Git.

## Validation status

The Post 001 Boolean truth table was checked independently in Python. The SystemVerilog files have not been compiled or simulated in the authoring environment. Expected simulator output is documented, not claimed as an observed result.
