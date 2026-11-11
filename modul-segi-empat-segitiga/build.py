# -*- coding: utf-8 -*-
"""Ilustrasi SVG orisinal untuk modul Segi Empat dan Segitiga."""
NAVY="#1b2559"; BLUE="#3b6ef5"; ORG="#ff8a3d"; GRN="#16a37b"; YEL="#ffc93c"; PUR="#7b5cf0"; RED="#ef4b5a"; GREY="#5d6788"
PBLUE="#e9f0ff"; PORG="#fff1e6"; PGRN="#e3f6ef"; PPUR="#efeafe"; PRED="#fde8ea"; PYEL="#fff8e1"

def T(x,y,t,size=12,fill=NAVY,weight=700,anchor="middle"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans,sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>'
def svg(body,w=300,h=170):
    return f'<svg viewBox="0 0 {w} {h}" class="fig" xmlns="http://www.w3.org/2000/svg">'+''.join(body)+'</svg>'
def base(title): return [f'<rect x="3" y="3" width="294" height="164" rx="15" fill="#f7f9fd" stroke="#dfe5f2"/>',T(150,22,title,11,BLUE)]
def fig_family():
    s=base('Keluarga bangun datar')
    s += ['<rect x="24" y="43" width="64" height="48" fill="#e9f0ff" stroke="#3b6ef5" stroke-width="3"/>','<rect x="111" y="43" width="86" height="48" fill="#fff1e6" stroke="#ff8a3d" stroke-width="3"/>','<path d="M220 91 L250 42 L280 91 Z" fill="#e3f6ef" stroke="#16a37b" stroke-width="3"/>',T(56,108,'persegi',10),T(154,108,'persegi panjang',9),T(250,108,'segitiga',10),'<path d="M25 128 H275" stroke="#b9c3d9" stroke-width="2"/>',T(150,148,'Segitiga: 3 sisi · Segi empat: 4 sisi',10,NAVY),T(56,120,'4 sisi',8,BLUE),T(154,120,'4 sisi',8,ORG),T(250,120,'3 sisi',8,GRN),'<circle cx="24" cy="43" r="3" fill="#1b2559"/>','<circle cx="88" cy="43" r="3" fill="#1b2559"/>','<circle cx="250" cy="42" r="3" fill="#1b2559"/>']
    return svg(s)
def fig_square():
    s=base('Lantai ubin persegi 4 × 4')
    for i in range(4):
      for j in range(4): s.append(f'<rect x="78" y="42" width="28" height="24" transform="translate({j*29} {i*25})" fill="{[PBLUE,PYEL][(i+j)%2]}" stroke="{BLUE}"/>')
    s += [T(135,35,'4 cm',10),T(66,91,'4 cm',10),T(136,153,'16 ubin satuan → luas 16 cm²',10,GRN)]
    return svg(s)
def fig_rectangle():
    s=base('Kebun berbentuk persegi panjang')
    s += ['<rect x="55" y="48" width="190" height="78" rx="3" fill="#e3f6ef" stroke="#16a37b" stroke-width="3"/>','<path d="M55 42 V34 M245 42 V34 M55 38 H245" stroke="#1b2559" stroke-width="1.5"/>',T(150,31,'10 m',11),'<path d="M48 48 H40 M48 126 H40 M44 48 V126" stroke="#1b2559"/>',T(31,91,'4 m',10),'<circle cx="92" cy="83" r="8" fill="#16a37b"/><circle cx="150" cy="83" r="8" fill="#16a37b"/><circle cx="208" cy="83" r="8" fill="#16a37b"/>',T(150,147,'P = 28 m · L = 40 m',11,GRN),'<circle cx="92" cy="83" r="3" fill="#ff8a3d"/>','<circle cx="150" cy="83" r="3" fill="#ff8a3d"/>','<circle cx="208" cy="83" r="3" fill="#ff8a3d"/>']
    return svg(s)
def fig_parallelogram():
    s=base('Geser segitiga: luas tetap')
    s += ['<path d="M80 126 L120 50 L235 50 L195 126 Z" fill="#e9f0ff" stroke="#3b6ef5" stroke-width="3"/>','<path d="M120 50 V126" stroke="#ff8a3d" stroke-width="2" stroke-dasharray="4 3"/>','<path d="M120 126 H235" stroke="#16a37b" stroke-width="2"/>',T(178,144,'alas 8 cm',10,GRN),T(104,90,'tinggi 3 cm',10,ORG),T(178,39,'geser tanpa mengubah luas',9),'<circle cx="80" cy="126" r="4" fill="#1b2559"/>','<circle cx="120" cy="50" r="4" fill="#1b2559"/>','<circle cx="235" cy="50" r="4" fill="#1b2559"/>',T(150,160,'L = 24 cm² · P = 26 cm',9,GRN)]
    return svg(s)
def fig_rhombus():
    s=base('Belah ketupat dan diagonal')
    s += ['<path d="M150 35 L245 85 L150 135 L55 85 Z" fill="#efeafe" stroke="#7b5cf0" stroke-width="3"/>','<path d="M55 85 H245 M150 35 V135" stroke="#ff8a3d" stroke-width="2" stroke-dasharray="5 3"/>',T(92,76,'d₁ = 8 cm',8),T(255,89,'d₂ = 6 cm',9,ORG,'700','start'),T(150,155,'L = ½ × 8 × 6 = 24 cm²',10,PUR),'<path d="M55 85 H245" stroke="#1b2559" stroke-width=1 stroke-dasharray="2 3"/>','<circle cx="150" cy="35" r="4" fill="#1b2559"/>','<circle cx="245" cy="85" r="4" fill="#1b2559"/>','<circle cx="150" cy="135" r="4" fill="#1b2559"/>','<circle cx="55" cy="85" r="4" fill="#1b2559"/>']
    return svg(s)
def fig_kite():
    s=base('Layang-layang: dua pasang sisi berdekatan')
    s += ['<path d="M150 35 L225 92 L150 140 L75 92 Z" fill="#fff1e6" stroke="#ff8a3d" stroke-width="3"/>','<path d="M150 35 V140 M75 92 H225" stroke="#3b6ef5" stroke-width="2" stroke-dasharray="5 3"/>',T(162,58,'d₁ = 16 cm',8,BLUE),T(190,115,'d₂ = 10 cm',8,ORG),T(150,158,'L = ½ × 16 × 10 = 80 cm²',10),'<path d="M140 92 H160" stroke="#1b2559" stroke-width=1.5"/>','<circle cx="150" cy="35" r="4" fill="#1b2559"/>','<circle cx="225" cy="92" r="4" fill="#1b2559"/>','<circle cx="150" cy="140" r="4" fill="#1b2559"/>','<circle cx="75" cy="92" r="4" fill="#1b2559"/>']
    return svg(s)
def fig_trapezoid():
    s=base('Trapesium: dua sisi sejajar')
    s += ['<path d="M88 48 H212 L260 128 H40 Z" fill="#e3f6ef" stroke="#16a37b" stroke-width="3"/>','<path d="M150 48 V128" stroke="#ff8a3d" stroke-width="2" stroke-dasharray="5 3"/>',T(120,62,'a = 8 cm',9),T(150,145,'b = 14 cm · t = 5 cm',10,GRN),T(150,160,'L = ½(a+b)t = 55 cm²',10),'<path d="M88 38 H212" stroke="#1b2559" stroke-width=1 stroke-dasharray="3 3"/>','<circle cx="88" cy="48" r="4" fill="#1b2559"/>','<circle cx="212" cy="48" r="4" fill="#1b2559"/>','<circle cx="40" cy="128" r="4" fill="#1b2559"/>','<circle cx="260" cy="128" r="4" fill="#1b2559"/>']
    return svg(s)
def fig_triangle_types():
    s=base('Segitiga menurut panjang sisi')
    s += ['<path d="M35 115 L75 45 L115 115 Z" fill="#e9f0ff" stroke="#3b6ef5" stroke-width="2.5"/>','<path d="M137 115 L177 45 L217 115 Z" fill="#fff1e6" stroke="#ff8a3d" stroke-width="2.5"/>','<path d="M235 115 L275 57 L290 115 Z" fill="#e3f6ef" stroke="#16a37b" stroke-width="2.5"/>',T(75,136,'sama sisi: 3-3-3',8),T(177,136,'sama kaki: 5-5-8',8),T(262,136,'4-5-6',8),T(150,157,'3 sisi sama · 2 sisi sama · semua berbeda',9),'<circle cx="35" cy="115" r="3" fill="#1b2559"/>','<circle cx="75" cy="45" r="3" fill="#1b2559"/>','<circle cx="115" cy="115" r="3" fill="#1b2559"/>','<circle cx="137" cy="115" r="3" fill="#1b2559"/>','<circle cx="177" cy="45" r="3" fill="#1b2559"/>','<circle cx="217" cy="115" r="3" fill="#1b2559"/>']
    return svg(s)
def fig_perimeter():
    s=base('Keliling: telusuri seluruh tepi')
    s += ['<path d="M75 125 L171 125 L75 53 Z" fill="#fff8e1" stroke="#3b6ef5" stroke-width="4"/>',T(123,145,'alas 8 cm',10,BLUE),T(60,90,'6 cm',10,ORG),T(135,78,'10 cm',10,GRN),T(150,160,'6 + 8 + 10 = 24 cm',10,BLUE),'<circle cx="75" cy="125" r="4" fill="#ff8a3d"/>','<circle cx="171" cy="125" r="4" fill="#ff8a3d"/>','<circle cx="75" cy="53" r="4" fill="#ff8a3d"/>','<path d="M75 115 H85 V125" fill="none" stroke="#ff8a3d" stroke-width="2"/>','<path d="M50 53 L50 125" stroke="#1b2559" stroke-width="1.2" stroke-dasharray="3 3"/>']
    return svg(s)
def fig_triangle_area():
    s=base('Tinggi tegak lurus pada alas')
    s += ['<path d="M65 130 L240 130 L180 45 Z" fill="#efeafe" stroke="#7b5cf0" stroke-width="3"/>','<path d="M180 45 V130" stroke="#ff8a3d" stroke-width="2.5" stroke-dasharray="5 3"/>','<path d="M180 120 H190 V130" fill="none" stroke="#ff8a3d" stroke-width="2"/>',T(150,148,'alas 10 cm · tinggi 6 cm',10),T(194,87,'6 cm',9,ORG),T(150,162,'L = ½ × 10 × 6 = 30 cm²',10,PUR),'<circle cx="65" cy="130" r="4" fill="#1b2559"/>','<circle cx="240" cy="130" r="4" fill="#1b2559"/>','<circle cx="180" cy="45" r="4" fill="#1b2559"/>']
    return svg(s)
def fig_composite():
    s=base('Bangun gabungan: pecah lalu jumlahkan')
    s += ['<rect x="60" y="55" width="110" height="75" fill="#e9f0ff" stroke="#3b6ef5" stroke-width="3"/>','<path d="M170 130 L225 55 L280 130 Z" fill="#fff1e6" stroke="#ff8a3d" stroke-width="3"/>','<path d="M170 55 V130" stroke="#1b2559" stroke-dasharray="4 3"/><path d="M225 55 V130" stroke="#ff8a3d" stroke-width=2 stroke-dasharray="4 3"/>',T(115,95,'A',16,BLUE),T(200,110,'B',16,ORG),T(150,151,'L gabungan = 60 + 20 = 80 m²',10),T(115,44,'10 m',9,BLUE),T(225,44,'alas 10 m',9,ORG),T(240,96,'4 m',8,ORG),'<circle cx="60" cy="55" r="4" fill="#1b2559"/>','<circle cx="170" cy="55" r="4" fill="#1b2559"/>','<circle cx="280" cy="130" r="4" fill="#1b2559"/>']
    return svg(s)
def fig_units():
    s=base('Satuan panjang dan luas berbeda skala')
    s += ['<rect x="35" y="52" width="95" height="50" fill="#e9f0ff" stroke="#3b6ef5" stroke-width="2"/>','<path d="M35 42 H130" stroke="#1b2559"/><path d="M35 38 V46 M130 38 V46" stroke="#1b2559"/>',T(82,33,'1 m',10),'<rect x="170" y="52" width="95" height="50" fill="#e3f6ef" stroke="#16a37b" stroke-width="2"/>',T(217,82,'1 m²',13,GRN),T(150,130,'1 m = 100 cm',11),T(150,151,'1 m² = 10.000 cm²',11,ORG),T(150,165,'100 cm × 100 cm',9,BLUE),'<path d="M35 110 H130 M170 110 H265" stroke="#ff8a3d" stroke-width=1.5 stroke-dasharray="3 3"/>']
    return svg(s)

def fig_cover():
    return '<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" width="520" height="300"><path d="M75 230 L75 90 L215 90 L215 230 Z" fill="#e9f0ff" stroke="#1b2559" stroke-width="7"/><path d="M270 230 L390 70 L500 230 Z" fill="#fff1e6" stroke="#1b2559" stroke-width="7"/><circle cx="135" cy="145" r="9" fill="#1b2559"/><circle cx="175" cy="145" r="9" fill="#1b2559"/><path d="M132 180 Q155 200 180 180" fill="none" stroke="#1b2559" stroke-width="6" stroke-linecap="round"/><circle cx="380" cy="160" r="9" fill="#1b2559"/><circle cx="420" cy="160" r="9" fill="#1b2559"/><path d="M380 190 Q400 210 420 190" fill="none" stroke="#1b2559" stroke-width="6" stroke-linecap="round"/><text x="145" y="265" text-anchor="middle" font-size="17" fill="#1b2559">Kotak & segitiga</text></svg>'

def fig_map():
    pts=[(45,55),(145,42),(245,65),(345,42),(455,62),(555,100),(505,190),(390,205),(275,185),(160,210),(55,175),(45,55)]
    s=['<svg viewBox="0 0 600 250" class="fig" xmlns="http://www.w3.org/2000/svg">','<path d="M45 55 L145 42 L245 65 L345 42 L455 62 L555 100 L505 190 L390 205 L275 185 L160 210 L55 175" fill="none" stroke="#dfe6fb" stroke-width="18" stroke-linecap="round"/>']
    names=['Kenali','Persegi','Persegi panjang','Jajar genjang','Belah ketupat','Layang-layang','Trapesium','Jenis segitiga','Keliling','Luas segitiga','Gabungan']
    for i,(x,y) in enumerate(pts[:-1]):
      s.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{[BLUE,ORG,GRN,PUR,RED][i%5]}" stroke="white" stroke-width="3"/>')
      s.append(T(x,y+4,str(i+1),10,'#ffffff'))
      s.append(T(x,y-22 if i<6 else y+34,names[i],9,NAVY))
    s.append('</svg>')
    return ''.join(s)

FIG={
 'cover':fig_cover(), 'c01':fig_family(), 'c02':fig_square(), 'c03':fig_rectangle(), 'c04':fig_parallelogram(),
 'c05':fig_rhombus(), 'c06':fig_kite(), 'c07':fig_trapezoid(), 'c08':fig_triangle_types(), 'c09':fig_perimeter(),
 'c10':fig_triangle_area(), 'c11':fig_composite(), 'c12':fig_units(), 'map':fig_map()
}

