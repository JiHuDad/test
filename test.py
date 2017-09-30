import os
import sys

class test:
    def search(self, path):
        print path
        filenames = os.listdir(path)
        for filename in filenames:
            fullFileName = os.path.join(path, filename)
            print fullFileName

    def search2(self, path):
        for (path, dir, files) in os.walk(path):
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == '.py':
                    print("%s/%s" % (path, filename))

if __name__ == "__main__":
    test = test()
    path = sys.argv[1]

    test.search2(path)
    #test.search(path)