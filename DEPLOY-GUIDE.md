# 🌍 Deployment Guide — Nehal Portfolio (Free Hosting)

Ye guide batata hai ki site ko **free hosting** par kaise live kare.
2 options: **Render** (recommended) ya **Railway**.

---

## 🎯 Option A: Render.com (Recommended)

### 1. Render account banao
- https://render.com → "Get Started" → GitHub se signup

### 2. Code GitHub par push karo
```bash
cd nehal-portfolio
git init
git add .
git commit -m "Nehal Agarwal — medical portfolio v1"
# GitHub par naya repo banao, phir:
git remote add origin https://github.com/USERNAME/nehal-portfolio.git
git push -u origin main
```

### 3. Render par deploy karo
Is repo me `render.yaml` blueprint ready hai. Render Dashboard → **New → Blueprint** se repo select karo, phir secret values enter karo. Manual Web Service use kar rahe ho to ye settings rakho:
1. Dashboard → **New** → **Web Service**
2. Apna repo connect karo
3. Settings:

| Setting | Value |
|---|---|
| **Name** | `nehal-portfolio` |
| **Runtime** | Node |
| **Build Command** | `npm install && npm run build` |
| **Start Command** | `npm start` |
| **Root Directory** | (empty — root) |

4. **Environment Variables** add karo (New → Environment):
```
JWT_SECRET=kuch-strong-secret
ADMIN_USERNAME=admin
ADMIN_PASSWORD=apna-password
MONGODB_URI=         (recommended — MongoDB Atlas)
CLIENT_ORIGIN=       (optional)
CLOUDINARY_CLOUD_NAME=   (optional — uploads persist karne ke liye)
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

5. **Create Web Service** → Render install + deploy karega (2-4 min)

### Vercel frontend + Render API
Vercel par frontend deploy karte waqt `VITE_API_URL` ko apne Render backend URL par set karo, for example `https://nehal-portfolio.onrender.com` (trailing slash ke bina). Render ke `CLIENT_ORIGIN` me `https://nehal-agarwal.vercel.app` add karo. Vercel redeploy ke baad `/api/content` 404 nahi karega.

### 4. Done! 🎉
Render link dega: `https://nehal-portfolio.onrender.com`
- Website: usi link par
- Admin: `https://nehal-portfolio.onrender.com/admin`

> ⚠️ Render free tier par server inactivity me sleep ho sakta hai — pehla load thoda slow
> hota hai (resume hota hai). Ye normal hai.

---

## 🎯 Option B: Railway.app

Railway par **New Project** → Deploy from GitHub repo.

- Build: `npm install && npm run build`
- Start: `npm start`
- Env vars bhi wahi daalo

---

## 🗄️ MongoDB Atlas (free database)

JSON files **server par change hokar redeploy par reset ho jati hain** (free hosting ka filesystem
ephemeral hota hai). **Production me MongoDB chahiye** taaki Nehal ke edits persist rahe:

1. https://mongodb.com → Atlas free cluster banao
2. Database + user banao
3. Connection string copy karo:
   `mongodb+srv://USER:PASS@cluster.mongodb.net/nehal-portfolio?retryWrites=true&w=majority`
4. Render env me `MONGODB_URI` me daalo

> Pehli baar `/api/content` hit hone par seed data (`server/data/db.json`) Mongo me copy ho jata hai.
> Uske baad Mongo wala data hi authoritative hai.

---

## 🖼️ Photo & certificate uploads

Free hosting par `server/uploads/` folder ephemeral hai — redeploy par files chali jati hain.
Production ke liye **Cloudinary** (free tier) best hai:

1. https://cloudinary.com → free account
2. Dashboard se `cloud_name`, `api_key`, `api_secret` copy karo
3. Render env me teeno daalo
4. Bas — ab uploads seedha Cloudinary par jayenge aur permanently rahenge

Cloudinary set nahi kiya to bhi site chalegi, bas uploads local disk par rahenge.

---

## 🔐 Security Checklist (deploy se pehle)

- [ ] Is chat/local `.env` me exposed MongoDB, Cloudinary, admin aur JWT credentials ko revoke/rotate karo; in values ko GitHub ya screenshots me kabhi commit na karo
- [ ] `JWT_SECRET` — lambi random string (32+ chars)
- [ ] `ADMIN_USERNAME` / `ADMIN_PASSWORD` — `.env` wali values ya nayi strong values set karo
- [ ] Panel ke Settings se username + password change karke verify karo
- [ ] MongoDB connected (edits persist honge)
- [ ] Cloudinary set (certificates/photos persist honge)
- [ ] `CLIENT_ORIGIN` sirf deployed origin par set
- [ ] Deploy ke baad `/api/health`, homepage, `/admin`, contact form, LinkedIn link aur ek upload test verify karo
- [ ] Nehal ki real email/phone/photo bhari gayi (`python3 scripts/list_todos.py` se check karo)

---

## 📁 Project Structure (quick)

```
nehal-portfolio/
├── package.json            # npm scripts
├── .env.example            # env template
├── scripts/
│   ├── build_content.py    # seed content generator (db.json)
│   └── list_todos.py       # kya bharna baaki hai — content check
├── server/
│   ├── index.js            # Express API (port 5000)
│   ├── store.js            # data read/write (MongoDB ya JSON)
│   ├── config.js           # env parsing, JWT, Cloudinary
│   ├── adminStore.js       # admin credentials
│   ├── middleware/auth.js  # JWT auth
│   ├── models/             # Mongoose models
│   └── data/
│       ├── db.json         # content (local fallback / seed)
│       └── messages.json   # contact messages (local)
└── client/
    ├── index.html          # SEO meta tags
    ├── vite.config.js      # proxy /api -> 5000
    ├── public/
    │   └── profile-photo.svg   # placeholder (real photo: profile-photo.png)
    └── src/
        ├── main.jsx        # React app (site + admin panel)
        └── styles.css      # sab styling (medical teal/dark theme)
```

**Done! Ab Nehal ki website duniya me live hai. 🌍🚀**
