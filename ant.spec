%bcond_with                  bootstrap

%define gcj_support          1
%define ant_home             %{_datadir}/ant
%define section              free
%define build_javadoc        1

%if %with bootstrap
%define build_javadoc        0
%endif

Name:           ant
Version:        1.7.0
Release:        %mkrel 3.3.9
Epoch:          0
Summary:        Ant build tool for java
Summary(it):    Tool per la compilazione di programmi java
Summary(fr):    Outil de compilation pour java
License:        Apache License
URL:            http://ant.apache.org/
Group:          Development/Java
#Vendor:        JPackage Project
#Distribution:  JPackage
Source0:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2
Source1:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2.asc
Source2:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2.md5
Source3:        http://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.bz2.sha1
# Ant configuration file which is edited when each optional subpackage
# is installed/uninstalled
Source4:        apache-ant-1.7.0.ant.conf
Patch0:         apache-ant-1.7.0-rpmmode.patch
Patch1:         apache-ant-1.7.0-native2ascii.patch
# javah: BZ 157750
# https://www.zarb.org/pipermail/jpackage-discuss/2005-September/008781.html
# https://www.zarb.org/pipermail/jpackage-discuss/2005-September/008785.html
# Message-ID: <432A8E37.8050101@zarb.org>
Patch2:         apache-ant-1.7.0-javah.patch
# Fix some places where copies of classes are included in the wrong jarfiles
Patch4:         apache-ant-jars.patch
Requires:       xerces-j2
#Requires:       jaxp_parser_impl
Requires:       jpackage-utils >= 0:1.5
%if %without bootstrap
Requires:       xml-commons-jaxp-1.3-apis
%endif
#BuildRequires:  jaxp_parser_impl
BuildRequires:  xerces-j2
BuildRequires:  java-rpmbuild >= 0:1.5
%if %without bootstrap
BuildRequires:  ant
BuildRequires:  xml-commons-jaxp-1.3-apis
%else
BuildRequires:  junit
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:      ant-optional < %{epoch}:%{version}-%{release}
Provides:       ant-optional = %{epoch}:%{version}-%{release}
Obsoletes:      ant-optional-clean < %{epoch}:%{version}-%{release}
Provides:       ant-optional-clean = %{epoch}:%{version}-%{release}
Obsoletes:      ant-optional-full < %{epoch}:%{version}-%{release}
Provides:       ant-optional-full = %{epoch}:%{version}-%{release}
# RHEL3 and FC2
Obsoletes:      %{name}-libs < %{epoch}:%{version}-%{release}, %{name}-core < %{epoch}:%{version}-%{release}
Provides:       %{name}-libs = %{epoch}:%{version}-%{release}
Provides:       %{name}-core = %{epoch}:%{version}-%{release}
# Mandriva
Obsoletes:      j2sdk-ant < %{epoch}:%{version}-%{release}
Provides:       j2sdk-ant = %{epoch}:%{version}-%{release}
# libgcj aot-compiled native libraries
%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel >= 0:1.0.31
%else
BuildRequires:  java-devel
BuildArch:      noarch
%endif
Requires:	java-devel
Obsoletes:      ant-bootstrap < %{epoch}:%{version}-%{release}
Provides:       ant-bootstrap = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jai < %{epoch}:%{version}-%{release}
Provides:       ant-jai = %{epoch}:%{version}-%{release}
Obsoletes:      ant-manifest-only < %{epoch}:%{version}-%{release}
Provides:       ant-manifest-only = %{epoch}:%{version}-%{release}

%description
Ant is a platform-independent build tool for java. It's used by apache
jakarta and xml projects.

%description -l fr
Ant est un outil de compilation multi-plateformes pour java. Il est
utilisé par les projets apache-jakarta et apache-xml.

%description -l it
Ant e' un tool indipendente dalla piattaforma creato per faciltare la
compilazione di programmi java.
Allo stato attuale viene utilizzato dai progetti apache jakarta ed
apache xml.

%if %without bootstrap
%package antlr
Summary:        Optional antlr tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       antlr
BuildRequires:  antlr
Provides:       ant-antlr = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description antlr
Optional antlr tasks for %{name}.

%description antlr -l fr
Taches antlr optionelles pour %{name}.

%package apache-bsf
Summary:        Optional apache bsf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bsf
BuildRequires:  bsf
Provides:       ant-apache-bsf = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-bsf
Optional apache bsf tasks for %{name}.

%description apache-bsf -l fr
Taches apache bsf optionelles pour %{name}.

%package apache-resolver
Summary:        Optional apache resolver tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       xml-commons-resolver12
BuildRequires:  xml-commons-resolver12
Provides:       ant-apache-resolver = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-resolver
Optional apache resolver tasks for %{name}.

%description apache-resolver -l fr
Taches apache resolver optionelles pour %{name}.

%package commons-logging
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-logging
BuildRequires:  jakarta-commons-logging
Provides:       ant-commons-logging = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description commons-logging
Optional commons logging tasks for %{name}.

%description commons-logging -l fr
Taches commons logging optionelles pour %{name}.

%package commons-net
Summary:        Optional commons logging tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jakarta-commons-net
BuildRequires:  jakarta-commons-net
Provides:       ant-commons-net = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description commons-net
Optional commons net tasks for %{name}.

%description commons-net -l fr
Taches commons net optionelles pour %{name}.

%package apache-bcel
Summary:        Optional apache bcel tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       bcel
BuildRequires:  bcel
Provides:       ant-apache-bcel = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-bcel = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-bcel < %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-bcel
Optional apache bcel tasks for %{name}.

%description apache-bcel -l fr
Taches apache bcel optionelles pour %{name}.

%package apache-log4j
Summary:        Optional apache log4j tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       log4j
BuildRequires:  log4j
Provides:       ant-apache-log4j = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-log4j = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-log4j < %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-log4j
Optional apache log4j tasks for %{name}.

%description apache-log4j -l fr
Taches apache log4j optionelles pour %{name}.

%package apache-oro
Summary:        Optional apache oro tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       oro
BuildRequires:  oro
Provides:       ant-apache-oro = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-oro = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-oro < %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-oro
Optional apache oro tasks for %{name}.

%description apache-oro -l fr
Taches apache oro optionelles pour %{name}.

%package apache-regexp
Summary:        Optional apache regexp tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       regexp
BuildRequires:  regexp
Provides:       ant-apache-regexp = %{epoch}:%{version}-%{release}
Provides:       ant-jakarta-regexp = %{epoch}:%{version}-%{release}
Obsoletes:      ant-jakarta-regexp < %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description apache-regexp
Optional apache regexp tasks for %{name}.

%description apache-regexp -l fr
Taches apache regexp optionelles pour %{name}.

%package javamail
Summary:        Optional javamail tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       geronimo-javamail-1.3.1-api
Requires:       geronimo-jaf-1.0.2-api
BuildRequires:  geronimo-javamail-1.3.1-api
BuildRequires:  geronimo-jaf-1.0.2-api
Provides:       ant-javamail = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description javamail
Optional javamail tasks for %{name}.

%description javamail -l fr
Taches javamail optionelles pour %{name}.

%package jdepend
Summary:        Optional jdepend tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jdepend
BuildRequires:  jdepend
Provides:       ant-jdepend = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description jdepend
Optional jdepend tasks for %{name}.

%description jdepend -l fr
Taches jdepend optionelles pour %{name}.

%package jmf
Summary:        Optional jmf tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-jmf = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description jmf
Optional jmf tasks for %{name}.

%description jmf -l fr
Taches jmf optionelles pour %{name}.

%package jsch
Summary:        Optional jsch tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jsch
BuildRequires:  jsch
Provides:       ant-jsch = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description jsch
Optional jsch tasks for %{name}.

%description jsch -l fr
Taches jsch optionelles pour %{name}.

%package junit
Summary:        Optional junit tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       junit
BuildRequires:  junit
Provides:       ant-junit = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description junit
Optional junit tasks for %{name}.

%description junit -l fr
Taches junit optionelles pour %{name}.

%package nodeps
Summary:        Optional tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-nodeps = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description nodeps
Optional tasks for %{name}.

%description nodeps -l fr
Taches optionelles pour %{name}.

%package swing
Summary:        Optional swing tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Provides:       ant-swing = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description swing
Optional swing tasks for %{name}.

%description swing -l fr
Taches swing optionelles pour %{name}.

%package trax
Summary:        Optional trax tasks for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jaxp_transform_impl
Provides:       ant-trax = %{epoch}:%{version}-%{release}
# The ant-xalan jar has been merged into the ant-trax one
Obsoletes:      ant-xalan2 < %{epoch}:%{version}-%{release}
Provides:       ant-xalan2 = %{epoch}:%{version}-%{release}
#Conflicts:      ant-optional-clean, ant-optional-full

%description trax
Optional trax tasks for %{name}.

%description trax -l fr
Taches trax optionelles pour %{name}.

%package scripts
Summary:        Additional scripts for %{name}
Group:          Development/Java
AutoReqProv:    no
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       perl-base
Requires:       /usr/bin/python

%description scripts
Additional Perl and Python scripts for %{name}.

%description scripts -l fr
Scripts additionels pour %{name}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Java

%description manual
Documentation for %{name}.

%description manual -l it
Documentazione di %{name}.

%description manual -l fr
Documentation pour %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.
%endif

%prep
%setup -q -n apache-ant-%{version}

# Set rpm_mode=true by default
%patch0 -p1
# fix GNU Native2ASCII location
%patch1 -p1
# https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=157750
# #157750: make the javah task work with java-gcj-compat
%patch2 -p1
# Fix some places where copies of classes are included in the wrong jarfiles
%patch4 -p1

# clean jar files
%{_bindir}/find . -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%build
# classpath selects optional components to build
perl -pi -e 's|1.2|1.4|g' build.xml

# create javah task
cp src/main/org/apache/tools/ant/taskdefs/optional/javah/Kaffeh.java src/main/org/apache/tools/ant/taskdefs/optional/javah/MyJavah.java
perl -pi -e 's|kaffeh|javah|g' src/main/org/apache/tools/ant/taskdefs/optional/javah/MyJavah.java
perl -pi -e 's|Kaffeh|MyJavah|g' src/main/org/apache/tools/ant/taskdefs/optional/javah/MyJavah.java

export OPT_JAR_LIST=:
%if %without bootstrap
export CLASSPATH=$(build-classpath xerces-j2 xml-commons-jaxp-1.3-apis antlr bcel jaf javamail/mailapi jdepend junit log4j oro regexp bsf commons-logging commons-net jsch xml-commons-resolver12)
%{ant} jars
%if %{build_javadoc}
%{ant} javadocs
%endif
%else
export JAVA_HOME=%{java_home}
export CLASSPATH=$JAVA_HOME/lib/tools.jar:$(build-classpath junit)
sh ./build.sh --noconfig jars
%endif

%install
rm -rf $RPM_BUILD_ROOT

# ANT_HOME and subdirs
mkdir -p $RPM_BUILD_ROOT%{ant_home}/{lib,etc}

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/lib/ant.jar $RPM_BUILD_ROOT%{_javadir}/ant-%{version}.jar
cp -p build/lib/ant-launcher.jar $RPM_BUILD_ROOT%{_javadir}/ant-launcher-%{version}.jar

# optional jars
%if %without bootstrap
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -p build/lib/%{name}-antlr.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
cp -p build/lib/%{name}-apache-bsf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
cp -p build/lib/%{name}-apache-resolver.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
cp -p build/lib/%{name}-commons-logging.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
cp -p build/lib/%{name}-commons-net.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
cp -p build/lib/%{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
cp -p build/lib/%{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
cp -p build/lib/%{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
cp -p build/lib/%{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
ln -sf %{name}-apache-bcel.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
ln -sf %{name}-apache-log4j.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
ln -sf %{name}-apache-oro.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-oro.jar
ln -sf %{name}-apache-regexp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
cp -p build/lib/%{name}-javamail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
cp -p build/lib/%{name}-jdepend.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
cp -p build/lib/%{name}-jmf.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
cp -p build/lib/%{name}-jsch.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
cp -p build/lib/%{name}-junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-junit-%{version}.jar
cp -p build/lib/%{name}-nodeps.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
cp -p build/lib/%{name}-swing.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swing-%{version}.jar
cp -p build/lib/%{name}-trax.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-trax-%{version}.jar
%endif

# jar aliases
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/ant && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

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
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/ant.conf

# OPT_JAR_LIST fragments
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
%if %without bootstrap
echo "antlr ant/ant-antlr" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/antlr
echo "bsf ant/ant-apache-bsf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bsf
echo "xml-commons-resolver12 ant/ant-apache-resolver" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-resolver
echo "jakarta-commons-logging ant/ant-commons-logging" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-logging
echo "jakarta-commons-net ant/ant-commons-net" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/commons-net
echo "bcel ant/ant-apache-bcel" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-bcel
echo "log4j ant/ant-apache-log4j" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-log4j
echo "oro ant/ant-apache-oro" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-oro
echo "regexp ant/ant-apache-regexp" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/apache-regexp
echo "javamail jaf ant/ant-javamail" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/javamail
echo "jdepend ant/ant-jdepend" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jdepend
echo "ant/ant-jmf" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jmf
echo "jsch ant/ant-jsch" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/jsch
echo "junit ant/ant-junit" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/junit
echo "ant/ant-nodeps" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/nodeps
echo "ant/ant-swing" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/swing
echo "jaxp_transform_impl ant/ant-trax xalan-j2-serializer" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.d/trax
%endif

# javadoc
%if %{build_javadoc}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
%endif

# fix link between manual and javadoc
(cd docs/manual; ln -sf %{_javadocdir}/ant-%{version} api)

%if %with bootstrap
find $RPM_BUILD_ROOT%{_datadir}/ant/etc -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 -exec rm -f {} \;
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%pre
rm -f %{_javadir}/ant.jar
rm -f %{_javadir}/ant-optional.jar

%if %without bootstrap
%post
%if %{gcj_support}
%{update_gcjdb}

%postun
%{clean_gcjdb}

%post antlr
%{update_gcjdb}

%postun antlr
%{clean_gcjdb}

%post apache-bsf
%{update_gcjdb}

%postun apache-bsf
%{clean_gcjdb}

%post apache-resolver
%{update_gcjdb}

%postun apache-resolver
%{clean_gcjdb}

%post commons-logging
%{update_gcjdb}

%postun commons-logging
%{clean_gcjdb}

%post commons-net
%{update_gcjdb}

%postun commons-net
%{clean_gcjdb}

%post apache-bcel
%{update_gcjdb}

%postun apache-bcel
%{clean_gcjdb}

%post apache-log4j
%{update_gcjdb}

%postun apache-log4j
%{clean_gcjdb}

%post apache-oro
%{update_gcjdb}

%postun apache-oro
%{clean_gcjdb}

%post apache-regexp
%{update_gcjdb}

%postun apache-regexp
%{clean_gcjdb}

%if 0
%post javamail
%{update_gcjdb}

%postun javamail
%{clean_gcjdb}

%post jdepend
%{update_gcjdb}

%postun jdepend
%{clean_gcjdb}

%post jmf
%{update_gcjdb}

%postun jmf
%{clean_gcjdb}

%post jsch
%{update_gcjdb}

%postun jsch
%{clean_gcjdb}

%post junit
%{update_gcjdb}

%postun junit
%{clean_gcjdb}

%post nodeps
%{update_gcjdb}

%postun nodeps
%{clean_gcjdb}

%post swing
%{update_gcjdb}

%postun swing
%{clean_gcjdb}

%post trax
%{update_gcjdb}

%postun trax
%{clean_gcjdb}
%endif
%endif

%if %{build_javadoc}
%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi
%endif
%endif

%files
%defattr(0644,root,root,0755)
%doc KEYS LICENSE NOTICE README WHATSNEW
%config(noreplace) %{_sysconfdir}/ant.conf
%attr(0755,root,root) %{_bindir}/ant
%attr(0755,root,root) %{_bindir}/antRun
%{_javadir}/ant.jar
%{_javadir}/ant-launcher.jar
%{_javadir}/ant-%{version}.jar
%{_javadir}/ant-launcher-%{version}.jar
%dir %{ant_home}
%dir %{ant_home}/etc
%{ant_home}/etc/ant-update.xsl
%{ant_home}/etc/changelog.xsl
%if %without bootstrap
%{ant_home}/etc/common2master.xsl
%endif
%{ant_home}/etc/log.xsl
%{ant_home}/etc/tagdiff.xsl
%{ant_home}/etc/junit-frames-xalan1.xsl
%dir %{ant_home}/lib
%dir %config(noreplace) %{_sysconfdir}/ant.d
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-%{version}.jar.*
%attr(-,root,root) %{_libdir}/gcj/%{name}/ant-launcher-%{version}.jar.*

%if %without bootstrap
%files antlr
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-antlr.jar
%{_javadir}/%{name}/%{name}-antlr-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/antlr
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-antlr-%{version}.jar.*
%endif

%files apache-bsf
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-bsf.jar
%{_javadir}/%{name}/%{name}-apache-bsf-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bsf
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-bsf-%{version}.jar.*
%endif

%files apache-resolver
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-resolver.jar
%{_javadir}/%{name}/%{name}-apache-resolver-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-resolver
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-resolver-%{version}.jar.*
%endif

%files commons-logging
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-commons-logging.jar
%{_javadir}/%{name}/%{name}-commons-logging-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-logging
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-commons-logging-%{version}.jar.*
%endif

%files commons-net
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-commons-net.jar
%{_javadir}/%{name}/%{name}-commons-net-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/commons-net
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-commons-net-%{version}.jar.*
%endif

%files apache-bcel
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-bcel.jar
%{_javadir}/%{name}/%{name}-apache-bcel-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-bcel.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-bcel
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-bcel-%{version}.jar.*
%endif

%files apache-log4j
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-log4j.jar
%{_javadir}/%{name}/%{name}-apache-log4j-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-log4j.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-log4j
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-log4j-%{version}.jar.*
%endif

%files apache-oro
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-oro.jar
%{_javadir}/%{name}/%{name}-apache-oro-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-oro.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-oro
%{ant_home}/etc/maudit-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-oro-%{version}.jar.*
%endif

%files apache-regexp
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-apache-regexp.jar
%{_javadir}/%{name}/%{name}-apache-regexp-%{version}.jar
%{_javadir}/%{name}/%{name}-jakarta-regexp.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/apache-regexp
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-apache-regexp-%{version}.jar.*
%endif

%files javamail
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-javamail.jar
%{_javadir}/%{name}/%{name}-javamail-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/javamail
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-javamail-%{version}.jar.*
%endif

%files jdepend
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jdepend.jar
%{_javadir}/%{name}/%{name}-jdepend-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jdepend
%{ant_home}/etc/jdepend.xsl
%{ant_home}/etc/jdepend-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jdepend-%{version}.jar.*
%endif

%files jmf
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jmf.jar
%{_javadir}/%{name}/%{name}-jmf-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jmf
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jmf-%{version}.jar.*
%endif

%files jsch
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-jsch.jar
%{_javadir}/%{name}/%{name}-jsch-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/jsch
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-jsch-%{version}.jar.*
%endif

%files junit
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-junit.jar
%{_javadir}/%{name}/%{name}-junit-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/junit
%{ant_home}/etc/junit-frames.xsl
%{ant_home}/etc/junit-noframes.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-junit-%{version}.jar.*
%endif

%files nodeps
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-nodeps.jar
%{_javadir}/%{name}/%{name}-nodeps-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/nodeps
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-nodeps-%{version}.jar.*
%endif

%files swing
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-swing.jar
%{_javadir}/%{name}/%{name}-swing-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/swing
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-swing-%{version}.jar.*
%endif

%files trax
%defattr(0644,root,root,0755)
%{_javadir}/%{name}/%{name}-trax.jar
%{_javadir}/%{name}/%{name}-trax-%{version}.jar
%config(noreplace) %{_sysconfdir}/%{name}.d/trax
%{ant_home}/etc/mmetrics-frames.xsl
%{ant_home}/etc/coverage-frames.xsl
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-trax-%{version}.jar.*
%endif

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/*.pl
%{_bindir}/*.py*

%files manual
%defattr(0644,root,root,0755)
%doc docs/*

%if %{build_javadoc}
%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%endif
%endif


