"""Create the Pages artifact without docs, local photos, or hidden files."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
ASSET_TYPES = {'.png', '.svg', '.json'}


def prepare():
    if SITE.is_symlink() or (ROOT / 'assets').is_symlink():
        raise ValueError('Publication folders must not be symlinks')
    files = []
    for source in (ROOT / 'assets').rglob('*'):
        if source.is_symlink():
            raise ValueError(f'Symlink cannot be published: {source.name}')
        if not source.is_file():
            continue
        if any(part.startswith('.') for part in source.relative_to(ROOT / 'assets').parts):
            continue
        if source.suffix.lower() in {'.jpg', '.jpeg'}:
            continue
        if source.suffix.lower() not in ASSET_TYPES:
            raise ValueError(f'Review unexpected asset type: {source.name}')
        files.append(source)
    for name in ('index.html', 'style.css', 'app.js'):
        if not (ROOT / name).is_file() or (ROOT / name).is_symlink():
            raise ValueError(f'Missing regular source file: {name}')
    if not files:
        raise ValueError('No public assets found')
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    for name in ('index.html', 'style.css', 'app.js'):
        shutil.copyfile(ROOT / name, SITE / name)
    for source in files:
        destination = SITE / source.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    print(f'Prepared _site: 3 web files + {len(files)} public assets')


if __name__ == '__main__':
    prepare()
