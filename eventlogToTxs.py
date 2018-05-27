# coding: utf-8

import json
import pandas as pd

def extract_vals(results):
    ret = []
    for result in results:
        tmp = []
        tmp.append(result['transactionHash'])
        tmp.append(int(result['blockNumber'],16))
        tmp.append(hex(int(result['topics'][1],16))) # from_address 0x0...と0が続くのであえて一度hex変換でフォーマットしている
        tmp.append(hex(int(result['topics'][2],16))) # to_address 
        tmp.append(int(result['data'],16) / (10**18)) # value BEC は18桁なので10の18乗で割る
        ret.append(tmp) 
    return ret

def main():
    f = open('event_logs.json', 'r')
    json_data = json.load(f)
    f.close()
    txs = extract_vals(json_data['result'])
    df = pd.DataFrame(txs,columns=['transactionHash','blockNumber','from','to','data'])
    df.to_csv('txs.csv',index=False)

if __name__ == '__main__':
    main()