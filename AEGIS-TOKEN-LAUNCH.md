# ⚡ AEGIS TOKEN DEPLOYMENT - COMPLETE WALKTHROUGH

## 🎯 Mission: Deploy AEGIS Token to Binance Smart Chain

**Current Status:** Smart contract ready, documentation complete
**Next Step:** Deploy to BSC (Testnet → Mainnet)
**Timeline:** 30 minutes to 1 hour
**Cost:** ~$50-200 BNB (~$20-100 USD)

---

## 📋 REQUIREMENTS CHECKLIST

Before you start, ensure you have:

- [ ] MetaMask wallet (browser extension)
- [ ] BSC testnet BNB (free from faucet)
- [ ] BSC mainnet BNB (for deployment)
- [ ] This smart contract file
- [ ] A laptop/desktop with internet
- [ ] Approximately 30 minutes

---

## 🔧 PHASE 1: SETUP (10 minutes)

### Step 1.1: Install MetaMask
1. Go to https://metamask.io/
2. Install extension for Chrome/Firefox/Edge
3. Create new wallet (save seed phrase somewhere SAFE)
4. Set password

### Step 1.2: Add BSC Network to MetaMask

**For BSC Testnet (FREE testing):**
1. Open MetaMask
2. Click network dropdown (top-left)
3. Click "Add Network"
4. Fill in:
   ```
   Network Name: BSC Testnet
   New RPC URL: https://data-seed-prebsc-1-s1.binance.org:8545
   Chain ID: 97
   Currency Symbol: tBNB
   Block Explorer: https://testnet.bscscan.com
   ```
5. Save

**For BSC Mainnet (REAL tokens):**
1. Click network dropdown
2. Click "Add Network"
3. Fill in:
   ```
   Network Name: Binance Smart Chain
   New RPC URL: https://bsc-dataseed.binance.org
   Chain ID: 56
   Currency Symbol: BNB
   Block Explorer: https://bscscan.com
   ```
4. Save

### Step 1.3: Get Test BNB (Free)
**For Testnet Only:**
1. Go to https://testnet.binance.org/faucet-smart
2. Paste your MetaMask wallet address
3. Click "Give me BNB"
4. Wait 1 minute (appears in wallet)
5. You now have free tBNB for testing!

---

## 🚀 PHASE 2: DEPLOY TO TESTNET (10 minutes)

### Step 2.1: Open Remix IDE
1. Go to https://remix.ethereum.org/
2. Click "Create New File"
3. Name it: `AegisOneToken.sol`
4. Copy-paste the entire smart contract code

### Step 2.2: Compile Contract
1. Click **Solidity Compiler** icon (left sidebar)
2. Select Compiler Version: `0.8.0` or higher
3. Click **"Compile AegisOneToken.sol"**
4. Should show ✅ (green checkmark)

### Step 2.3: Deploy to Testnet
1. Click **Deploy & Run Transactions** icon (left sidebar)
2. Environment: Select **"Injected Provider - MetaMask"**
3. MetaMask popup: Click **"Connect"**
4. Select your wallet account
5. Make sure MetaMask shows **"BSC Testnet"** network
6. Contract: Select **"AegisOneToken"**
7. Click **"Deploy"**
8. MetaMask popup: Review gas fee (~0.005 tBNB)
9. Click **"Confirm"**
10. Wait 30 seconds...
11. ✅ Deployment successful!
12. Copy your **Contract Address** (shows at bottom)

**Save this address!** You'll need it.

### Step 2.4: Test on Testnet
In Remix, you should see your contract with functions:
- `transfer` - Send tokens
- `balanceOf` - Check balance
- `approve` - Approve spending
- Click any to test them!

---

## ✅ PHASE 3: VERIFY ON BSCSCAN TESTNET (5 minutes)

### Step 3.1: Find Your Contract
1. Go to https://testnet.bscscan.com/
2. Search for your **Contract Address** (from Phase 2.4)
3. Should show your AEGIS token details

### Step 3.2: Verify Contract
1. Scroll down to **"Contract"** section
2. Click **"Verify and Publish"**
3. Fill in:
   ```
   Contract Address: [Your contract address]
   Compiler Type: Solidity (Single file)
   Compiler Version: 0.8.0
   License: MIT
   ```
4. Click **"Continue"**
5. Paste your entire `AegisOneToken.sol` code
6. Click **"Verify and Publish"**
7. Wait 30 seconds...
8. ✅ Contract verified!

Now anyone can see your code on BscScan! (This builds trust)

---

## 🎉 PHASE 4: DEPLOY TO MAINNET (Real Tokens!)

**⚠️ WARNING:** This is the REAL deployment. Use REAL BNB. Cannot be undone!

### Step 4.1: Get Mainnet BNB
You need ~0.3 BNB (~$100 USD) to:
- Deploy contract: ~0.1 BNB
- Create PancakeSwap liquidity: ~0.2 BNB

**How to get BNB:**
1. Buy from exchange: Binance, Coinbase, FTX
2. Withdraw to MetaMask wallet address
3. Make sure you're on BSC Mainnet network
4. Wait for confirmation

### Step 4.2: Deploy to Mainnet (Repeat Phase 2)
Same process as testnet but:
1. Make sure MetaMask shows **"Binance Smart Chain"** (not testnet)
2. Open Remix: https://remix.ethereum.org/
3. Create `AegisOneToken.sol` file
4. Compile
5. Deploy (same steps)
6. **Confirm in MetaMask** - review gas fee
7. Wait for confirmation
8. ✅ YOUR AEGIS TOKEN IS NOW LIVE!

### Step 4.3: Verify on Mainnet BscScan
1. Go to https://bscscan.com/
2. Search for your contract address
3. Click "Verify and Publish"
4. Complete verification (same as testnet)
5. ✅ Public contract code!

---

## 💰 PHASE 5: LIST ON PANCAKESWAP (5-10 minutes)

Now people can buy your AEGIS tokens!

### Step 5.1: Add Liquidity
1. Go to https://pancakeswap.finance/
2. Click **"Liquidity"**
3. Click **"Add Liquidity"**
4. Token 1: Select **AEGIS** (paste your contract address)
5. Token 2: Select **WBNB** (already listed)
6. Amount: 
   - AEGIS: 10,000,000 (10M tokens)
   - WBNB: 100 BNB (or amount you want)
7. Click **"Supply"**
8. MetaMask: Click **"Confirm"**
9. Wait for transaction...
10. ✅ Liquidity pool created!
11. People can now buy AEGIS on PancakeSwap!

**You've created a market!** 🎉

---

## 📊 PHASE 6: INVESTOR DISTRIBUTION

Now distribute tokens to investors:

### Token Allocation (1 Billion Total)
```
200M - Early Backers
200M - Seed Round
250M - Public Sale (IDO)
150M - Team & Advisors
100M - Community Rewards
100M - Reserve
```

### Send Tokens to Investors
In Remix or BscScan:
1. Use `transfer()` function
2. Enter investor wallet address
3. Amount: e.g., 100000000000000000000000 (for 100K tokens)
4. Click **"Write"**
5. Confirm in MetaMask
6. ✅ Tokens sent!

**Or use vesting contract** (if needed for time-locked tokens)

---

## 🎯 NEXT STEPS: INVESTOR MARKETING

### Option 1: IDO Platform (Raise Funds)
Use: Pinksale, Unicrypt, or DxSale
- Create fundraising campaign
- Set token price + amount
- Investors send BNB → Receive AEGIS
- Funds go to project wallet

### Option 2: Direct Investor Management
- Send tokens directly to investor wallets
- Keep track in spreadsheet
- Set vesting schedules (if needed)

### Option 3: Staking Program
- Create staking website
- Investors lock AEGIS tokens
- Earn rewards (interest)
- Demonstrates long-term value

---

## 🔗 IMPORTANT LINKS

| Service | Link |
|---------|------|
| Remix IDE | https://remix.ethereum.org/ |
| MetaMask | https://metamask.io/ |
| BscScan Testnet | https://testnet.bscscan.com/ |
| BscScan Mainnet | https://bscscan.com/ |
| PancakeSwap | https://pancakeswap.finance/ |
| BSC Faucet | https://testnet.binance.org/faucet-smart |
| Pinksale (IDO) | https://www.pinksale.finance/ |

---

## 💼 MARKETING YOUR TOKEN

### Before Launch:
- [ ] Create Twitter (@AegisOneOfficial)
- [ ] Create Telegram group
- [ ] Create Discord server
- [ ] Write whitepaper
- [ ] Build community

### During Launch:
- [ ] Announce on social media
- [ ] List on CoinGecko
- [ ] List on CoinMarketCap
- [ ] Post contract on BscScan
- [ ] Share link to PancakeSwap

### After Launch:
- [ ] Weekly community updates
- [ ] Governance voting
- [ ] Staking rewards
- [ ] Liquidity incentives

---

## 💡 COST BREAKDOWN

| Item | Cost |
|------|------|
| Deploy to Testnet | FREE (test BNB) |
| Deploy to Mainnet | ~0.1 BNB (~$30) |
| PancakeSwap Liquidity | Gas fee ~0.01 BNB (~$3) |
| Initial Liquidity (BNB) | Your choice (e.g., 100 BNB) |
| CoinGecko/CMC Listing | FREE |
| **TOTAL** | **~$30 + your BNB liquidity** |

---

## 🚨 SECURITY CHECKLIST

- ✅ Smart contract compiled without errors
- ✅ Contract verified on BscScan
- ✅ Backup wallet seed phrase (SAFE place)
- ✅ Multiple people can verify code
- ✅ Use hardware wallet for large amounts (optional)
- ✅ Never share private keys
- ✅ Keep contract address documented

---

## 🎓 WHAT HAPPENS NEXT

### Once Deployed:
1. **Liquidity Pool Created** - People can buy/sell AEGIS
2. **Price Discovery** - Market determines value
3. **Investor Transfers** - Send tokens to early backers
4. **Staking Launches** - Earn interest on holdings
5. **Community Growth** - Build network effect
6. **Value Increases** - Network grows = token value

### Revenue Model:
- 30% of Aegis One net profit → AEGIS holders
- Staking rewards (5-10% annual)
- Governance participation
- Discount on vehicles (utility)

---

## 🆘 TROUBLESHOOTING

### MetaMask won't connect?
- Refresh Remix page
- Disconnect/reconnect MetaMask
- Try different browser

### Deployment failed?
- Check gas price isn't too low
- Ensure you have enough BNB
- Try again in 1 minute

### Can't verify contract?
- Copy-paste EXACT code (no changes)
- Select correct compiler version
- Check contract address is correct

### No liquidity on PancakeSwap?
- Try swapping small amount first
- If error: increase liquidity ratio
- Tokens may be locked (check vesting)

---

## ✨ YOU NOW HAVE:

✅ AEGIS Token deployed to BSC
✅ Live on PancakeSwap (tradeable)
✅ Public contract on BscScan (verified)
✅ Ready for investor distribution
✅ Working with global Aegis One platform
✅ Community ownership through tokenomics

---

## 🎉 CONGRATULATIONS!

You've successfully launched AEGIS token on Binance Smart Chain!

**Your token is now:**
- Live and trading
- Owned by your community
- Powering Aegis One globally
- Ready for investor participation
- Part of the future of electric mobility

---

## 📞 NEXT: 

1. **Announce launch** on social media
2. **Send tokens** to early backers
3. **Launch staking** program
4. **Build community** on Telegram/Discord
5. **Plan Phase 2** expansion

---

**Ready to launch AEGIS?**

Follow the steps above and you'll have a live cryptocurrency on Binance Smart Chain in under 1 hour.

*Questions? Check TOKEN-DEPLOYMENT-GUIDE.md for more details.*
