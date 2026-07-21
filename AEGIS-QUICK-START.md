# ⚡ AEGIS TOKEN LAUNCH - QUICK CHECKLIST

## 🎯 YOUR MISSION: Deploy AEGIS Token to Binance Smart Chain

**Time Required:** 30-60 minutes  
**Cost:** $30 (deployment) + Your BNB liquidity  
**Result:** Live cryptocurrency trading on PancakeSwap  

---

## ✅ PHASE 1: SETUP (Do Once)

### Install & Configure
- [ ] Download MetaMask: https://metamask.io/
- [ ] Create wallet (save seed phrase SECURELY)
- [ ] Add BSC Testnet network to MetaMask
- [ ] Add BSC Mainnet network to MetaMask
- [ ] Get free test BNB: https://testnet.binance.org/faucet-smart

### Files Ready
- [ ] Open [AegisOneToken.sol](AegisOneToken.sol)
- [ ] Read [AEGIS-TOKEN-LAUNCH.md](AEGIS-TOKEN-LAUNCH.md)
- [ ] Have Remix IDE bookmarked: https://remix.ethereum.org/

---

## ✅ PHASE 2: TEST DEPLOYMENT (Testnet)

### Compile & Deploy
1. [ ] Go to Remix IDE: https://remix.ethereum.org/
2. [ ] Create file `AegisOneToken.sol`
3. [ ] Copy-paste [AegisOneToken.sol](AegisOneToken.sol) code
4. [ ] Compile (Solidity 0.8.0+)
5. [ ] Select "Injected Provider - MetaMask"
6. [ ] Switch MetaMask to **BSC Testnet**
7. [ ] Click **"Deploy"**
8. [ ] Confirm transaction in MetaMask
9. [ ] Wait 30 seconds
10. [ ] **✅ Testnet deployment complete!**
11. [ ] Save contract address

### Verify & Test
- [ ] Go to https://testnet.bscscan.com/
- [ ] Search your contract address
- [ ] Click "Verify and Publish"
- [ ] Verify contract (select Solidity Single file, 0.8.0)
- [ ] Test functions in Remix (transfer, balanceOf, etc.)

---

## ✅ PHASE 3: MAINNET DEPLOYMENT (Real!)

### Get Mainnet BNB
- [ ] Buy ~0.3 BNB from exchange (Binance, Coinbase, etc.)
- [ ] Withdraw to MetaMask wallet address
- [ ] Wait for confirmation
- [ ] See BNB in MetaMask (BSC Mainnet)

### Deploy to Mainnet
1. [ ] Go to Remix IDE: https://remix.ethereum.org/
2. [ ] Create file `AegisOneToken.sol`
3. [ ] Copy-paste smart contract code
4. [ ] Compile (Solidity 0.8.0+)
5. [ ] Select "Injected Provider - MetaMask"
6. [ ] Switch MetaMask to **Binance Smart Chain** (mainnet)
7. [ ] Click **"Deploy"**
8. [ ] Confirm transaction in MetaMask
9. [ ] Wait 1-2 minutes
10. [ ] **✅ AEGIS token LIVE on BSC!**
11. [ ] Save contract address (IMPORTANT!)
12. [ ] Take screenshot of BscScan showing your token

### Verify on BscScan
- [ ] Go to https://bscscan.com/
- [ ] Search your contract address
- [ ] Click "Verify and Publish"
- [ ] Follow verification process
- [ ] ✅ Public contract verified!

---

## ✅ PHASE 4: LISTING ON PANCAKESWAP

### Create Liquidity Pool
1. [ ] Go to https://pancakeswap.finance/
2. [ ] Click "Liquidity"
3. [ ] Click "Add Liquidity"
4. [ ] Token 1: Paste your AEGIS contract address
5. [ ] Token 2: Select WBNB
6. [ ] Amount: 10M AEGIS + 100 BNB (or your choice)
7. [ ] Click "Supply"
8. [ ] Approve token spending
9. [ ] Confirm in MetaMask
10. [ ] Wait for confirmation
11. [ ] **✅ Liquidity pool created!**
12. [ ] People can now buy/sell AEGIS!

### Test Trading
- [ ] Go to https://pancakeswap.finance/swap
- [ ] Try swapping small BNB → AEGIS
- [ ] Try swapping AEGIS → BNB
- [ ] ✅ Trading works!

---

## ✅ PHASE 5: INVESTOR DISTRIBUTION

### Send Tokens to Investors
- [ ] Open BscScan with your contract
- [ ] Click "Contract" → "Write Contract"
- [ ] Connect MetaMask
- [ ] Use `transfer()` function
- [ ] Enter investor wallet address
- [ ] Enter token amount (with 18 decimals)
- [ ] Click "Write"
- [ ] Confirm in MetaMask
- [ ] ✅ Tokens sent!

**Example:** For 100K AEGIS, send: `100000000000000000000000`

### Track Distribution
- [ ] Create spreadsheet of investors
- [ ] Record wallet addresses
- [ ] Record amounts sent
- [ ] Record transaction hashes
- [ ] Note vesting dates (if applicable)

---

## ✅ PHASE 6: MARKETING & LAUNCH

### Announce to World
- [ ] Post on Twitter (tag exchanges)
- [ ] Share on Telegram
- [ ] Announce on Discord
- [ ] Update Aegis One website
- [ ] Send to investor email list

### Listings & Directories
- [ ] List on CoinGecko (free)
- [ ] List on CoinMarketCap (free)
- [ ] List on BSC token list
- [ ] Add to TrustWallet (free)

### Community Management
- [ ] Create Twitter account
- [ ] Create Telegram group
- [ ] Create Discord server
- [ ] Daily community updates
- [ ] Weekly AMA (Ask Me Anything)

---

## 📊 REFERENCE: QUICK COMMANDS

### For Sending Tokens:
```
Token Amount (with 18 decimals):
100K tokens    = 100000000000000000000000
1M tokens      = 1000000000000000000000000
10M tokens     = 10000000000000000000000000
100M tokens    = 100000000000000000000000000
```

### Network Details:

**BSC Testnet:**
- RPC: https://data-seed-prebsc-1-s1.binance.org:8545
- Chain ID: 97
- Explorer: https://testnet.bscscan.com
- Test BNB: FREE from faucet

**BSC Mainnet:**
- RPC: https://bsc-dataseed.binance.org
- Chain ID: 56
- Explorer: https://bscscan.com
- Needs real BNB

---

## 🎯 KEY MILESTONES

| Milestone | Status | Date |
|-----------|--------|------|
| Smart contract ready | ✅ DONE | Now |
| MetaMask setup | [ ] TODO | |
| Testnet deployment | [ ] TODO | |
| Mainnet deployment | [ ] TODO | |
| BscScan verification | [ ] TODO | |
| PancakeSwap listing | [ ] TODO | |
| First trade | [ ] TODO | |
| 100 holders | [ ] GOAL | Week 1 |
| $1M market cap | [ ] GOAL | Month 1 |
| 10K holders | [ ] GOAL | Year 1 |

---

## 💡 COST BREAKDOWN

| Item | Cost | Note |
|------|------|------|
| Testnet deployment | FREE | Use free test BNB |
| Mainnet deployment | ~$30 | 0.1 BNB deployment fee |
| PancakeSwap gas | ~$3 | Small transaction fee |
| Initial liquidity | YOUR BNB | You decide (e.g., 100 BNB) |
| Marketing | $0 | Social media is free |
| **TOTAL** | ~$33 + liquidity | Very affordable |

---

## 🆘 QUICK FIXES

**Problem:** MetaMask won't connect to Remix
- **Fix:** Refresh page, disconnect/reconnect, try different browser

**Problem:** Deployment fails
- **Fix:** Check gas price, ensure you have enough BNB, wait and retry

**Problem:** Can't find your token on PancakeSwap
- **Fix:** Paste exact contract address, use WBNB not BNB, wait for indexing

**Problem:** People say "unverified contract"
- **Fix:** Go to BscScan, verify contract with your source code

---

## 📞 SUPPORT RESOURCES

| Resource | Link | Use Case |
|----------|------|----------|
| Remix IDE | https://remix.ethereum.org/ | Deploy contract |
| BscScan | https://bscscan.com/ | Verify contract |
| PancakeSwap | https://pancakeswap.finance/ | Trade tokens |
| MetaMask | https://metamask.io/ | Manage wallet |
| Binance Academy | https://academy.binance.com/ | Learn crypto |

---

## 🎉 SUCCESS INDICATORS

Your AEGIS token is **LIVE** when:

✅ Contract deployed to BSC mainnet
✅ Verified on BscScan (public code)
✅ Appears on PancakeSwap
✅ People can buy/sell tokens
✅ Listed on CoinGecko/CoinMarketCap
✅ Community members holding AEGIS
✅ Trading volume increasing
✅ Market cap growing

---

## 🚀 NEXT PHASE

Once AEGIS is live:

1. **Announce globally** - Tell world about token
2. **Distribute to backers** - Send to early investors
3. **Launch staking** - Let people earn interest
4. **Build community** - Telegram, Discord, Twitter
5. **Plan phase 2** - More countries, more volume
6. **Roadmap updates** - Regular communication

---

## ⭐ YOU'VE GOT THIS!

**Timeline:** 1 hour  
**Difficulty:** Medium (first time) / Easy (afterwards)  
**Result:** A live cryptocurrency used globally  
**Impact:** Funding Aegis One's global expansion  

**Follow the checklist above and you'll have AEGIS token live on Binance Smart Chain!**

---

*Need help? Check AEGIS-TOKEN-LAUNCH.md for detailed instructions.*

*Ready? Open Remix IDE and let's go! 🚀*
