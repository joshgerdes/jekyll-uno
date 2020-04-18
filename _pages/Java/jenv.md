# jenv

jenv is for a equivalent of rbenv, but for Java environment. It allow to easily switch between several JDKs installations (already presents), and configure which one to use per project.

For full documentation, see: https://github.com/hikage/jenv#readme

Install using brew:

```
brew update
brew cask install java
brew install jenv
```

Include this config in your bash profile

```
eval "$(jenv init -)"
```

## Plugins

Jenv provides plugins to make command-line tools aware of which JDK is activated.

```
$ jenv plugins
ant
golo
gradle
grails
groovy
lein
maven
sbt
scala
vlt
```

### Maven

Let's say you want Maven to use the JDK activated with Jenv, not the default JAVA_HOME configuration. You need to activate Jenv's maven plugin.

```
$ jenv enable-plugin maven
maven plugin activated

$ jenv disable-plugin maven
maven disabled
```

### Export

Another one useful plugin is the "export", that expose JAVA_HOME automatically :

```
$ jenv enable-plugin export
You may restart your session to activate jenv export plugin echo export plugin activated
```
