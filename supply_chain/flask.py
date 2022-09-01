from typing import ChainMap
from flask import Flask, request, render_template
import hashlib as hasher
import datetime as date
import Supply_Chain
from Supply_Chain import view_blockchain
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15

import random
import time
# Global variables
supply_blockchain = []
utxo_array = []
manufacturers_list = []
other_users_list = []
global_index = 0
pow_proof = int(0)

import Supply_Block

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def ro():
    if request.method == "POST":
        f = request.form.get("name")
        return render_template('templates')

if __name__ == '__main__':
    app.run(debug=True, port=5000)