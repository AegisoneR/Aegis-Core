# Domain Setup: aegismotors.com

## Step 1: Buy Domain
Register at: Namecheap, GoDaddy, Cloudflare, or Google Domains
**Domain:** aegismotors.com

---

## Step 2: GitHub Pages Setup

### Option A: GitHub Pages (Free)
1. Go to: https://github.com/Shad-Brothers/Aegis-Core/settings/pages
2. Source: Deploy from a branch
3. Branch: main, / (root)
4. Custom domain: aegismotors.com
5. Save

### Option B: Cloudflare Pages
1. Go to: https://pages.cloudflare.com
2. Connect GitHub repo
3. Deploy branch: main
4. Custom domain: aegismotors.com

---

## Step 3: DNS Configuration

### Cloudflare DNS Records

| Type | Name | Content | Proxy |
|------|------|---------|-------|
| A | @ | 192.0.2.1 | Grey cloud |
| CNAME | www | Shad-Brothers.github.io | Orange cloud |
| CNAME | @ | Shad-Brothers.github.io | Orange cloud |

**Note:** Replace 192.0.2.1 with your actual server IP if self-hosting.

---

## Step 4: Enable SSL
1. In Cloudflare dashboard
2. SSL/TLS → Overview
3. Set to "Full" or "Flexible" (Full for GitHub Pages)

---

## Step 5: Email Setup (Google Workspace)

###MX Records for Gmail:
| Priority | Host | Value |
|----------|------|-------|
| 1 | @ | aspmx.l.google.com |
| 5 | @ | alt1.aspmx.l.google.com |
| 5 | @ | alt2.aspmx.l.google.com |
| 10 | @ | alt3.aspmx.l.google.com |
| 10 | @ | alt4.aspmx.l.google.com |

### TXT Record:
```
v=spf1 include:_spf.google.com ~all
```

---

## Step 6: www Redirect

### Cloudflare Page Rule:
```
URL: www.aegismotors.com/*
Forward to: https://aegismotors.com/$1
Status: 301 (Permanent)
```

---

## Verification Checklist

- [ ] Domain purchased
- [ ] GitHub Pages enabled
- [ ] DNS propagated
- [ ] SSL certificate active
- [ ] Email configured
- [ ] www redirect working
- [ ] HTTPS forced

---

## Timeline
- Domain purchase: Immediate
- DNS propagation: 24-48 hours
- SSL certificate: Automatic (Let's Encrypt)
- Email setup: 1-2 hours
