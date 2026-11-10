#!/usr/bin/env python3
"""CHRONOS Excel -> karten.json. Nur Python-Standardbibliothek benötigt."""
import json, re, sys, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}

def xlsx_rows(path):
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            root=ET.fromstring(z.read('xl/sharedStrings.xml'))
            shared=[''.join(t.text or '' for t in si.findall('.//m:t',NS)) for si in root.findall('m:si',NS)]
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        sheets=wb.findall('.//m:sheets/m:sheet',NS)
        if not sheets: raise ValueError('Keine Tabellenblätter gefunden')
        chosen=next((s for s in sheets if s.get('name')=='Karten'),sheets[0])
        rel=chosen.get('{'+NS['r']+'}id')
        relroot=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        target=next((e.get('Target') for e in relroot if e.get('Id')==rel),None)
        if not target: raise ValueError('Tabellenblatt nicht gefunden')
        from posixpath import normpath
        sheetpath=target.lstrip('/') if target.startswith('/') else normpath('xl/'+target)
        sheet=ET.fromstring(z.read(sheetpath))
        for row in sheet.findall('.//m:sheetData/m:row',NS):
            cells={}
            for cell in row.findall('m:c',NS):
                ref=cell.get('r',''); col=re.match(r'[A-Z]+',ref)
                if not col:continue
                n=0
                for letter in col.group():n=n*26+ord(letter)-64
                typ=cell.get('t'); v=cell.find('m:v',NS)
                if typ=='inlineStr':value=''.join(t.text or '' for t in cell.findall('.//m:t',NS))
                elif v is None:value=''
                elif typ=='s':value=shared[int(v.text)]
                else:value=v.text or ''
                cells[n-1]=value
            yield [cells.get(i,'') for i in range(19)]

def main():
    source=Path(sys.argv[1] if len(sys.argv)>1 else 'CHRONOS_Mastertabelle.xlsx')
    rows=list(xlsx_rows(source));cards=[]
    for i,r in enumerate(rows[1:],2):
        if not str(r[0]).strip():continue
        id=str(r[0]).strip().zfill(3)
        if not r[1] or not r[2] or not r[6]:raise ValueError(f'Zeile {i}: Komponist, Werktitel und Audio fehlen')
        def val(k):return str(r[k] or '').strip()
        year=int(float(r[4])) if str(r[4]).strip() else ''
        cards.append({'id':id,'composer':val(1),'title':val(2),'movement':val(3),'year':year,'dateType':val(5),'audio':val(6),'vocalBonus':val(14),'solution':val(15),'conductor':val(16),'ensemble':val(17),'soloists':val(18)})
    if len(set(c['id'] for c in cards))!=len(cards):raise ValueError('Doppelte Karten-IDs gefunden')
    dest=Path(__file__).with_name('karten.json')
    dest.write_text(json.dumps(cards,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'{len(cards)} Karten aktualisiert: {dest}')
if __name__=='__main__':main()
