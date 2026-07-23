# Aegis One - Global Electric Mobility Platform

**Status:** 🚀 Ready for Launch
**Current Phase:** Worldwide Reservations Open
**Goal:** Collect 100 sign-ups to validate market demand

## Executive Summary

Aegis One is a **premium electric mobility platform** powered by innovative technology and global partnerships. We're launching with a two-pronged strategy:

1. **B2C Reservations** - Direct consumer reservations for Aegis One vehicles
2. **B2B Partnerships** - Manufacturing, distribution, and investor networks
3. **Tokenized Investment** - AEGIS token on Binance Smart Chain for community ownership

---

## 🎯 Project Overview

### What is Aegis One?

Aegis One is a next-generation electric vehicle platform combining:
- **Premium Design** - Sleek, aerodynamic styling
- **Performance** - 150km+ range, 0-60km in 6 seconds
- **Safety** - Advanced collision detection, emergency braking
- **Affordability** - Competitive pricing vs. competitors
- **Sustainability** - Zero emissions, clean energy focus

### Market Position

- **Premium Tier** - Focus on reliability and stability, not luxury
- **Global Market** - 40+ countries across 5 phases
- **First Markets** - Sri Lanka, India, Southeast Asia (Phase 1)
- **Demand Validation** - Target 100 genuine reservations before manufacturing

---

## 📁 Project Structure

```
Aegis-Core/
├── index.html                      # Global landing page with reservation form
├── token.html                      # AEGIS token investor landing page
├── manufacturer-inquiry.html       # B2B manufacturer partnership form
├── distributor-inquiry.html        # B2B distributor partnership form
├── investor-inquiry.html           # Investor inquiry form
│
├── server.py                       # Python HTTP server (ThreadingHTTPServer)
├── reservation_store.py            # SQLite database management
├── aegis_core.py                   # Legacy placeholder
│
├── AegisOneToken.sol              # BEP-20 smart contract (1B tokens)
│
├── styles.css                      # Responsive dark theme styling (493 lines)
├── app.js                          # Form handling & validation (180+ lines)
│
├── admin.html                      # Admin dashboard
├── admin.css                       # Admin styling
├── reservations.json               # Backup data format
│
├── _config.yml                     # Jekyll GitHub Pages config
├── .gitignore                      # Version control exclusions
│
├── TOKEN-DEPLOYMENT-GUIDE.md       # Step-by-step token deployment
├── CRYPTO-INVESTMENT-STRATEGY.md   # Token economics & fundraising
├── README.md                       # This file
│
└── tests/
    ├── conftest.py                # Test configuration
    ├── test_reservation_flow.py    # Reservation tests
    └── test_user_input_handler.py  # Input validation tests
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser
- (Optional) Git for version control

### Installation

```bash
# Clone repository
git clone https://github.com/aegis-one/Aegis-Core.git
cd Aegis-Core

# No dependencies needed - pure Python + HTML/CSS/JS
# Run server
python server.py
```

Server will start at **http://localhost:8000**

### Accessing Pages

| Page | URL | Purpose |
|------|-----|---------|
| Home | http://localhost:8000/ | Global landing page |
| Token | http://localhost:8000/token | AEGIS token info |
| Manufacturer | http://localhost:8000/manufacturer-inquiry.html | B2B partnerships |
| Distributor | http://localhost:8000/distributor-inquiry.html | Distribution network |
| Investor | http://localhost:8000/investor-inquiry.html | Investment inquiries |
| Admin | http://localhost:8000/admin | Dashboard |

---

## 📊 Pages & Features

### 1. **index.html** - Global Landing Page
Showcase platform, collect worldwide reservations
- Hero section with CTA
- 4-card feature grid
- Technical specs (range, speed, capacity, charging)
- 11 safety features
- 14-field global reservation form
- 3 business partnership tiers
- 5-year timeline
- Responsive design

### 2. **token.html** - AEGIS Token Landing Page
Attract investors, explain token economics
- Token stats (1B supply, BEP-20, BSC)
- Allocation breakdown (6 categories)
- 4-year vesting schedule
- Investment tiers (Angel/Seed/Growth)
- Step-by-step purchase guide
- Use of funds breakdown
- Risk disclaimer

### 3. **manufacturer-inquiry.html**
Capture B2B manufacturing partnerships
- Company details, experience, certifications
- Production capacity, message

### 4. **distributor-inquiry.html**
Capture B2B distribution partnerships
- Company details, sales channels
- Annual targets, market focus

### 5. **investor-inquiry.html**
Capture investor inquiries
- Investment type, amount range
- Stage interest, geography
- Message

---

## 💻 Backend

### Server (server.py)
**Type:** Python ThreadingHTTPServer on port 8000

**Endpoints:**
- GET `/` → index.html
- GET `/token` → token.html
- GET `/{page}.html` → HTML pages
- GET `/admin` → Admin dashboard
- GET `/admin-data` → JSON data
- POST `/validate` → Input validation
- POST `/reserve` → Save reservation
- POST `/submit-inquiry` → Save business inquiry

### Database (reservation_store.py)
**Type:** SQLite3 (reservations.sqlite3)

**Tables:**
1. **reservations** - Customer reservations with vehicle/timeline/quantity
2. **inquiries** - Business partner inquiries (manufacturer/distributor/investor)

---

## 🎨 Frontend

### Styling (styles.css - 493 lines)
- Dark theme (#07111f background)
- Cyan accents (#7fd9ff)
- Responsive grids
- Mobile breakpoint: 768px
- Components: navbar, hero, buttons, cards, timeline, footer

### JavaScript (app.js - 180+ lines)
- Real-time form validation (300ms debounce)
- Email/phone regex validation
- Smooth scrolling, loading states
- Dynamic form submission
- Hint messaging system

---

## 🔗 Smart Contract (AegisOneToken.sol)

### Token Specs
```
Name:           Aegis One
Symbol:         AEGIS
Standard:       BEP-20
Blockchain:     Binance Smart Chain
Total Supply:   1,000,000,000
Decimals:       18
```

### Features
✅ Standard transfer/approve/transferFrom
✅ Minting (owner-controlled)
✅ Pausable mechanism
✅ Burn function
✅ No hidden functions

---

## 📈 AEGIS Token Economics

### Supply Allocation
- 20% Early Backers (200M)
- 20% Seed Round (200M)
- 25% Public Sale (250M)
- 15% Team & Advisors (150M)
- 10% Community Rewards (100M)
- 10% Reserve (100M)

### Vesting: 4 years
- TGE: 25% immediate
- Months 1-36: 2.08% per month

### Investment Tiers
| Tier | AEGIS | BNB | Price |
|------|-------|-----|-------|
| Angel | 100K | 100 | 0.001 |
| Seed | 500K | 500 | 0.001 |
| Growth | 1M | 1000 | 0.001 |

**See:** [TOKEN-DEPLOYMENT-GUIDE.md](TOKEN-DEPLOYMENT-GUIDE.md) and [CRYPTO-INVESTMENT-STRATEGY.md](CRYPTO-INVESTMENT-STRATEGY.md)

---

## 💡 Zero-Cost Launch

Aegis One launches with **$0 budget** using:
- GitHub Pages (hosting)
- SQLite (database)
- Google Forms (data collection alternative)
- GitHub Pages SSL (HTTPS)
- Gmail (email)
- Google Sheets (analytics)

**Total cost:** $0

---

## 🎯 Launch Strategy

### Phase 1: Demand Validation
- Publish landing page globally
- Open worldwide reservations
- Target: 100 sign-ups
- Validate market demand

### Phase 2: Partnerships
- Approach manufacturing partners
- Secure distribution agreements
- Begin token fundraising
- Build supply chain

### Phase 3: Production
- Manufacturing begins
- Quality testing
- Initial production run
- Soft launch in Phase 1 markets

### Phase 4: Global Expansion
- 40+ countries over 5 years
- Multiple manufacturing partners
- Token trading begins
- Revenue-sharing ecosystem

---

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Manual test - reservation
curl -X POST http://localhost:8000/reserve \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@test.com","phone":"1234567890",...}'

# Manual test - inquiry
curl -X POST http://localhost:8000/submit-inquiry \
  -H "Content-Type: application/json" \
  -d '{"inquiry_type":"manufacturer","company_name":"Test Corp",...}'
```

---

## 🌐 Deployment

### GitHub Pages (FREE)
```bash
git push origin main
# Enable Pages in repository settings
# Site: https://aegis-one.github.io
```

### Local Development
```bash
python server.py
# http://localhost:8000
```

---

## 📱 Responsive Design

✅ Desktop (1024px+) - Full navigation, multi-column
✅ Tablet (768-1023px) - Optimized layout
✅ Mobile (<768px) - Vertical stacks, touch-friendly

---

## 🔐 Security & Privacy

- HTTPS via GitHub Pages
- Client + server validation
- No password storage
- Daily data backups
- GDPR compliant
- No third-party tracking

---

## 📞 Contact

- **Investors:** investors@aegisone.com
- **Partnerships:** partnerships@aegisone.com
- **Technical:** technical@aegisone.com
- **Telegram:** [@AegisOneOfficial]

---

## 📚 Documentation

- [TOKEN-DEPLOYMENT-GUIDE.md](TOKEN-DEPLOYMENT-GUIDE.md) - Smart contract deployment
- [CRYPTO-INVESTMENT-STRATEGY.md](CRYPTO-INVESTMENT-STRATEGY.md) - Token economics
- [README.md](README.md) - This file

---

## 📊 Current Status

| Component | Status |
|-----------|--------|
| Landing Page | ✅ Complete |
| Forms (5) | ✅ Complete |
| Backend API | ✅ Complete |
| Database | ✅ Complete |
| Token Contract | ✅ Complete |
| Smart Contract Docs | ✅ Complete |
| GitHub Pages Config | ✅ Complete |
| Testing | ✅ Complete |
| **Ready for Launch** | **✅ YES** |

---

## 🚀 Next Steps

1. Push to GitHub
2. Enable GitHub Pages
3. Marketing campaign
4. Collect 100 sign-ups
5. Approach manufacturing partners
6. Deploy token to BSC
7. Launch IDO

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

---

## 🎓 Vision

**2026** - Global landing page live, AEGIS token deployed
**2027** - Manufacturing partnerships, first vehicles produced
**2028+** - 40+ countries operational, global brand

---

**Building the future of electric mobility. Join Aegis One.**

*Last Updated: July 2026*
