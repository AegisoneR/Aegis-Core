# Aegis One Token (AEGIS) - BEP-20 Deployment Guide

## Overview
AEGIS is a BEP-20 token on Binance Smart Chain (BSC) for Aegis One investors and community members.

**Token Details:**
- Name: Aegis One
- Symbol: AEGIS
- Network: Binance Smart Chain (BSC)
- Total Supply: 1,000,000,000 tokens (1 billion)
- Decimals: 18
- Token Type: BEP-20 (equivalent to ERC-20 on Ethereum)

---

## Step 1: Deploy Smart Contract to BSC

### Method A: Using Remix IDE (Easiest for Beginners)

1. Go to **Remix IDE**: https://remix.ethereum.org/
2. Create new file: `AegisOneToken.sol`
3. Paste the smart contract code
4. Compile (Solidity version 0.8.0+)
5. Connect MetaMask wallet to **BSC Testnet** or **BSC Mainnet**

**Network Configuration:**
```
Testnet:
- Network: BSC Testnet
- RPC URL: https://data-seed-prebsc-1-s1.binance.org:8545
- Chain ID: 97

Mainnet:
- Network: Binance Smart Chain
- RPC URL: https://bsc-dataseed.binance.org
- Chain ID: 56
```

6. Deploy contract (Gas cost: ~0.3 BNB on mainnet)
7. Copy deployed contract address

---

## Step 2: Verify Contract on BscScan

1. Go to **BscScan**: https://bscscan.com/ (or testnet: https://testnet.bscscan.com/)
2. Search for your contract address
3. Click **"Verify and Publish"**
4. Upload `AegisOneToken.sol`
5. Enter compiler version: 0.8.0
6. Verify

Once verified, anyone can see and interact with your contract.

---

## Step 3: Launch Token Exchange Listing

### Option A: Pancake Swap (Decentralized)

1. Go to **PancakeSwap**: https://pancakeswap.finance/
2. Connect MetaMask wallet
3. Create liquidity pool:
   - Add AEGIS tokens
   - Add BNB (liquidity)
   - Set price ratio
4. Provide liquidity
5. Token is now tradeable on PancakeSwap

**Cost:** Minimal gas fees (~$10-50)

### Option B: IDO (Initial DEX Offering)

- Use **Pinksale**, **Unicrypt**, or **DxSale**
- Create fundraising campaign
- Investors buy tokens using BNB
- Funds go to Aegis project wallet
- Tokens distributed to investors

---

## Step 4: Marketing & Distribution

### Investor Distribution Strategy

1. **Early Backers** (Angel Investors): 10-20% allocation
2. **Seed Round**: 15-20% allocation
3. **Public Sale (IDO)**: 20-30% allocation
4. **Team & Advisors**: 15-20% allocation
5. **Community/Rewards**: 10-15% allocation
6. **Reserve**: 10-15% allocation

### Example Allocation (1 billion tokens)
```
Early Backers:     150M AEGIS
Seed Round:        200M AEGIS
Public Sale:       250M AEGIS
Team/Advisors:     150M AEGIS
Community:         100M AEGIS
Reserve:           150M AEGIS
Total:            1,000M AEGIS
```

---

## Step 5: Security Best Practices

✅ **DO:**
- Get smart contract audited before mainnet launch
- Use multi-sig wallet for owner functions
- Keep private keys secure
- Test on testnet first
- Publish contract source on BscScan

❌ **DON'T:**
- Deploy with personal wallet (use multi-sig)
- Share private keys
- Promises of guaranteed returns
- Unlocked liquidity

---

## Step 6: Token Economics for Investors

### Investment Use Cases

| Use Case | Token Purpose |
|----------|---------------|
| **Equity-like** | Voting rights, profit sharing |
| **Utility** | Discounts on Aegis One purchases |
| **Community** | Staking rewards, governance |
| **Fundraising** | Direct capital for development |

### Suggested Structure
```
Token Price at Launch: 0.001 BNB (or $0.30 USD estimate)

Investor Tiers:
- Angel: 100,000 AEGIS = 100 BNB
- Seed: 500,000 AEGIS = 500 BNB
- Growth: 1,000,000 AEGIS = 1,000 BNB

Vesting (4-year standard):
- 25% unlocked at TGE (Token Generation Event)
- 75% vested over 36 months
```

---

## Step 7: Build Investor Landing Page

Create a dedicated page (`investor-token.html`) on your website:

```html
<section>
  <h2>AEGIS Token - Invest in the Future</h2>
  <ul>
    <li>1 Billion AEGIS tokens</li>
    <li>Binance Smart Chain (BSC)</li>
    <li>Trading on PancakeSwap</li>
    <li>Contract: [Your Address]</li>
    <li>BscScan: [Link]</li>
  </ul>
  <button>Buy on PancakeSwap</button>
</section>
```

---

## Step 8: Regulatory Compliance

**Important:** Cryptocurrency regulations vary by jurisdiction.

**Consider:**
- Consult with legal advisor before launching IDO
- Whitelist jurisdictions (US, certain EU countries may have restrictions)
- KYC (Know Your Customer) for large purchases
- Clear disclaimers: "Not an investment in securities"
- Disclaimer: "Cryptocurrency is volatile and risky"

---

## Cost Breakdown

| Item | Cost |
|------|------|
| BSC Testnet Deployment | Free |
| BSC Mainnet Deployment | ~$50-200 (gas fees) |
| BscScan Verification | Free |
| Pancake Swap Listing | $0 |
| Website Update | $0 |
| Legal Review | $1,000-5,000 |

**Total: $1,050-5,200**

---

## Step 9: Connecting Token to Landing Page

Update your website to include:

1. **Token info section** with:
   - Contract address
   - BscScan link
   - Buy links (PancakeSwap, exchange)
   - Token economics
   - Investor documentation

2. **Investor page** with:
   - Token whitepaper
   - Vesting schedule
   - Use of funds breakdown
   - Team information

3. **Smart links**:
   ```
   Buy AEGIS: https://pancakeswap.finance/swap?outputCurrency=TOKENADDRESS
   View Contract: https://bscscan.com/token/TOKENADDRESS
   ```

---

## Next Steps

1. ✅ Deploy contract to BSC testnet
2. ✅ Test token transfers
3. ✅ Deploy to BSC mainnet
4. ✅ Verify on BscScan
5. ✅ Create PancakeSwap liquidity pool
6. ✅ Launch IDO (if fundraising)
7. ✅ Update landing page with token info
8. ✅ List on CoinGecko/CoinMarketCap

---

## Resources

- **Remix IDE**: https://remix.ethereum.org/
- **MetaMask**: https://metamask.io/
- **BscScan**: https://bscscan.com/
- **PancakeSwap**: https://pancakeswap.finance/
- **Pinksale IDO**: https://www.pinksale.finance/
- **BSC Documentation**: https://docs.binance.org/

---

## Questions?

For technical help, visit:
- BSC Docs: https://docs.binance.org/
- PancakeSwap Support: https://pancakeswap.finance/
- Ethereum Dev: https://ethereum.org/developers

For legal/regulatory questions, consult with a blockchain lawyer in your jurisdiction.
