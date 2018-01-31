# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import argparse, requests
from pip.operations import freeze
from argparse import RawTextHelpFormatter


header ="""
      ___           ___           ___           ___           ___           ___     
     /\  \         /\  \         /\  \         /\  \         /\  \         /\  \    
    /::\  \       /::\  \        \:\  \       /::\  \       /::\  \       /::\  \   
   /:/\:\  \     /:/\:\  \        \:\  \     /:/\:\  \     /:/\:\  \     /:/\:\  \  
  /:/  \:\  \   /::\~\:\  \       /::\  \   /::\~\:\  \   /::\~\:\  \    \:\~\:\  \ 
 /:/__/_\:\__\ /:/\:\ \:\__\     /:/\:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\    \:\ \:\_\\
 \:\  /\ \/__/ \:\~\:\ \/__/    /:/  \/__/ \/_|::\/:/  / \:\~\:\ \/__/     \:\/:/  /
  \:\ \:\__\    \:\ \:\__\     /:/  /         |:|::/  /   \:\ \:\__\        \::/  / 
   \:\/:/  /     \:\ \/__/     \/__/          |:|\/__/     \:\ \/__/        /:/  /  
    \::/  /       \:\__\                      |:|  |        \:\__\         /:/  /   
     \/__/         \/__/                       \|__|         \/__/         \/__/    
"""
reload(sys)
sys.setdefaultencoding('utf8')

parser = argparse.ArgumentParser(
    description='Script to get requirements used in a python script.',
    epilog='python getReq.py  -f fichero.py -o salida.txt'
)
# parser.add_argument('--date',               "-d",   type=str,               help='Envio de fecha del fichero DD/MM/YYYY')
parser.add_argument('--fichero',          "-i",   type=str,                help='Name of the file to analize')
parser.add_argument('--salida',           "-o",   type=str,                help='Output file to write the requirements')

VERBOSE = False
args = parser.parse_args()

def getReqs(filename, salida):
    toImport = []
    #Imports necesarios
    with open(filename) as f:
        for line in f.readlines():
            if 'import' in line:
                if ',' in line:
                    words = line.split()
                    words = [s.replace(',', '') for s in words]
                    toImport.extend(words[words.index('import'):])
                else:
                    words = line.split()
                    toImport.append(words[words.index('import') + 1])

    
    #print toImport
    fileSalida = open(salida,"w") 
    x = freeze.freeze()
    for p in x:
        #print p
        if any(s.lower() in p for s in toImport):
            fileSalida.write(p+"\n")
            print p

    fileSalida.close()
    f.close()


print header
if args.fichero and args.salida:
    getReqs(args.fichero, args.salida)
else:
    print "Need more arguments. Look the help (-h)"

