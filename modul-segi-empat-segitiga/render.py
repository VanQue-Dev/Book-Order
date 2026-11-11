# -*- coding: utf-8 -*-
"""Gabungkan SVG ke HTML, render PDF A4, dan laporkan jumlah halaman."""
import os, importlib, sys, shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent
ns={}
exec((BASE/'build.py').read_text(encoding='utf-8'),ns)
h=(BASE/'page.html').read_text(encoding='utf-8')
for k,v in ns['FIG'].items(): h=h.replace('{{'+k+'}}',v)
if '{{' in h: raise SystemExit('Masih ada placeholder SVG yang belum diganti.')
html=BASE/'modul.html'; html.write_text(h,encoding='utf-8')
out=BASE/'Modul_Segi_Empat_dan_Segitiga.pdf'
chrome=shutil.which('chromium') or shutil.which('google-chrome')
if importlib.util.find_spec('playwright') and chrome:
    import asyncio
    from playwright.async_api import async_playwright
    async def main():
        async with async_playwright() as p:
            browser=await p.chromium.launch(executable_path=chrome,args=['--no-sandbox'])
            page=await browser.new_page()
            await page.set_content(h,wait_until='load'); await page.pdf(path=str(out),format='A4',print_background=True,prefer_css_page_size=True)
            await browser.close()
    asyncio.run(main()); engine='Chrome/Playwright'
elif importlib.util.find_spec('weasyprint'):
    from weasyprint import HTML
    HTML(filename=str(html)).write_pdf(str(out)); engine='WeasyPrint'
elif importlib.util.find_spec('xhtml2pdf'):
    from xhtml2pdf import pisa
    with out.open('wb') as f: pisa.CreatePDF(h,dest=f)
    engine='xhtml2pdf'
else: raise SystemExit('Tidak ada mesin render yang didukung.')
try:
    import fitz
    doc=fitz.open(out); pages=len(doc)
except Exception: pages='tidak terbaca'
print(f'PDF: {out}\nMesin: {engine}\nHalaman: {pages}\nBytes: {out.stat().st_size}')

