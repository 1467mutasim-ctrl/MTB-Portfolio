"""Build the downloadable CV from confirmed facts in cv-profile.json."""
import json
import shutil
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'tools/cv-profile.json').read_text(encoding='utf-8'))
output = ROOT / 'output/pdf/Mutasim-Billah-CV.pdf'
output.parent.mkdir(parents=True, exist_ok=True)

ink = colors.HexColor('#182537')
blue = colors.HexColor('#304d73')
muted = colors.HexColor('#4f5b68')
rule = colors.HexColor('#c9d2dc')
MARGIN = 42
FRAME_PADDING = 6  # SimpleDocTemplate's frame pads each side by 6pt
WIDTH = A4[0] - 2 * MARGIN - 2 * FRAME_PADDING
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=24, leading=28, textColor=ink),
    'headline': ParagraphStyle('headline', fontName='Helvetica', fontSize=11, leading=15, textColor=blue, spaceBefore=1, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=8.6, leading=12, textColor=muted),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=blue, spaceBefore=7),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9, leading=12, textColor=ink),
    'title': ParagraphStyle('title', fontName='Helvetica-Bold', fontSize=9.4, leading=12.4, textColor=ink),
    'meta': ParagraphStyle('meta', fontName='Helvetica-Oblique', fontSize=8.6, leading=12.4, textColor=muted, alignment=2),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9, leading=11.8, textColor=ink, leftIndent=11, bulletIndent=1, spaceBefore=1),
}


def p(text, kind='body', **kwargs):
    return Paragraph(text, styles[kind], **kwargs)


def link(url, label):
    return f'<link href="{escape(url)}" color="#304d73">{escape(label)}</link>'


def heading(text):
    return [p(text.upper(), 'heading'), HRFlowable(width='100%', thickness=0.6, color=rule, spaceBefore=2, spaceAfter=5)]


def two_columns(left, right, left_width=0.68):
    table = Table([[left, right]], colWidths=[WIDTH * left_width, WIDTH * (1 - left_width)])
    table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 0), ('TOPPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 0)]))
    return table


def entry(item):
    title = '<b>' + escape(item['title']) + '</b>'
    if item.get('link'):
        title += ' &nbsp;' + link(item['link'], 'GitHub')
    parts = [two_columns(p(title, 'title'), p(escape(item['meta']), 'meta'))]
    parts += [p(escape(text), 'bullet', bulletText='•') for text in item['bullets']]
    parts.append(Spacer(1, 3))
    return KeepTogether(parts)


short = lambda url: url.split('://', 1)[1].removeprefix('www.').rstrip('/')
story = [
    p(escape(data['name']), 'name'),
    p(escape(data['headline']), 'headline'),
    p(' &nbsp;·&nbsp; '.join([escape(data['location']), link('mailto:' + data['email'], data['email']), escape(data['phone'])]), 'contact'),
    p(' &nbsp;·&nbsp; '.join([link(data['linkedin'], short(data['linkedin'])), link(data['github'], short(data['github'])), link(data['portfolio'], 'Portfolio')]), 'contact'),
    Spacer(1, 2),
]
story += heading('Summary') + [p(escape(data['summary']))]

story += heading('Education')
for item in data['education']:
    story.append(two_columns(p('<b>' + escape(item['degree']) + '</b><br/>' + escape(item['school']), 'title'), p(escape(item['dates']), 'meta')))

story += heading('Technical skills')
rows = [[p('<b>' + escape(label) + '</b>'), p(escape(value))] for label, value in data['skills']]
skills = Table(rows, colWidths=[118, WIDTH - 118], hAlign='LEFT')
skills.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0), ('RIGHTPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 1), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
story.append(skills)

story += heading('Projects') + [entry(item) for item in data['projects']]
story += heading('Leadership and activities') + [entry(item) for item in data['leadership']]
story += heading('Achievements') + [p(escape(text), 'bullet', bulletText='•') for text in data['achievements']]
if data.get('interests'):
    story += heading('Interests') + [p(escape(data['interests']))]

doc = SimpleDocTemplate(str(output), pagesize=A4, topMargin=32, bottomMargin=30, leftMargin=MARGIN, rightMargin=MARGIN,
                        title='Mutasim Billah - CV', author=data['name'], subject='Curriculum vitae')
doc.build(story)
destination = ROOT / 'dist/assets/Mutasim-Billah-CV.pdf'
shutil.copyfile(output, destination)
print(destination)
