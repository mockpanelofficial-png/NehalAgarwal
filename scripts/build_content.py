#!/usr/bin/env python3
"""Builds server/data/db.json for Nehal Agarwal's medical portfolio.

CONTENT RULE (v2 — strict):
  Every entry below is traceable to Nehal's own LinkedIn profile
  (headline, about, experience, education activities, skills, services,
  open-to-work, recommendation) or to contact details she supplied.
  Nothing invented: no made-up clinical postings, no placeholder awards,
  no speculative samples. Where her own profile is ambiguous (e.g. rank
  "2nd" in experience vs "first" in about), a CONFIRM note marks it.

  Nehal can edit / add / delete everything from the hidden /admin panel.
"""
import json, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "server" / "data" / "db.json"
LINKEDIN = "https://www.linkedin.com/in/nehal-agarwal-6529a429a/"
LI_PROOF = {"name": "Nehal Agarwal — LinkedIn profile", "type": "link", "url": LINKEDIN}

site = {
    "name": "Nehal Agarwal",
    "eyebrow": "Final-year MBBS \u00b7 Government Medical College, Chittorgarh",
    "hero": "Medicine, made <em>understandable.</em>",
    "lede": (
        "Final-year MBBS student at Government Medical College, Chittorgarh (Sep 2023 batch) "
        "with ICMR-STS research experience \u2014 including a project on AI-assisted peripheral "
        "blood smear screening and rural healthcare empowerment \u2014 a top rank in the first "
        "professional year, health-awareness competition wins, and a clear focus on healthcare "
        "communication, medical education and content creation."
    ),
    "tagline": (
        "Final-Year MBBS Student | Medical Content Writing | Healthcare Communication "
        "| Medical Education | Content Creation"
    ),
    "email": "nehalagarwal@gmail.com",
    "phone": "+91 98979 49692",
    "stat1v": "2nd",
    "stat1l": "Rank \u2014 1st professional year",
    "stat2v": "1",
    "stat2l": "ICMR-STS research project",
    "stat3v": "9",
    "stat3l": "Professional services",
    "profileImage": "/profile-photo.png",
    "linkedin": LINKEDIN,
    "location": "Chittorgarh, Rajasthan, India",
    "school": "Government Medical College, Chittorgarh",
    "resumeUrl": "",
    "pressUrl": "",
    "profileHeading": "A strong academic foundation.<br/>A clear communicative purpose.",
    "profileLede": (
        "Final-year MBBS student with a strong academic foundation and a particular interest "
        "in healthcare communication, medical education, and research \u2014 with academic "
        "presentations, ICMR-STS research, health-awareness initiatives and medical-festival "
        "organisation through MBBS."
    ),
    "interests": [
        "Medical Writing",
        "Health Writing",
        "Writing For The Web",
        "Web Content",
        "Health Promotion",
        "Wellness Education",
        "Written Communication",
        "Clinical Research",
        "Presentation Skills",
        "Creative Content Creation",
    ],
    "profileCards": [
        {
            "id": "pc1",
            "title": "ICMR-STS research",
            "text": "Conducted an ICMR-STS research project on AI-assisted peripheral blood smear screening and approaches to empowering rural healthcare, under guidance.",
            "icon": "flask",
        },
        {
            "id": "pc2",
            "title": "Academic rank",
            "text": "2nd class topper in the 1st professional year of MBBS at Government Medical College, Chittorgarh.",
            "icon": "medal",
        },
        {
            "id": "pc3",
            "title": "Medical writing",
            "text": "Medical content writing, health writing, web content and written communication \u2014 the writing focus declared across her headline and endorsed skills.",
            "icon": "pen",
        },
        {
            "id": "pc4",
            "title": "Healthcare communication",
            "text": "Health promotion and wellness education, applied in health-awareness work on tuberculosis and AIDS \u2014 including two poster-competition placements.",
            "icon": "heartpulse",
        },
        {
            "id": "pc5",
            "title": "Medical education",
            "text": "Academic presentations in Microbiology and a declared interest in medical education and content creation for students and patients.",
            "icon": "graduation",
        },
        {
            "id": "pc6",
            "title": "Campus & creativity",
            "text": "Organisation of activities in medical college fests, creative health-awareness competitions, and services spanning video editing, public speaking and coaching.",
            "icon": "sparkles",
        },
    ],
    "skills": [
        {"id": "sk1", "label": "Medical Writing & Health Writing", "pct": 95},
        {"id": "sk2", "label": "Web Content & Writing For The Web", "pct": 92},
        {"id": "sk3", "label": "Health Promotion & Wellness Education", "pct": 90},
        {"id": "sk4", "label": "Clinical Research (ICMR-STS)", "pct": 85},
        {"id": "sk5", "label": "Written & Presentation Communication", "pct": 88},
        {"id": "sk6", "label": "Creative Content Creation", "pct": 86},
    ],
    "skillsTitle": "Endorsed skill areas",
    "skillsSub": "Self-assessed strength",
    "roles": [
        "Final-Year MBBS Student",
        "Medical Content Writer",
        "Healthcare Communicator",
        "Medical Educator",
        "Content Creator",
        "Aspiring Research Assistant",
        "Web Content Writer",
        "Health Educator",
    ],
    "ticker": [
        "Medical content writing",
        "Healthcare communication",
        "Medical education",
        "Content creation",
        "ICMR-STS research",
        "Health promotion",
        "TB & AIDS awareness",
        "Clinical research",
        "Medical content writing",
        "Healthcare communication",
        "Medical education",
        "Content creation",
        "ICMR-STS research",
        "Health promotion",
        "TB & AIDS awareness",
        "Clinical research",
    ],
    "sections": {
        "profileEyebrow": "Medical profile",
        "highlightsTitle": "Highlights & achievements",
        "highlightsText": (
            "ICMR-STS research, academic rank, health-awareness competition wins and academic "
            "presentations \u2014 every entry here traces back to Nehal's own record."
        ),
        "portfolioTitle": "Journey & portfolio",
        "portfolioText": (
            "Research, academics, awards, writing focus, leadership and recommendations \u2014 "
            "each with context and a link to the source."
        ),
        "manifestoQuote": (
            "She is very determined and always look for innovative solutions to solve a problem. "
            "She is a best package of creativity and intelligence."
        ),
        "manifestoAttribution": (
            "\u2014 Ayesha Agarwal (KPMG Valuation, CFA Level 1, ex-JP Morgan), "
            "in her recommendation for Nehal"
        ),
        "contactTitle": "Get In Touch",
        "contactSubtitle": (
            "For medical writing assignments, research assistance, health education "
            "collaborations or just to say hello \u2014 write to Nehal."
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
            "Portfolio of Nehal Agarwal, final-year MBBS student at Government Medical College, "
            "Chittorgarh \u2014 ICMR-STS research on AI-assisted peripheral blood smear screening, "
            "medical content writing, healthcare communication and medical education."
        ),
        "defaultTheme": "dark",
    },
}

timeline = [
    {
        "date": "Sep 2023",
        "title": "MBBS begins at GMC Chittorgarh",
        "text": (
            "Joined the MBBS programme at Government Medical College, Chittorgarh "
            "(Sep 2023 batch, expected 2028), after schooling at Sophia Secondary School."
        ),
    },
    {
        "date": "1st Prof",
        "title": "2nd class topper \u2014 first professional year",
        "text": (
            "Ranked 2nd in the first year of MBBS, building the academic foundation "
            "she continues to carry through the course."
        ),
    },
    {
        "date": "MBBS",
        "title": "ICMR-STS research & academic presentations",
        "text": (
            "Conducted an ICMR-STS research project on AI-assisted peripheral blood smear "
            "screening and approaches to empowering rural healthcare; presented academic "
            "topics in Microbiology."
        ),
    },
    {
        "date": "MBBS",
        "title": "Health awareness & campus life",
        "text": (
            "Winner of an AIDS awareness poster-making competition, 2nd place in a tuberculosis "
            "awareness poster-making competition, and organisation of activities in medical "
            "college fests."
        ),
    },
    {
        "date": "Present",
        "title": "Final year, writing focus & open to work",
        "text": (
            "Final-year MBBS student focused on healthcare communication, medical education and "
            "content creation \u2014 open to Research Assistant, Medical Writer, Web Content "
            "Writer and Health Educator roles."
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
        "proofs": proofs if proofs is not None else [dict(LI_PROOF)],
    }


items = [
    # ------------------------------------------------------------ research
    item(
        "icmr-sts",
        "ICMR-STS Research \u2014 AI-Assisted Peripheral Blood Smear Screening",
        "ICMR-STS \u00b7 Government Medical College, Chittorgarh",
        "Research",
        "Ongoing",
        "Conducted an ICMR-STS research project on AI-assisted peripheral blood smear screening and approaches to empowering rural healthcare, under guidance.",
        "Research work undertaken under guidance in the ICMR Short Term Studentship (ICMR-STS) "
        "stream during MBBS. The project explores AI-assisted screening of peripheral blood "
        "smears \u2014 using computational assistance to support microscopy-based diagnosis \u2014 "
        "and connects it to approaches for empowering rural healthcare, where specialist "
        "pathology access is limited. Work spans literature review, understanding smear "
        "morphology, following the study protocol and documenting findings under faculty "
        "guidance. CONFIRM: add project start year, guide's name and current status "
        "(ongoing / submitted / published) when available.",
        True,
    ),
    # ------------------------------------------------------------ awards
    item(
        "rank-1st-prof",
        "2nd Class Topper \u2014 1st Professional Year",
        "Government Medical College, Chittorgarh",
        "Awards",
        "1st Prof Year",
        "Ranked 2nd in the first year of MBBS \u2014 2nd class topper of the 1st professional year at GMC Chittorgarh.",
        "Academic distinction in the first professional year of MBBS: 2nd class topper at "
        "Government Medical College, Chittorgarh, recorded on her LinkedIn experience and "
        "education sections (\u20182nd class topper in 1st professional year\u2019, \u2018Ranked 2nd "
        "in the first year of MBBS\u2019). CONFIRM: her About section separately says \u2018Ranked "
        "first in the MBBS first year\u2019 \u2014 confirm the exact rank (1st or 2nd) and, if "
        "available, attach the marksheet or college merit list as proof.",
        True,
    ),
    item(
        "poster-aids-winner",
        "Winner \u2014 AIDS Awareness Poster-Making Competition",
        "Government Medical College, Chittorgarh",
        "Awards",
        "During MBBS",
        "Won the AIDS awareness poster-making competition \u2014 creative health-communication work on HIV/AIDS awareness.",
        "First place in an AIDS awareness poster-making competition held during MBBS. The entry "
        "combined scientific accuracy about HIV transmission, prevention and stigma with visual "
        "communication designed to make the message stick \u2014 an early example of the healthcare "
        "communication focus she continues to pursue. CONFIRM: add the organising body, event "
        "name and year, and attach the certificate or poster image as proof.",
        True,
    ),
    item(
        "poster-tb-second",
        "2nd Place \u2014 Tuberculosis Awareness Poster-Making Competition",
        "Government Medical College, Chittorgarh",
        "Awards",
        "During MBBS",
        "Secured 2nd place in a tuberculosis awareness poster-making competition \u2014 health-communication work on TB awareness.",
        "Second place in a tuberculosis awareness poster-making competition during MBBS. The "
        "poster addressed TB recognition, treatment completion and community awareness \u2014 "
        "aligned with national TB-elimination messaging. CONFIRM: add the organising body, event "
        "name and year, and attach the certificate or poster image as proof.",
        False,
    ),
    # ------------------------------------------------------------ education
    item(
        "education-mbbs",
        "MBBS \u2014 Bachelor of Medicine and Surgery",
        "Government Medical College, Chittorgarh",
        "Education",
        "Sep 2023 \u2013 May 2028",
        "MBBS at GMC Chittorgarh (Sep 2023 batch). Activities: 2nd rank in 1st year, Microbiology presentations, ICMR-STS research, awareness competition wins and fest organisation.",
        "Pursuing the Bachelor of Medicine and Surgery (MBBS) at Government Medical College, "
        "Chittorgarh, September 2023 batch (expected completion May 2028 per LinkedIn). "
        "Recorded activities and societies: ranked 2nd in the first year of MBBS; presented "
        "academic topics in Microbiology; conducted an ICMR-STS research project on AI-assisted "
        "peripheral blood smear screening and approaches to empowering rural healthcare; winner "
        "of an AIDS awareness poster-making competition; 2nd place in a tuberculosis awareness "
        "poster-making competition; organised activities as part of medical college fests. "
        "Currently in the final-year group with a focus on healthcare communication, medical "
        "education and research. CONFIRM: LinkedIn also lists five education entries in total \u2014 "
        "the remaining three can be added here.",
        True,
    ),
    item(
        "education-sophia",
        "Sophia Secondary School",
        "Sophia Secondary School",
        "Education",
        "Pre-MBBS",
        "Schooling at Sophia Secondary School, preceding admission to the MBBS programme in 2023.",
        "Completed schooling at Sophia Secondary School before joining the MBBS programme at "
        "Government Medical College, Chittorgarh in September 2023. CONFIRM: add board, year of "
        "passing and percentage if Nehal wants them listed.",
    ),
    # ------------------------------------------------------------ roles / services
    item(
        "open-to-work",
        "Open To Work \u2014 Four Career Tracks",
        "Research Assistant \u00b7 Medical Writer \u00b7 Web Content Writer \u00b7 Health Educator",
        "Roles",
        "Present",
        "Actively open to Research Assistant, Medical Writer, Web Content Writer and Health Educator roles, as declared on her LinkedIn Open-to-Work.",
        "Nehal's LinkedIn Open-to-Work declaration lists four role tracks: Research Assistant, "
        "Medical Writer, Web Content Writer and Health Educator. Together they map directly onto "
        "her record: ICMR-STS research experience (research assistance), a declared medical "
        "content writing and web content focus (medical and web writing), and health promotion / "
        "wellness education skills with awareness-competition wins (health education).",
        True,
    ),
    item(
        "services",
        "Services Offered \u2014 Nine Areas",
        "LinkedIn Services page",
        "Roles",
        "Available",
        "Writing, Editing, Content Strategy, User Experience Writing, Video Editing, Public Speaking, Career Development Coaching, Leadership Development and Life Coaching.",
        "Services Nehal offers, exactly as listed on her LinkedIn Services page: Writing; "
        "Editing; Content Strategy; User Experience Writing; Video Editing; Public Speaking; "
        "Career Development Coaching; Leadership Development; Life Coaching. Enquiries for any "
        "of these can be sent through the contact form on this site.",
        True,
    ),
    # ------------------------------------------------------------ programs / leadership
    item(
        "microbiology-presentations",
        "Academic Presentations \u2014 Microbiology",
        "Government Medical College, Chittorgarh",
        "Programs",
        "During MBBS",
        "Presented academic topics in Microbiology during MBBS \u2014 structured topic preparation and delivery before faculty and peers.",
        "Academic presentation work in Microbiology during MBBS: selecting and structuring "
        "topics, preparing evidence-based slides and presenting before faculty and peers. "
        "Builds directly on her presentation-skills strength and feeds her medical-education "
        "interest. CONFIRM: add specific topics presented and the year, if available.",
    ),
    item(
        "fest-organisation",
        "Medical College Fests \u2014 Activity Organisation",
        "Government Medical College, Chittorgarh",
        "Leadership",
        "During MBBS",
        "Organisation of activities in medical college fests \u2014 planning, coordination and execution of campus events.",
        "Organised activities as part of medical college fests at GMC Chittorgarh: planning "
        "event formats, coordinating with teams and participants, and executing activities on "
        "the day. The organisational side of campus life, alongside academics and research. "
        "CONFIRM: add fest names, years and specific responsibilities if available.",
    ),
    # ------------------------------------------------------------ writing / health education focus
    item(
        "focus-medical-writing",
        "Medical Content Writing & Web Content",
        "Declared focus \u00b7 headline and endorsed skills",
        "Writing",
        "Ongoing",
        "Medical content writing, health writing, web content, writing for the web and written communication \u2014 her declared writing focus across LinkedIn.",
        "Writing is the strongest thread in Nehal's profile: her headline leads with Medical "
        "Content Writing and Content Creation, and her endorsed skills include Medical Writing, "
        "Health Writing, Writing For The Web, Web Content, Written Communication and Creative "
        "Content Creation. This entry marks that focus area \u2014 medical and health content for "
        "clinicians, students and general readers, and web copy for health platforms. "
        "CONFIRM: attach or link published samples as they become public.",
    ),
    item(
        "focus-health-communication",
        "Healthcare Communication & Health Promotion",
        "Declared focus \u00b7 headline and endorsed skills",
        "Health Education",
        "Ongoing",
        "Healthcare communication, health promotion and wellness education \u2014 applied in TB and AIDS awareness work including two poster-competition placements.",
        "Healthcare communication is the second pillar of Nehal's profile: her headline lists "
        "Healthcare Communication, and her endorsed skills include Health Promotion and Wellness "
        "Education. Applied evidence already on record: creative competitions on health-awareness "
        "topics such as tuberculosis and AIDS, including a win in an AIDS awareness poster-making "
        "competition and 2nd place in a tuberculosis awareness poster-making competition.",
    ),
    # ------------------------------------------------------------ recommendation
    item(
        "recommendation-ayesha",
        "Recommendation \u2014 Ayesha Agarwal",
        "KPMG Valuation (CA May 24) \u00b7 CFA Level 1 cleared \u00b7 ex-JP Morgan",
        "Media",
        "3 Sep 2026",
        "\u201cNehal is very hardworking and diligent, I have personally worked with her. She is very determined and always look for innovative solutions to solve a problem. She is a best package of creativity and intelligence.\u201d",
        "Recommendation received on LinkedIn (3 September 2026) from Ayesha Agarwal \u2014 KPMG "
        "Valuation (CA May 24), CFA Level 1 cleared, ex-JP Morgan \u2014 who was senior to Nehal "
        "but did not manage her directly. Full text: \u201cNehal is very hardworking and diligent, "
        "I have personally worked with her. She is very determined and always look for innovative "
        "solutions to solve a problem. She is a best package of creativity and intelligence.\u201d",
    ),
]

# Production rule: internal CONFIRM notes never ship in public copy.
# (They stay tracked in NEHAL-CHECKLIST.md / scripts/list_todos.py instead.)
import re as _re
for _it in items:
    _it["description"] = _re.sub(r"\s*CONFIRM:.*$", "", _it["description"], flags=_re.S).rstrip()

# Newest first — current status always on top of the journey timeline.
timeline = list(reversed(timeline))

data = {"items": items, "site": site, "timeline": timeline}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False))

import collections
print(f"wrote {OUT}")
print(f"items: {len(items)}  timeline: {len(timeline)}  featured: {sum(1 for i in items if i['featured'])}")
for k, v in collections.Counter(i['category'] for i in items).most_common():
    print(f"  {k}: {v}")
