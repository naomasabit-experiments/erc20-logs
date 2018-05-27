# erc20-logs

# extract eventlog by json format from ethereum node

## parity example

curl 'http://127.0.0.1:8545' -H 'Content-Type: application/json' -H 'Accept: application/json' --data-binary '{"id":1,"jsonrpc":"2.0","params":[{"fromBlock":"0x0","toBlock":"latest","address":"0xea610b1153477720748dc13ed378003941d84fab"}],"method":"eth_getLogs"}' >> event_logs.json

## processing eventlog

python eventlogToTxs.py
