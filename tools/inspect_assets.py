from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import json, struct, zlib

root=Path(r'E:\Download\Download')
out=Path(r'D:\Claude\mutasim-portfolio\reference')
files=sorted([p for p in root.iterdir() if p.suffix.lower() in {'.jpg','.jpeg','.png','.webp','.heic'}])
manifest=[]
for start in range(0,len(files),24):
    batch=files[start:start+24]
    sheet=Image.new('RGB',(1200, len(range(0,len(batch),4))*215),'#ededed')
    draw=ImageDraw.Draw(sheet)
    for n,p in enumerate(batch):
        idx=start+n
        try:
            im=ImageOps.exif_transpose(Image.open(p)).convert('RGB')
            manifest.append({'id':idx,'name':p.name,'width':im.width,'height':im.height})
            im.thumbnail((288,175))
            x=(n%4)*300; y=(n//4)*215
            sheet.paste(im,(x+(300-im.width)//2,y))
            draw.text((x+8,y+178),f'{idx}: {p.name[:37]}',fill='black')
        except Exception as e:
            manifest.append({'id':idx,'name':p.name,'error':str(e)})
    sheet.save(out/f'contact-{start//24+1}.jpg')
(out/'assets.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')

# Recover complete entries only from the incomplete reference download.
data=Path(r'C:\Users\Mutasim\Downloads\Shafi-Portfolio-main.7GZ9q-KB.zip.part').read_bytes()
offset=0; recovered=[]
while offset+30<=len(data) and data[offset:offset+4]==b'PK\x03\x04':
    head=struct.unpack_from('<IHHHHHIIIHH',data,offset)
    flags,method,compressed,namelen,extralen=head[2],head[3],head[7],head[9],head[10]
    name=data[offset+30:offset+30+namelen].decode('utf-8','replace')
    begin=offset+30+namelen+extralen
    if flags&8 or begin+compressed>len(data):break
    raw=data[begin:begin+compressed]
    if name.endswith(('.html','.css','.js','.json','.md')):
        try:
            content=zlib.decompress(raw,-15) if method==8 else raw
            dest=(out/'recovered'/name).resolve()
            if dest.is_relative_to((out/'recovered').resolve()):
                dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(content);recovered.append(name)
        except Exception:pass
    offset=begin+compressed
print(json.dumps({'photos':len(files),'contact_sheets':(len(files)+23)//24,'recovered':recovered,'bytes_examined':offset},indent=2))
