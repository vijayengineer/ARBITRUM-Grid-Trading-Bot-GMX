<div align="center">
  <img src="auros.png" width="400"/>
  <h2>GMX Grid Trading Bot (SPOT/FUTURES)</h2>
  <h2>WORKING ON A GUI SO IF YOU DONT KNOW HOW TO SET UP WAIT FOR UPDATE</h2>
  <p>Actually profitable(?) leverage/spot trading bot using python for GMX. I tested it for 4 months and made about 8-11% a month with 7x leverage, DYOR AND RISK MANAGE YOUR MONEY PROPERLY</p>
  <p>Thank you for all the stars! But please create issues with bugs so I can fix and improve the bot :)</p>
  
[![Go](https://github.com/c9s/bbgo/actions/workflows/go.yml/badge.svg?branch=main)](https://github.com/c9s/bbgo/actions/workflows/go.yml)
[![GoDoc](https://godoc.org/github.com/c9s/bbgo?status.svg)](https://pkg.go.dev/github.com/c9s/bbgo)
[![Go Report Card](https://goreportcard.com/badge/github.com/c9s/bbgo)](https://goreportcard.com/report/github.com/c9s/bbgo)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
 <a href="https://circleci.com/gh/badges/shields/tree/master">
        <img src="https://img.shields.io/circleci/project/github/badges/shields/master" alt="build status"></a>
  
</div>

## What You Can Do With This Bot?

- Set up the right grid range for a pair on GMX and run a profitable trading bot
- Set up your own leverage (125x anyone?)
- Completely decentralized, from and to your wallet no deposits nor withdrawals to any platforms
- Set Indicators to true and the bot will buy only if it thinks the market is ready to go long
- That's it, what else do you want lmao

## Supported Exchanges

- GMX
- Working on adding other DEXes

## Requirements

- Python 3.7+ on your PC and set up in your Visual Studio Code


## Installation

Follow the steps below

```sh
0. Download the code and extract the zip then open the folder in Visual Studio Code and open terminal
1. pip3 install -r requirements.txt 
2. Open data.json and fill your main details (Don't share this file anywhere)
3. Open inputs.json, Read all the descriptions and fill your trading strategy (Once you run the bot for the first time all the descriptions will disappear)
4. Run the bot with "python3 gmx.py"
5. Stop with CTRL + C
```
Good luck!


Big thanks to DeFiMasterd for bringing my attention to DeFi coding, I learned a lot from his code and now I hope to code my own bots. Cheers!
