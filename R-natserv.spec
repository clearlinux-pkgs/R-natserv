#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-natserv
Version  : 0.3.0
Release  : 5
URL      : https://cran.r-project.org/src/contrib/natserv_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/natserv_0.3.0.tar.gz
Summary  : 'NatureServe' Interface
Group    : Development/Tools
License  : MIT
Requires: R-crul
Requires: R-data.table
Requires: R-tibble
Requires: R-vcr
BuildRequires : R-crul
BuildRequires : R-data.table
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : buildreq-R

%description
natserv
=======
[![cran checks](https://cranchecks.info/badges/worst/natserv)](https://cranchecks.info/pkgs/natserv)
[![Build Status](https://travis-ci.org/ropensci/natserv.svg?branch=master)](https://travis-ci.org/ropensci/natserv)
[![Build status](https://ci.appveyor.com/api/projects/status/mvmi4h4jn5ixf3hs?svg=true)](https://ci.appveyor.com/project/sckott/natserv)
[![codecov](https://codecov.io/gh/ropensci/natserv/branch/master/graph/badge.svg)](https://codecov.io/gh/ropensci/natserv)
[![cran version](http://www.r-pkg.org/badges/version/natserv)](https://cran.r-project.org/package=natserv)
[![rstudio mirror downloads](http://cranlogs.r-pkg.org/badges/natserv)](https://github.com/metacran/cranlogs.app)

%prep
%setup -q -c -n natserv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548253465

%install
export SOURCE_DATE_EPOCH=1548253465
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library natserv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library natserv
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library natserv
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library natserv|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/natserv/DESCRIPTION
/usr/lib64/R/library/natserv/INDEX
/usr/lib64/R/library/natserv/LICENSE
/usr/lib64/R/library/natserv/Meta/Rd.rds
/usr/lib64/R/library/natserv/Meta/data.rds
/usr/lib64/R/library/natserv/Meta/features.rds
/usr/lib64/R/library/natserv/Meta/hsearch.rds
/usr/lib64/R/library/natserv/Meta/links.rds
/usr/lib64/R/library/natserv/Meta/nsInfo.rds
/usr/lib64/R/library/natserv/Meta/package.rds
/usr/lib64/R/library/natserv/Meta/vignette.rds
/usr/lib64/R/library/natserv/NAMESPACE
/usr/lib64/R/library/natserv/NEWS.md
/usr/lib64/R/library/natserv/R/natserv
/usr/lib64/R/library/natserv/R/natserv.rdb
/usr/lib64/R/library/natserv/R/natserv.rdx
/usr/lib64/R/library/natserv/data/Rdata.rdb
/usr/lib64/R/library/natserv/data/Rdata.rds
/usr/lib64/R/library/natserv/data/Rdata.rdx
/usr/lib64/R/library/natserv/doc/index.html
/usr/lib64/R/library/natserv/doc/natserv_vignette.Rmd
/usr/lib64/R/library/natserv/doc/natserv_vignette.html
/usr/lib64/R/library/natserv/help/AnIndex
/usr/lib64/R/library/natserv/help/aliases.rds
/usr/lib64/R/library/natserv/help/natserv.rdb
/usr/lib64/R/library/natserv/help/natserv.rdx
/usr/lib64/R/library/natserv/help/paths.rds
/usr/lib64/R/library/natserv/html/00Index.html
/usr/lib64/R/library/natserv/html/R.css
/usr/lib64/R/library/natserv/vign/natserv_vignette.Rmd
