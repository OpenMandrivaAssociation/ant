%bcond_without bootstrap

%global ant_home %{_datadir}/ant
%global major_version 1.8

Name:           ant
Version:        1.10.5
Release:        1
Summary:        Build tool for java
License:        ASL 2.0
URL:            http://ant.apache.org/
Source0:        http://archive.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Patch0:		ant-1.10.5-drop-windows-and-osx-support.patch

# Fix some places where copies of classes are included in the wrong jarfiles
#Patch0:         apache-ant-class-path-in-manifest.patch

BuildRequires:  java-devel >= 0:1.5.0
Requires:       java-devel >= 0:1.5.0

BuildArch:      noarch

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
%if ! %{with bootstrap}
BuildRequires:  antlr
%endif

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
build-jar-repository -s -p lib/optional antlr bcel javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver xalan-j2-serializer xerces-j2 xml-commons-apis
%endif

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

%build
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
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

%if %with javadoc
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

%if %with tests
%check
%{ant} test
%endif

%files
%doc KEYS LICENSE NOTICE README WHATSNEW
%attr(0755,root,root) %{_bindir}/ant
%dir %{_datadir}/ant
%dir %{_datadir}/ant/lib
%{_datadir}/ant/lib/ant.jar
%{_datadir}/ant/lib/ant-launcher.jar

# Some modules get built even in bootstrap mode because of
# prebuilt jars
%files junit
%{_datadir}/ant/lib/ant-junit.jar
%{_datadir}/ant/lib/ant-junit4.jar
%{_datadir}/ant/lib/ant-junitlauncher.jar

%files jmf
%{_datadir}/ant/lib/%{name}-jmf.jar

%files swing
%{_datadir}/ant/lib/%{name}-swing.jar

%files testutil
%{_datadir}/ant/lib/%{name}-testutil.jar

%if ! %{with bootstrap}
%files antlr
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr

%files apache-bsf
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf

%files apache-resolver
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver

%files commons-logging
%defattr(-,root,root,-)
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging

%files commons-net
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net

# Disable as we dont ship the dependencies
%if 0
%files jai
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%endif

%files apache-bcel
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel

%files apache-log4j
%{ant_home}/lib/%{name}-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j

%files apache-oro
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl

%files apache-regexp
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp

%files apache-xalan2
%{ant_home}/lib/%{name}-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2

%files javamail
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail

%files jdepend
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl

%files jsch
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch

%files manual
%doc LICENSE NOTICE
%doc manual/*

%if %with javadoc
%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}
%endif
%endif
