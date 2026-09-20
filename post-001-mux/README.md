# Post 001 A 2 to 1 multiplexer

## Specification

For binary inputs, `sel = 0` selects `a`; `sel = 1` selects `b`. The MUX is combinational: no clock or stored state is required.

## Files

- `rtl/mux2.sv`: synthesizable MUX.
- `tb/tb_mux2.sv`: exhaustive test of the eight binary combinations.
- `files.f`: source paths relative to this folder.
- `expected.txt`: expected success message.

## Run

From the repository root, run `python run.py`. The runner compiles with Icarus Verilog in SystemVerilog mode and then runs the simulation. The compiled simulation and waveform are placed in `build/post-001-mux/`.

To compile manually, run these commands from this example folder:

```text
iverilog -g2012 -s tb -o mux2.vvp -f files.f
vvp mux2.vvp
```

The manual commands create `mux2.vvp` and `mux2.vcd` in the current folder; remove those generated files before committing. The repository runner avoids that by using `build/`.

## Expected result

```text
PASS: all 8 binary combinations
```

The simulator may also print waveform and finish messages. Any output mismatch invokes `$fatal` and fails the run.

## Learn from a deliberate bug

Temporarily change the RTL to `assign y = a;` and rerun. The test should fail for `a = 0, b = 1, sel = 1`. Restore the original expression after the experiment. Testing only equal data inputs cannot expose swapped inputs.

## Scope

This example covers settled binary behavior, not X/Z inputs or physical timing. The testbench wait lets simulation updates settle; it does not model hardware propagation delay. The expected value uses the equivalent Boolean expression.

These HDL files have not been simulated in the authoring environment. The success message above is an expected result.
