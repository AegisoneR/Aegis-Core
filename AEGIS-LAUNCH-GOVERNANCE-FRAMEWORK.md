# AEGIS Launch Governance Framework
## Version 1.0 | July 2026

---

## Executive Summary

This document establishes the governance framework for AEGIS One's pre-launch, launch, and post-launch phases. It defines:

- **Launch blockers** that must be resolved before public activity
- **Validation requirements** for each phase gate
- **Governance standards** for token, treasury, and operations
- **Single source of truth** for all AEGIS communications

**Current Readiness Score: 5/10**

**Target Score (All Groups Complete): 8.5/10**

**Target Score (Full Package): 9+/10**

---

## Phase Gates

| Gate | Criteria | Unlock |
|------|----------|--------|
| **Gate 0: Internal Development** | Group A complete | Private testing |
| **Gate 1: Demand Validation** | Group A + B+1 targets | Public reservations |
| **Gate 2: Partner Outreach** | Group A + B + Visual Package | Manufacturer/dealer talks |
| **Gate 3: Fundraising** | Group A + B + C + E | Investor conversations |
| **Gate 4: Token Sale** | Group C fully resolved | Token launch |

---

# Group A — Immediate Launch Blockers

*Fix before collecting public reservations or speaking to investors.*

*These create legal exposure, kill credibility, and expose customer data.*

---

## A1: Company Identity

| Item | Required | Status | Priority |
|------|----------|--------|----------|
| Registered company name | Legal entity name | ❌ Missing | 🔴 Critical |
| Registration number | Official business ID | ❌ Missing | 🔴 Critical |
| Country of incorporation | Jurisdiction | ❌ Missing | 🔴 Critical |
| Registered office address | Physical location | ❌ Missing | 🔴 Critical |
| Contact number | Direct line | ❌ Missing | 🔴 Critical |
| Public email domain | @aegis-motors.com | ⚠️ Inconsistent | 🟡 High |

**Why it matters:** Without a disclosed legal entity, visitors assume the project is anonymous. This destroys trust with investors, partners, and customers immediately.

---

## A2: Founder Credibility Package

| Item | Required | Status | Priority |
|------|----------|--------|----------|
| Founder photo | Professional headshot | ❌ Missing | 🔴 Critical |
| Professional biography | 200-400 words | ❌ Missing | 🔴 Critical |
| Experience timeline | Career highlights | ❌ Missing | 🔴 Critical |
| LinkedIn profile | Public verification | ❌ Missing | 🔴 Critical |
| Public email | Direct contact | ❌ Missing | 🔴 Critical |

**Why it matters:** Founders are the product in early-stage companies. Anonymous or absent founders signal a project that may disappear.

---

## A3: Legal Pages

| Document | Status | Action Required |
|----------|--------|-----------------|
| Terms of Service | ❌ Missing | Create binding T&Cs for reservations |
| Privacy Policy | ❌ Missing | GDPR-compliant data handling policy |
| Reservation Policy | ❌ Missing | Refund/cancellation terms, non-binding disclosure |
| Warranty Framework | ❌ Missing | Basic warranty terms (can be placeholder) |

**Why it matters:** Operating without these exposes AEGIS to legal liability and prevents customers from trusting the reservation system.

---

## A4: Security & Data Protection

| Issue | Severity | Current Status | Fix Required |
|-------|----------|----------------|--------------|
| Admin dashboard unprotected | 🔴 Critical | Exposed | Add authentication or restrict access |
| No rate limiting | 🔴 High | Vulnerable | Implement request throttling on API |
| No CAPTCHA | 🔴 High | Bot target | Add to all public forms |
| SQL injection risk | 🔴 High | Possible | Parameterized queries or ORM |
| No email verification | 🟡 Medium | Unverified | Send confirmation on reservation |

**Admin exposure is the most urgent.** Full customer PII (names, emails, phones, preferences) is publicly accessible at `/admin`.

---

## A5: Technical Bugs

| Bug | Location | Impact |
|-----|----------|--------|
| Duplicate code block | server.py lines 163-197 | Will cause execution errors |

---

## A6: Documentation Discrepancies

| Claim | Document A | Document B | Resolution |
|-------|-----------|-----------|------------|
| Range | README: "150km+" | index.html: "60 km" | Lock one specification |

---

# Group A+1 — Reputation Blockers

*Not legal blockers, but can destroy trust immediately.*

---

## A+1.1: Company Public Information

| Item | Required | Status |
|------|----------|--------|
| Registered company name | Disclosed | ❌ Missing |
| Registration number | Disclosed | ❌ Missing |
| Country of incorporation | Disclosed | ❌ Missing |
| Registered office address | Disclosed | ❌ Missing |
| Contact number | Disclosed | ❌ Missing |

---

## A+1.2: Visual Proof Package

| Item | Required | Status | Priority |
|------|----------|--------|----------|
| Front render | Vehicle visualization | ❌ Missing | 🔴 High |
| Side render | Vehicle visualization | ❌ Missing | 🔴 High |
| Rear render | Vehicle visualization | ❌ Missing | 🔴 High |
| Feature highlights | Annotated views | ❌ Missing | 🟡 Medium |
| Product Overview PDF | 1-page downloadable | ❌ Missing | 🔴 High |

**Why it matters:** Customers cannot reserve what they cannot visualize. Even concept sketches dramatically increase conversion.

---

# Group A+2 — Product Credibility Blockers

*Required before production commitments, but needed for reservations.*

---

## A+2.1: Minimum Visual Requirements

| Asset | Purpose | Priority |
|-------|---------|----------|
| Front render | Hero image, social | 🔴 High |
| Side render | Specifications context | 🔴 High |
| Rear render | Complete view | 🟡 Medium |
| Interior detail | Premium positioning | 🟡 Medium |
| Feature callouts | Value communication | 🟡 Medium |

---

## A+2.2: Product Overview PDF

**Required content:**

- Vehicle overview paragraph
- Preliminary specifications table
- Timeline/roadmap
- Contact information
- Disclaimer language

**Template disclaimer:**
> *"Vehicle specifications shown are preliminary targets based on engineering estimates. Final specifications will be confirmed following prototype testing and manufacturing partner selection. Reservations are non-binding and will not be charged until production is confirmed."*

---

# Group B — Important But Not Required for Demand Validation

*The audit was too strict in demanding production-ready assets. Transparency is acceptable.*

---

## Transparency Language (Required)

All product pages must include:

> *"Specifications shown are preliminary and subject to engineering validation. Images are concept renders. Final product may vary."*

---

## What You Do NOT Need for Phase 1:

| Item | Why Not Required | Alternative |
|------|-----------------|-------------|
| Production-ready vehicle | Validated demand is the goal | Transparency language |
| Final prototype | Can come after reservations | Development timeline |
| Type approval | Required only before sales | Certification roadmap |
| Signed manufacturing contract | Validates after demand proven | Partnership interest |

---

## What You DO Need in Group B:

| Item | Purpose | Status |
|------|---------|--------|
| Concept renders or sketches | Customer imagination aid | ❌ Missing |
| Preliminary spec sheet | Sets expectations | ⚠️ Inconsistent |
| Estimated MSRP range | Enables purchase decision | ❌ Missing |
| Clear "preliminary" labeling | Legal protection | ❌ Missing |

---

# Group B+1 — Demand Validation Requirements

*Explicit success criteria before manufacturing discussions.*

---

## Phase 1 Targets

| Metric | Target | Purpose |
|--------|--------|---------|
| Total reservation leads | 100+ | Market demand validation |
| Qualified leads | 25+ | Serious buyer interest |
| Fleet inquiries | 10+ | B2B demand signal |
| Dealer inquiries | 5+ | Distribution interest |

---

## Success Criteria

| Gate | Must Achieve | Enables |
|------|--------------|---------|
| Demand Validation | 100 reservations | Proceed to manufacturing talks |
| Qualified Interest | 25 qualified | Proceed to investor conversations |
| B2B Signal | 10 fleet + 5 dealer | Proceed to partner outreach |

---

# Group B+2 — Manufacturing Readiness

*Required before production commitments, but not before reservations.*

---

## Required Before Production:

| Item | Purpose | Status |
|------|---------|--------|
| RFQ package | Manufacturing specifications | ❌ Missing |
| Cost model | Unit economics | ❌ Missing |
| Supplier list | Supply chain | ❌ Missing |
| Manufacturing partner shortlist | Candidate partners | ❌ Missing |
| Warranty framework | Customer protection | ❌ Missing |

---

# Group C — Token Launch Concerns

*These represent the highest regulatory and credibility risk. Must be resolved before any public token sale.*

---

## C1: Unlimited Minting Risk 🔴

**The Problem:**

```solidity
function mint(address to, uint256 amount) public onlyOwner {
    _balances[to] += amount;
    _totalSupply += amount;
}
```

The contract allows unlimited token minting. This creates:

| Risk | Impact |
|------|--------|
| Investor trust | "Owner can dump unlimited tokens" |
| Exchange listing | CEX may reject due to inflation risk |
| Credibility | Community flags as potential rugpull |
| Regulatory | May be classified as security |

**Required Fix (Choose One):**

| Option | Implementation | Complexity |
|--------|---------------|----------|
| Remove minting | Delete function entirely | Low |
| Strict cap | Only mint up to max supply | Medium |
| Multi-sig | Require multiple approvals | High |

---

## C2: Vesting Not Enforced ⚠️

**The Problem:**

- Documentation: "4-year vesting"
- Contract: NO vesting logic
- Reality: Owner can distribute 100% immediately

**The Risk:**

| Issue | Consequence |
|-------|-------------|
| False advertising | Investor lawsuits |
| Securities violations | Regulatory action |
| Reputation damage | Community trust loss |

**Required Fix (Choose One):**

| Option | Implementation | Complexity |
|--------|---------------|----------|
| Implement vesting contract | Time-locked release | High |
| Remove claims | Delete vesting language | Low |
| Escrow wallet | Multisig for team tokens | Medium |

---

## C3: Profit Sharing Claims ⚠️

**The Problem:**

Documents state: *"30% of net profit distributed to token holders"*

| Jurisdiction | Risk Level | Action |
|--------------|------------|--------|
| United States | High | Remove or consult attorney |
| EU | Medium | MiCA compliance review |
| Singapore | Low | Still requires compliance |
| Most Asia-Pacific | Varies | Jurisdiction review |

**Required Fix:**

| Avoid | Use Instead |
|-------|-------------|
| ❌ Guaranteed returns | ✅ Community participation |
| ❌ Profit distribution promises | ✅ Ecosystem utility |
| ❌ Investment opportunity language | ✅ Governance participation |

**Until formal legal review is completed.**

---

## C4: Token Without Registered Company

Cannot legally:
- Issue tokens on behalf of an unnamed entity
- Open exchange accounts
- Sign listing agreements
- Protect token holders

**This blocks the entire token launch.**

---

# Group C+1 — Treasury Governance

*Who controls funds? Investors will ask.*

---

## Required Treasury Controls:

| Item | Requirement | Status |
|------|-------------|--------|
| Multi-signature wallet | 3-of-5 or similar | ❌ Missing |
| Monthly reporting | Public fund updates | ❌ Missing |
| Fund allocation disclosure | Use of funds clarity | ⚠️ Partial |
| Spending authority | Defined approval process | ❌ Missing |
| Audit process | Annual or quarterly | ❌ Missing |

---

## Treasury Governance Checklist:

- [ ] Multi-sig wallet established (3-of-5 recommended)
- [ ] Signers identified and disclosed
- [ ] Monthly reporting template created
- [ ] Fund allocation policy documented
- [ ] Spending authority matrix defined
- [ ] Audit process established

---

# Group C+2 — Regulatory Language

*Remove absolute claims. Use compliant language.*

---

## Prohibited Language:

| ❌ Avoid | Reason |
|----------|--------|
| "Guaranteed returns" | False promise |
| "Profit distribution" | Security risk |
| "Investment opportunity" | Regulatory classification |
| "Passive income" | Securities risk |
| "Must buy" | Coercive |
| "Limited time" | Manipulative |

---

## Approved Language:

| ✅ Use Instead | Context |
|----------------|---------|
| "Community participation" | Token utility |
| "Ecosystem utility" | Token purpose |
| "Governance participation" | Token rights |
| "Staking rewards" | If implemented |
| "Subject to" | All forward-looking statements |
| "Preliminary" | All specifications |

---

# Group D — Operations Readiness

*Completely missing from current documentation.*

---

## D1: Customer Support

| Item | Required | Status |
|------|----------|--------|
| Support email | hello@aegis-motors.com | ⚠️ Inconsistent |
| Ticket process | System for tracking | ❌ Missing |
| FAQ | Common questions | ❌ Missing |
| After-sales contact | Post-purchase support | ❌ Missing |

---

## D2: Service Infrastructure

| Item | Required | Status |
|------|----------|--------|
| Service plan | Maintenance offerings | ❌ Missing |
| Warranty process | Claims procedure | ❌ Missing |
| Spare parts strategy | Availability plan | ❌ Missing |
| Fleet support | Dedicated service | ❌ Missing |

---

## D3: Fleet Support

| Item | Required | Status |
|------|----------|--------|
| Fleet onboarding | Process for bulk orders | ❌ Missing |
| Maintenance support | Ongoing service | ❌ Missing |
| Account management | Dedicated contact | ❌ Missing |

---

# Group E — Investor Readiness

*Before approaching investors, these materials are required.*

---

## E1: Executive Summary

| Item | Length | Status |
|------|--------|--------|
| Company overview | 1 paragraph | ❌ Missing |
| Problem statement | 1 paragraph | ❌ Missing |
| Solution | 1 paragraph | ❌ Missing |
| Market opportunity | 1 paragraph | ❌ Missing |
| Team summary | 1 paragraph | ❌ Missing |
| Ask | Clear ask | ❌ Missing |

**Target length: 2 pages maximum**

---

## E2: Investor Deck

| Section | Slides | Status |
|---------|--------|--------|
| Problem | 1-2 | ❌ Missing |
| Solution | 2-3 | ❌ Missing |
| Product | 2-3 | ❌ Missing |
| Market | 1-2 | ❌ Missing |
| Business model | 1-2 | ❌ Missing |
| Traction | 1-2 | ❌ Missing |
| Team | 1-2 | ❌ Missing |
| Financials | 2-3 | ❌ Missing |
| Ask | 1 | ❌ Missing |

**Target: 10-15 slides**

---

## E3: Financial Model

| Item | Required | Status |
|------|----------|--------|
| 3-year projections | Minimum | ❌ Missing |
| Revenue model | Detailed | ❌ Missing |
| Cost structure | Per unit | ❌ Missing |
| Margin analysis | Gross/net | ❌ Missing |
| Cash flow | Monthly | ❌ Missing |

---

## E4: Corporate Governance

| Item | Required | Status |
|------|----------|--------|
| Cap table | Ownership structure | ❌ Missing |
| Funding plan | Use of funds | ⚠️ Partial |
| Dilution schedule | Per round | ❌ Missing |
| Voting rights | Share class details | ❌ Missing |

---

# Readiness Scorecard

---

## Current State Assessment

| Category | Score | Key Issues |
|----------|-------|------------|
| Website | 7.5/10 | Functional but security gaps |
| Product Definition | 4/10 | No renders, inconsistent specs |
| Business Structure | 3/10 | No company, no entity |
| Legal Readiness | 1/10 | No T&C, privacy, warranty |
| Manufacturing Readiness | 2/10 | No RFQs, no cost model |
| Investor Readiness | 2/10 | No deck, no model |
| Token Readiness | 1/10 | Security risks, no vesting |
| Operations Readiness | 0/10 | No support infrastructure |

---

## Current Overall Score: 5/10

---

## After Completing Groups A-E: 8.5/10

---

## After Full Package: 9+/10

**Full Package Includes:**
- [ ] Company registration
- [ ] Product renders
- [ ] Manufacturing LOI
- [ ] Financial model
- [ ] Investor deck

---

# Recommended Deliverable: AEGIS Master Dossier v1.0

**Single source of truth for all AEGIS communications.**

---

## Dossier Structure

```
AEGIS Master Dossier v1.0/
├── 01-Executive-Summary/
│   ├── Executive-Summary.docx
│   └── One-Pager.pdf
├── 02-Founder-Profile/
│   ├── Founder-Bio.docx
│   ├── Headshots/
│   └── LinkedIn-Links.txt
├── 03-Company-Information/
│   ├── Registration-Certificate.pdf
│   ├── Company-Overview.docx
│   └── Office-Address.txt
├── 04-Product-Definition/
│   ├── Product-Overview.pdf
│   ├── Specifications-Sheet.pdf
│   ├── Renders/
│   │   ├── Front.png
│   │   ├── Side.png
│   │   ├── Rear.png
│   │   └── Feature-Callouts.png
│   └── Roadmap.pdf
├── 05-Manufacturing-Strategy/
│   ├── Manufacturing-Approach.docx
│   ├── RFQ-Package.pdf
│   ├── Cost-Model.xlsx
│   └── Supplier-List.xlsx
├── 06-Market-Analysis/
│   ├── TAM-SAM-SOM.pdf
│   ├── Competitive-Analysis.xlsx
│   └── Target-Markets.pdf
├── 07-Revenue-Model/
│   ├── Revenue-Model.xlsx
│   └── Unit-Economics.pdf
├── 08-Fleet-Strategy/
│   ├── Fleet-Program-Overview.pdf
│   └── Fleet-Pricing.docx
├── 09-Dealer-Strategy/
│   ├── Dealer-Program-Overview.pdf
│   └── Dealer-Terms.docx
├── 10-Financial-Model/
│   ├── 3-Year-Projections.xlsx
│   ├── Cash-Flow.xlsx
│   └── Cap-Table.xlsx
├── 11-Roadmap/
│   └── Roadmap.pdf
├── 12-Legal-Framework/
│   ├── Terms-of-Service.docx
│   ├── Privacy-Policy.docx
│   ├── Reservation-Policy.docx
│   ├── Warranty-Terms.docx
│   └── Disclaimer-Language.txt
├── 13-Risk-Register/
│   └── Risk-Register.xlsx
├── 14-Token-Information/
│   ├── Token-Economics.pdf
│   ├── Smart-Contract-Audit.pdf
│   ├── Treasury-Policy.docx
│   └── Regulatory-Compliance.docx
└── 15-Investor-Summary/
    ├── Executive-Summary.pdf
    ├── Investor-Deck.pptx
    └── FAQ.pdf
```

---

## Dossier Governance

| Rule | Requirement |
|------|-------------|
| Version control | Increment version for each change |
| Owner | Designated AEGIS executive |
| Access | Controlled distribution list |
| Review cycle | Quarterly review |
| Update trigger | Any material change |

---

# Implementation Roadmap

---

## Phase 1: Foundation (Weeks 1-4)

| Week | Deliverable | Owner |
|------|-------------|-------|
| 1 | Company registration | Founder |
| 1 | Founder profile | Founder |
| 2 | Legal pages (T&C, Privacy, Warranty) | Legal counsel |
| 2 | Admin security fix | Developer |
| 3 | Visual package (renders) | Design agency |
| 3 | Product Overview PDF | Founder |
| 4 | Specification lock | Engineering |
| 4 | Contact consolidation | Founder |

---

## Phase 2: Demand Validation (Weeks 5-12)

| Week | Deliverable | Success Metric |
|------|-------------|----------------|
| 5-8 | Launch reservation system | 25 reservations |
| 9-12 | Marketing push | 100 reservations |
| 12 | Gate 1 review | 25 qualified |
| 12 | Fleet outreach | 5 fleet inquiries |
| 12 | Dealer outreach | 3 dealer inquiries |

---

## Phase 3: Partner Readiness (Months 4-6)

| Month | Deliverable |
|-------|-------------|
| 4 | RFQ package |
| 4 | Cost model |
| 5 | Supplier shortlist |
| 5 | Manufacturing partner conversations |
| 6 | LOI or intent letter |

---

## Phase 4: Investor Readiness (Months 6-9)

| Month | Deliverable |
|-------|-------------|
| 6 | Executive summary |
| 7 | Investor deck |
| 8 | Financial model |
| 8 | Cap table |
| 9 | Legal structure review |

---

## Phase 5: Token Resolution (Months 6-12)

| Month | Deliverable |
|-------|-------------|
| 6 | Legal review of token structure |
| 7 | Smart contract fixes |
| 8 | Treasury governance |
| 9 | Community launch |
| 12 | Token sale (if approved) |

---

# Conclusion

---

## Launch Readiness Summary

| Phase | Status | Gate |
|-------|--------|------|
| Current State | 5/10 | Not ready |
| After Group A | 6.5/10 | Soft launch possible |
| After Groups A+B | 7.5/10 | Demand validation |
| After Groups A+B+C | 8/10 | Partner outreach |
| After Groups A+B+C+D+E | 8.5/10 | Investor ready |
| Full Package | 9+/10 | Production ready |

---

## The Fundamental Question

> *"Do you have anything to launch?"*

**Current answer:** You have a platform with no company, no product, no pricing, no legal framework, and a token with security concerns.

**Required before launch:**
1. Registered company
2. Founder profiles
3. Legal pages
4. Product renders (even concept)
5. Specification lock
6. Admin security fix

**Once these are complete, you have a legitimate pre-launch presence that can collect demand and approach partners.**

---

## Next Single Document

**Create the AEGIS Master Dossier v1.0**

This single document becomes the single source of truth for:
- Website pages
- Investor decks
- Manufacturer proposals
- Dealer packages
- Partnership presentations
- Legal filings
- Token documentation

Once it exists, every external communication is generated from it consistently.

---

*Framework Version: 1.0*
*Last Updated: July 2026*
*Next Review: October 2026*

---

**End of AEGIS Launch Governance Framework**
