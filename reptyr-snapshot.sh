#!/bin/sh

set -e

if [ -z "$1" ] ; then
    echo "usage: $0 <git-revision>"
    exit 1
fi

gitrev=$1
curdir=$(pwd)
tmpdir=$(mktemp -d)
trap cleanup EXIT
cleanup()
{
    set +e
    [ -z "$tmpdir" -o ! -d "$tmpdir" ] || rm -rf "$tmpdir"
}

release=$(date +%Y%m%d)git$gitrev

cd $tmpdir
git clone git://github.com/nelhage/reptyr.git
cd reptyr
git archive --format=tar --prefix=reptyr-$release/ $gitrev \
| bzip2 --best > $curdir/reptyr-$release.tar.bz2
