# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define _mavenpomdir /usr/share/maven2/poms

%global with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%global without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%global bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%global bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_with bootstrap

%if %with bootstrap
%global build_javadoc        0
%else
%global build_javadoc        1
%endif

%global with_manifest_only 0

%global ant_home %{_datadir}/ant

%global major_version 1.8
%global cvs_version 1.8.2

Name:           ant
Version:        1.8.2
Release:        8
Epoch:          0
Summary:        Build tool for java
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        ASL 2.0
URL:            http://ant.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{cvs_version}-src.tar.bz2
Source2:        apache-ant-%{major_version}.ant.conf

# Fix some places where copies of classes are included in the wrong jarfiles
Patch1:         apache-ant-bz163689.patch
Patch3:         apache-ant-no-test-jar.patch
Patch4:         apache-ant-class-path-in-manifest.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  java-devel >= 0:1.5.0
BuildRequires:  jaxp_transform_impl
BuildRequires:  java-rpmbuild
%if %without bootstrap
BuildRequires:  ant
BuildRequires:  junit
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
%endif

Requires:       jpackage-utils >= 0:1.7.5
Requires:       java-devel >= 0:1.5.0
%if %without bootstrap
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
%endif

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes:      ant-optional < %{version}-%{release}
Provides:       ant-optional = %{version}-%{release}
Obsoletes:      ant-optional-full < %{version}-%{release}
Provides:       ant-optional-full = %{version}-%{release}
# Allow subpackages not in RHEL to be installed from JPackage
Provides:       %{name} = %{version}-%{release}
# RHUG
Obsoletes:      ant-devel < %{version}-%{release}
Provides:       ant-devel = %{version}-%{release}
# Mandriva
Conflicts:      j2sdk-ant
# RHEL3 and FC2
Obsoletes:      %{name}-libs < %{version}-%{release}
Provides:       %{name}-libs = %{version}-%{release}
Obsoletes:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}
Obsoletes:       %{name}-nodeps < %{version}-%{release}
Provides:       %{name}-nodeps = %{version}-%{release}
Obsoletes:      %{name}-trax < %{version}-%{release}
Provides:       %{name}-trax = %{version}-%{release}

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%package jmf
Summary:        Optional jmf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-nodeps = %{version}-%{release}
Provides:       ant-jmf = %{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Provides:       ant-swing = %{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%if %without bootstrap
%if %{with_manifest_only}
%package manifest-only
Summary:        Manifest-only jars for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-icontract = %{version}-%{release}
Provides:       %{name}-netrexx = %{version}-%{release}
Provides:       %{name}-starteam = %{version}-%{release}
Provides:       %{name}-stylebook = %{version}-%{release}
Provides:       %{name}-vaj = %{version}-%{release}
Provides:       %{name}-weblogic = %{version}-%{release}
Provides:       %{name}-xalan1 = %{version}-%{release}
Provides:       %{name}-xslp = %{version}-%{release}

%description  manifest-only
Manifest-only jars for %{name}.
%endif

%package antlr
Summary:        Optional antlr tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       antlr
BuildRequires:  antlr
Provides:       ant-antlr = %{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       bsf
BuildRequires:  bsf
Provides:       ant-apache-bsf = %{version}-%{release}

%description apache-bsf
Optional apache bsf tasks for %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       xml-commons-resolver
BuildRequires:  xml-commons-resolver
Provides:       ant-apache-resolver = %{version}-%{release}

%description apache-resolver
Optional apache resolver tasks for %{name}.


%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jakarta-commons-logging
BuildRequires:  jakarta-commons-logging
Provides:       ant-commons-logging = %{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jakarta-commons-net
BuildRequires:  jakarta-commons-net
Provides:       ant-commons-net = %{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Summary:        Optional jai tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jai
BuildRequires:  jai
Provides:       ant-jai = %{version}-%{release}

%description jai
Optional jai tasks for %{name}.

%endif

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       bcel
BuildRequires:  bcel
Provides:       ant-apache-bcel = %{version}-%{release}
Provides:       ant-jakarta-bcel = %{version}-%{release}
Obsoletes:      ant-jakarta-bcel < %{version}-%{release}

%description apache-bcel
Optional apache bcel tasks for %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       log4j
BuildRequires:  log4j
Provides:       ant-apache-log4j = %{version}-%{release}
Provides:       ant-jakarta-log4j = %{version}-%{release}
Obsoletes:      ant-jakarta-log4j < %{version}-%{release}

%description apache-log4j
Optional apache log4j tasks for %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       oro
BuildRequires:  oro
Provides:       ant-apache-oro = %{version}-%{release}
Provides:       ant-jakarta-oro = %{version}-%{release}
Obsoletes:      ant-jakarta-oro < %{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Provides:       ant-apache-regexp = %{version}-%{release}
Provides:       ant-jakarta-regexp = %{version}-%{release}
Obsoletes:      ant-jakarta-regexp < %{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%package apache-xalan2
Summary:        Optional apache xalan2 tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Provides:       ant-apache-xalan2 = %{version}-%{release}

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       javamail >= 0:1.2-5jpp
BuildRequires:  javamail >= 0:1.2-5jpp
Provides:       ant-javamail = %{version}-%{release}

%description javamail
Optional javamail tasks for %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jdepend
BuildRequires:  jdepend
Provides:       ant-jdepend = %{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jsch
BuildRequires:  jsch
Provides:       ant-jsch = %{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       junit
Requires:       xalan-j2
Provides:       ant-junit = %{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%package testutil
Summary:        Test utility classes for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       junit
Provides:       ant-testutil = %{version}-%{release}

%description testutil
Test utility tasks for %{name}.

%package scripts
Summary:        Additional scripts for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires:       %{name} = %{version}-%{release}
Requires:       perl-base
Requires:       python

%description scripts
Additional Perl and Python scripts for %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%endif

# -----------------------------------------------------------------------------

%prep
%setup -q -n apache-ant-%{cvs_version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//
#https://issues.apache.org/bugzilla/show_bug.cgi?id=47669
sed -i -e "s|IMAGE_FILE_TYPE|BINARY_FILE_TYPE|g" src/main/org/apache/tools/ant/taskdefs/optional/net/FTP.java
# Disable the style and xmlvalidate tasks on ppc64 and s390x (#163689).
%ifarch ppc64 s390x
%patch1 -p1
%endif

# When bootstrapping, we don't have junit
%patch3 -p1

# Fix class-path-in-manifest rpmlint warning
%patch4 -p0

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm

#install jars
%if %without bootstrap
build-jar-repository -s -p lib/optional xerces-j2 xml-commons-jaxp-1.3-apis antlr bcel javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver
%endif

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

# Provides: exclude perl(oata), perl(examples)
cat <<__EOF__ > %{name}-perl.prov
#!/bin/sh
/usr/lib/rpm/perl.prov \$* | grep -v '^perl(oata)$' | grep -v '^perl(examples)$'
__EOF__
%define __perl_provides %{_builddir}/apache-ant-%{cvs_version}/%{name}-perl.prov
chmod +x %{__perl_provides}


# Requires: exclude bogus perl(the)
cat <<__EOF__ > %{name}-perl.req
#!/bin/sh
/usr/lib/rpm/perl.req \$* | grep -v '^perl(the)$'
__EOF__
%define __perl_requires %{_builddir}/apache-ant-%{cvs_version}/%{name}-perl.req
chmod +x %{__perl_requires}

# -----------------------------------------------------------------------------

%build
export OPT_JAR_LIST=:
%if %without bootstrap
%{ant} jars test-jar
%if %{build_javadoc}
export CLASSPATH=$(build-classpath xerces-j2 xml-commons-jaxp-1.3-apis antlr bcel jaf javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver)
%{ant} javadocs
%endif
%else
export JAVA_HOME=%{java_home}
export CLASSPATH=$JAVA_HOME/lib/tools.jar
sh ./build.sh --noconfig jars
%endif

# -----------------------------------------------------------------------------

%install
rm -rf %{buildroot}

# ANT_HOME and subdirs
mkdir -p %{buildroot}%{ant_home}/{lib,etc}

# jars
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms

for jar in build/lib/*.jar
do
  jarname=$(basename $jar .jar)
  pomname="JPP.%{name}-${jarname}.pom"

  #Determine where to put it
  case $jarname in
#These go into %%{_javadir}, pom files have different names
  ant | ant-bootstrap | ant-launcher) destdir=%{buildroot}%{_javadir}; destname="";pomname="JPP-$jarname.pom";;
#Bootstracp builds an incomplete ant-junit, don't ship it
%if %with bootstrap
  ant-junit) continue;;
%endif
#These go into %%{_javadir}/ant
  *) destdir=%{buildroot}%{_javadir}/%{name}; destname="/%{name}";
  esac

  #instal jar
  install -m 644 ${jar} ${destdir}/${jarname}.jar
  # jar aliases
  ln -sf ../../java${destname}/${jarname}.jar %{buildroot}%{ant_home}/lib/${jarname}.jar

  #bootstrap does not have a pom
  [ $jarname == ant-bootstrap ] && continue

  #install pom
  install -m 644 src/etc/poms/${jarname}/pom.xml %{buildroot}%{_datadir}/maven2/poms/${pomname}
  %add_to_maven_depmap org.apache.ant ${jarname} %{version} JPP${destname} ${jarname}
done

#ant-parent pom
install -m 644 src/etc/poms/pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-parent.pom
%add_to_maven_depmap org.apache.ant ant-parent %{version} JPP ant-parent

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl %{buildroot}%{ant_home}/etc

# install everything else
mkdir -p %{buildroot}%{_bindir}
%if %without bootstrap
cp -p src/script/* %{buildroot}%{_bindir}
%else
cp -p src/script/ant{,Run} %{buildroot}%{_bindir}
%endif

# default ant.conf
mkdir -p %{buildroot}%{_sysconfdir}
cp -p %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/%{name}.d
echo "ant/ant-jmf" > %{buildroot}%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-swing" > %{buildroot}%{_sysconfdir}/%{name}.d/swing
%if %without bootstrap
echo "antlr ant/ant-antlr" > %{buildroot}%{_sysconfdir}/%{name}.d/antlr
echo "bsf ant/ant-apache-bsf" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver ant/ant-apache-resolver" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-resolver
echo "jakarta-commons-logging ant/ant-commons-logging" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-logging
echo "jakarta-commons-net ant/ant-commons-net" > %{buildroot}%{_sysconfdir}/%{name}.d/commons-net
#echo "jai ant/ant-jai" > %{buildroot}%%{_sysconfdir}/%%{name}.d/jai
echo "bcel ant/ant-apache-bcel" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j ant/ant-apache-log4j" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant/ant-apache-oro" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-regexp
echo "xalan-j2 ant/ant-apache-xalan2" > %{buildroot}%{_sysconfdir}/%{name}.d/apache-xalan2
echo "javamail jaf ant/ant-javamail" > %{buildroot}%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant/ant-jdepend" > %{buildroot}%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant/ant-jsch" > %{buildroot}%{_sysconfdir}/%{name}.d/jsch
echo "junit ant/ant-junit" > %{buildroot}%{_sysconfdir}/%{name}.d/junit
echo "testutil ant/ant-testutil" > %{buildroot}%{_sysconfdir}/%{name}.d/testutil
%endif

%if %{build_javadoc}
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadocs/* %{buildroot}%{_javadocdir}/%{name}
%endif

# fix link between manual and javadoc
(cd docs/manual; ln -sf %{_javadocdir}/%{name} api)

%if %with bootstrap
find %{buildroot}%{_datadir}/ant/etc -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name coverage-frames.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name mmetrics-frames.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 | xargs -t rm
%endif

%clean
rm -rf %{buildroot}

# -----------------------------------------------------------------------------

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(-,root,root,-)
%doc KEYS LICENSE NOTICE README WHATSNEW
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant
%attr(0755,root,root) %{_bindir}/antRun
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-bootstrap.jar
%dir %{_javadir}/%{name}
%dir %{ant_home}
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%{ant_home}/etc/coverage-frames.xsl
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%if %without bootstrap
%{ant_home}/etc/common2master.xsl
%{ant_home}/etc/printFailingTests.xsl
%endif
%dir %{ant_home}/lib
%{ant_home}/lib/%{name}.jar
%{ant_home}/lib/%{name}-launcher.jar
%{ant_home}/lib/%{name}-bootstrap.jar
%dir %{_sysconfdir}/%{name}.d
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files jmf
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-jmf.jar
%{ant_home}/lib/%{name}-jmf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf

%files swing
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-swing.jar
%{ant_home}/lib/%{name}-swing.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing

%if %without bootstrap
%if %{with_manifest_only}
%files manifest-only
%defattr(-,root,root,-)
%{_javadir}/%{name}/ant-icontract.jar
%{_javadir}/%{name}/ant-netrexx.jar
%{_javadir}/%{name}/ant-starteam.jar
%{_javadir}/%{name}/ant-stylebook.jar
%{_javadir}/%{name}/ant-vaj.jar
%{_javadir}/%{name}/ant-weblogic.jar
%{_javadir}/%{name}/ant-xalan1.jar
%{_javadir}/%{name}/ant-xslp.jar
%endif

%files antlr
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-antlr.jar
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr

%files apache-bsf
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf

%files apache-resolver
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver

%files commons-logging
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging

%files commons-net
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-commons-net.jar
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net

# Disable as we dont ship the dependencies
%if 0
%files jai
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-jai.jar
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%endif

%files apache-bcel
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel

%files apache-log4j
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{ant_home}/lib/%{name}-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j

%files apache-oro
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl

%files apache-regexp
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp

%files apache-xalan2
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-apache-xalan2.jar
%{ant_home}/lib/%{name}-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2

%files javamail
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-javamail.jar
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail

%files jdepend
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-jdepend.jar
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl

%files jsch
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-jsch.jar
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch

%files junit
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-junit.jar
%{ant_home}/lib/%{name}-junit.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl

%files testutil
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-testutil.jar
%{ant_home}/lib/%{name}-testutil.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/testutil

%files scripts
%defattr(-,root,root,-)
%{_bindir}/*.pl
%{_bindir}/*.py*

%files manual
%defattr(-,root,root,-)
%doc docs/*

%if %{build_javadoc}
%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}
%endif
%endif

