from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume-Tasin-Naveed.pdf"
profile_pic = current_dir / "assets" / "picture.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Tasin Naveed"
PAGE_ICON = ":wave:"
NAME = "Tasin Naveed"
DESCRIPTION = """
SecOps | DevOps | DataOps.
"""
EMAIL = "tan7@njit.edu"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCZFy1gIvFjw7gYkfbP5HsNg/about",
    "LinkedIn": "https://www.linkedin.com/in/tasin-naveed/",
    "GitHub": "https://github.com/tan7-njit",
}
PROJECTS = {
    "🏆 IT491 Capstone Project - Astia App - Smishing Platform": "https://it491-astia.streamlit.app/",
    "🏆 IT490 - Threat Intelligence Platform for Security Analyst": "http://securitymap.herokuapp.com/",
    "🏆 Investigating digital crime scenarios which includes collecting evidence, and computer forensics": "",
    "🏆 Conducted penetration testing and prepared reports.": "",
    "🏆 Completed hands-on lab on Vulnerability Scanning, Malware Analysis, and Cryptography": "",
    "🏆 Completed 100+ capturing flag rooms(challenges) based on different topics of cybersecurity in TryHackMe.com (Ranked TOP 1%).": "https://tryhackme.com/p/N4v33d",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- :school:️ New Jersey Institute of Technology
- :mortar_board:️ Bachelor of Science, Information Technology
- :dart: Concentration: Cyber Security Specialization
- :slot_machine: Cumulative GPA: 3.78/4.00
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- ‍💻 Programming: HTML, CSS, JavaScript, PHP, PYTHON, SQL, POWERSHELL, BASH
- :desktop_computer: OS: Windows, MAC, Ubuntu, Centos 7, Kali, VMWare.
- 📚 Areas: Threat Intelligence and Vulnerability Management, Security Operations and Monitoring, Incident Response and Forensics, Malware Analysis and Vulnerability Research, Web and Network Penetration Testing, Data Analytics (Python Streamlit)
- :desktop_computer: Tools/Platforms/Software: Cisco Talos, Burp Suite, Zeek, Networkminer, Brim, Wireshark, Splunk, MISP, OpenCTI, Wazuh, Hive, Tenable Nessus, Rapid7, Sysinternals, Sysmon, Snort, Metasploit, OpenVAS, Zap, Nikto, Nmap, Maltego, Autopsy, Office 365
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write(":closed_lock_with_key:", "**Cybersecurity Intern | Infosys Ltd**")
st.write("06/2022 - 08/2022")
st.write(
    """
- ► Created web-app with Python Streamlit framework to analyze risk and severity.
- ► Worked with OWASP ASVS framework.
- ► Researched on Threat Hunting: analysis, possibilities of automation, traffic analysis and made a workflow.
- ► Created Python Scripts to to extract significant analytics data from security report, automate vulnerability management service by using API. It includes raising incident tickets, attaching reference documents and other automation.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
