---
title: DCS A10 C Warthog Crashing Windows Vista/Windows 7
date: 2012-09-05T17:58:26+00:00
authors: [Luke]
tags:
  - Windows
---
Having random crashes on DCS A10 C Warthog? With Texture mismatches and Runtime errors? This is usually due to security permissions inside Windows.

  1. Click Start
  2. In the Search field, type: CMD. Then press enter.
  3. Type** _bcdedit /set increaseuserva 3072_** and press enter

_You may need to temporarily disable UAC/run as administrator for this to work_

_If you wish to reverse this command back to default, simply use &#8220;bcdedit /deletevalue increaseuserva&#8221;_