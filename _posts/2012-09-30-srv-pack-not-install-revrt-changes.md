---
title: Service Pack did not install. Reverting changes
date: 2012-10-01 03:55:20 +13:00
permalink: "/win/srv-pack-not-install-revrt-changes/"
categories:
- Windows
id: 1542
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1542
dsq_thread_id:
- '4884485677'
omc_review_enable:
- '0'
omc_user_ratings_visibility:
- '0'
omc_review_type:
- stars
omc_criteria_display:
- n
omc_featured_post:
- '0'
omc_comment_type:
- wp
mfn-post-love:
- '0'
post_views_count:
- '9'
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