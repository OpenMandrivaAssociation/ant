%bcond_without bootstrap
# Bootstrapping jpackage stuff is a giant mess. Ant can be built without it,
# but then doesn't provide all the mvn(*) dependencies jpackage is so fond
# of.
%bcond_with jpackage
# Optional dependencies...
%bcond_without antlr

%global ant_home %{_datadir}/ant
%global major_version 1.8

Name:           ant
Version:        1.10.15
Release:        1
Summary:        Build tool for java
License:        ASL 2.0
URL:            https://ant.apache.org/
Source0:        http://archive.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Patch0:		ant-1.10.5-drop-windows-and-osx-support.patch
# Avoids dependency on junit while bootstrapping
Patch1:		ant-1.10.5-no-test-jar.patch

# Fix some places where copies of classes are included in the wrong jarfiles
#Patch0:         apache-ant-class-path-in-manifest.patch

BuildRequires:  jdk-current >= 12.33-5

BuildArch:      noarch

%if %{with jpackage}
BuildRequires:	javapackages-local
%endif
%if %{with antlr}
BuildRequires:  antlr antlr-tool
%endif
%if ! %{with bootstrap}
BuildRequires:	junit
%endif

BuildRequires:	locales-extra-charsets

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%package jmf
Summary:        Optional jmf tasks for %{name}
Requires:       %{name} = %{EVRD}

%description jmf
Optional jmf tasks for %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Requires:       %{name} = %{EVRD}

%description swing
Optional swing tasks for %{name}.

%package antlr
Summary:        Optional antlr tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       antlr

%description antlr
Optional antlr tasks for %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       bsf
%if ! %{with bootstrap}
BuildRequires:  bsf
%endif

%description apache-bsf
Optional apache bsf tasks for %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       xml-commons-resolver
%if ! %{with bootstrap}
BuildRequires:  xml-commons-resolver
%endif

%description apache-resolver
Optional apache resolver tasks for %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       apache-commons-logging
%if ! %{with bootstrap}
BuildRequires:  apache-commons-logging
%endif

%description commons-logging
Optional commons logging tasks for %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       apache-commons-net
%if ! %{with bootstrap}
BuildRequires:  apache-commons-net
%endif

%description commons-net
Optional commons net tasks for %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Summary:        Optional jai tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       jai
%if ! %{with bootstrap}
BuildRequires:  jai
%endif

%description jai
Optional jai tasks for %{name}.
%endif

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       bcel
%if ! %{with bootstrap}
BuildRequires:  bcel
%endif

%description apache-bcel
Optional apache bcel tasks for %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       log4j
%if ! %{with bootstrap}
BuildRequires:  log4j
%endif

%description apache-log4j
Optional apache log4j tasks for %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       jakarta-oro
%if ! %{with bootstrap}
BuildRequires:  jakarta-oro
%endif

%description apache-oro
Optional apache oro tasks for %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       regexp
%if ! %{with bootstrap}
BuildRequires:  regexp
%endif

%description apache-regexp
Optional apache regexp tasks for %{name}.

%package apache-xalan2
Summary:        Optional apache xalan2 tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       regexp
%if ! %{with bootstrap}
BuildRequires:  regexp
%endif
Requires:       xalan-j2

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       javamail >= 0:1.2-5jpp
%if ! %{with bootstrap}
BuildRequires:  javamail >= 0:1.2-5jpp
%endif

%description javamail
Optional javamail tasks for %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       jdepend
%if ! %{with bootstrap}
BuildRequires:  jdepend
%endif

%description jdepend
Optional jdepend tasks for %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       jsch
%if ! %{with bootstrap}
BuildRequires:  jsch
%endif

%description jsch
Optional jsch tasks for %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Requires:       %{name} = %{EVRD}
Requires:       junit
Requires:       xalan-j2

%description junit
Optional junit tasks for %{name}.

%package testutil
Summary:        Test utility classes for %{name}
Requires:       %{name} = %{EVRD}
Requires:       junit

%description testutil
Test utility tasks for %{name}.

%package manual
Summary:        Manual for %{name}

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

# -----------------------------------------------------------------------------

%prep
%autosetup -p1 -n apache-ant-%{version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//

%if ! %{with bootstrap}
# During bootstrap, we have to rely on some prebuilt jars.
# We'll get rid of them when not bootstrapping.
find . -name "*.jar" | %{_bindir}/xargs -t rm
%endif

%if 0
# failing testcases. TODO see why
rm src/tests/junit/org/apache/tools/ant/types/selectors/SignedSelectorTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsFileSelectedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/condition/IsSignedTest.java \
   src/tests/junit/org/apache/tools/ant/taskdefs/JarTest.java \
   src/tests/junit/org/apache/tools/mail/MailMessageTest.java
%endif

%if ! %{with bootstrap}
#install jars
DEPS="bcel jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver xalan-j2-serializer xerces-j2 xml-commons-apis"
%if %{with antlr}
DEPS="antlr $DEPS"
%endif
# DEPS="$DEPS javamail/mailapi"
build-jar-repository -s -p lib/optional $DEPS
%endif

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-15 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-15 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

%build
. /etc/profile.d/90java.sh
./bootstrap.sh
./build.sh

# ant builds a number of plugins that are empty (except for manifests) rather
# than missing if dependencies aren't there. Let's get rid of those, better
# to have a hard build failure than to package non-working crap!
for i in dist/lib/*.jar; do
	jar tf $i |grep -q .class || rm -f $i
done


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/ant/lib
cp dist/bin/ant %{buildroot}%{_bindir}
cp dist/lib/*.jar %{buildroot}%{_datadir}/ant/lib

%if %{with jpackage}
%mvn_alias :ant org.apache.ant:ant-nodeps apache:ant ant:ant
%mvn_alias :ant-launcher ant:ant-launcher
%mvn_file ':%{ant,ant-bootstrap,ant-launcher}' %{name}/@1 @1

for jar in dist/lib/*.jar; do
	jarname=$(basename $jar .jar)
	pom=src/etc/poms/${jarname}/pom.xml
	[ "$jarname" == ant-bootstrap ] && pom='org.apache.ant:ant-bootstrap:%{version}'
echo ${pom} ${jar}
	%mvn_artifact ${pom} ${jar}
done

# ant-parent
%mvn_artifact src/etc/poms/pom.xml

%mvn_package :ant lib
%mvn_package :ant-launcher lib
%mvn_package :ant-bootstrap lib
%mvn_package :ant-parent lib
%mvn_package :ant-junit4 junit
%mvn_package ':ant-{*}' @1
# FIXME workaround until fixed xmvn has been bootstrapped correctly
pwd
ls -l .xmvn-reactor
while grep -q ns0:optional .xmvn-reactor; do sed -i -e '/ns0:optional/d' .xmvn-reactor; done
%mvn_install
%endif

%if %with javadoc
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

%if %with tests
%check
%{ant} test
%endif

%if %{with jpackage}
%files -f .mfiles-lib
%else
%files
%endif
%doc KEYS LICENSE NOTICE README WHATSNEW
%attr(0755,root,root) %{_bindir}/ant
%dir %{_datadir}/ant
%dir %{_datadir}/ant/lib
%{_datadir}/ant/lib/ant.jar
%{_datadir}/ant/lib/ant-imageio.jar
%{_datadir}/ant/lib/ant-launcher.jar

# Some modules get built even in bootstrap mode because of
# prebuilt jars
%if %{with jpackage}
%files junit -f .mfiles-junit
%else
%files junit
%endif
%{_datadir}/ant/lib/ant-junitlauncher.jar
%{_datadir}/ant/lib/ant-junit.jar
%{_datadir}/ant/lib/ant-junit4.jar

%if %{with jpackage}
%files jmf -f .mfiles-jmf
%else
%files jmf
%endif
%{_datadir}/ant/lib/%{name}-jmf.jar

%if %{with jpackage}
%files swing -f .mfiles-swing
%else
%files swing
%endif
%{_datadir}/ant/lib/%{name}-swing.jar

%if 0
%files testutil -f .mfiles-testutil
%{_datadir}/ant/lib/%{name}-testutil.jar
%endif

%if ! %{with bootstrap}
%if %{with antlr}
%files antlr -f .mfiles-antlr
%{ant_home}/lib/%{name}-antlr.jar
%endif

%files apache-bsf -f .mfiles-apache-bsf
%{ant_home}/lib/%{name}-apache-bsf.jar

%files apache-resolver -f .mfiles-apache-resolver
%{ant_home}/lib/%{name}-apache-resolver.jar

%files commons-logging -f .mfiles-commons-logging
%defattr(-,root,root,-)
%{ant_home}/lib/%{name}-commons-logging.jar

%files commons-net -f .mfiles-commons-net
%{ant_home}/lib/%{name}-commons-net.jar

# Disable as we dont ship the dependencies
%if 0
%files jai -f .mfiles-jai
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%endif

%files apache-bcel -f .mfiles-apache-bcel
%{ant_home}/lib/%{name}-apache-bcel.jar

%files apache-log4j -f .mfiles-apache-log4j
%{ant_home}/lib/%{name}-apache-log4j.jar

%files apache-oro -f .mfiles-apache-oro
%{ant_home}/lib/%{name}-apache-oro.jar

%files apache-regexp -f .mfiles-apache-regexp
%{ant_home}/lib/%{name}-apache-regexp.jar

%files apache-xalan2 -f .mfiles-apache-xalan2
%{ant_home}/lib/%{name}-apache-xalan2.jar

%if 0
%files javamail -f .mfiles-javamail
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail
%endif

%files jdepend -f .mfiles-jdepend
%{ant_home}/lib/%{name}-jdepend.jar

%files jsch -f .mfiles-jsch
%{ant_home}/lib/%{name}-jsch.jar

%files manual
%doc LICENSE NOTICE
%doc manual/*

%if %with javadoc
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}
%endif
%endif
