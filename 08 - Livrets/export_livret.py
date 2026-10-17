"""Export du livret de règles (Markdown Obsidian) vers ODT pour Scribus.
Usage : python3 export_livret.py <livret.md> <sortie.odt>
- retire le frontmatter et la ligne de renvoi Obsidian ;
- encadrés « Exemple » / « À retenir » -> styles Encadre_Exemple / Encadre_A_retenir ;
- lignes {ILLUS:…} -> style Illustration (le texte reste, c'est le cahier des charges) ;
- marqueurs {VERT}, {DÉ:…}… laissés en texte pour le rechercher-remplacer ;
- reference.odt : page A4, styles nommés à habiller dans Scribus.
"""
import re, sys, subprocess, zipfile, shutil, os, tempfile

STYLES = '''
<style:style style:name="Encadre_Exemple" style:display-name="Encadré Exemple" style:family="paragraph" style:parent-style-name="Text_20_body">
 <style:paragraph-properties fo:margin-left="0.5cm" fo:margin-right="0.5cm" fo:margin-top="0.25cm" fo:margin-bottom="0.25cm" fo:padding="0.2cm" fo:background-color="#efe9dc" fo:border-left="0.08cm solid #8a6d3b"/>
 <style:text-properties fo:font-style="italic"/>
</style:style>
<style:style style:name="Encadre_A_retenir" style:display-name="Encadré À retenir" style:family="paragraph" style:parent-style-name="Text_20_body">
 <style:paragraph-properties fo:margin-top="0.3cm" fo:margin-bottom="0.3cm" fo:padding="0.2cm" fo:background-color="#dfe7ef" fo:border="0.06cm solid #2f4f6f"/>
 <style:text-properties fo:font-weight="bold"/>
</style:style>
<style:style style:name="Illustration" style:display-name="Illustration" style:family="paragraph" style:parent-style-name="Text_20_body">
 <style:paragraph-properties fo:text-align="center" fo:margin-top="0.3cm" fo:margin-bottom="0.3cm" fo:padding="0.3cm" fo:border="0.03cm dashed #888888"/>
 <style:text-properties fo:font-size="8pt" fo:color="#666666"/>
</style:style>
'''

def preprocess(md):
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    out = []
    for line in md.split('\n'):
        if line.startswith('> Conventions d') and '[[' in line:
            continue  # renvoi interne Obsidian
        m = re.match(r'^> \*\*(Exemple|À retenir)\*\*', line)
        if m:
            style = 'Encadre_Exemple' if m.group(1) == 'Exemple' else 'Encadre_A_retenir'
            out += [f'::: {{custom-style="{style}"}}', line[2:], ':::']
            continue
        if line.startswith('{ILLUS:'):
            out += ['::: {custom-style="Illustration"}', line.replace('*', r'\*'), ':::']
            continue
        out.append(line)
    return '\n'.join(out)

def set_heading(s, name, size, page_break):
    """Hiérarchie des titres : # titre du livret, ## chapitre (nouvelle page), ### section."""
    pat = r'(<style:style style:name="' + name + r'".*?>)\s*<style:text-properties.*?/>'
    para = '<style:paragraph-properties fo:break-before="page"/>' if page_break else ''
    text = (f'<style:text-properties fo:font-size="{size}" fo:font-weight="bold" '
            f'style:font-size-asian="{size}" style:font-weight-asian="bold" '
            f'style:font-size-complex="{size}" style:font-weight-complex="bold"/>')
    s2, n = re.subn(pat, lambda m: m.group(1) + para + text, s, count=1, flags=re.S)
    assert n == 1, name
    return s2

def build_reference(path):
    base = subprocess.run(['pandoc', '--print-default-data-file', 'reference.odt'],
                          capture_output=True, check=True).stdout
    tmp = path + '.tmp'
    open(tmp, 'wb').write(base)
    with zipfile.ZipFile(tmp) as zin, zipfile.ZipFile(path, 'w') as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == 'styles.xml':
                s = data.decode('utf-8')
                s = s.replace('</office:styles>', STYLES + '</office:styles>', 1)
                s = set_heading(s, 'Heading_20_1', '20pt', page_break=False)
                s = set_heading(s, 'Heading_20_2', '16pt', page_break=True)
                s = set_heading(s, 'Heading_20_3', '12.5pt', page_break=False)
                s = re.sub(r'fo:page-width="[^"]*"', 'fo:page-width="21cm"', s)
                s = re.sub(r'fo:page-height="[^"]*"', 'fo:page-height="29.7cm"', s)
                data = s.encode('utf-8')
            comp = zipfile.ZIP_STORED if item.filename == 'mimetype' else zipfile.ZIP_DEFLATED
            zout.writestr(item, data, compress_type=comp)
    os.remove(tmp)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    work = tempfile.mkdtemp()
    ref = os.path.join(work, 'reference.odt')
    build_reference(ref)
    mdp = os.path.join(work, 'livret.md')
    open(mdp, 'w', encoding='utf-8').write(preprocess(open(src, encoding='utf-8').read()))
    subprocess.run(['pandoc', mdp, '-f', 'markdown-smart', '-o', dst,
                    f'--reference-doc={ref}', '--metadata', 'lang=fr-FR'], check=True)
    print('ODT écrit :', dst)
