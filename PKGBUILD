pkgname=archmate
pkgver=2.1
pkgrel=1
pkgdesc="A simple, lightweight, user-friendly tool for managing and configuring Arch Linux systems, written in python."
arch=('x86_64')
url="https://github.com/SharafatKarim/${pkgname}"
license=('MIT')
depends=('python' 'bash')
provides=('amate')
conflicts=('amate')
source=("git+https://github.com/SharafatKarim/archmate.git")
md5sums=('SKIP')

package() {
  install -Dm755 "$srcdir/$pkgname/amate.py" "$pkgdir/usr/bin/amate"
  install -Dm644 "$srcdir/$pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
