import sys
import codecs

# Usage: replace.py [filename] [character to replace] [character to replace with]

f = codecs.open(sys.argv[1], encoding='utf-8')
contents = f.read()
f.close()

newContent = contents.replace(sys.argv[2],sys.argv[3])
f = open(sys.argv[1], 'w')
f.write(newContent)
f.close()
print "Done"