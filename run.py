"""Compile and run Post 001 using Icarus Verilog. No Python packages required."""
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    compiler = shutil.which('iverilog')
    runtime = shutil.which('vvp')
    if not compiler or not runtime:
        print('Install Icarus Verilog and add iverilog and vvp to PATH.', file=sys.stderr)
        return 2
    root = Path(__file__).resolve().parent
    example = root / 'post-001-mux'
    build = root / 'build' / 'post-001-mux'
    build.mkdir(parents=True, exist_ok=True)
    executable = build / 'mux2.vvp'
    try:
        subprocess.run([compiler, '-g2012', '-s', 'tb', '-o', str(executable),
                        '-f', 'files.f'], cwd=example, check=True)
        subprocess.run([runtime, str(executable)], cwd=build, check=True)
    except subprocess.CalledProcessError as exc:
        return exc.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
