import filecmp
import os
import subprocess


def run_program(program, input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        subprocess.run(['python', program], stdin=infile, stdout=outfile)


def compare_outputs(output_a, output_b):
    return filecmp.cmp(output_a, output_b, shallow=False)


def main():
    input_file = "input.txt"
    output_a = "output_a.txt"
    output_b = "output_b.txt"

    for i in range(100):
        print(f"Running test {i + 1}...")
        subprocess.run(['python', 'input_gen.py'])

        run_program('xxx.py', input_file, output_a)
        run_program('yyy.py', input_file, output_b)

        if not compare_outputs(output_a, output_b):
            print("Discrepancy found!")
            with open("discrepancy_input.txt", 'w') as f:
                with open(input_file, 'r') as infile:
                    f.write(infile.read())

            with open("discrepancy_output_a.txt", 'w') as f:
                with open(output_a, 'r') as outfile_a:
                    f.write(outfile_a.read())

            with open("discrepancy_output_b.txt", 'w') as f:
                with open(output_b, 'r') as outfile_b:
                    f.write(outfile_b.read())
            
            break
    else:
        print("All tests passed!")


if __name__ == "__main__":
    main()
