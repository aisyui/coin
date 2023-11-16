#!/bin/zsh

rate=`curl -sL https://coincheck.com/api/rate/btc_jpy|jq -r .rate`
json=`curl -sL https://aisyui.github.io/coin/btc.json`
btc=`echo $json|jq -r ".[0].amount"`
jpy=`echo $((btc * rate))|cut -d . -f 1`
echo "$json"| jq -s ".+[{\"jpy\":$jpy,\"rate\":$rate}]"
