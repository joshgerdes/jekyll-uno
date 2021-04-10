---
title: How to Remove VirtualBox Guest Additions
date: 2012-08-12T08:38:12+00:00
author: Luke
categories:
  - Linux
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