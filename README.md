# SystemVerilog MUX and Testbench

A combinational 2-to-1 multiplexer with a self-checking SystemVerilog testbench.

## Design and verification

- [MUX specification and testbench instructions](post-001-mux/README.md)
- [Combinational MUX and sequential register](combinational-sequential/README.md)

The MUX selects input `a` when `sel = 0` and input `b` when `sel = 1`. The testbench checks all eight binary combinations of `a`, `b` and `sel`, fails on an output mismatch, and writes a VCD waveform. The source folder contains the RTL, testbench, file list and expected result.

## Requirements

Install Python 3 and Icarus Verilog with `iverilog` and `vvp` available on PATH. Run commands from the repository root. Other SystemVerilog simulators may also be used with the supplied source files.

```text
python run.py
```

Simulation outputs go under `build/`, which is ignored by Git.

## Validation status

The binary truth table was checked independently in Python. The SystemVerilog files have not been compiled or simulated in the authoring environment. Expected simulator output is documented, not claimed as an observed result.
