#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-misc3d
Version  : 0.9.1
Release  : 36
URL      : https://cran.r-project.org/src/contrib/misc3d_0.9-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/misc3d_0.9-1.tar.gz
Summary  : Miscellaneous 3D Plots
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R
BuildRequires : tcl-dev
BuildRequires : tk-dev

%description
isosurfaces.

%prep
%setup -q -c -n misc3d
cd %{_builddir}/misc3d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641059975

%install
export SOURCE_DATE_EPOCH=1641059975
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library misc3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library misc3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library misc3d
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc misc3d || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/misc3d/CITATION
/usr/lib64/R/library/misc3d/DESCRIPTION
/usr/lib64/R/library/misc3d/INDEX
/usr/lib64/R/library/misc3d/Meta/Rd.rds
/usr/lib64/R/library/misc3d/Meta/data.rds
/usr/lib64/R/library/misc3d/Meta/demo.rds
/usr/lib64/R/library/misc3d/Meta/features.rds
/usr/lib64/R/library/misc3d/Meta/hsearch.rds
/usr/lib64/R/library/misc3d/Meta/links.rds
/usr/lib64/R/library/misc3d/Meta/nsInfo.rds
/usr/lib64/R/library/misc3d/Meta/package.rds
/usr/lib64/R/library/misc3d/NAMESPACE
/usr/lib64/R/library/misc3d/R/misc3d
/usr/lib64/R/library/misc3d/R/misc3d.rdb
/usr/lib64/R/library/misc3d/R/misc3d.rdx
/usr/lib64/R/library/misc3d/data/teapot.rda
/usr/lib64/R/library/misc3d/demo/lighting.R
/usr/lib64/R/library/misc3d/demo/teapot.R
/usr/lib64/R/library/misc3d/help/AnIndex
/usr/lib64/R/library/misc3d/help/aliases.rds
/usr/lib64/R/library/misc3d/help/misc3d.rdb
/usr/lib64/R/library/misc3d/help/misc3d.rdx
/usr/lib64/R/library/misc3d/help/paths.rds
/usr/lib64/R/library/misc3d/html/00Index.html
/usr/lib64/R/library/misc3d/html/R.css
