import os, re, argparse

parser = argparse.ArgumentParser(description='Archive.')
parser.add_argument('--src_path', type=str, default="./testdest")
parser.add_argument('--dst_path', type=str, default="./testrestore")
parser.add_argument('--key', type=str, help="key's corresponding email addr", default="test@key")


args = parser.parse_args()

srcPath = args.src_path # "./testdest" #  os.path.abspath("./testdest")
dstPath = args.dst_path # "./testrestore" #  os.path.abspath("./testrestore")
key=args.key

#for gpg
os.environ["tty"]=os.environ["GPG_TTY"]


def CreateDestPath(dstpath):
    if not os.path.exists(dstpath):
      os.makedirs(dstpath)
      print("created %s" % dstpath)


def Restore(srcpath, dstpath):
    CreateDestPath(dstpath)
    cmd = "cat %s | gpg --decrypt -r %s | zstd -d | tar -x -C %s" % (srcpath, key, dstpath)
    print(cmd)
    os.system(cmd)



def RestoreAll(srcpath, dstpath):
    if os.path.isfile(srcpath):
        # print("found file: %s" % path)
        return
           
    files = []
    for f in os.listdir(srcpath):
        subSrcPath = os.path.join(srcpath, f)
        if os.path.isfile(subSrcPath):
            hasFile = True
            files.append(subSrcPath)
        else:
            RestoreAll(subSrcPath, dstPath)

    if len(files)>1:
        raise("found more than 1 files in %s", srcpath)
    if len(files)>0:
        Restore(files[0], dstpath)



RestoreAll(srcPath, dstPath)
