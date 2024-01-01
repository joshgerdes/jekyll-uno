---
title: Service Pack did not install. Reverting changes
date: 2012-09-30T14:55:20+00:00
authors: [Luke]
tags:
  - Windows
---
_This usually happens when a service that is required, the Trusted Installer is not running. Follow the instructions below to repair this._

<ol start="1">
  <li>
    Click <strong>Start</strong>
  </li>
  <li>
    Click <strong>Run</strong>
  </li>
  <li>
    Type: <strong><em>services.msc</em></strong><em> </em>> Press <strong>Enter</strong>
  </li>
  <li>
    You should be greeted with a Services dialog list look for TrustedInstaller.
  </li>
  <li>
    <strong>Right</strong> <strong>click</strong> <strong><em>TrustedInstaller</em></strong> and click <strong>Properties</strong>
  </li>
  <li>
    <strong>Set</strong> the TrustedInstaller service to <strong>Automatic</strong> and click <strong>Start</strong>
  </li>
  <li>
    Attempt Service Pack installation again.
  </li>
</ol>