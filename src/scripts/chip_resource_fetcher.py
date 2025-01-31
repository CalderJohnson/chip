import os;
import pathlib;
import re;
from time import time;
import markdown2;
LEN_LIM = 700;
REPO_URL = 'https://github.com/uwindsorcss/wiki.git';
def recursive_directory_iterator(pth):
    for i in pth.iterdir():
        if i.is_dir():
            yield from recursive_directory_iterator(i);
        else:
            yield i;
def traverse(ts):
    try:
        os.system('git pull');
        dat = '';
        for p in recursive_directory_iterator(pathlib.Path('resources')):
            if p.suffix == '.md':
                lmt = p.stat().st_mtime;
                if lmt > ts:
                    dat += generate(p);
        with open("updated.csv", 'w') as fh:
            fh.write(dat);
    except OSError as e:
        os.system('git clone ' + REPO_URL);
        print('Run the script again, inside the wiki repository this time.');
def generate(pth):
    print(pth);
    rows = '';
    rowcurr = '';
    rcnt = 0;
    plain = str(markdown2.markdown(pth.read_text()));
    plain = re.sub(r'<[^>]+>', '', plain);
    parags = plain.split('\n\n');
    for p in parags:
        p = p.replace('\n', ' ');
        p = p.strip() + ' ';
        if len(rowcurr) + len(p) > LEN_LIM:
            rowcurr = rowcurr.strip();
            rows += str(pth) + ' part ' + str(rcnt) + ',' + '"' + rowcurr + '"' + '\n';
            rowcurr = p;
            rcnt += 1;
        else:
            rowcurr += p;
    if len(rowcurr) > 0:
        rows += str(rcnt) + ',' + '"' + rowcurr + '"' + '\n';
    return rows;
timestamp = 0;
try:
    with open('timestamp.txt') as fh:
        cont = fh.readline().strip();
        timestamp = int(cont);
except:
    pass;
traverse(timestamp);
with open('timestamp.txt' , 'w') as fh:
    ts = int(time());
    print(ts, file = fh);
