from blockchain import *;
from time import time;
import pprint
import json;

pp= pprint.PrettyPrinter(indent=4)

blockchain = Blockchain();
transactions =[];

block = Block(transactions, time(), 0);
blockchain.addBlock(block);


block = Block(transactions, time(), 1);
blockchain.addBlock(block);

block = Block(transactions, time(), 2);
blockchain.addBlock(block);

block = Block(transactions, time(), 3);
blockchain.addBlock(block);

pp.pprint(blockchain.chainJSONencode());
print("Length: ", len(blockchain.chain));