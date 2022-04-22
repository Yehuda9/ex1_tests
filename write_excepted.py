import subprocess

path_to_script = '../ex1/tennis.sh'
if __name__ == '__main__':
    r1 = subprocess.run(path_to_script, input=b'5\n10\n5\n10\n15\n10\n15\n10\n10\n10\n',
                        capture_output=True).stdout
    r2 = subprocess.run(path_to_script, input=b'10\n10\n15\n24\n12\n14\n3\n2\n', capture_output=True).stdout
    r3 = subprocess.run(path_to_script, input=b'11\n17\n15\n14\n4\n7\n7\n2\n5\n4\n8\n6\n',
                        capture_output=True).stdout
    with open('expected1', 'wb') as f:
        f.write(r1.replace(b'[H[2J[3J', b''))
    with open('expected2', 'wb') as f:
        f.write(r2.replace(b'[H[2J[3J', b''))
    with open('expected3', 'wb') as f:
        f.write(r3.replace(b'[H[2J[3J', b''))
