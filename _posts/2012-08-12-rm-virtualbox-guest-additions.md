---
title: How to Remove VirtualBox Guest Additions
date: 2012-08-12 20:38:12 +12:00
permalink: "/linux/rm-virtualbox-guest-additions/"
categories:
- Linux
id: 1407
author: Luke
layout: post
guid: http://techdrive.co.nz/?p=1407
mfn-post-love:
- '0'
dsq_thread_id:
- '4881414104'
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
post_views_count:
- '7'
---

<ol start="1">
  <li>
    First thing is first <strong>close</strong> all instances of <strong>VirtualBox</strong>
  </li>
  <li>
    Open up a <strong>Terminal</strong>
  </li>
  <li>
    Type: <pre class="lang:sh decode:true">sudo find /etc -name "*vboxadd*" -exec rm {} ;</pre>
    
    <p>
      press Enter</li> 
      
      <li>
        Type: <pre class="lang:sh decode:true">sudo find /etc -name "*vboxvfs*" -exec rm {} ;;</pre>
        
        <p>
          press Enter</li> 
          
          <li>
            Type: <pre class="lang:sh decode:true">sudo rm -r /usr/src/vboxadd-*</pre>
            
            <p>
              press Enter</li> 
              
              <li>
                Type: <pre class="lang:sh decode:true">sudo rm -r /usr/src/vboxvfs-*</pre>
                
                <p>
                  press Enter</li> 
                  
                  <li>
                    Type: <pre class="lang:sh decode:true">sudo rm /usr/sbin/vboxadd-timesync</pre>
                    
                    <p>
                      press Enter</li> 
                      
                      <li>
                        Type: <pre class="lang:sh decode:true">sudo rm /lib/modules/`uname -r`/misc/vboxadd.ko</pre>
                        
                        <p>
                          press Enter</li> 
                          
                          <li>
                            Type: <pre class="lang:sh decode:true ">sudo rm /lib/modules/`uname -r`/misc/vboxvfs.ko</pre>
                            
                            <p>
                              press Enter</li> 
                              
                              <li>
                                Now <strong>open</strong> <strong>Virtualbox</strong>
                              </li></ol>