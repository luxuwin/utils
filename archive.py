import os, re, argparse

parser = argparse.ArgumentParser(description='Archive.')
parser.add_argument('--src_path', type=str, default="./testsource")
parser.add_argument('--dst_path', type=str, default="./testdest")
parser.add_argument('--key', type=str, help="key's corresponding email addr", default="test@key")
parser.add_argument('--max_depth', type=int, default=2)

args = parser.parse_args()

srcPath = args.src_path
dstPath = args.dst_path
maxDepth = args.max_depth
key= args.key

#for gpg
os.environ["tty"]=os.environ["GPG_TTY"]


ignores = [ R".DS_Store$" ]

def Ignore(f):
    for ig in ignores:
        if re.search(ig, f):
            return True
    return False


def CreateDestPath(dstpath):
    if not os.path.exists(dstpath):
      os.makedirs(dstpath)
      print("created %s" % dstpath)


def Exec(input, output):
    cmd = "tar --zstd -cv %s | gpg --encrypt -r %s | split -b 100M  - '%s.tar.zst.gpg.'" % (input, key,output)
    print(cmd)
    os.system(cmd)


def ArchiveFolder(srcpath, dstpath):
#    print("reached max depth: %s" % srcpath)    
    output = os.path.join(dstpath, "folder")    
    input = "'%s'" % srcpath
    CreateDestPath(dstpath)
    Exec(input, output)


def ArchiveFilesOnly(srcpath, dstpath, files):
#    print("has files in: %s: %s" % (srcpath, files))
    input = " ".join(["'%s'" % f  for f in files])
    output = os.path.join(dstpath, "files_only")
    
    CreateDestPath(dstpath)
    Exec(input, output)


def ArchiveAll(srcpath, dstpath, depth, maxDepth):
    # print("processing %s" % path)
    if os.path.isfile(srcpath):
        # print("found file: %s" % path)
        return
    
    if depth >= maxDepth:
        ArchiveFolder(srcpath, dstpath)
        return
       
    hasFile = False
    files = []
    dirList = os.listdir(srcpath)
    dirList.sort()
    for f in dirList:
        subSrcPath = os.path.join(srcpath, f)
        subDstPath = os.path.join(dstpath, f)
        if os.path.isfile(subSrcPath) and not Ignore(subSrcPath):
            hasFile = True
            files.append(subSrcPath)
        else:
            ArchiveAll(subSrcPath, subDstPath, depth+1, maxDepth)

    if hasFile:
        ArchiveFilesOnly(srcpath, dstpath, files)



ArchiveAll(srcPath, dstPath, 0, maxDepth)
