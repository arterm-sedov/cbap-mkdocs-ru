"""Boilerplate/noise patterns for cmwlab.com (English-language site)."""
import re

BOILERPLATE = [
    # Cookie / privacy / consent
    re.compile(r'(?i).*\b(cookies|privacy\s*policy|terms\s*of\s*(use|service)|data\s*protection|gdpr|ccpa).*'),
    # Copyright / legal
    re.compile(r'(?i).*\b(all\s*rights\s*reserved|copyright\s*©|©\s*\d{4}).*'),
    # Sitemap / footer nav
    re.compile(r'(?i).*\b(sitemap|site\s*map|all\s*pages).*'),
    # Phone numbers (US/international)
    re.compile(r'.*\+?1?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}.*'),
    # Email addresses
    re.compile(r'.*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}.*'),
    # Social media
    re.compile(r'(?i).*\b(facebook|linkedin|twitter|x\.com|youtube|instagram|pinterest)\b.*'),
    # Subscribe / newsletter
    re.compile(r'(?i).*\b(subscribe|newsletter|stay\s*(up\s*to\s*date|in\s*touch|informed)|join\s*our).*'),
    # Share / bookmark widgets
    re.compile(r'(?i).*\b(share\s*(this|on)|tweet|pin\s*it|linkedin\s*share).*'),
    # Comments / author box
    re.compile(r'(?i).*\b(leave\s*a\s*comment|comments?\s*are\s*closed|about\s*the\s*author|written\s*by|posted\s*by).*'),
    # Related posts sidebar
    re.compile(r'(?i).*\b(related\s*(posts|articles)|you\s*may\s*also\s*like|popular\s*posts|recent\s*posts|latest\s*posts).*'),
    # CTA buttons — demo / trial / quote
    re.compile(r'(?i).*\[(Request\s*(a\s*)?demo|Get\s*(a\s*)?(quote|started)|Start\s*(a\s*)?(free\s*)?trial|See\s*pricing|Talk\s*to\s*(sales|us|an?\s*expert)|Contact\s*(sales|us|experts|our\s*team)|Book\s*.*demo|Schedule\s*.*(demo|call)).*'),
    # Pricing / trial links
    re.compile(r'(?i).*\b\[Pricing\]\(https?://.*\).*'),
    re.compile(r'(?i).*\b\[Trial\]\(https?://.*\).*'),
    re.compile(r'(?i).*\b\[Support\]\(https?://.*\).*'),
    # Horizontal rules / separators
    re.compile(r'^[-=_*]{3,}$'),
    # Empty headings (nav chrome)
    re.compile(r'^#{1,6}\s*$'),
    # Blog categories / tags sidebar
    re.compile(r'(?i).*\b(categories|tags|archive|filter\s*by|browse\s*by)\b.*'),
    # Search widget
    re.compile(r'(?i).*\b(search\s*(this\s*site|blog|articles)|enter\s*keywords).*'),
]

SUSPECT_PHRASES = re.compile(
    r'(?i)(request\s*(a\s*)?demo|get\s*(a\s*)?quote|start\s*(a\s*)?trial|see\s*pricing|'
    r'talk\s*to\s*sales|contact\s*(us|experts|our\s*team)|book\s*a?\s*(demo|call)|'
    r'schedule\s*a?\s*(demo|call|consultation)|try\s*(it\s*)?(for\s*)?free|'
    r'download\s*(now|free|brochure|whitepaper|ebook)|sign\s*up|register\s*now|'
    r'learn\s*more|read\s*more|find\s*out\s*more|discover\s*how|'
    r'case\s*stud(y|ies)|success\s*stor(y|ies)|client\s*stor(y|ies)|'
    r'low.code|no.code|bpm.*platform|workflow.*automation)'
)

CTA_BUTTON_RE = re.compile(
    r'(?i)\[ Request (a )?Demo \]|\[ Get (a )?Quote \]|'
    r'\[ Start (a )?(Free )?Trial \]|'
    r'\[ Talk to (Sales|Us|an Expert) \]|'
    r'\[ Contact (Us|Experts|Our Team|Sales) \]|'
    r'\[ See Pricing \]|\[ Try (it )?(for )?Free \]|'
    r'\[ (Download|Read) (Now|Free|More) \]|'
    r'\[ Subscribe \]|\[ Sign Up \]'
)

FOOTER_FINGERPRINTS = [
    # Consent / privacy footer
    re.compile(r'(?i).*\b(we\s*use\s*cookies|this\s*site\s*uses\s*cookies|by\s*using\s*this\s*site).*'),
    re.compile(r'(?i).*\b(privacy\s*(policy|notice)|terms\s*of\s*(use|service)|data\s*processing).*'),
    re.compile(r'(?i).*\b(gdpr|ccpa|data\s*subject\s*rights|opt\s*out|do\s*not\s*sell\s*my).*'),
    # reCaptcha / form footer
    re.compile(r'(?i).*\b(recaptcha|re\.captcha|captcha|protected\s*by).*'),
    re.compile(r'(?i).*\b(required\s*fields|all\s*fields\s*are\s*required|form\s*is\s*protected).*'),
    # Company address / contact footer
    re.compile(r'(?i).*\b(headquarters|address|suite\s*\d+|boston|massachusetts|ma\s*\d{5}|united\s*states).*'),
    re.compile(r'(?i).*\b(toll[\s-]*free|1[\s-]?8\d{2}|phone|fax|email\s*us).*'),
    # CTA banner images
    re.compile(r'(?i).*!\[.*\]\(.*/(search-icon|icon-|logo-|share-|rating|social-).*\).*'),
    re.compile(r'(?i).*!\[.*\]\(.*/(cta|banner|hero|landing|cover|demo|trial|consult).*\).*'),
    # Nav section labels (sidebar chrome)
    re.compile(r'^\*{2}(How It Works|What.s Inside|By Business Need|By Industry|By Department|'
               r'Products|Solutions|Pricing|Support|Company|Resources):?\*{2}$'),
    # "Follow us" / social sections
    re.compile(r'(?i).*\b(follow\s*us|connect\s*with\s*us|find\s*us\s*on|social\s*media).*'),
    # Search / magnifying glass icons
    re.compile(r'(?i).*!\[.*\]\(.*/(magnifying|search|loupe).*\).*'),
]
