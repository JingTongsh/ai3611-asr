import os


def get_size(path: str):
    c = 1024 ** 3
    if os.path.isdir(path):
        size = 0
        for root, dirs, files in os.walk(path):
            for f in files:
                fp = os.path.join(root, f)
                size += os.path.getsize(fp)
    else:
        size = os.path.getsize(path)

    return size / c  # GiB


source = '/dssg/home/acct-stu/stu463/course_proj/asr1'
target = './'
for f in os.listdir(source):
    print(f)
    full = os.path.join(source, f)
    if get_size(full) > 1:
        print('{} is too large: {:.1f}G'.format(full, get_size(full)))
    elif os.path.isdir(full):
        cm = 'cp -r ' + full + ' ' + target
        print(cm)
        os.system(cm)
    else:
        cm = 'cp ' + full  + ' ' + target
        print(cm)
        os.system(cm)
