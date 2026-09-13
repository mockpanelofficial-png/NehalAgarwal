# 🚀 Nehal Portfolio — Kaise Run Kare (Hindi Guide)

Ye ek **MERN-stack** medical portfolio hai (React + Express + MongoDB optional).
Nehal Agarwal — Final-Year MBBS, GMC Chittorgarh ke liye banaya gaya hai.
Neeche **3 tarike** diye hain — jo aapke liye aasaan lage wahi use karo.

---

## ✅ Requirement (pehle check karo)

- **Node.js** version 18+
- **npm** (Node ke saath aata hai)
- Internet (dependencies download karne ke liye)

Check karo:
```bash
node --version
npm --version
```

---

## 🟢 TARIKA 1 — Development Mode (sabse aasaan)

```bash
# 1. Project folder me jao
cd nehal-portfolio

# 2. Dependencies install karo (sirf pehli baar)
npm install

# 3. Server + Client dono ek saath chalao
npm run dev
```

**Bas!** Fir browser me kholo:

| Kya | URL |
|---|---|
| 🌐 **Website** | http://localhost:5173 |
| 🔐 **Admin panel** | http://localhost:5173/admin |

**Admin login:** `admin` / `portfolio2026`

> 💡 `npm run dev` ek saath 2 cheezein chalata hai:
> - Express API → port `5000`
> - React (Vite) → port `5173`
>
> `Ctrl + C` se band karo. Code change karte hi page **auto-refresh** hota hai (hot reload).

---

## 🟡 TARIKA 2 — Production Mode (final build)

Jab website ready ho aur deploy karna ho:

```bash
cd nehal-portfolio
npm install
npm run build     # React ka optimized build banata hai (client/dist me)
npm start         # Express serve karta hai — build wala site + API dono
```

**Website:** http://localhost:5000
**Admin:** http://localhost:5000/admin

> 💡 Production me sirf ek server (5000) chalta hai — frontend + backend dono usi se serve hote hain.

---

## 🟠 TARIKA 3 — MongoDB + Real .env (optional, production ke liye)

Development me sab **local JSON files** me save hota hai (`server/data/db.json`) — bina MongoDB ke sab chal jata hai.

Production ke liye:

```bash
cp .env.example .env
```

`.env` me apni values daalo:

```env
PORT=5000
MONGODB_URI=mongodb+srv://USER:PASSWORD@CLUSTER/nehal-portfolio
JWT_SECRET=kuch-lambi-random-secret-string
ADMIN_USERNAME=admin
ADMIN_PASSWORD=apna-strong-password
CLIENT_ORIGIN=http://localhost:5173
```

Fir:
```bash
npm install
npm run build
npm start
```

> 💡 **MongoDB nahi daala toh bhi sab kaam karta hai** — JSON fallback use hota hai.
> MongoDB daalne par data waha save hota hai (deploy ke baad edits persist rehte hain).

---

## 📋 Quick Reference — Scripts

| Command | Kya karta hai |
|---|---|
| `npm install` | Sab dependencies install (pehli baar) |
| `npm run dev` | Dev server (5173 frontend + 5000 API) |
| `npm run build` | React production build banata hai |
| `npm start` | Production server (5000) — build serve karta hai |
| `npm run server` | Sirf backend (5000) |
| `npm run client` | Sirf frontend (5173) |

**Content scripts (Python):**

| Command | Kya karta hai |
|---|---|
| `python3 scripts/list_todos.py` | Kya-kya bharna baaki hai, sab list kar deta hai |
| `python3 scripts/build_content.py` | Seed content dobara banata hai (`server/data/db.json`) |

---

## 🔑 Admin Panel — sab kuch yaha se edit hota hai

- URL me `/admin` type karo (ya footer me 🔒 Admin link)
- Login: `admin` / `portfolio2026`
- Admin me **sab kuch edit** kar sakte ho:
  - **Entries** — portfolio entries add/edit/delete + certificate/photo/link proof attach
  - **Profile & hero** — naam, tagline, photo, stats, interests, profile cards, skills
  - **Sections & design** — headings, typed roles, ticker, contact section text
  - **Timeline** — MBBS journey ke milestones
  - **Inbox** — contact form se aaye messages
  - **Settings** — SEO title/description, default theme, password change

> ⚠️ Deploy karne se pehle `.env` me `ADMIN_PASSWORD` aur `JWT_SECRET` zaroor badlo!

---

## 🖼️ Photo kaise lagayein

1. Nehal ki photo ko `client/public/profile-photo.png` naam se save karo, **ya**
2. Admin panel → Profile → `Profile image` field me `/uploads/...` ya koi bhi URL daalo.

Abhi `client/public/profile-photo.svg` ek medical placeholder (stethoscope + ECG + `NA`) hai.

---

## 🧹 Problem aaye to

| Problem | Fix |
|---|---|
| `npm install` error | Internet check, phir `rm -rf node_modules client/node_modules && npm install` |
| Port 5173/5000 busy | `fuser -k 5173/tcp 5000/tcp` (Linux/Mac) ya process band karo |
| Blank page | `Ctrl+Shift+R` (hard refresh) — cache clear |
| Admin login fail | Password `.env` me change kiya? Wahi use karo |
| MongoDB connect error | `.env` se `MONGODB_URI` hata do — JSON fallback chalega |
| Uploads gayab ho gaye | Free hosting par folder ephemeral hota hai → Cloudinary env vars set karo |

---

**Happy coding! 🚀** Koi bhi issue aaye to pooch lo.
