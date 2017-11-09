import os
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


floder = "include"
os.system("rm -rf" + floder + "*")
mkdir_p(floder)

index_file = open("include/index.txt", 'w')

os.system("echo | g++ -v -x c++ -E - > output.txt 2>&1")
output = open("output.txt")

start = False
for line in output:
    line = line.strip()
    if line == "End of search list.":
        start = False
    
    if start == True:
        cur_dir = floder + "/" + line[1:]
        mkdir_p(cur_dir)
        cp = "cp -r " + line + "/* " + cur_dir
        os.system(cp)
        index_file.write(cur_dir + "\n")
        print(cp)

    if line == "#include <...> search starts here:":
        start = True
index_file.close()
os.system("tar cfz " + floder + ".tgz " + floder)
