#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-natserv
Version  : 1.0.0
Release  : 26
URL      : https://cran.r-project.org/src/contrib/natserv_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/natserv_1.0.0.tar.gz
Summary  : 'NatureServe' Interface
Group    : Development/Tools
License  : MIT
Requires: R-crul
Requires: R-jsonlite
Requires: R-tibble
Requires: R-vcr
BuildRequires : R-crul
BuildRequires : R-jsonlite
BuildRequires : R-tibble
BuildRequires : R-vcr
BuildRequires : buildreq-R

%description
Includes methods to get data, image metadata, search taxonomic names,
    and make maps.

%prep
%setup -q -c -n natserv
cd %{_builddir}/natserv

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589870962

%install
export SOURCE_DATE_EPOCH=1589870962
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc natserv || :


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
/usr/lib64/R/library/natserv/doc/natserv.Rmd
/usr/lib64/R/library/natserv/doc/natserv.html
/usr/lib64/R/library/natserv/help/AnIndex
/usr/lib64/R/library/natserv/help/aliases.rds
/usr/lib64/R/library/natserv/help/figures/plot.states-1.png
/usr/lib64/R/library/natserv/help/figures/status.map-1.png
/usr/lib64/R/library/natserv/help/natserv.rdb
/usr/lib64/R/library/natserv/help/natserv.rdx
/usr/lib64/R/library/natserv/help/paths.rds
/usr/lib64/R/library/natserv/html/00Index.html
/usr/lib64/R/library/natserv/html/R.css
/usr/lib64/R/library/natserv/tests/fixtures/ns_altid.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_ecohier.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_export.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_export_status.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_id.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_search_comb.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_search_eco.yml
/usr/lib64/R/library/natserv/tests/fixtures/ns_search_spp.yml
/usr/lib64/R/library/natserv/tests/test-all.R
/usr/lib64/R/library/natserv/tests/testthat/helper-natserv.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_altid.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_ecohier.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_export.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_id.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_search_comb.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_search_eco.R
/usr/lib64/R/library/natserv/tests/testthat/test-ns_search_spp.R
/usr/lib64/R/library/natserv/tests/testthat/test-utils.R
