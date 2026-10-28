#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerates every brand asset from the client's supplied logo artwork.

    python3 tools/make-brand-assets.py path/to/logo.webp

Build time only -- nothing here runs at deploy time. Needs Pillow.

Writes:
    assets/images/arco-emblem.webp        wreath + A, transparent, for the
                                          header and footer brand marks
    assets/images/arco-outdoors-logo.webp full lockup, transparent, JSON-LD logo
    assets/images/apple-touch-icon.png    180x180 on the ink ground
    favicon-32.png                        32x32 on the ink ground

The supplied artwork is flat gold composited on a near-black ground, so every
pixel is gold*alpha. Alpha is recovered from the peak channel and divided back
out, which gives edges that sit correctly on the sand header AND the ink footer.
Keying out black instead leaves a dark fringe on the cream ground.

The band coordinates below were measured from the supplied 1500x2000 artwork
with row and column ink profiles. A different source file needs them re-measured
-- see PROJECT-SPEC.md §9.15.
"""
import os, sys
from PIL import Image

SRC = sys.argv[1] if len(sys.argv) > 1 else 'brand-source.webp'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
INK = (26, 21, 15)
PEAK = 249.0        # brightest channel value present in the artwork
CUTOFF = 0.10       # the ground is (5,5,5); anything fainter is background
im = Image.open(SRC).convert('RGB')
px = im.load()


def cut(box, pad=0):
    """Crop, then turn the black ground into alpha.

    The source is flat gold artwork composited on near-black, so every pixel is
    gold*alpha. Recovering alpha from the peak channel and dividing it back out
    gives clean antialiased edges that sit correctly on ANY background -- the
    sand header and the ink footer both. Keying out black instead would leave a
    dark fringe on the cream ground."""
    l,t,r,b=box
    c=im.crop((l-pad,t-pad,r+1+pad,b+1+pad)).convert('RGBA')
    px=c.load(); W,H=c.size
    for y in range(H):
        for x in range(W):
            rr,gg,bb,_=px[x,y]
            a=max(rr,gg,bb)/PEAK
            if a<=CUTOFF: px[x,y]=(0,0,0,0); continue   # the ground is (5,5,5); anything that faint is background, not artwork
            a=min(a,1.0)
            px[x,y]=(min(255,int(rr/a)),min(255,int(gg/a)),min(255,int(bb/a)),int(round(a*255)))
    return c

# measured bands
emblem = cut((218,582,1281,1092))
word   = cut((218,1201,1281,1274))
full   = cut((218,582,1281,1274))

def save(img,name,width):
    h=round(img.height*width/img.width)
    r=img.resize((width,h),Image.LANCZOS)
    p=OUT+'assets/images/'+name
    r.save(p,'WEBP',quality=92,method=6,lossless=False)
    print("%-34s %4dx%-4d %6d B"%(name,r.width,r.height,os.path.getsize(p)))
    return r

# the emblem is near-square; trim it to its own bbox first so it centres properly
eb=emblem.getbbox(); emblem=emblem.crop(eb)
print("emblem trimmed to",emblem.size)
save(emblem,'arco-emblem.webp',320)
save(full,'arco-outdoors-logo.webp',760)

# The A + column sits inside the wreath. Row and column ink profiles put the
# glyph at x 555-845, y 635-935; outside that is laurel, which turns to mush at
# favicon sizes. Scanning a loose "centre region" instead pulled in wreath
# fragments, which is what the first attempt got wrong.
GLYPH=(555,635,846,936)

def keyed(box):
    c=im.crop(box).convert('RGBA'); p=c.load()
    for yy in range(c.height):
        for xx in range(c.width):
            r,g,b,_=p[xx,yy]
            a=max(r,g,b)/PEAK
            if a<=CUTOFF: p[xx,yy]=(0,0,0,0); continue
            a=min(a,1.0)
            p[xx,yy]=(min(255,int(r/a)),min(255,int(g/a)),min(255,int(b/a)),int(round(a*255)))
    return c

glyph=keyed(GLYPH)

def drop_specks(img,min_px=400):
    """A leaf tip from the surrounding wreath clips the corner of any rectangle
    tight enough to hold the glyph. Keeping only large connected components
    removes it without nudging the crop in and shaving the A's swash."""
    W,H=img.size; p=img.load()
    seen=[[False]*W for _ in range(H)]; keep=set()
    for sy in range(H):
        for sx in range(W):
            if seen[sy][sx] or p[sx,sy][3]<24: continue
            stack=[(sx,sy)]; seen[sy][sx]=True; comp=[]
            while stack:
                x,y=stack.pop(); comp.append((x,y))
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<W and 0<=ny<H and not seen[ny][nx] and p[nx,ny][3]>=24:
                        seen[ny][nx]=True; stack.append((nx,ny))
            if len(comp)>=min_px: keep.update(comp)
            else: print("   dropped speck of %d px at %s"%(len(comp),comp[0]))
    for y in range(H):
        for x in range(W):
            if (x,y) not in keep: p[x,y]=(0,0,0,0)
    return img

glyph=drop_specks(glyph)
glyph=glyph.crop(glyph.getbbox())

def icon(size,pad_ratio,path,ground=INK,radius=None):
    """Glyph centred on the ink ground -- the logo's native presentation, and the
    only one that stays legible against light and dark browser chrome alike."""
    canvas=Image.new('RGBA',(size,size),ground+(255,))
    box=int(size*(1-pad_ratio*2))
    g=glyph.copy()
    g.thumbnail((box,box),Image.LANCZOS)
    canvas.paste(g,((size-g.width)//2,(size-g.height)//2),g)
    canvas.convert('RGB').save(OUT+path,'PNG',optimize=True)
    print("%-38s %dx%d  %6d B"%(path,size,size,os.path.getsize(OUT+path)))

icon(32,0.16,'favicon-32.png')
icon(180,0.18,'assets/images/apple-touch-icon.png')
