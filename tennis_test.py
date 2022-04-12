import subprocess

path_to_script = '../ex1/tennis.sh'
if __name__ == '__main__':
    r1 = subprocess.run(path_to_script, input=b'5\n10\n5\n10\n15\n10\n15\n10\n10\n10\n',
                        capture_output=True).stdout
    r2 = subprocess.run(path_to_script, input=b'10\n10\n15\n24\n12\n14\n3\n2\n', capture_output=True).stdout
    r3 = subprocess.run(path_to_script, input=b'11\n17\n15\n14\n4\n7\n7\n2\n5\n4\n8\n6\n',
                        capture_output=True).stdout
    with open('expected1', 'rb') as f:
        e1 = f.read()
    with open('expected2', 'rb') as f:
        e2 = f.read()
    with open('expected3', 'rb') as f:
        e3 = f.read()

    if e1 != r1:
        print('error test 1')
    if e2 != r2:
        print('error test 2')
    if e3 != r3:
        print('error test 3')
