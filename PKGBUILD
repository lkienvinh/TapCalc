pkgname=tapcalc
pkgver=1.0
pkgrel=1
pkgdesc="TapCalc PyQt6 Calculator"
arch=('any')
license=('MIT')

depends=('python' 'python-pyqt6')

source=('main.py'
        'calculator.py'
        'tapcalc.desktop'
        'tapcalc.png')

sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP')
package() {

    install -d "$pkgdir/usr/share/tapcalc"

    install -m755 main.py \
        "$pkgdir/usr/share/tapcalc/main.py"

    install -m644 calculator.py \
        "$pkgdir/usr/share/tapcalc/calculator.py"

    mkdir -p "$pkgdir/usr/bin"

    echo '#!/bin/bash
python3 /usr/share/tapcalc/main.py' \
    > "$pkgdir/usr/bin/tapcalc"

    chmod +x "$pkgdir/usr/bin/tapcalc"

    install -Dm644 tapcalc.desktop \
        "$pkgdir/usr/share/applications/tapcalc.desktop"

    install -Dm644 tapcalc.png \
        "$pkgdir/usr/share/pixmaps/tapcalc.png"
}
