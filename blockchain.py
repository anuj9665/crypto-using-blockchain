import hashlib
import json
from time import time

class Blockchain (object): 
    def __init__(self):
        self.chain = []; 


    def getLastBlock(self):
        return self.chain[-1];


    def addBlock(self, block):
        if(len(self.chain) > 0):
            block.prev = self.getLastBlock().hash;
        else:
            block.prev = "none";
        self.chain.append(block);
    

    def chainJSONencode(self):
        blockArrJSON = [];
        for block in self.chain:
            blockJSON = {};
            blockJSON['hash'] = block.hash;
            blockJSON['index'] = block.index;
            blockJSON['prev'] = block.prev;
            blockJSON['time'] = block.time;


            transactionsJSON = [];
            tJSON = {};
            for transaction in block.transactions:
                tJSON['time'] = transaction.time;
                tJSON['sender'] = transaction.sender;
                tJSON['reciever'] = transaction.reciever;
                tJSON['amt'] = transaction.amt;
                tJSON['hash'] = transaction.hash;
                transactionsJSON.append(tJSON);

            blockJSON['transactions'] = transactionsJSON;

            blockArrJSON.append(blockJSON);

        return blockArrJSON;



class Block (object):
    def __init__(self, transactions, time, index):
        self.index = index; #Block Number
        self.transactions = transactions; #Transaction Data
        self.time = time; #Time block was created
        self.prev = ''; #Hash of Previous Block
        self.hash = self.calculateHash(); #Hash of Block


    def calculateHash(self):
        hashTransactions = "";
        for transaction in self.transactions:
            hashTransactions += transaction.hash;

        hashString = str(self.time) + hashTransactions + self.prev + str(self.index);
        hashEncoded = json.dumps(hashString, sort_keys=True).encode();
        return hashlib.sha256(hashEncoded).hexdigest();


class Transaction (object):
    def __init__(self, sender, reciever, amt):
        self.sender = sender;
        self.reciever = reciever;
        self.amt = amt;
        self.time = time();
        self.hash = self.calculateHash();


    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time);
        hashEncoded = json.dumps(hashString, sort_keys=True).encode();
        return hashlib.sha256(hashEncoded).hexdigest();