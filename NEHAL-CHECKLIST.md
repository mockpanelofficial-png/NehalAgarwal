# ✅ Nehal Checklist — kya chahiye, kya ready hai

Ye site Nehal Agarwal ke **public LinkedIn profile** se li gayi information par bani hai.
Jo cheezein LinkedIn par nahi thi, wo **khali ya placeholder** rakhi gayi hain — kuch bhi
invented nahi kiya gaya.

---

## 1. LinkedIn se confirm ho chuka hai (site par laga diya gaya)

| Cheez | Value | Kaha use hui |
|---|---|---|
| Naam | Nehal Agarwal (She/Her) | Hero, footer, meta tags, preloader |
| Padhai | Final-Year MBBS | Hero tagline, stats, timeline, education entries |
| College | Government Medical College, Chittorgarh | Education, clinical entries, location |
| School | Sophia Secondary School | Education entry (`education-school`) |
| Location | Chittorgarh, Rajasthan, India | Profile location |
| Headline focus | Medical Content Writing · Healthcare Communication · Medical Education · Content Creation | Roles, writing entries, skills |
| Open to work | Research Assistant, Medical Writer, Web Content Writer, Health Educator | 4 alag "Roles" entries + `open-to-work` highlight |
| Services | Video Editing, Career Development Coaching, Leadership Development, Public Speaking, Editing, Content Strategy, Life Coaching, UX Writing, Writing | `services` entry + skills + leadership entries |
| LinkedIn URL | https://www.linkedin.com/in/nehal-agarwal-6529a429a/ | Footer link, project entry proof |

---

## 2. MBBS curriculum se standard structure (verify karwa lein)

Ye **NMC CBME curriculum** ka standard sequence hai — har MBBS student ka yahi hota hai.
Fir bhi exact years Nehal se confirm karwa lein:

- **Phase I (2022)** — Anatomy, Physiology, Biochemistry
- **Phase II (2023)** — Pathology, Microbiology, Pharmacology
- **Phase III Part 1 (2024)** — ENT, Ophthalmology, FMT, Community Medicine (RHTC/URHC)
- **Phase III Part 2 (2025)** — Medicine, Surgery, OBG, Paediatrics
- **Final year (2026)** + 12-month CRMI internship

> Admission year `2022` maana gaya hai. Agar Nehal ka batch alag hai to **admin panel → Timeline**
> me saal badal dein (aur education entries me `2022–2026` update karein).

---

## 3. ⚠️ Nehal se chahiye — ye bharna zaroori hai

### A. Photo
- [ ] Nehal ki professional photo → `client/public/profile-photo.png` naam se save karo
      (admin panel se bhi upload kar sakte hain)
- Abhi medical placeholder SVG laga hai (stethoscope + ECG + `NA`)

### B. Contact
- [ ] **Email** — abhi `your.email@example.com` placeholder hai
- [ ] **Phone** (optional)
- [ ] **Resume/CV link** (optional — `site.resumeUrl`)

### C. Exact academic details
- [ ] MBBS admission batch / university name
- [ ] School: city, board (CBSE/RBSE/ICSE), year, percentage
- [ ] Elective subject (Phase III)
- [ ] Koi external BLS/ACLS certification

### D. Achievements — sabse important
- [ ] Certificates (courses, workshops, conferences) — image/PDF
- [ ] Awards, distinctions, competition results
- [ ] Publications / posters / paper presentations
- [ ] Published articles ke links
- [ ] Health camps — naam, jagah, date, kitne patients
- [ ] Leadership positions (societies, committees, events)

> In 4 cheezon ke liye admin panel me 3 **placeholder entries** pehle se bani hain:
> `cert-slot` (Certifications), `award-slot` (Awards), `media-slot` (Media).
> Har certificate ke liye entry duplicate karke proof attach kar dein.

---

## 4. Content me `CONFIRM:` notes

11 entries me `CONFIRM:` note chhoda gaya hai — matlab "yaha real detail daalni hai".
Sab ek saath dekhne ke liye:

```bash
python3 scripts/list_todos.py
```

---

## 5. Site me kya-kya hai (44 entries)

| Category | Entries | Kya hai |
|---|---|---|
| Clinical | 8 | Medicine, Surgery, OBG, Paediatrics, PSM/RHTC, ENT-Ophthal-FMT, Para-clinical, Pre-clinical |
| Writing | 6 | Patient education, medical education, web health, editing/strategy, video content |
| Roles | 6 | Open to work + 4 target roles + services |
| Health Education | 4 | Practice, vernacular Hindi, priority topics |
| Education | 3 | MBBS, school |
| Volunteering | 3 | Camps, awareness, peer mentoring |
| Leadership | 3 | Public speaking, organising, coaching |
| Programs | 3 | Skills lab/AETCOM, ECE/electives, self-learning |
| Research | 2 | Interests & appraisal, evidence-based practice |
| Projects | 2 | This portfolio, content library |
| Certifications / Awards / Media | 3 | Placeholder — Nehal bharegi |
| Community Health | 1 | RHTC/URHC field training |

**Timeline:** 5 steps (2022 → 2026) — hero section me dikhta hai.

---

## 6. Nehal ko bhejne se pehle final check

```bash
# 1. site chalao
npm install
npm run dev

# 2. content check
python3 scripts/list_todos.py

# 3. browser me kholo
#    http://localhost:5173        -> site
#    http://localhost:5173/admin  -> admin (admin / portfolio2026)
```

- [ ] Photo lag gayi
- [ ] Email/phone bhar diya
- [ ] Batch years confirm
- [ ] Kam se kam 2-3 real certificates/proofs attach
- [ ] Placeholder entries (`cert-slot`, `award-slot`, `media-slot`) fill ya delete
- [ ] Dark + light theme dono check
- [ ] Mobile par check
- [ ] Contact form submit karke admin → Inbox me message aaya ya nahi

---

## 7. Deploy ke baad

- Admin password + JWT secret change (`.env` me)
- MongoDB Atlas connect ( warna redeploy par edits reset)
- Cloudinary set (warna certificate uploads redeploy par gayab)
- Full guide: `DEPLOY-GUIDE.md`
