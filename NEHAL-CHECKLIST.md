# ✅ Nehal Checklist — v2 (actual-data-only rebuild)

**Rule followed:** jo cheez Nehal ke LinkedIn profile / diye gaye details me nahi thi,
wo site se **hata di gayi hai**. Ab har entry traceable hai — koi invented clinical
posting, placeholder award ya speculative sample nahi bacha.

---

## 1. Jo lag chuka hai (real data)

| Cheez | Value | Source |
|---|---|---|
| Photo | `client/public/profile-photo.png` (clean crop, frame removed) | di gayi image |
| Framed original | `archive/profile-photo-linkedin-framed.png` (#OPENTOWORK version, archive) | di gayi image |
| Email | nehalagarwal@gmail.com | diye gaye details |
| Phone | +91 98979 49692 (contact section me `tel:` link ke saath) | diye gaye details |
| Headline / tagline | Final-Year MBBS Student \| Medical Content Writing \| Healthcare Communication \| Medical Education \| Content Creation | LinkedIn headline |
| Experience | Student, GMC Chittorgarh, Sep 2023 – Present (ICMR-STS research, TB/AIDS awareness competitions, 2nd class topper, fest organisation) | LinkedIn experience |
| Education | MBBS, GMC Chittorgarh, Sep 2023 – May 2028 + activities; Sophia Secondary School | LinkedIn education |
| Open to work | Research Assistant, Medical Writer, Web Content Writer, Health Educator | LinkedIn open-to-work |
| Services (9) | Writing, Editing, Content Strategy, UX Writing, Video Editing, Public Speaking, Career Development Coaching, Leadership Development, Life Coaching | LinkedIn services |
| Skills (chips) | Medical Writing, Health Writing, Writing For The Web, Web Content, Health Promotion, Wellness Education, Written Communication, Clinical Research, Presentation Skills, Creative Content Creation | LinkedIn skills |
| Recommendation | Ayesha Agarwal (KPMG Valuation, CFA L1, ex-JP Morgan), 3 Sep 2026 — verbatim quote | LinkedIn recommendation |
| ICMR-STS project | AI-assisted peripheral blood smear screening + rural healthcare empowerment | LinkedIn education activities |
| Awards | 2nd class topper (1st prof year); AIDS poster winner; TB poster 2nd | LinkedIn |
| Presentations | Academic topics in Microbiology | LinkedIn |
| Leadership | Medical college fest activities organisation | LinkedIn |

**Site structure:** 13 entries · 6 highlights · 5-step timeline · 9 categories.

---

## 2. v1 se kya-kya HATAYA gaya (unwanted content)

- ❌ 8 invented clinical posting entries (Medicine/Surgery/OBG/Paediatrics/PSM/ENT/Para/Pre-clinical) — LinkedIn par nahi the
- ❌ Generic research-interest / evidence-based-practice entries
- ❌ 5 speculative writing-sample entries (patient education, exam content, web articles, editing, video)
- ❌ 3 generic health-education entries, 3 generic volunteering entries, 2 generic leadership entries
- ❌ 3 programs entries (skills lab/AETCOM, ECE, self-learning)
- ❌ Placeholder slots: `cert-slot`, `award-slot`, `media-slot`
- ❌ 4 alag target-role entries + content-library/portfolio-project entries
- ✅ Retained (real): ICMR-STS, rank, 2 posters, MBBS, Sophia, open-to-work, services, Microbiology presentations, fest organisation, 2 focus entries (headline+skills se), recommendation

---

## 3. ⚠️ Ab bhi confirm karna hai (chhote items)

1. **Rank contradiction:** experience + education me "2nd / 2nd class topper", About me
   "Ranked first in the MBBS first year". Site par **2nd** likha hai (2 sources vs 1).
   Ye note ab site par nahi dikhta (production copy clean hai) — yahan track ho raha hai; Nehal se exact rank pooch lein.
2. **ICMR-STS:** project start year, guide ka naam, status (ongoing/submitted/published).
3. **Posters:** organising body, event name, year + certificate/poster images (proof attach karein).
4. **Education:** LinkedIn par total **5 education entries** hain — sirf 2 visible thi;
   baaki 3 add kar sakte hain.
5. **Sophia Secondary School:** board, year, percentage (optional).
6. **Skills ke %:** skill bars self-assessed hain (naam LinkedIn se, percentage subjective) —
   admin → Profile se badal sakte hain.
7. **Writing samples:** jab published links/PDF mil jayein, Writing entry me proof attach karein.

Ye notes public site par nahi chhape jate (build script unhe descriptions se strip kar deta hai) — sirf yahan track hote hain.

Sab ek command se:
```bash
python3 scripts/list_todos.py
```

---

## 4. Admin login (production credentials)

| Kya | Value |
|---|---|
| URL | site ke aage `/admin` |
| Username | `nehal` |
| Password | `Nehal@2026` |

- Dono cheezein **panel ke andar se change** hoti hain: **Settings → "Change admin password"** aur **"Change admin username (login ID)"** (current password required).
- Password bcrypt hash me store hota hai; 5 galat attempts par 15-min lock.
- `.env` me yahi credentials hain (gitignored) — deploy par Render/Railway env me set karein.

## 5. Nehal ko bhejne se pehle final check

```bash
npm install
npm run dev          # site: :5173  ·  admin: :5173/admin  (admin / portfolio2026)
python3 scripts/list_todos.py
```

- [x] Real photo (clean crop) lagi hui
- [x] Email + phone contact section me
- [x] Sirf actual LinkedIn data — 13 entries
- [ ] Rank confirm (1st ya 2nd)
- [ ] Certificates/poster images proof ke roop me attach
- [ ] Dark + light theme, mobile check
- [ ] Contact form → admin Inbox test

---

## 5. Deploy

Full guide: `DEPLOY-GUIDE.md` (Render + MongoDB Atlas + Cloudinary).
Deploy se pehle: `ADMIN_PASSWORD` + `JWT_SECRET` change karein.
