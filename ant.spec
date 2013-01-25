%bcond_with bootstrap
# junit4 has lots of build dependencies that in turn need more than the
# bootstrap version of ant.
# Full bootstrap is in 3 steps:
# - ant --with bootstrap --without junit4
# - ant --without bootstrap --without junit4
# - ant --without bootstrap --with-junit4
%bcond_with junit4

%if %with bootstrap
%bcond_with javadoc
%else
%bcond_without javadoc
%endif

%global with_manifest_only 0

%global ant_home %{_datadir}/ant

%global major_version 1.8

Name:           ant
Version:        1.8.4
Release:        2
Epoch:          0
Summary:        Build tool for java
License:        ASL 2.0
URL:            http://ant.apache.org/
Group:          Development/Java
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Source2:        apache-ant-%{major_version}.ant.conf

# Fix some places where copies of classes are included in the wrong jarfiles
Patch1:         apache-ant-bz163689.patch
Patch3:         apache-ant-no-test-jar.patch
Patch4:         apache-ant-class-path-in-manifest.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  java-1.6.0-openjdk-devel
%if %without bootstrap
BuildRequires:  ant
BuildRequires:  junit3
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
%endif

Requires:       jpackage-utils >= 0:1.7.5
Requires:       java-devel >= 0:1.6.0
%if %without bootstrap
Requires:       xerces-j2
%endif

BuildArch:      noarch
# Allow subpackages not in RHEL to be installed from JPackage
Provides:       %{name} = %{epoch}:%{version}-%{release}
#Drop in F-18
Obsoletes:       %{name}-nodeps < %{epoch}:%{version}-%{release}
Provides:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-trax < %{epoch}:%{version}-%{release}
Provides:       %{name}-trax = %{epoch}:%{version}-%{release}

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%package jmf
Summary:        Optional jmf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-nodeps = %{epoch}:%{version}-%{release}
Provides:       ant-jmf = %{epoch}:%{version}-%{release}

%description jmf
Optional jmf tasks for %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-swing = %{epoch}:%{version}-%{release}

%description swing
Optional swing tasks for %{name}.

%if %without bootstrap
%if %{with_manifest_only}
%package manifest-only
Summary:        Manifest-only jars for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       %{name}-icontract = %{epoch}:%{version}-%{release}
Provides:       %{name}-netrexx = %{epoch}:%{version}-%{release}
Provides:       %{name}-starteam = %{epoch}:%{version}-%{release}
Provides:       %{name}-stylebook = %{epoch}:%{version}-%{release}
Provides:       %{name}-vaj = %{epoch}:%{version}-%{release}
Provides:       %{name}-weblogic = %{epoch}:%{version}-%{release}
Provides:       %{name}-xalan1 = %{epoch}:%{version}-%{release}
Provides:       %{name}-xslp = %{epoch}:%{version}-%{release}

%description  manifest-only
Manifest-only jars for %{name}.
%endif

%package antlr
Summary:        Optional antlr tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       antlr
BuildRequires:  antlr-java
Provides:       ant-antlr = %{epoch}:%{version}-%{release}

%description antlr
Optional antlr tasks for %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bsf
BuildRequires:  bsf
Provides:       ant-apache-bsf = %{epoch}:%{version}-%{release}

%description apache-bsf
Optional apache bsf tasks for %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       xml-commons-resolver
BuildRequires:  xml-commons-resolver
Provides:       ant-apache-resolver = %{epoch}:%{version}-%{release}

%description apache-resolver
Optional apache resolver tasks for %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-logging
BuildRequires:  jakarta-commons-logging
Provides:       ant-commons-logging = %{epoch}:%{version}-%{release}

%description commons-logging
Optional commons logging tasks for %{name}.

%package commons-net
Summary:        Optional commons net tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       apache-commons-net
BuildRequires:  apache-commons-net
Provides:       ant-commons-net = %{epoch}:%{version}-%{release}

%description commons-net
Optional commons net tasks for %{name}.

# Disable because we don't ship the dependencies
%if 0
%package jai
Summary:        Optional jai tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jai
BuildRequires:  jai
Provides:       ant-jai = %{epoch}:%{version}-%{release}

%description jai
Optional jai tasks for %{name}.
%endif

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bcel
BuildRequires:  bcel
Provides:       ant-apache-bcel = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-bcel = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-bcel < %{epoch}:%{version}-%{release}

%description apache-bcel
Optional apache bcel tasks for %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       log4j
BuildRequires:  log4j
Provides:       ant-apache-log4j = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-log4j = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-log4j < %{epoch}:%{version}-%{release}

%description apache-log4j
Optional apache log4j tasks for %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jakarta-oro
BuildRequires:  jakarta-oro
Provides:       ant-apache-oro = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-oro = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-oro < %{epoch}:%{version}-%{release}

%description apache-oro
Optional apache oro tasks for %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Provides:       ant-apache-regexp = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-regexp = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-regexp < %{epoch}:%{version}-%{release}

%description apache-regexp
Optional apache regexp tasks for %{name}.

%package apache-xalan2
Summary:        Optional apache xalan2 tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildRequires:  xalan-j2
Requires:       xalan-j2
Provides:       ant-apache-xalan2 = %{epoch}:%{version}-%{release}

%description apache-xalan2
Optional apache xalan2 tasks for %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       javamail >= 0:1.2-5jpp
BuildRequires:  javamail >= 0:1.2-5jpp
Provides:       ant-javamail = %{epoch}:%{version}-%{release}

%description javamail
Optional javamail tasks for %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jdepend
BuildRequires:  jdepend
Provides:       ant-jdepend = %{epoch}:%{version}-%{release}

%description jdepend
Optional jdepend tasks for %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jsch
BuildRequires:  jsch
Provides:       ant-jsch = %{epoch}:%{version}-%{release}

%description jsch
Optional jsch tasks for %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit
Requires:       xalan-j2
Provides:       ant-junit = %{epoch}:%{version}-%{release}

%description junit
Optional junit tasks for %{name}.

%package testutil
Summary:        Test utility classes for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit3
Provides:       ant-testutil = %{epoch}:%{version}-%{release}

%description testutil
Test utility tasks for %{name}.

%package scripts
Summary:        Additional scripts for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{_bindir}/perl
Requires:       %{_bindir}/python

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
%setup -q -n apache-ant-%{version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//
# Disable the style and xmlvalidate tasks on ppc64 and s390x (#163689).
%ifarch ppc64 s390x
%patch1 -p1
%endif

# When bootstrapping, we don't have junit
%patch3 

# Fix class-path-in-manifest rpmlint warning
%patch4

# clean jar files
find . -name "*.jar" | %{_bindir}/xargs -t rm

#install jars
%if %without bootstrap
build-jar-repository -s -p lib/optional xerces-j2 antlr bcel javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver
%endif

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE

%build
export JAVA_HOME=%_prefix/lib/jvm/java-1.6.0/
export CLASSPATH=$JAVA_HOME/lib/tools.jar
%if %without bootstrap
ant jars test-jar
%if %{with javadoc}
export CLASSPATH=$(build-classpath xerces-j2 antlr bcel javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xalan-j2 xml-commons-resolver)
ant javadocs
%endif
%else
sh ./build.sh --noconfig jars
%endif

#remove empty jai and netrexx jars. Due to missing dependencies they contain only manifests.
rm -fr build/lib/ant-jai.jar build/lib/ant-netrexx.jar
# -----------------------------------------------------------------------------

%install
# ANT_HOME and subdirs
mkdir -p $RPM_BUILD_ROOT%{ant_home}/{lib,etc}

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for jar in build/lib/*.jar
do
  jarname=$(basename $jar .jar)
  pomname="JPP.%{name}-${jarname}.pom"

  #Determine where to put it
  case $jarname in
#These go into %%{_javadir}, pom files have different names
  ant | ant-bootstrap | ant-launcher) destdir=$RPM_BUILD_ROOT%{_javadir}; destname="";pomname="JPP-$jarname.pom";;
#Bootstracp builds an incomplete ant-junit, don't ship it
%if %with bootstrap
  ant-junit) continue;;
%endif
#These go into %%{_javadir}/ant
  *) destdir=$RPM_BUILD_ROOT%{_javadir}/%{name}; destname="/%{name}";
  esac

  #instal jar
  install -m 644 ${jar} ${destdir}/${jarname}.jar
  # jar aliases
  ln -sf ../../java${destname}/${jarname}.jar $RPM_BUILD_ROOT%{ant_home}/lib/${jarname}.jar

  #bootstrap does not have a pom
  [ $jarname == ant-bootstrap ] && continue

  #install pom
  install -m 644 src/etc/poms/${jarname}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/${pomname}
  %add_to_maven_depmap org.apache.ant ${jarname} %{version} JPP${destname} ${jarname}
done

# add backward compatibility for nodeps jar that is now part of
# main jar
%add_to_maven_depmap org.apache.ant ant-nodeps %{version} JPP ant

#ant-parent pom
install -m 644 src/etc/poms/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-parent.pom
%add_to_maven_depmap org.apache.ant ant-parent %{version} JPP ant-parent

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl $RPM_BUILD_ROOT%{ant_home}/etc

# install everything else
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%if %without bootstrap
cp -p src/script/* $RPM_BUILD_ROOT%{_bindir}
%else
cp -p src/script/ant{,Run} $RPM_BUILD_ROOT%{_bindir}
%endif

# default ant.conf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d
echo "ant/ant-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
%if %without bootstrap
echo "antlr ant/ant-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
echo "bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
echo "apache-commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
echo "apache-commons-net ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
#echo "jai ant/ant-jai" > $RPM_BUILD_ROOT%%{_sysconfdir}/%%{name}.d/jai
echo "bcel ant/ant-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j ant/ant-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant/ant-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
echo "xalan-j2 xalan-j2-serializer ant/ant-apache-xalan2" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-xalan2
echo "javamail jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant/ant-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
echo "jsch ant/ant-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
echo "junit ant/ant-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
%if %with junit4
echo "junit ant/ant-junit4" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit4
%endif
echo "testutil ant/ant-testutil" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/testutil
%endif

%if %{with javadoc}
# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%endif

# fix link between manual and javadoc
(cd manual; ln -sf %{_javadocdir}/%{name} api)

%if %with bootstrap
find $RPM_BUILD_ROOT%{_datadir}/ant/etc -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name coverage-frames.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name mmetrics-frames.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 | xargs -t rm
%endif

# Delete bogus jars that were built, but are dummies because we lack
# a build dependency
cd %buildroot%_javadir/ant
for i in *; do
	if [ `jar tf $i |grep -v META-INF |wc -l` -eq 0 ]; then
		rm -f $i
		rm -f %buildroot%ant_home/lib/$i
	fi
done

%files
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
%{_javadir}/%{name}/%{name}-jmf.jar
%{ant_home}/lib/%{name}-jmf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf

%files swing
%{_javadir}/%{name}/%{name}-swing.jar
%{ant_home}/lib/%{name}-swing.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing

%if %without bootstrap
%if %{with_manifest_only}
%files manifest-only
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
%{_javadir}/%{name}/%{name}-antlr.jar
%{ant_home}/lib/%{name}-antlr.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr

%files apache-bsf
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{ant_home}/lib/%{name}-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf

%files apache-resolver
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{ant_home}/lib/%{name}-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver

%files commons-logging
%defattr(-,root,root,-)
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{ant_home}/lib/%{name}-commons-logging.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging

%files commons-net
%{_javadir}/%{name}/%{name}-commons-net.jar
%{ant_home}/lib/%{name}-commons-net.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net

# Disable as we dont ship the dependencies
%if 0
%files jai
%{_javadir}/%{name}/%{name}-jai.jar
%{ant_home}/lib/%{name}-jai.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jai
%endif

%files apache-bcel
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{ant_home}/lib/%{name}-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel

%files apache-log4j
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{ant_home}/lib/%{name}-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j

%files apache-oro
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{ant_home}/lib/%{name}-apache-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl

%files apache-regexp
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{ant_home}/lib/%{name}-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp

%files apache-xalan2
%{_javadir}/%{name}/%{name}-apache-xalan2.jar
%{ant_home}/lib/%{name}-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-xalan2

%files javamail
%{_javadir}/%{name}/%{name}-javamail.jar
%{ant_home}/lib/%{name}-javamail.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail

%files jdepend
%{_javadir}/%{name}/%{name}-jdepend.jar
%{ant_home}/lib/%{name}-jdepend.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl

%files jsch
%{_javadir}/%{name}/%{name}-jsch.jar
%{ant_home}/lib/%{name}-jsch.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch

%files junit
%{_javadir}/%{name}/%{name}-junit.jar
%{ant_home}/lib/%{name}-junit.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%if %with junit4
%{_javadir}/%{name}/%{name}-junit4.jar
%{ant_home}/lib/%{name}-junit4.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit4
%endif
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl

%files testutil
%{_javadir}/%{name}/%{name}-testutil.jar
%{ant_home}/lib/%{name}-testutil.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/testutil

%files scripts
%attr(0755,root,root) %{_bindir}/*.pl
%attr(0755,root,root) %{_bindir}/*.py*

%files manual
%doc manual/*

%if %{with javadoc}
%files javadoc
%{_javadocdir}/%{name}
%endif
%endif

# -----------------------------------------------------------------------------
