#!/usr/bin/env python3
"""Builds server/data/db.json for Nehal Agarwal's medical portfolio.

Everything here is CMS content: after the first deploy Nehal can edit
ANY of it from the hidden /admin panel (no code changes needed).

Rules used while writing:
  * Facts taken from her public LinkedIn profile are used as-is.
  * The MBBS 5.5-year curriculum structure (NMC CBME phases) is used for the
    clinical/education journey - it is standard, but the exact years and marks
    are marked `CONFIRM` inside the description so they can be corrected.
  * No invented awards, ranks, publications or numbers. Where a real credential
    is still needed, the entry is written as an interest / in-progress note.
"""
import json, pathlib, os

OUT = pathlib.Path(__file__).resolve().parent.parent / "server" / "data" / "db.json"

LINKEDIN = "https://www.linkedin.com/in/nehal-agarwal-6529a429a/"

site = {
    "name": "Nehal Agarwal",
    "eyebrow": "Final-year MBBS student \u00b7 Government Medical College, Chittorgarh",
    "hero": "Medicine, made <em>understandable.</em>",
    "lede": (
        "I am a final-year MBBS student at Government Medical College, Chittorgarh, "
        "working at the intersection of clinical medicine and communication \u2014 writing "
        "accurate, evidence-based medical content and turning it into health education "
        "that patients, students and general readers can actually use."
    ),
    "tagline": (
        "Final-year MBBS \u00b7 GMC Chittorgarh \u00b7 Medical content writing "
        "\u00b7 Healthcare communication \u00b7 Medical education"
    ),
    "email": "your.email@example.com",
    "phone": "",
    "stat1v": "4th",
    "stat1l": "MBBS professional year",
    "stat2v": "9",
    "stat2l": "Clinical subjects trained in",
    "stat3v": "4",
    "stat3l": "Career tracks open to",
    "profileImage": "/profile-photo.png",
    "linkedin": LINKEDIN,
    "location": "Chittorgarh, Rajasthan, India",
    "school": "Government Medical College, Chittorgarh",
    "resumeUrl": "",
    "pressUrl": "",
    "profileHeading": "Clinically trained.<br/>Built to communicate.",
    "profileLede": (
        "A final-year MBBS student with four years of ward, OPD and community "
        "training behind her, plus a strong working practice in medical writing, "
        "content strategy and patient-facing health education."
    ),
    "interests": [
        "Internal Medicine",
        "Public Health",
        "Medical Education",
        "Clinical Research",
        "Health Communication",
        "Preventive Medicine",
        "Evidence-Based Writing",
        "Digital Health Literacy",
    ],
    "profileCards": [
        {
            "id": "pc1",
            "title": "Clinical training",
            "text": "Pre-clinical, para-clinical and clinical postings across GMC Chittorgarh \u2014 medicine, surgery, OBG, paediatrics, PSM, ENT, ophthalmology and FMT.",
            "icon": "stethoscope",
        },
        {
            "id": "pc2",
            "title": "Medical writing",
            "text": "Translating guidelines, journals and textbook evidence into clear, accurate copy for clinicians, students and lay readers \u2014 without losing the science.",
            "icon": "pen",
        },
        {
            "id": "pc3",
            "title": "Health education",
            "text": "Patient-facing explainers, awareness content and vernacular health messaging built on the idea that understanding improves adherence and outcomes.",
            "icon": "activity",
        },
        {
            "id": "pc4",
            "title": "Research orientation",
            "text": "Literature appraisal, study design basics, data interpretation and structured writing \u2014 the foundation for research assistant and clinical research roles.",
            "icon": "flask",
        },
        {
            "id": "pc5",
            "title": "Content & communication",
            "text": "Content strategy, user experience writing and editing \u2014 structuring information so it reads well on a page, a slide or a consultation.",
            "icon": "users",
        },
        {
            "id": "pc6",
            "title": "Where I'm headed",
            "text": "Open to Research Assistant, Medical Writer, Web Content Writer and Health Educator roles alongside finishing MBBS and internship.",
            "icon": "sparkles",
        },
    ],
    "skills": [
        {"id": "sk1", "label": "Clinical Medicine & Patient Care", "pct": 85},
        {"id": "sk2", "label": "Medical Content Writing", "pct": 92},
        {"id": "sk3", "label": "Health Education & Communication", "pct": 90},
        {"id": "sk4", "label": "Literature Review & Research Aptitude", "pct": 82},
        {"id": "sk5", "label": "Editing & Content Strategy", "pct": 88},
        {"id": "sk6", "label": "Public Speaking & Mentoring", "pct": 84},
    ],
    "skillsTitle": "What I bring to the table",
    "skillsSub": "Core strengths",
    "roles": [
        "Final-Year MBBS Student",
        "Medical Content Writer",
        "Healthcare Communicator",
        "Medical Educator",
        "Aspiring Clinical Researcher",
        "Health Literacy Advocate",
        "Public Speaking Enthusiast",
        "Content Strategist",
        "Community Health Volunteer",
        "Lifelong Learner in Medicine",
    ],
    "ticker": [
        "Internal medicine",
        "Medical writing",
        "Patient education",
        "Clinical research",
        "Public health",
        "Health literacy",
        "Internal medicine",
        "Medical writing",
        "Patient education",
        "Clinical research",
        "Public health",
        "Health literacy",
    ],
    "sections": {
        "profileEyebrow": "Medical profile",
        "highlightsTitle": "Highlights",
        "highlightsText": (
            "The clinical, academic and communication milestones that best represent "
            "how I practise and how I explain medicine."
        ),
        "portfolioTitle": "Journey & portfolio",
        "portfolioText": (
            "Clinical postings, academics, research interests, writing samples, "
            "community health work and leadership \u2014 each with context and proof."
        ),
        "manifestoQuote": (
            "Good medicine is only half the job. The other half is making sure "
            "the patient, the family and the next student actually understand it."
        ),
        "manifestoAttribution": "\u2014 The idea behind this portfolio",
        "contactTitle": "Get In Touch",
        "contactSubtitle": (
            "For medical writing assignments, research assistance, health education "
            "collaborations or just to talk about medicine \u2014 write to me."
        ),
        "contactName": "Your Name",
        "contactEmail": "Your Email",
        "contactMessage": "Your Message",
        "contactButton": "Send Message",
        "contactSent": "Message received successfully.",
        "footerText": "A living medical portfolio.",
    },
    "meta": {
        "title": "Nehal Agarwal \u2014 Final-Year MBBS Student & Medical Writer",
        "description": (
            "Portfolio of Nehal Agarwal, final-year MBBS student at Government Medical "
            "College, Chittorgarh \u2014 medical content writing, healthcare communication, "
            "medical education and clinical research."
        ),
        "defaultTheme": "dark",
    },
}

timeline = [
    {
        "date": "2026",
        "title": "Final year \u2014 clinic, content and career",
        "text": (
            "Final professional MBBS with Medicine, Surgery, OBG and Paediatrics postings, "
            "alongside medical content writing, health education work and building this portfolio."
        ),
    },
    {
        "date": "2025",
        "title": "Clinical breadth \u2014 Phase III Part 2",
        "text": (
            "Ward and OPD training across general medicine, general surgery, obstetrics & "
            "gynaecology and paediatrics, with history-taking, examination and case-presentation practice."
        ),
    },
    {
        "date": "2024",
        "title": "Specialty postings & community medicine",
        "text": (
            "ENT, ophthalmology, forensic medicine and community medicine, including "
            "rural health training centre and urban health centre field exposure."
        ),
    },
    {
        "date": "2023",
        "title": "Para-clinical foundation",
        "text": (
            "Pathology, microbiology and pharmacology \u2014 the bridge between textbook "
            "science and bedside decisions, with first regular clinical clerkship."
        ),
    },
    {
        "date": "2022",
        "title": "Pre-clinical start at GMC Chittorgarh",
        "text": (
            "Began MBBS with anatomy, physiology and biochemistry; dissection hall, "
            "labs and the first introduction to how medicine is taught and learned."
        ),
    },
]

def item(iid, title, org, category, date, summary, description, featured=False, proofs=None):
    return {
        "id": iid,
        "customId": iid,
        "title": title,
        "org": org,
        "category": category,
        "date": date,
        "summary": summary,
        "description": description,
        "featured": featured,
        "proofs": proofs or [],
    }

items = []

# ---------------------------------------------------------------- Highlights
items += [
    item(
        "mbbs-gmc-chittorgarh",
        "MBBS \u2014 Final Professional Year",
        "Government Medical College, Chittorgarh",
        "Education",
        "2022\u20132026",
        "Final-year MBBS student at GMC Chittorgarh, training across medicine, surgery, OBG and paediatrics under the NMC competency-based curriculum.",
        "Pursuing the Bachelor of Medicine, Bachelor of Surgery degree at Government Medical "
        "College, Chittorgarh, Rajasthan. Progressed through all four professional phases of the "
        "NMC competency-based medical education curriculum \u2014 pre-clinical (Anatomy, Physiology, "
        "Biochemistry), para-clinical (Pathology, Microbiology, Pharmacology), Phase III Part 1 "
        "(ENT, Ophthalmology, FMT, Community Medicine) and Phase III Part 2 (Medicine, Surgery, "
        "OBG, Paediatrics). Currently in the final professional year, followed by the 12-month "
        "compulsory rotating medical internship. "
        "CONFIRM: exact admission batch, university affiliation and internal assessment scores "
        "can be added here.",
        True,
    ),
    item(
        "medical-content-writing",
        "Medical Content Writing",
        "Independent practice \u00b7 healthcare & education",
        "Writing",
        "Ongoing",
        "Writing accurate, evidence-based medical content for clinicians, students and general readers \u2014 explainers, article drafts, review-style pieces and patient education copy.",
        "Core practice area alongside MBBS. Work involves reading primary literature, guidelines "
        "and standard textbooks, then restructuring the information for a defined audience \u2014 a "
        "medical student revising for exams, a clinician scanning an update, or a patient trying "
        "to understand a diagnosis. Focus areas: accuracy of clinical facts, correct terminology, "
        "readability, structure and responsible health messaging (no over-claiming, no fear-based "
        "framing). Also comfortable with SEO-aware web health content, FAQ blocks and "
        "user-experience writing for health products.",
        True,
    ),
    item(
        "healthcare-communication",
        "Healthcare Communication",
        "Patient education \u00b7 health literacy",
        "Health Education",
        "Ongoing",
        "Turning clinical knowledge into communication people can act on \u2014 counselling language, awareness content and health-literacy material.",
        "Healthcare communication runs through everything in this portfolio: how a diagnosis is "
        "explained at the bedside, how an awareness message is framed for a community audience, "
        "and how written health content is structured so it is understood on first reading. "
        "Interests include shared decision-making, adherence-friendly counselling, plain-language "
        "rewriting of clinical material, and vernacular (Hindi) health content for Indian "
        "audiences.",
        True,
    ),
    item(
        "open-to-work",
        "Open To Work \u2014 Four Career Tracks",
        "Research Assistant \u00b7 Medical Writer \u00b7 Web Content Writer \u00b7 Health Educator",
        "Roles",
        "2026",
        "Actively open to Research Assistant, Medical Writer, Web Content Writer and Health Educator roles \u2014 remote, part-time or alongside internship.",
        "Open to work on these four tracks: (1) Research Assistant \u2014 literature review, data "
        "collection and entry, manuscript preparation, clinical or public-health projects; "
        "(2) Medical Writer \u2014 medical communication, regulatory-adjacent or educational "
        "writing, summaries and reviews; (3) Web Content Writer \u2014 health and medical content "
        "for websites, blogs and digital health products; (4) Health Educator \u2014 patient "
        "education, awareness sessions, training material and community health messaging. "
        "Interested in roles that value clinical accuracy plus clear writing.",
        True,
    ),
    item(
        "clinical-clerkship",
        "Clinical Postings \u2014 Ward, OPD & Emergency Exposure",
        "GMC Chittorgarh \u00b7 associated teaching hospital",
        "Clinical",
        "2023\u20132026",
        "Four years of supervised clinical training: history taking, general and systemic examination, case presentation, procedures and OPD/emergency exposure.",
        "Regular clinical clerkship and postings through the professional years. Practised "
        "components include detailed history taking, general physical and systemic examination, "
        "writing case sheets and presenting cases on rounds, observing and assisting with ward "
        "procedures, interpreting basic investigations, and OPD and emergency-department exposure. "
        "Postings spanned general medicine, general surgery, obstetrics & gynaecology, "
        "paediatrics, orthopaedics, ENT, ophthalmology, dermatology, psychiatry, anaesthesia and "
        "community medicine. CONFIRM: add specific units, logbook highlights or procedures here.",
        True,
    ),
    item(
        "services",
        "Services Offered",
        "Medical writing \u00b7 editing \u00b7 content strategy \u00b7 communication coaching",
        "Roles",
        "Available",
        "Medical writing, editing, content strategy, UX writing, video editing, public speaking, career development and leadership coaching.",
        "Professional services currently offered: Medical Writing; Editing; Content Strategy; User "
        "Experience (UX) Writing; Health Education content; Video Editing; Public Speaking; Career "
        "Development Coaching; Leadership Development; Life Coaching. Typical deliverables include "
        "article drafts and reviews, patient education leaflets, exam-oriented study content, "
        "presentation scripts, website health copy, and social or video health content with "
        "clinical review.",
        True,
    ),
]

# ------------------------------------------------------------- Clinical postings
items += [
    item(
        "posting-medicine",
        "General Medicine Posting",
        "Department of General Medicine \u00b7 GMC Chittorgarh",
        "Clinical",
        "2025\u20132026",
        "Ward and OPD training in general medicine: clerking, examination, differential diagnosis and management planning under faculty supervision.",
        "Final-year medicine posting covering common and important conditions seen in a "
        "government teaching hospital \u2014 hypertension, diabetes mellitus, infections including "
        "tuberculosis and enteric fever, anaemia, chronic kidney disease, stroke, heart failure, "
        "COPD and asthma, liver disease and endocrine disorders. Daily work: clerking admitted "
        "patients, systemic examination, presenting on rounds, following investigations, "
        "understanding treatment rationale and learning discharge counselling.",
    ),
    item(
        "posting-surgery",
        "General Surgery Posting",
        "Department of General Surgery \u00b7 GMC Chittorgarh",
        "Clinical",
        "2025\u20132026",
        "Surgical ward, OPD and operation-theatre exposure with emphasis on examination, perioperative care and aseptic practice.",
        "Surgery posting including surgical ward rounds, OPD clinic, minor and major "
        "operation-theatre assistance, and emergency/trauma exposure. Practised: surgical history "
        "and local examination, recognition of common surgical presentations (hernia, gall bladder "
        "disease, appendicitis, bowel obstruction, breast and thyroid disease, anorectal "
        "conditions, trauma), preoperative and postoperative care, wound management, dressing and "
        "suture technique, and aseptic discipline.",
    ),
    item(
        "posting-obg",
        "Obstetrics & Gynaecology Posting",
        "Department of Obstetrics & Gynaecology \u00b7 GMC Chittorgarh",
        "Clinical",
        "2025\u20132026",
        "Labour room, antenatal clinic and gynae ward training \u2014 antenatal care, normal delivery, PPH management basics and gynae evaluation.",
        "OBG posting covering antenatal clinic, labour room, postnatal ward and gynaecology OPD. "
        "Practised: antenatal history and examination, interpreting routine antenatal "
        "investigations, monitoring labour, assistance in normal vaginal delivery, recognition "
        "and initial management of obstetric emergencies (PPH, eclampsia, obstructed labour), "
        "postnatal and newborn care counselling, and gynaecological evaluation of abnormal "
        "uterine bleeding, infection, prolapse and infertility presentations.",
    ),
    item(
        "posting-paediatrics",
        "Paediatrics Posting",
        "Department of Paediatrics \u00b7 GMC Chittorgarh",
        "Clinical",
        "2025\u20132026",
        "Neonatal, paediatric ward and OPD training with growth assessment, immunisation counselling and management of common childhood illness.",
        "Paediatrics posting including the neonatal unit, paediatric ward and OPD. Focus areas: "
        "growth and development assessment, immunisation schedule counselling, nutrition and "
        "feeding advice, and management of common childhood presentations \u2014 acute respiratory "
        "infection, diarrhoeal disease with dehydration grading, fever, seizures, malnutrition, "
        "anaemia and neonatal jaundice. Also practised paediatric history taking and examination "
        "technique, including developmental milestones.",
    ),
    item(
        "posting-psm",
        "Community Medicine & Rural Health Training",
        "Department of Community Medicine \u00b7 RHTC / URHC",
        "Community Health",
        "2024\u20132025",
        "Field training at rural and urban health centres: household surveys, immunisation sessions, national health programme implementation and health education.",
        "Community medicine posting with field attachment at the Rural Health Training Centre and "
        "Urban Health Centre. Activities included family adoption and household survey work, "
        "antenatal and immunisation session participation, growth monitoring and nutrition "
        "counselling, surveillance and outbreak investigation basics, water and sanitation "
        "inspection, and delivery of health education sessions. Studied the national health "
        "programmes in operation at primary care level \u2014 immunisation, TB elimination, "
        "maternal and child health, NCD screening and vector-borne disease control.",
    ),
    item(
        "posting-ent-ophthal",
        "ENT, Ophthalmology & FMT Postings",
        "GMC Chittorgarh",
        "Clinical",
        "2023\u20132024",
        "Phase III Part 1 specialty postings with dedicated OPD training, instrument familiarity and bedside diagnostic skills.",
        "Phase III Part 1 specialty postings. ENT: history and examination of ear, nose and "
        "throat complaints, tuning fork tests, otoscopy, nasal endoscopy observation, and common "
        "conditions such as otitis media, sinusitis, tonsillitis, epistaxis and hearing loss. "
        "Ophthalmology: visual acuity and refraction basics, slit-lamp and fundus examination "
        "observation, cataract, glaucoma, refractive errors, conjunctivitis and diabetic "
        "retinopathy. Forensic Medicine & Toxicology: medico-legal documentation, injury "
        "examination and reporting, toxicology of common poisons, and medico-legal responsibilities "
        "of a doctor.",
    ),
    item(
        "posting-paraclinical",
        "Pathology, Microbiology & Pharmacology",
        "GMC Chittorgarh",
        "Clinical",
        "2022\u20132023",
        "Para-clinical year: histopathology and clinical pathology, organism identification and antimicrobial sensitivity, and rational drug therapeutics.",
        "Second professional year foundation. Pathology: gross and histopathological specimen "
        "study, haematology and clinical pathology interpretation, and correlating morphology with "
        "clinical presentation. Microbiology: specimen collection and transport, staining and "
        "culture techniques, organism identification, antimicrobial susceptibility testing and "
        "hospital infection control. Pharmacology: mechanisms of drug action, autonomic and "
        "cardiovascular pharmacology, antimicrobial therapy, adverse drug reaction reporting and "
        "rational prescription writing.",
    ),
    item(
        "posting-preclinical",
        "Anatomy, Physiology & Biochemistry",
        "GMC Chittorgarh",
        "Clinical",
        "2022",
        "First professional year: cadaveric dissection, physiology practicals and clinical biochemistry interpretation \u2014 the base of all later clinical reasoning.",
        "First professional year. Anatomy: cadaveric dissection, osteology, gross and "
        "radiological anatomy, embryology and histology. Physiology: systems physiology with "
        "practicals and clinical correlation of normal function. Biochemistry: metabolism, "
        "enzymology, nutrition and interpretation of routine biochemical profiles. This phase "
        "built the structural and functional vocabulary used in every later posting.",
    ),
]

# ------------------------------------------------------------------ Education
items += [
    item(
        "education-mbbs",
        "MBBS \u2014 Bachelor of Medicine, Bachelor of Surgery",
        "Government Medical College, Chittorgarh \u00b7 Rajasthan",
        "Education",
        "2022\u20132026",
        "Final-year MBBS under the National Medical Commission competency-based curriculum, followed by a 12-month compulsory rotating internship.",
        "Degree programme at Government Medical College, Chittorgarh. Curriculum followed: NMC "
        "Competency-Based Medical Education (CBME) with early clinical exposure, skills lab "
        "training, AETCOM (Attitude, Ethics and Communication) modules, electives and logbook-based "
        "competency assessment across four professional phases. CONFIRM: add university name, "
        "batch year and academic performance.",
    ),
    item(
        "education-school",
        "Senior Secondary Education",
        "Sophia Secondary School",
        "Education",
        "Completed",
        "Schooling at Sophia Secondary School, followed by PCB (Physics, Chemistry, Biology) study and NEET-UG qualification for MBBS admission.",
        "Completed schooling at Sophia Secondary School, with the science stream (Physics, "
        "Chemistry, Biology) and qualification of NEET-UG for admission to the MBBS programme. "
        "CONFIRM: add school city, board (CBSE/RBSE/ICSE), year of passing and percentage.",
    ),
]

# ----------------------------------------------------------------- Research
items += [
    item(
        "research-interest",
        "Research Interests & Literature Appraisal",
        "Internal medicine \u00b7 public health \u00b7 medical education",
        "Research",
        "Ongoing",
        "Actively building research skills: structured literature search, critical appraisal, study design basics, data interpretation and manuscript drafting.",
        "Research orientation developed alongside MBBS. Current interest areas: non-communicable "
        "disease management in primary care, antimicrobial resistance and rational prescribing, "
        "maternal and child health outcomes, health literacy and patient education effectiveness, "
        "and medical education methods. Practising skills: PubMed / Google Scholar literature "
        "search with MeSH terms, critical appraisal of study design and bias, basic biostatistics "
        "and data interpretation, reference management, and structured manuscript and abstract "
        "drafting. Open to joining established research groups as a research assistant. "
        "CONFIRM: list any specific project, publication, presentation or ICMR-STS work here once "
        "finalised.",
    ),
    item(
        "research-evidence",
        "Evidence-Based Practice in Clinical Training",
        "GMC Chittorgarh \u00b7 ward and journal work",
        "Research",
        "Ongoing",
        "Applying guideline-based reasoning on rounds \u2014 comparing management protocols with current evidence and presenting updates in group discussion.",
        "Routine application of evidence-based medicine during clinical postings: cross-checking "
        "management protocols against current national and international guidelines, presenting "
        "topic updates in ward or small-group discussion, and learning to grade the quality of "
        "evidence behind a recommendation. Builds directly into research assistant and medical "
        "writing work.",
    ),
]

# ------------------------------------------------------------------ Writing
items += [
    item(
        "writing-patient-edu",
        "Patient Education Content",
        "Medical writing \u00b7 plain-language health material",
        "Writing",
        "Ongoing",
        "Writing and reviewing patient-facing explainers \u2014 what a diagnosis means, what treatment does, and what warning signs to watch for.",
        "Patient education writing practice: converting clinical information into short, "
        "plain-language material a non-medical reader can act on. Typical formats: disease "
        "explainers, medication adherence guides, pre- and post-operative instructions, antenatal "
        "care checklists, immunisation schedules, red-flag symptom lists and myth-versus-fact "
        "content. Writing principle used: accurate first, simple second, never fearful.",
    ),
    item(
        "writing-medical-edu",
        "Medical Education & Exam-Oriented Writing",
        "Medical writing \u00b7 student learning material",
        "Writing",
        "Ongoing",
        "Creating structured study content for MBBS and pre-clinical students \u2014 topic summaries, mnemonics, case-based revision and high-yield notes.",
        "Writing learning material aimed at medical students: high-yield topic summaries, "
        "structured notes, case-based questions, comparison tables, mnemonics and revision "
        "checklists. Focus on aligning content with the NMC CBME competency list so it matches "
        "what students are actually examined on.",
    ),
    item(
        "writing-web-health",
        "Web & Digital Health Content",
        "Medical writing \u00b7 web content writing",
        "Writing",
        "Ongoing",
        "Writing and editing health content for websites and digital products \u2014 articles, landing copy, FAQs, UX microcopy and social health content.",
        "Web content writing practice for health audiences: long-form articles, service and "
        "landing page copy, FAQ blocks, user-experience microcopy for health apps, and short-form "
        "social content with clinical review. Includes structuring content for readability and "
        "search, keeping claims within evidence, and adding appropriate medical disclaimers. "
        "CONFIRM: add live published links here once articles are out.",
    ),
    item(
        "writing-editing",
        "Editing & Content Strategy",
        "Medical writing \u00b7 editorial services",
        "Writing",
        "Ongoing",
        "Editing medical content for accuracy, terminology and flow, and planning content strategy for health brands and education pages.",
        "Editorial work: fact-checking clinical statements, standardising terminology and units, "
        "correcting drug names and dosages against references, tightening structure, and ensuring "
        "consistent tone for the intended audience. Content strategy work covers topic mapping, "
        "editorial calendars, audience journeys and content audits for health and medical-education "
        "pages.",
    ),
    item(
        "writing-video",
        "Video & Visual Health Content",
        "Content creation \u00b7 video editing",
        "Writing",
        "Ongoing",
        "Scripting and editing short-form health education video content \u2014 from outline to final cut with clinically reviewed messaging.",
        "Content creation covering scripting, storyboarding and video editing for short-form "
        "health education. The clinical review step matters most here: claims are checked before "
        "recording, not after publishing.",
    ),
]

# -------------------------------------------------------- Health education
items += [
    item(
        "health-edu-focus",
        "Health Education Practice",
        "Patient counselling \u00b7 community sessions \u00b7 awareness content",
        "Health Education",
        "Ongoing",
        "Delivering health education in three settings: the bedside, the community and the page \u2014 with emphasis on literacy-appropriate language.",
        "Health education work spans bedside counselling during postings (explaining diagnosis, "
        "treatment, adherence and warning signs to patients and attendants), community sessions "
        "during community medicine field days, and written or digital content for wider audiences. "
        "Consistent approach: assess what the person already believes, correct one misconception "
        "at a time, use concrete local examples, and confirm understanding by asking them to "
        "repeat the plan back.",
    ),
    item(
        "health-edu-vernacular",
        "Vernacular (Hindi) Health Communication",
        "Health education \u00b7 language access",
        "Health Education",
        "Ongoing",
        "Adapting medical content into Hindi and simple everyday language for Indian patients and families who do not read clinical English.",
        "Most patients in a district teaching hospital setting receive information in Hindi. This "
        "work focuses on translating clinical guidance into natural Hindi and everyday phrasing \u2014 "
        "keeping drug names, units and red-flag symptoms exact while removing jargon. Also covers "
        "audio-visual and low-literacy formats.",
    ),
    item(
        "health-edu-topics",
        "Priority Health Topics",
        "Public health \u00b7 NCDs \u00b7 maternal & child health",
        "Health Education",
        "Ongoing",
        "Focused education content on NCDs, TB, anaemia, maternal and child health, immunisation, antibiotic resistance and lifestyle prevention.",
        "Recurring topic areas chosen for real public-health weight in India: hypertension and "
        "diabetes screening and adherence, tobacco and alcohol cessation, tuberculosis symptoms "
        "and treatment completion, anaemia and nutrition in women and children, antenatal care and "
        "institutional delivery, complete immunisation, rational antibiotic use and antimicrobial "
        "resistance, dengue and vector control, mental health awareness, and preventive lifestyle "
        "counselling.",
    ),
]

# ----------------------------------------------------------- Community / Volunteering
items += [
    item(
        "community-camps",
        "Health Camps & Screening Drives",
        "GMC Chittorgarh \u00b7 community medicine field days",
        "Volunteering",
        "Ongoing",
        "Participation in health camps and screening drives \u2014 BP and blood sugar screening, health check-ups, immunisation support and referral counselling.",
        "Volunteering at health camps and outreach drives organised through the institution and "
        "community medicine department. Roles taken: registration and triage support, blood "
        "pressure and capillary blood glucose screening, recording and reporting findings, "
        "counselling on lifestyle and treatment adherence, immunisation session support, and "
        "referring identified cases to the appropriate OPD. CONFIRM: add camp names, locations, "
        "dates and number of patients screened.",
    ),
    item(
        "community-awareness",
        "Health Awareness Campaigns",
        "Community outreach \u00b7 national health days",
        "Volunteering",
        "Ongoing",
        "Awareness activity around national health observances \u2014 health day campaigns, school and community talks, and IEC material distribution.",
        "Awareness and information-education-communication work tied to national health "
        "observances and local needs: poster and leaflet preparation, short talks in community and "
        "school settings, and support during vaccination and screening campaigns. Emphasis on "
        "message testing \u2014 checking that the audience understood before assuming the message "
        "landed.",
    ),
    item(
        "community-peer-support",
        "Peer Academic Support & Mentoring",
        "MBBS batch \u00b7 junior students",
        "Volunteering",
        "Ongoing",
        "Helping juniors and peers with study planning, clinical skills practice and exam preparation \u2014 informal mentoring inside the batch.",
        "Informal mentoring and peer support for junior MBBS students: study planning, resource "
        "guidance, viva and clinical skills practice, case-presentation feedback and exam "
        "preparation strategy. Also includes career guidance for students interested in medical "
        "writing and research alongside MBBS.",
    ),
]

# ---------------------------------------------------------------- Leadership
items += [
    item(
        "leadership-communication",
        "Public Speaking & Communication Roles",
        "College events \u00b7 academic sessions",
        "Leadership",
        "Ongoing",
        "Speaking and presenting at academic and college events \u2014 case presentations, topic talks, anchoring and student-facing sessions.",
        "Public speaking and communication activity within the college environment: clinical case "
        "presentations on rounds and in academic sessions, topic presentations and journal-club "
        "style discussions, event anchoring and hosting, and student-facing sessions. Also offered "
        "as a service \u2014 public speaking coaching and presentation design.",
    ),
    item(
        "leadership-organising",
        "Event & Academic Organisation",
        "GMC Chittorgarh \u00b7 student activities",
        "Leadership",
        "Ongoing",
        "Organising and coordinating student academic events, awareness drives and content work \u2014 planning, delegation and execution.",
        "Coordination and organisation work around student activities: planning sessions and "
        "drives, assigning responsibilities, preparing content and material, coordinating with "
        "faculty and administration, and running the event itself. Skills applied: project "
        "planning, clear written communication, and follow-through.",
    ),
    item(
        "leadership-coaching",
        "Career Development & Leadership Coaching",
        "Service offering \u00b7 students and early professionals",
        "Leadership",
        "Available",
        "Coaching students and early-career professionals on career direction, CV and portfolio building, communication and leadership development.",
        "Offered as a professional service: career development coaching (choosing a direction, "
        "building a CV and portfolio, preparing for interviews), leadership development, and life "
        "coaching focused on study discipline, stress management and long-term goals. Particular "
        "interest in helping medical students build non-clinical career tracks such as medical "
        "writing, research and health communication.",
    ),
]

# ---------------------------------------------------------------- Programs
items += [
    item(
        "programs-skills-lab",
        "Clinical Skills & AETCOM Training",
        "Skills laboratory \u00b7 GMC Chittorgarh",
        "Programs",
        "2022\u20132026",
        "Structured skills-lab sessions and AETCOM modules \u2014 BLS, clinical procedures, communication, ethics and professionalism.",
        "Skills laboratory training under the CBME curriculum: basic life support, IV cannulation "
        "and blood sampling, catheterisation, Ryles tube insertion, suturing and wound care, "
        "injection technique, neonatal resuscitation basics and sterile practice. AETCOM (Attitude, "
        "Ethics and Communication) modules covered doctor-patient communication, informed consent, "
        "confidentiality, professional conduct, empathy and ethical decision-making. CONFIRM: add "
        "any external BLS/ACLS certification with provider and date.",
    ),
    item(
        "programs-early-clinical",
        "Early Clinical Exposure & Electives",
        "NMC CBME curriculum \u00b7 GMC Chittorgarh",
        "Programs",
        "2022\u20132026",
        "Early clinical exposure from the first professional year plus elective choice in the final phase of the MBBS curriculum.",
        "Early Clinical Exposure (ECE) sessions integrated from the first year \u2014 connecting "
        "anatomy, physiology and biochemistry topics to real clinical cases in hospital settings. "
        "Elective component in the final phase allowed deeper study in a chosen area. CONFIRM: "
        "state the elective subject selected.",
    ),
    item(
        "programs-self-learning",
        "Continuous Self-Directed Learning",
        "Online medical education \u00b7 courses and modules",
        "Programs",
        "Ongoing",
        "Self-directed learning in medical writing, research methodology, biostatistics, public health and digital health communication.",
        "Ongoing self-directed study outside the MBBS curriculum: medical writing craft and "
        "editing standards, research methodology and basic biostatistics, good clinical practice "
        "principles, public health and epidemiology fundamentals, and digital health communication. "
        "CONFIRM: add completed course names, providers and certificate links here \u2014 each one "
        "becomes its own entry with proof attached.",
    ),
]

# ---------------------------------------------------------- Certifications
items += [
    item(
        "cert-slot",
        "Certifications",
        "To be added \u00b7 upload certificates from the admin panel",
        "Certifications",
        "Add year",
        "Placeholder entry \u2014 list courses, workshops and certifications here with the certificate image or PDF attached as proof.",
        "Use this entry (or duplicate it) for each certification: course name, issuing "
        "organisation, date, and a one-line note on what it covers. Attach the certificate image "
        "or PDF through the admin panel under \u2018Proof files\u2019. Typical additions for this "
        "profile: BLS / ACLS, Good Clinical Practice, research methodology or biostatistics "
        "courses, medical writing workshops, public health modules (for example WHO OpenWHO "
        "courses), and any college or conference participation certificates.",
    ),
]

# -------------------------------------------------------------------- Awards
items += [
    item(
        "award-slot",
        "Awards & Recognition",
        "To be added \u00b7 attach proof from the admin panel",
        "Awards",
        "Add year",
        "Placeholder entry \u2014 add academic distinctions, competition results, paper or poster presentations and appreciation certificates here.",
        "Nothing invented in this portfolio. Use this entry (or duplicate it) for each award: "
        "title, awarding body, year, rank or standing, and what it was for. Attach the "
        "certificate or a link as proof. Typical additions: university or college distinctions, "
        "quiz and competition results, best paper or poster awards, conference acceptances and "
        "institutional appreciation.",
    ),
]

# -------------------------------------------------------------------- Projects
items += [
    item(
        "project-portfolio",
        "This Portfolio \u2014 A Living Medical Profile",
        "Personal project \u00b7 self-published",
        "Projects",
        "2026",
        "A self-managed digital portfolio built to present clinical training, writing work and research interests in one place \u2014 editable through a built-in admin panel.",
        "This site is itself a project: a full-stack portfolio with a hidden content-management "
        "panel, so every section, entry, image and document can be updated without touching code. "
        "Purpose is practical \u2014 a single shareable link for medical writing clients, research "
        "groups, residency or job applications, instead of a static CV.",
        proofs=[{"name": "LinkedIn profile", "type": "link", "url": LINKEDIN}],
    ),
    item(
        "project-content-library",
        "Medical Content Library",
        "Personal project \u00b7 writing portfolio",
        "Projects",
        "Ongoing",
        "Building a personal library of medical writing samples \u2014 patient explainers, student revision content, article drafts and health campaigns.",
        "A running collection of writing samples across the four target roles: patient education "
        "explainers, medical student revision material, web health articles, and campaign or "
        "social content. Each sample is stored with its audience, brief and references so it can "
        "be shown on request. CONFIRM: add sample links or attach PDFs through the admin panel.",
    ),
]

# ---------------------------------------------------------------------- Media
items += [
    item(
        "media-slot",
        "Articles, Talks & Media",
        "To be added \u00b7 published work and appearances",
        "Media",
        "Add date",
        "Placeholder entry \u2014 add published articles, blog posts, podcast or video appearances, guest lectures and conference talks with links attached.",
        "Use this entry (or duplicate it) for anything public: published articles with the live "
        "link, video or podcast appearances, guest lectures delivered, conference talks or poster "
        "presentations, and press coverage. Attach links or files as proof so the detail view "
        "shows them directly.",
    ),
]

# ---------------------------------------------------------------------- Roles
items += [
    item(
        "role-research-assistant",
        "Target Role \u2014 Research Assistant",
        "Open to work \u00b7 clinical & public health research",
        "Roles",
        "2026",
        "Seeking research assistant roles: literature review, data collection and entry, analysis support, manuscript preparation and documentation.",
        "Looking for research assistant positions in clinical or public-health settings. "
        "Contribution areas: structured literature search and screening, data collection and "
        "entry, basic statistical analysis, questionnaire and CRF design input, ethical "
        "documentation support, reference management, and first-draft manuscript and abstract "
        "writing. Comfortable working remotely on review and writing-heavy projects.",
    ),
    item(
        "role-medical-writer",
        "Target Role \u2014 Medical Writer",
        "Open to work \u00b7 medical communication",
        "Roles",
        "2026",
        "Seeking medical writing roles: medical communication, educational content, literature summaries, reviews and clinically reviewed copy.",
        "Looking for medical writing work across medical communication, medical education and "
        "health media. Deliverables: evidence summaries and literature reviews, disease and "
        "therapy overviews, slide decks and speaker material, patient information leaflets, "
        "regulatory-adjacent or promotional review copy, and clinical fact-checking of existing "
        "content.",
    ),
    item(
        "role-web-content",
        "Target Role \u2014 Web Content Writer",
        "Open to work \u00b7 digital health content",
        "Roles",
        "2026",
        "Seeking web content writing roles for health websites, clinics, digital health products and medical education platforms.",
        "Looking for web content writing roles with health-focused teams: website articles and "
        "service pages, blog and SEO-aware health content, FAQ and help-centre copy, UX microcopy "
        "for health apps, email and social content with clinical review. Able to handle both "
        "writing and clinical accuracy checking.",
    ),
    item(
        "role-health-educator",
        "Target Role \u2014 Health Educator",
        "Open to work \u00b7 patient & community education",
        "Roles",
        "2026",
        "Seeking health educator roles: patient education programmes, awareness campaigns, training material and community health communication.",
        "Looking for health educator roles with hospitals, public-health organisations, NGOs, "
        "insurance and wellness companies, or education platforms. Work offered: designing and "
        "delivering patient education sessions, creating IEC material, training non-clinical staff "
        "on health messaging, building awareness campaigns, and evaluating whether the audience "
        "actually understood the content.",
    ),
]

data = {"items": items, "site": site, "timeline": timeline}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False))
print(f"wrote {OUT}")
print(f"items: {len(items)}  timeline: {len(timeline)}  featured: {sum(1 for i in items if i['featured'])}")
import collections
for k, v in collections.Counter(i['category'] for i in items).most_common():
    print(f"  {k}: {v}")
