Name:		ant
Version:	1.10.18
Release:	2
Summary:	Java build tool
Group:		Development/Java
License:	Apache-2.0
URL:		https://ant.apache.org/
Source0:	https://downloads.apache.org/ant/source/apache-ant-%{version}-src.tar.gz
Source1:	ant.asciidoc
Source2:	ant.conf
Source3:	https://archive.apache.org/dist/ant/source/apache-ant-1.10.17-src.tar.gz
Patch0:		ant-system-classpath.patch
BuildArch:	noarch
BuildRequires:	asciidoctor
BuildRequires:	java-current-devel
BuildRequires:	javapackages-filesystem
BuildRequires:	python
BuildRequires:	sysjar
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.hamcrest:hamcrest)
BuildRequires:	mvn(commons-net:commons-net)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	apache-commons-bcel >= 6.13.0
BuildRequires:	apache-commons-lang3 >= 3.21.0
BuildRequires:	mvn(antlr:antlr)
BuildRequires:	mvn(jakarta-regexp:jakarta-regexp)
BuildRequires:	mvn(xml-resolver:xml-resolver)
BuildRequires:	xz-java >= 1.12
Requires:	%{name}-lib = %{EVRD}
Requires:	java-current
Provides:	%{name}-jdk-binding = %{EVRD}
Obsoletes:	%{name}-openjdk21 < %{version}-%{release}
Obsoletes:	%{name}-openjdk25 < %{version}-%{release}
Obsoletes:	%{name}-unbound < %{version}-%{release}
Obsoletes:	%{name}-jsch < %{version}-%{release}
Obsoletes:	%{name}-apache-oro < %{version}-%{release}
Obsoletes:	%{name}-apache-bsf < %{version}-%{release}
Obsoletes:	%{name}-jdepend < %{version}-%{release}
Obsoletes:	%{name}-apache-xalan2 < %{version}-%{release}
Obsoletes:	%{name}-apache-log4j < %{version}-%{release}

%description
Apache Ant drives a build from targets and tasks. This package is the
command line tool. It uses the current Java and system jars. The
1.10.17 ant and ant-launcher jars are installed beside %{version}
for callers that pin that release. Optional tasks whose libraries
are not packaged (JSch, ORO, BSF, JDepend, Xalan, Log4j 1, Jakarta
Mail, JUnit 5) are not built.

%package lib
Summary:	Core libraries for %{name}
Group:		Development/Java
Requires:	javapackages-filesystem

%description lib
Apache Ant's launcher and core classes, installed as system jars.

%package junit
Summary:	JUnit 4 tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}
Requires:	mvn(org.hamcrest:hamcrest)

%description junit
JUnit 4 and JUnit 4.x adapter tasks for Apache Ant.

%package commons-net
Summary:	Commons Net tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}
Requires:	mvn(commons-io:commons-io)

%description commons-net
FTP, rexec and telnet tasks for Apache Ant.

%package commons-logging
Summary:	Commons Logging listener for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description commons-logging
Commons Logging listener for Apache Ant.

%package apache-bcel
Summary:	BCEL tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}
Requires:	apache-commons-bcel >= 6.13.0
Requires:	apache-commons-lang3 >= 3.21.0
Requires:	mvn(commons-io:commons-io)

%description apache-bcel
Byte Code Engineering Library tasks for Apache Ant.

%package apache-regexp
Summary:	Jakarta Regexp tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description apache-regexp
Jakarta Regexp tasks for Apache Ant.

%package apache-resolver
Summary:	XML resolver tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description apache-resolver
XML Commons Resolver tasks for Apache Ant.

%package antlr
Summary:	ANTLR task for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}
Requires:	mvn(antlr:antlr)

%description antlr
ANTLR 2 task for Apache Ant.

%package xz
Summary:	XZ tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}
Requires:	xz-java >= 1.12

%description xz
XZ compression tasks for Apache Ant.

%package swing
Summary:	Swing tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description swing
Swing splash-screen task for Apache Ant.

%package imageio
Summary:	ImageIO tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description imageio
ImageIO drawing tasks for Apache Ant.

%package jmf
Summary:	Sound tasks for %{name}
Group:		Development/Java
Requires:	%{name} = %{EVRD}

%description jmf
Java Sound tasks for Apache Ant. The package name is the upstream
ant-jmf artifact. The implementation uses javax.sound.

%package manual
Summary:	Manual for %{name}
Group:		Development/Java
License:	Apache-2.0 AND Apache-1.1
Requires:	%{name}-lib = %{EVRD}

%description manual
HTML manual for Apache Ant. One tutorial archive contains source under
the Apache-1.1 license.

%prep
%setup -q -n apache-ant-%{version}
%autopatch -p1
%setup -q -T -D -a 3 -n apache-ant-%{version}
# The source archives ship prebuilt jars. Use the system copies instead.
find . \( -name '*.jar' -o -name '*.class' -o -name '*.so' -o -name '*.node' -o -name '*.wasm' \) -delete
sed -i 's/commons-logging-api/commons-logging/' src/etc/poms/ant-commons-logging/pom.xml
# The distribution target also builds the test jar, which needs the
# whole test suite. The runtime jars do not.
sed -i 's/depends="jars,test-jar,component-boms,-ant-dist-warn-jdk9+"/depends="jars,-ant-dist-warn-jdk9+"/' build.xml
sed -i 's/depends="jars,test-jar,-ant-dist-warn-jdk9+"/depends="jars,-ant-dist-warn-jdk9+"/' apache-ant-1.10.17/build.xml

%build
export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/java}"
opt=lib/optional
mkdir -p "$opt"
linkjar() {
	test -f "$1"
	ln -s "$1" "$opt/$2"
}
linkjar %{_javadir}/junit.jar junit.jar
linkjar %{_javadir}/hamcrest/hamcrest.jar hamcrest.jar
linkjar %{_javadir}/commons-net.jar commons-net.jar
linkjar %{_javadir}/commons-io.jar commons-io.jar
linkjar %{_javadir}/commons-logging.jar commons-logging.jar
linkjar %{_javadir}/bcel.jar bcel.jar
linkjar %{_javadir}/commons-lang3.jar commons-lang3.jar
linkjar %{_javadir}/antlr.jar antlr.jar
linkjar %{_javadir}/regexp.jar regexp.jar
linkjar %{_javadir}/xml-resolver.jar xml-resolver.jar
linkjar %{_javadir}/xz.jar xz.jar
sh bootstrap.sh
for jar in build/lib/*.jar; do
	if ! "$JAVA_HOME/bin/jar" tf "$jar" | grep -q '\.class$'; then
		rm -f "$jar"
	fi
done
# JUnit 5 is not packaged. The confined classes compile without it and
# would be a broken task jar.
rm -f build/lib/ant-junitlauncher.jar
for jar in ant ant-launcher ant-bootstrap ant-junit ant-junit4 \
	ant-commons-net ant-commons-logging ant-apache-bcel \
	ant-apache-regexp ant-apache-resolver ant-antlr ant-xz \
	ant-swing ant-imageio ant-jmf; do
	test -s "build/lib/${jar}.jar"
done
asciidoctor -b manpage -D man %{SOURCE1}
python - << 'PY'
open("build/ant-bootstrap.pom", "w").write("""<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.ant</groupId>
  <artifactId>ant-bootstrap</artifactId>
  <version>%{version}</version>
  <name>Apache Ant Bootstrap</name>
  <description>Minimal Ant entry point used to bootstrap the full distribution.</description>
</project>
""")
PY

# org.apache.ant:ant and ant-launcher 1.10.17 stay beside %{version}.
# The command and the Ant lib symlinks keep %{version}.
(
cd apache-ant-1.10.17
opt=lib/optional
mkdir -p "$opt"
linkjar %{_javadir}/junit.jar junit.jar
linkjar %{_javadir}/hamcrest/hamcrest.jar hamcrest.jar
linkjar %{_javadir}/commons-net.jar commons-net.jar
linkjar %{_javadir}/commons-io.jar commons-io.jar
linkjar %{_javadir}/commons-logging.jar commons-logging.jar
linkjar %{_javadir}/bcel.jar bcel.jar
linkjar %{_javadir}/commons-lang3.jar commons-lang3.jar
linkjar %{_javadir}/antlr.jar antlr.jar
linkjar %{_javadir}/regexp.jar regexp.jar
linkjar %{_javadir}/xml-resolver.jar xml-resolver.jar
linkjar %{_javadir}/xz.jar xz.jar
sh bootstrap.sh
test -s build/lib/ant.jar
test -s build/lib/ant-launcher.jar
python - << 'PY'
from pathlib import Path
def write_pom(artifact):
    text = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.apache.ant</groupId>
  <artifactId>ARTIFACT</artifactId>
  <version>1.10.17</version>
  <name>Apache Ant</name>
  <description>Apache Ant ARTIFACT 1.10.17, built from source.</description>
  <url>https://ant.apache.org/</url>
  <licenses>
    <license>
      <name>Apache-2.0</name>
      <url>https://www.apache.org/licenses/LICENSE-2.0.txt</url>
      <distribution>repo</distribution>
    </license>
  </licenses>
</project>
"""
    Path("build/" + artifact + "-1.10.17.pom").write_text(text.replace("ARTIFACT", artifact))
write_pom("ant")
write_pom("ant-launcher")
PY
)

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/ant/{bin,lib,etc,manual}
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 src/script/ant %{buildroot}%{_bindir}/ant
install -m 755 src/script/antRun %{buildroot}%{_datadir}/ant/bin/antRun
ln -s %{_bindir}/ant %{buildroot}%{_datadir}/ant/bin/ant
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/ant.conf
install -m 644 man/ant.1 %{buildroot}%{_mandir}/man1/ant.1
# ant-nodeps.jar and ant-bootstrap.jar repeat classes from ant.jar.
# Keep them available to Maven and off Ant's runtime library directory.
ln -s ../../java/ant.jar %{buildroot}%{_datadir}/ant/lib/ant.jar
ln -s ../../java/ant-launcher.jar %{buildroot}%{_datadir}/ant/lib/ant-launcher.jar
cp -p src/etc/ant-update.xsl src/etc/changelog.xsl src/etc/common2master.xsl \
	src/etc/coverage-frames.xsl src/etc/mmetrics-frames.xsl src/etc/log.xsl \
	src/etc/tagdiff.xsl src/etc/printFailingTests.xsl \
	%{buildroot}%{_datadir}/ant/etc/
cp -a manual/. %{buildroot}%{_datadir}/ant/manual/

install_art() {
	list=$1
	pom=$2
	jar=$3
	shift 3
	sysjar install --buildroot %{buildroot} --artifact "${pom}:${jar}" --filelist "${list}" "$@"
}
sysjar install --buildroot %{buildroot} \
	--artifact "apache-ant-1.10.17/build/ant-1.10.17.pom:apache-ant-1.10.17/build/lib/ant.jar" \
	--file-name ant-1.10.17 \
	--alias ant:ant --alias apache:ant \
	--filelist .mfiles-ant1017
/bin/mv %{buildroot}/usr/share/sysjar/index/org.apache.ant/ant.sysjar \
	%{buildroot}/usr/share/sysjar/index/org.apache.ant/ant-1.10.17.sysjar
sed -i 's|/usr/share/sysjar/index/org.apache.ant/ant\.sysjar|/usr/share/sysjar/index/org.apache.ant/ant-1.10.17.sysjar|' .mfiles-ant1017
sysjar install --buildroot %{buildroot} \
	--artifact "apache-ant-1.10.17/build/ant-launcher-1.10.17.pom:apache-ant-1.10.17/build/lib/ant-launcher.jar" \
	--file-name ant-launcher-1.10.17 \
	--alias ant:ant-launcher \
	--filelist .mfiles-launcher1017
/bin/mv %{buildroot}/usr/share/sysjar/index/org.apache.ant/ant-launcher.sysjar \
	%{buildroot}/usr/share/sysjar/index/org.apache.ant/ant-launcher-1.10.17.sysjar
sed -i 's|/usr/share/sysjar/index/org.apache.ant/ant-launcher\.sysjar|/usr/share/sysjar/index/org.apache.ant/ant-launcher-1.10.17.sysjar|' .mfiles-launcher1017
install_art .mfiles-ant src/etc/poms/ant/pom.xml build/lib/ant.jar \
	--alias ant:ant --alias apache:ant --alias org.apache.ant:ant-nodeps
install_art .mfiles-launcher src/etc/poms/ant-launcher/pom.xml build/lib/ant-launcher.jar \
	--alias ant:ant-launcher
install_art .mfiles-bootstrap build/ant-bootstrap.pom build/lib/ant-bootstrap.jar
sysjar install --buildroot %{buildroot} --artifact src/etc/poms/pom.xml --filelist .mfiles-parent
cat .mfiles-ant .mfiles-launcher .mfiles-bootstrap .mfiles-parent .mfiles-ant1017 .mfiles-launcher1017 | awk '!seen[$0]++' > .mfiles-lib

liblink() {
	ln -s "../../java/$2" "%{buildroot}%{_datadir}/ant/lib/$1"
}
fragment() {
	name=$1
	shift
	: > "%{buildroot}%{_sysconfdir}/ant.d/${name}"
	for jar in "$@"; do
		echo "$jar" >> "%{buildroot}%{_sysconfdir}/ant.d/${name}"
	done
}
install_art .mfiles-junit-a src/etc/poms/ant-junit/pom.xml build/lib/ant-junit.jar
install_art .mfiles-junit-b src/etc/poms/ant-junit4/pom.xml build/lib/ant-junit4.jar
cat .mfiles-junit-a .mfiles-junit-b | awk '!seen[$0]++' > .mfiles-junit
liblink ant-junit.jar ant-junit.jar
liblink ant-junit4.jar ant-junit4.jar
fragment junit %{_javadir}/junit.jar %{_javadir}/hamcrest/hamcrest.jar
cp -p src/etc/junit-frames.xsl src/etc/junit-noframes.xsl \
	src/etc/junit-frames-xalan1.xsl src/etc/junit-frames-saxon.xsl \
	src/etc/junit-noframes-saxon.xsl \
	%{buildroot}%{_datadir}/ant/etc/

install_art .mfiles-commons-net src/etc/poms/ant-commons-net/pom.xml build/lib/ant-commons-net.jar
liblink ant-commons-net.jar ant-commons-net.jar
fragment commons-net %{_javadir}/commons-net.jar %{_javadir}/commons-io.jar

install_art .mfiles-commons-logging src/etc/poms/ant-commons-logging/pom.xml build/lib/ant-commons-logging.jar
liblink ant-commons-logging.jar ant-commons-logging.jar
fragment commons-logging %{_javadir}/commons-logging.jar

install_art .mfiles-apache-bcel src/etc/poms/ant-apache-bcel/pom.xml build/lib/ant-apache-bcel.jar
liblink ant-apache-bcel.jar ant-apache-bcel.jar
fragment apache-bcel %{_javadir}/bcel.jar %{_javadir}/commons-io.jar %{_javadir}/commons-lang3.jar

install_art .mfiles-apache-regexp src/etc/poms/ant-apache-regexp/pom.xml build/lib/ant-apache-regexp.jar
liblink ant-apache-regexp.jar ant-apache-regexp.jar
fragment apache-regexp %{_javadir}/regexp.jar

install_art .mfiles-apache-resolver src/etc/poms/ant-apache-resolver/pom.xml build/lib/ant-apache-resolver.jar
liblink ant-apache-resolver.jar ant-apache-resolver.jar
fragment apache-resolver %{_javadir}/xml-resolver.jar

install_art .mfiles-antlr src/etc/poms/ant-antlr/pom.xml build/lib/ant-antlr.jar
liblink ant-antlr.jar ant-antlr.jar
fragment antlr %{_javadir}/antlr.jar

install_art .mfiles-xz src/etc/poms/ant-xz/pom.xml build/lib/ant-xz.jar
liblink ant-xz.jar ant-xz.jar
fragment xz %{_javadir}/xz.jar

install_art .mfiles-swing src/etc/poms/ant-swing/pom.xml build/lib/ant-swing.jar
liblink ant-swing.jar ant-swing.jar

install_art .mfiles-imageio src/etc/poms/ant-imageio/pom.xml build/lib/ant-imageio.jar
liblink ant-imageio.jar ant-imageio.jar

install_art .mfiles-jmf src/etc/poms/ant-jmf/pom.xml build/lib/ant-jmf.jar
liblink ant-jmf.jar ant-jmf.jar

%check
export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/java}"
export ANT_HOME="$PWD/bootstrap"
python - << 'PY'
from pathlib import Path
javadir = "%{_javadir}"
Path("check.d").mkdir()
Path("check.d/junit").write_text(javadir + "/junit.jar\n" + javadir + "/hamcrest/hamcrest.jar\n")
Path("check-src").mkdir()
Path("check-src/HelloTest.java").write_text(
    "import org.junit.Test;\n"
    "import static org.junit.Assert.assertEquals;\n"
    "public class HelloTest {\n"
    "  @Test public void one() { assertEquals(2, 1 + 1); }\n"
    "}\n")
Path("check-build.xml").write_text(
    "<project default=\"t\">\n"
    "  <target name=\"t\">\n"
    "    <echo message=\"probe ok\"/>\n"
    "    <mkdir dir=\"check-classes\"/>\n"
    "    <javac srcdir=\"check-src\" destdir=\"check-classes\" includeantruntime=\"false\" release=\"8\"\n"
    "           classpath=\"" + javadir + "/junit.jar:" + javadir + "/hamcrest/hamcrest.jar\"/>\n"
    "    <junit printsummary=\"yes\" haltonfailure=\"yes\">\n"
    "      <classpath path=\"check-classes\"/>\n"
    "      <formatter type=\"plain\" usefile=\"false\"/>\n"
    "      <test name=\"HelloTest\"/>\n"
    "    </junit>\n"
    "    <echo message=\"junit ok\"/>\n"
    "  </target>\n"
    "</project>\n")
PY
cp bootstrap/bin/ant check-ant
chmod 755 check-ant
sed -i "s|/etc/ant.d|$PWD/check.d|g" check-ant
./check-ant -f check-build.xml -noinput > check.log
grep -F -q 'probe ok' check.log
grep -F -q 'junit ok' check.log
grep -F -q 'Failures: 0' check.log

cat > Ant1017Check.java << 'EOF'
public class Ant1017Check {
    public static void main(String[] args) throws Exception {
        String version = org.apache.tools.ant.Main.getAntVersion();
        String shortVersion = org.apache.tools.ant.Main.getShortAntVersion();
        if (!"1.10.17".equals(shortVersion)) {
            throw new RuntimeException(version);
        }
        if (!"org.apache.tools.ant.Main".equals(org.apache.tools.ant.launch.Launcher.MAIN_CLASS)) {
            throw new RuntimeException(org.apache.tools.ant.launch.Launcher.MAIN_CLASS);
        }
        org.apache.tools.ant.Project project = new org.apache.tools.ant.Project();
        project.init();
        project.setProperty("pin", "17");
        if (!"17".equals(project.getProperty("pin"))) {
            throw new RuntimeException(project.getProperty("pin"));
        }
        System.out.println("ant1017_ok " + shortVersion);
    }
}
EOF
"$JAVA_HOME/bin/javac" --release 8 -proc:none \
	-cp apache-ant-1.10.17/build/lib/ant.jar:apache-ant-1.10.17/build/lib/ant-launcher.jar \
	Ant1017Check.java
"$JAVA_HOME/bin/java" \
	-cp "apache-ant-1.10.17/build/lib/ant.jar:apache-ant-1.10.17/build/lib/ant-launcher.jar:." \
	Ant1017Check > check-1017.log
cat check-1017.log
grep -F -q 'ant1017_ok 1.10.17' check-1017.log

%files
%license LICENSE NOTICE
%doc README WHATSNEW
%config(noreplace) %{_sysconfdir}/ant.conf
%{_bindir}/ant
%dir %{_datadir}/ant
%dir %{_datadir}/ant/bin
%{_datadir}/ant/bin/ant
%{_datadir}/ant/bin/antRun
%{_mandir}/man1/ant.1*
%dir %{_datadir}/ant/etc
%{_datadir}/ant/etc/ant-update.xsl
%{_datadir}/ant/etc/changelog.xsl
%{_datadir}/ant/etc/common2master.xsl
%{_datadir}/ant/etc/coverage-frames.xsl
%{_datadir}/ant/etc/mmetrics-frames.xsl
%{_datadir}/ant/etc/log.xsl
%{_datadir}/ant/etc/tagdiff.xsl
%{_datadir}/ant/etc/printFailingTests.xsl
%dir %{_sysconfdir}/ant.d

%files lib -f .mfiles-lib
%dir %{_datadir}/ant
%dir %{_datadir}/ant/lib
%{_datadir}/ant/lib/ant.jar
%{_datadir}/ant/lib/ant-launcher.jar

%files junit -f .mfiles-junit
%{_datadir}/ant/lib/ant-junit.jar
%{_datadir}/ant/lib/ant-junit4.jar
%config(noreplace) %{_sysconfdir}/ant.d/junit
%{_datadir}/ant/etc/junit-frames.xsl
%{_datadir}/ant/etc/junit-noframes.xsl
%{_datadir}/ant/etc/junit-frames-xalan1.xsl
%{_datadir}/ant/etc/junit-frames-saxon.xsl
%{_datadir}/ant/etc/junit-noframes-saxon.xsl

%files commons-net -f .mfiles-commons-net
%{_datadir}/ant/lib/ant-commons-net.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-net

%files commons-logging -f .mfiles-commons-logging
%{_datadir}/ant/lib/ant-commons-logging.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-logging

%files apache-bcel -f .mfiles-apache-bcel
%{_datadir}/ant/lib/ant-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-bcel

%files apache-regexp -f .mfiles-apache-regexp
%{_datadir}/ant/lib/ant-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-regexp

%files apache-resolver -f .mfiles-apache-resolver
%{_datadir}/ant/lib/ant-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-resolver

%files antlr -f .mfiles-antlr
%{_datadir}/ant/lib/ant-antlr.jar
%config(noreplace) %{_sysconfdir}/ant.d/antlr

%files xz -f .mfiles-xz
%{_datadir}/ant/lib/ant-xz.jar
%config(noreplace) %{_sysconfdir}/ant.d/xz

%files swing -f .mfiles-swing
%{_datadir}/ant/lib/ant-swing.jar

%files imageio -f .mfiles-imageio
%{_datadir}/ant/lib/ant-imageio.jar

%files jmf -f .mfiles-jmf
%{_datadir}/ant/lib/ant-jmf.jar

%files manual
%license LICENSE NOTICE
%dir %{_datadir}/ant
%{_datadir}/ant/manual
