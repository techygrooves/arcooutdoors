# -*- coding: utf-8 -*-
"""Generates the 1200x630 social share cards in assets/images/og/.

Every page's own hero photograph is cover-cropped to the 1.91:1 ratio Facebook,
LinkedIn and X expect, darkened with the brand ink scrim, and captioned with the
page name in the site's own display face. Most heroes are 2.6:1 banners well
under 1200x630, which is why they cannot be used as share images directly.

Build-time only -- nothing here runs at deploy time, and no third-party asset is
introduced. Requires Pillow, plus fonttools+brotli to decompress the site's own
WOFF2 brand faces:  pip install pillow fonttools brotli
Run from the repository root:  python3 tools/make-og-cards.py
"""
import os, re, tempfile
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# page -> the hero photograph its card is cut from. Held here rather than read
# back out of the page, because og:image now names the generated card, not the
# hero. Pages with no hero of their own (the legal pages) share the homepage
# photograph. Card headlines come from each page's live og:title.
HEROES = [
    ("about-us/index.html",                               "hero-about-us.webp"),
    ("accessibility/index.html",                          "hero-outdoor-living-south-florida-1440.webp"),
    ("blog/artificial-turf-around-pools/index.html",      "hero-turf.webp"),
    ("blog/best-pool-deck-materials-florida/index.html",  "hero-pool-decks.webp"),
    ("blog/index.html",                                   "hero-blog.webp"),
    ("blog/outdoor-kitchen-planning-checklist/index.html", "hero-outdoor-kitchens.webp"),
    ("blog/pavers-vs-concrete-driveway-florida/index.html", "hero-driveways.webp"),
    ("blog/pergola-vs-tiki-hut/index.html",               "hero-pergolas.webp"),
    ("blog/planning-complete-backyard-remodel/index.html", "hero-complete-outdoor-transformation.webp"),
    ("contact-us/index.html",                             "hero-about-us.webp"),
    ("cookie-policy/index.html",                          "hero-outdoor-living-south-florida-1440.webp"),
    ("gallery/index.html",                                "hero-gallery.webp"),
    ("get-a-quote/index.html",                            "hero-complete-outdoor-transformation.webp"),
    ("index.html",                                        "hero-outdoor-living-south-florida-1440.webp"),
    ("privacy-policy/index.html",                         "hero-outdoor-living-south-florida-1440.webp"),
    ("projects/index.html",                               "hero-projects.webp"),
    ("reviews/index.html",                                "hero-reviews.webp"),
    ("service-areas/boca-raton-fl/index.html",            "hero-boca-raton-fl.webp"),
    ("service-areas/coral-springs-fl/index.html",         "hero-coral-springs-fl.webp"),
    ("service-areas/davie-fl/index.html",                 "hero-davie-fl.webp"),
    ("service-areas/fort-lauderdale-fl/index.html",       "hero-fort-lauderdale-fl.webp"),
    ("service-areas/index.html",                          "hero-service-areas.webp"),
    ("service-areas/parkland-fl/index.html",              "hero-parkland-fl.webp"),
    ("service-areas/pembroke-pines-fl/index.html",        "hero-pembroke-pines-fl.webp"),
    ("service-areas/plantation-fl/index.html",            "hero-plantation-fl.webp"),
    ("service-areas/weston-fl/index.html",                "hero-weston-fl.webp"),
    ("services/driveways/index.html",                     "hero-driveways.webp"),
    ("services/fence/index.html",                         "hero-fence.webp"),
    ("services/impact-windows-doors/index.html",          "hero-impact-windows-doors.webp"),
    ("services/index.html",                               "hero-services-outdoor-remodeling.webp"),
    ("services/outdoor-kitchens/index.html",              "hero-outdoor-kitchens.webp"),
    ("services/outdoor-remodeling/index.html",            "hero-complete-outdoor-transformation.webp"),
    ("services/patios/index.html",                        "hero-patios.webp"),
    ("services/paver-installation/index.html",            "hero-paver-installation.webp"),
    ("services/pergolas/index.html",                      "hero-pergolas.webp"),
    ("services/pool-decks/index.html",                    "hero-pool-decks.webp"),
    ("services/tiki-huts/index.html",                     "hero-tiki-huts.webp"),
    ("services/turf/index.html",                          "hero-turf.webp"),
]

W, H = 1200, 630
GOLD, SAND, MUTED, INK = (224,169,78), (246,241,232), (206,196,180), (36,29,21)
OUT = 'assets/images/og'
TMP = tempfile.mkdtemp()

for src, dst in (('assets/fonts/cormorant-garamond-latin.woff2', TMP+'/cormorant.ttf'),
                 ('assets/fonts/manrope-latin.woff2',            TMP+'/manrope.ttf')):
    f = TTFont(src); f.flavor = None; f.save(dst)
corm = lambda s: ImageFont.truetype(TMP+'/cormorant.ttf', s)
manr = lambda s: ImageFont.truetype(TMP+'/manrope.ttf', s)

def wrap(draw, text, font, width):
    lines, cur = [], ''
    for word in text.split():
        trial = (cur+' '+word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur: lines.append(cur)
            cur = word
    if cur: lines.append(cur)
    return lines

def card(photo, headline, dest):
    img = Image.open(photo).convert('RGB')
    r = max(W/img.width, H/img.height)
    img = img.resize((round(img.width*r), round(img.height*r)), Image.LANCZOS)
    l, t = (img.width-W)//2, (img.height-H)//2
    img = img.crop((l, t, l+W, t+H)).filter(ImageFilter.GaussianBlur(1.4))

    scrim = Image.new('L', (W, H)); sd = ImageDraw.Draw(scrim)
    for y in range(H):
        sd.line([(0,y),(W,y)], fill=int(158 + 90*(y/H)**1.4))
    img = Image.composite(Image.new('RGB',(W,H),INK), img, scrim)

    d = ImageDraw.Draw(img)
    d.rectangle([80,86,176,90], fill=GOLD)
    x, f = 80, manr(30)
    for ch in "ARCO OUTDOORS":
        d.text((x,122), ch, font=f, fill=GOLD); x += d.textlength(ch, font=f) + 5

    size = 96
    while size >= 52:
        f = corm(size); lines = wrap(d, headline, f, W-160)
        if len(lines) <= 3: break
        size -= 6
    lh = round(size*1.06)
    y = 452 - lh*len(lines)
    for line in lines:
        d.text((80,y), line, font=f, fill=SAND); y += lh

    d.text((80,506), "Complete outdoor transformations · South Florida", font=manr(26), fill=MUTED)
    d.text((80,558), "Licence CBC1269393  ·  305-951-8862", font=manr(24), fill=GOLD)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    img.save(dest, 'JPEG', quality=84, optimize=True, progressive=True)
    return os.path.getsize(dest)

def headline_for(title):
    """The page name with the brand removed. Titles are not uniformly
    'Page | Arco Outdoors': one reads 'Arco Outdoors | Page' and one ends
    'Arco Outdoors South Florida', so strip the brand only where it actually
    sits -- at the head or the tail. A title that carries the brand mid-phrase
    ('Contact Arco Outdoors') is left alone; the brand is the sentence there.
    """
    t = re.sub(r'^\s*Arco Outdoors\s*\|\s*', '', title)
    t = re.sub(r'\s*\|\s*Arco Outdoors(\s+South Florida)?\s*$', '', t)
    t = (t.strip() or 'Arco Outdoors').replace('&amp;', '&')
    return t.replace('\N{EM DASH}', '\N{EN DASH}')

if __name__ == '__main__':
    total = 0
    for page, hero in HEROES:
        title = re.search(r'<meta property="og:title" content="([^"]*)">',
                          open(page, encoding='utf-8').read()).group(1)
        slug = 'home' if page == 'index.html' else page[:-len('/index.html')].replace('/', '-')
        out = '%s/og-%s.jpg' % (OUT, slug)
        total += card('assets/images/' + hero, headline_for(title), out)
        print("%-46s %s" % (page, out))
    print("%d cards, %.0f KB total" % (len(HEROES), total/1024))
