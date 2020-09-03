def main():
    infile = open('lines.txt', 'rt') #read mode & text mode
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()