Adds python as interpreter
This is actually useful 
#!/usr/bin/env python
# coding: utf-8

    seq=''
    f=open(filename)
    for line in f:
        line=line.strip()
        if not '>' in line:
            seq=seq+line
    f.close()
    return seq
print(read_fasta('ae.fa'))

