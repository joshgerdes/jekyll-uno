---
title: Microsoft Ignite NZ 2016! What a blast!
permalink: /misc/microsoft-ignite-nz-2016-what-a-blast/
categories:
  - Misc
  - Windows
---
Microsoft Ignite NZ 2016! What a blast! _#NinjaCat #MSIgniteNZ_

[<img class="alignnone" title="image" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb.png?resize=714%2C37" alt="Microsoft Ignite NZ 2016" width="714" height="37" data-recalc-dims="1" />](https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image.png)

I was lucky enough to attend Microsoft Ignite this year, so I thought I would do a high level blog post about my experience at this event.

<!--more-->

<div id="toc_container" class="no_bullets">
  <p class="toc_title">
    Table of Contents
  </p>
  
  <ul class="toc_list">
    <li>
      <a href="#Prologue"><span class="toc_number toc_depth_1">1</span> Prologue:</a>
    </li>
    <li>
      <a href="#Day_1_Tuesday_25th_October_2016"><span class="toc_number toc_depth_1">2</span> Day 1 (Tuesday 25th October 2016):</a>
    </li>
    <li>
      <a href="#Day_2_Wednesday_26th_October_2016"><span class="toc_number toc_depth_1">3</span> Day 2 (Wednesday 26th October 2016):</a>
    </li>
    <li>
      <a href="#Day_3_Thursday_27th_October_2016"><span class="toc_number toc_depth_1">4</span> Day 3 (Thursday 27th October 2016):</a>
    </li>
    <li>
      <a href="#Day_4_Friday_28th_October_2016"><span class="toc_number toc_depth_1">5</span> Day 4 (Friday 28th October 2016):</a>
    </li>
  </ul>
</div>

### <span id="Prologue">Prologue:</span>

For those that don’t know – Microsoft Ignite NZ is an event hosted by Microsoft for IT Professionals – whether they are System Administrators or Developers – there is stuff for everyone! This event features sessions from key speakers, usually the top of their fields on their respective technologies covering the entire Microsoft stack and soft skill sessions such as dealing with stress etc. You can find out more – at the MS Ignite webpage &#8211; <a href="https://msignite.nz/why-attend" target="_blank">https://msignite.nz/why-attend</a>

This event was held at Sky City in Auckland, New Zealand between the 25<sup>th</sup> – 28<sup>th</sup> of October 2016.

This was an event I had been eager to attend for a few years, so finally being privileged enough to attend and experience it all was well worth the wait!

### <span id="Day_1_Tuesday_25th_October_2016">Day 1 (Tuesday 25<sup>th</sup> October 2016):</span>

Day 1 consisted of getting to Sky City early for the Exam Cram sessions hosted by Auldhouse _(and of course coffee!)_

The exam cram sessions were a high level overview of the Microsoft Azure platform for: **70-533 &#8211; Implementing Microsoft Infrastructure Solutions & 70-534 &#8211; Architecting Microsoft Azure Solutions**. This content was intended to turn the normal 5-day course offered by Auldhouse into 60 minute slots with the intention of giving an overview of features like ARM (Azure Resource Manager) and of course Azure WebApps and Virtual Machines.

As someone who supports the VMWare virtualization stack – I don’t have the privilege of working with the Microsoft Azure stack on a BAU basis however having stood up Azure Virtual Machines and WebApps in the past it was useful in seeing other aspects of the Azure Cloud and the advancements that Microsoft have made to their Cloud solution and how they are disrupting the market and pushing technology to its potential. It is definitely an exciting time!

These sessions were well worth attending and I gained huge value attending – thanks to Auldhouse for putting them on.

After the Exam Cram sessions – was **the Keynote**!

The keynote was the opening salvo for the rest of the conference! It certainly set the pace and the right attitude!

> _“We are living in one of the most extraordinary times in the history of our planet. Where transformation is at the very heart of the matter. We must transform or we will perish. Our Flame will die! Transform the way we do things, the way we do business, the way we live, the way we create, innovate and inspire&#8221; – Hilary Barry_
> 
> _“Our industry does not respect tradition — it only respects innovation” – Hilary Barry/Satya Nadella_
> 
> _“The art of the possible” – Hilary Barry_

This keynote featured a few awesome demos – that included but not limited to – The Microsoft Surface Hub – an awesome touch capable ‘whiteboard’ device running a variant of the Windows 10 operating system that leans towards team collaboration and sharing. A presentation by Donovan Brown on DevOps! As a developer he demonstrated Visual Studio and Visual Studio Team Services using the Build and Deploy release management! He was able to add changes to a mobile application _(OS independent)_ _‘People Tracker’_ during the demo and build the new version live – this was awesome and from an IT Professional perspective this was great insight into the DevOps pipeline. This was a great lead up to Regan Murphy from Microsoft New Zealand, displaying the Azure DevTest Lab – using the power of the Azure Cloud to stand up development/test environments in a standard and quick way and they now have automatic shutdown and start up at designated time – saving businesses a lot of money and allowing the environments to be accessible when required. Dona Sarkar the Windows Insider Program Lead from Microsoft Redmond also had a huge section of the Keynote! Her speech was more soft skills then technical but was definitely worth listening too! Dona was very inspiring with “_hustle the humans_” and using words like Experiment and not Project to try out new ideas and add value!

> _“We are all creative!” – Dona Sarkar_
> 
> _“The only real failure is not starting at all!” – Dona Sarkar_

<div style="width: 740px" class="wp-caption alignnone">
  <a href="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image-1.png"><img title="image" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb-1.png?resize=730%2C233" alt="Keynote" width="730" height="233" data-recalc-dims="1" /></a>
  
  <p class="wp-caption-text">
    MS Ignite NZ 2016 Keynote
  </p>
</div>

After the keynote I began my technical sessions _(each technical session was 60 minutes)!_

As the primary subject matter expert in System Centre Configuration Manager (SCCM) at work – it was natural that my first session was:

**30 things you should never do with System Center Configuration Manager!** This was a pretty light and hilarious but at the same time serious session detailing how not to do deployment – such deploy to All Systems and how dangerous the software is! It was also clarification and a push that I needed to take a fresh look at the role-based access control (RBAC) for the users and teams using the SCCM environment and re-evaluate what permissions they actual need to do their job to reduce configuration drift against the SCCM standards and to reduce the accidental collection deletion or untoward deployment that would be a resume ending event!

After some afternoon tea – my next session was: **Reducing the network impact of Windows 10 feature and quality updates** &#8211; the speaker for this session was Michael Niehaus one of the top experts in Windows deployment and management. This session detailed ‘_Windows as a service_’ Microsoft push with Windows 10 management – in terms of Feature updates and their size, and getting into the rhythm of maintaining and keeping the Windows Desktop and image up to date. With rough Feature update sizes about 3.5GB every 6 months this needs awareness and some changes to SCCM cache size on the endpoint devices – such as changing this to 10GB and using technologies such as Branch Cache Distributed Hosts or Configuration Manager Peer Cache to distribute the updates and allow them to be distributed from endpoint devices to other endpoint devices on the same subnet reducing the hit to the distribution points – which works well with the fluid nature of the SCCM client check-in _(one client will check in and store the update to the local cache, allowing the next client on the subnet that checks in to retrieve the content from that endpoint device without having to connect back to the datacentre and hit the distribution points)_.

### <span id="Day_2_Wednesday_26th_October_2016">Day 2 (Wednesday 26<sup>th</sup> October 2016):</span>

Day 2 – After the first day – I now knew where the rooms were for the sessions and was able to get myself into the rhythm. With my sessions and their locations added to my Calendar I was easily able to go from session to session without an issue – which was good timing considering this was the first full day of sessions!

I started the day with a soft-skills session &#8211; **Stay in control when everything is out of control, and other brain hacks for techies** this was held in the Sky City Theatre which and was very fascinating! The session revealed a few tricks to do while stress *_breathe_* and ways of thinking such as being the devil’s advocate for yourself as everyone is bias with their own opinions because of their personal and professional experiences, seeing how the other people may think differently and why they may thing differently. An interesting fact – because of the glucose levels – judges were much more likely to accept prisoners’ requests for parole at the beginning of the day than the at end after they had a break or a fresh start!

Next up was another soft session which was again quite interesting &#8211; **Microsoft&#8217;s trusted and secure cloud services** this session was led by Join Russell Craig, Microsoft NZ National Technology Officer and Michael Brick from Microsoft’s NZ Legal counsel and their discussion revolved around Azure Cloud Security. This was interesting in the development and the security certifications the Microsoft Azure platforms gets audited upon a daily basis. It is aligned to just about all security standards including Cloud Security Alliance and the GCIO and that New Zealand Clinical data was authorized and was getting stored on the Azure datacentres in Australia with the New Zealand government having a ‘_cloud first_’ approach which includes the Azure stack where applicable. This potentially opens up the ability for Office 365 and other Microsoft services for the New Zealand Health Industry outside of just identity management.

**From 0 to DevOps** was the next one I attended – this was an awesome session by Donovan Brown who used Visual Studio and Team Services in Azure to create a release pipeline from Visual Studio on his workstation device, uploaded to Team Services in Azure. He showed automated builds and how it could be used to build to Dev, UAT or Production at the same time using any language. He demonstrated using the Node JS language on an Ubuntu platform _(also running PowerShell – how cool is that)_ and then deployed to Team Services. The full stack that Donovan uses the following DevOps processes:

**Plan** _(Plan Work)_ **->** **Infra** _(Configure/Provision Environment)_ **->** **Test** (_Manual/Automated Test) **-> Approve** (Notify/Collect Approvals) **-> Monitor** (Diagnostics/Performance)_

<div style="width: 760px" class="wp-caption alignnone">
  <a href="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image-2.png"><img title="image" src="https://i1.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb-2.png?resize=750%2C327" alt="From 0 to DevOps" width="750" height="327" data-recalc-dims="1" /></a>
  
  <p class="wp-caption-text">
    “DevOps is the union of people, process, and products to enable continuous delivery of value to our end users.” – Donovan Brown
  </p>
</div>

This was an awesome session – especially from an Infrastructure Engineer point of view, this helped me gain insight into the Developer world and some of the processes that should be used in conjunction with PowerShell scripting, as DevOps becomes more supported and Operations and Development mingle. Source Control people!

After some lunch supplied by Microsoft and Sky City it was time to head to my next session:

**Customizing Windows 10: Image Creation Tips and Tricks** – another session by Michael Niehaus. This session was a lot of value in relation to doing image engineering with MDT 2013 Update 2. Having experience in MDT image creation for Windows 7 and Windows 8.1 – I gained a lot of value in understanding about best practices in terms of where to place the AppX package removal steps in the reference task sequence (just after the WinPE phase – before the OS starts) and how Windows 10 1607 will allow the Task Bar to be customized using the StartLayout export XML! About time! There was also a demo about adding in a language pack requires multiple downloads and merged into an MDT Application to add as part of the base WIM.

<div style="width: 339px" class="wp-caption alignnone">
  <a href="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image-3.png"><img title="image" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb-3.png?resize=329%2C255" alt="Customizing Windows 10: Image Creation Tips and Tricks" width="329" height="255" data-recalc-dims="1" /></a>
  
  <p class="wp-caption-text">
    Microsoft Ignite NZ 2016 &#8211; Windows 10: Image Creation Tips and Tricks!
  </p>
</div>

The next session I attended with was **The 9 Group Policy Principals that all IT Administrators should know!** This session was useful to reinforce best practice in terms of not using Block inheritance, Loop Back processing or of course to not use login scripts and wait for network! He also touched on plain text passwords in the group policy and of course the recent Microsoft patch (MS16-072) that resulted in some Group Policies not applying after Authenticated users had been removed The speaker was Alan Burchill who is a Group Policy MVP! So was right on track! Sometimes it’s good to take this kind of session – that allows you to take a step back to look at what may be setup or in use in a “friends” organization and what may and should be done to remedy it! Was a highly valuable session which was something that everyone running Active Directory would have got value out of it straight away, that doesn’t cost money!

Last official session of the day was: **Windows 10 Deployments: What I wish I knew before I started** by a New Zealand Microsoft consultant, Brendan Byrne. I got a lot of value from this session as it was down to earth, wasn’t a sales pitch and revealed a few things to keep in mind going forward – such as not thinking of Windows 10 as Windows 7. Thinking about using features such as Credential Guard and moving to UE-V for user profile management.

After that – and the Hub Happy hour – I attended mini session at the Citrix booth that had a demo and slides for using Citrix AppDNA for Application Migration and compatibility testing,

### <span id="Day_3_Thursday_27th_October_2016">Day 3 (Thursday 27<sup>th</sup> October 2016):</span>

This day was an awesome day – I did miss the Windows Device Smack down! session as I was using the session time to catch up with a few people! One of the best things about Microsoft Ignite NZ 2016 was being able to catch up with people – whether they are people you have worked with or vendors! It was definitely a social geek fest! I also missed Demystifying the Windows Firewall – Learn how to irritate attackers without crippling your network because I had to do some work but will definitely check it out later on the Channel9 website once the session has been uploaded _(link is below this post)_!

**Configuring and Deploying Just Enough and Just-In-Time Administration** – ****Awesome session, and was very interesting! The speaker for this session was: Orin Thomas who is an MVP and awesome technical writer (own a few of his books)! This session details using Just in Time Administration – Privileged Access Management which is a technology by Microsoft that utilizes Microsoft Identity Manager, to have a one-way forest trust with a privileged forest. The idea basically is a user goes to the Microsoft Identity Manager webpages and requests access such as ‘Domain Admin’ once that access is approved – MIM elevates a user’s system admin account for a designated time (for example 30 minutes) which then the user does the work and then MIM removes the elevated rights from the user after this time. The idea is no one is a member of an AD group unless they actually need it and then for a certain amount of time. This would work in well with Change Control, as part of the implementation steps you need to figure out how long the Change would be and add in a step to request the specified access for the time of that action that is then automatically removed. PAM supports any Active Directory group which is also handy – it doesn’t have to be an Active Directory Built-in group! Just Enough Administration (JEA) is all about granting a virtual token/account to a user based on a specific role that will only allow them to run very specific PowerShell commands – such as the demo Orin used as the ability to restart DNS servers, add DNS A records but not able to restart any other server or touch them! Very cool technology that I can see becoming the standard in terms of Role Based Access Control and PowerShell! This session gave me some concepts to think over!

**Righting the Right Rights &#8211; Active Directory & Domain Security, Administration & Maintenance** was my next session (which was luckily in the same room!) The speaker for this session was Jess Dodson from Australia! An MVP! This was a very fascinating and awesome session regarding Active Directory replication, Active Directory security which included Delegation – being more proactive in terms of AD event log monitoring and collecting and included maintenance and recommendations for Azure Active Directory and checking sync replication. This was another of those sessions that I can instantly get the most value from without having to spend money from – well worth a watch!! A Healthy Active Directory – keeps the Users away (I mean happy)!

Second to last session of the day was: **Everything you forgot to ask about Certificate Services** this was another session by Orin Thomas! Orin pretty much went back to basics on this session – what a RootCA is, Subordinates and explained CRLS. Certificate Services is usually something very important but often neglected so was great to attend this session which reminded me about how it all worked and gave me an idea that I had never considered before – Using System Center Operations Manager (SCOM) to monitor for expiring certificates! Definitely something that needs looking into!

My last session was then &#8211; **Enabling DevOps from an IT Pro perspective** this was a very interesting session using Team Services – this session had x2 speakers &#8211; Callum Lowe a Microsoft New Zealand &#8211; Premier Field Engineer (more from an Infrastructure/Operational background) and Daniel Larsen – another Field Engineer that was more from the Development side of the house. They simulated the build and deployment – Daniel gave his requirements to Callum who then used Team Services and Visual Studio to develop the necessary ARM templates to spin up the resources in Azure. This was a session that helped give some context to DevOps and how the people is a big part of the 3 ways.

Thursday night of course – was the MS Ignite New Zealand 2016 party! The food was awesome, with selections of Seafood, BBQ, Asian! Revera Cloud Services had custom made Beer made for the event which was awesome and the entertainment of the night was New Zealand band Shapeshifter! Which had me head banging and fist pumping! This was held at Shed 10 on the Auckland harbor – band was on the bottom floor and a few Xboxes, Table Tennis, VR gaming was at the top floor! Was #Epic! I hadn’t had that much fun in a while!

<div style="width: 756px" class="wp-caption alignnone">
  <a href="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image-4.png"><img title="image" src="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb-4.png?resize=746%2C190" alt="Thursday Night - Ignite NZ Party" width="746" height="190" data-recalc-dims="1" /></a>
  
  <p class="wp-caption-text">
    Microsoft Ignite NZ 2016 Party!
  </p>
</div>

### <span id="Day_4_Friday_28th_October_2016">Day 4 (Friday 28<sup>th</sup> October 2016):</span>

Last day! It seemed the week went really quickly and I had mixed feelings about heading back home or wanting to stay! The last day was only a half a day

After grabbing a coffee – it was straight into **Deploy, configure, and remotely manage Nano Server,** hosted by Benjamin Armstrong a Principle Program Manager at Microsoft this was definitely a good session! Last time I had stood up a Nano Server it was in technical preview and the provisioning of said Nano Server has come a long way –definite project for the weekend to stand up Nano Server 2016 – Hyper-V host on my Intel NUC. Nano Server will follow the same update ‘servicing model’ as Windows 10 with feature updates roughly every year. Benjamin explained that not all Roles & Features are supported in Nano server and what and why they removed parts of Windows that we have taken for granted and that has become bloated over the years such as MSI and the Plug & Play engine. This operating system – severely reduces attack surface, disk image space and reduces the need for restarts during Windows updates! This platform is definitely worth looking into and they have paid allot of attention to the ‘Voice of the Customer’ in what the pain points are.

<div style="width: 403px" class="wp-caption alignnone">
  <a href="https://i2.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image-5.png"><img title="image" src="https://i0.wp.com/luke.geek.nz/wp-content/uploads/2016/10/image_thumb-5.png?resize=393%2C298" alt="Deploy, configure, and remotely manage Nano Server, hosted by Benjamin Armstrong" width="393" height="298" data-recalc-dims="1" /></a>
  
  <p class="wp-caption-text">
    Deploying Nano Server with Nano Guy!
  </p>
</div>

After Nano server it was &#8211; **Migrating to Windows 10, make sure you don’t end up with Windows 7 again** another presentation by Brendan Byrne &#8211; another interesting session! This session was all about making sure to use or at least consider the Windows 10 features – so you don’t end up with a Windows 7 version of Windows 10 and miss out on modern features and security advancements made on the Desktop platform. There was also examples of a few companies who had deployed Windows 10 in different ways – 1 using in Place Upgrade and another allowing Self-Service upgrade from Windows 7 to Windows 10, which allowed users to upgrade to Windows 10 on demand – reducing the IT resourcing requirement and user impact which was an interesting concept. Brendan also touched on Application Testing putting your applications into certain baskets – as not everything can be tested.

**Discover -> Rationalize -> Prioritize -> Test**

He also touched on Windows as a Service and getting into the rhythm and managing it on a day to day basis – setting up the CB, CBB and Windows Insider rings inside the organization and using tools like UE-V and Enterprise State Roaming!

> _“If people aren’t more productive with just the OS along, how successful is the project?” &#8211; Brendan Byrne_

The last session of the event – was **30 terrible habits of Server and Cloud Administrators** by Orin Thomas. This was a useful session regarding how lazy we as system administrations have become and how dangerous it is, such as Windows Firewall being disabled, passwords stored in an excel spreadsheet, Service accounts that are set to never expired and part of Domain Admin!

Useful session that again I can get a lot of value and actions out of straight away!

> _“Builders often live in unfinished houses?” – Orin Thomas_
> 
> _“Hack the nerd is simpler and often more effective than hack the system” – Orin Thomas_

After some Lunch – the event was over and was time to head back home! My time at Microsoft Ignite NZ 2016 was fun, valuable, eventful and just all round awesome! I thank Microsoft and all the Speakers and Sponsors for this event! It is good to know that as an IT professional there are others having similar or same issues – the Pale Blue Dot does not look as small as it was a week ago!

**Resources:**

Sessions & Slides: <a href="https://channel9.msdn.com/Events/Ignite/2016" target="_blank">https://channel9.msdn.com/Events/Ignite/2016</a>

What is DevOps by Donovan Brown &#8211; <a href="http://donovanbrown.com/post/2015/09/01/what-is-devops" target="_blank">http://donovanbrown.com/post/2015/09/01/what-is-devops</a>

Azure IaaS Operations Guidance &#8211; <a href="https://blogs.technet.microsoft.com/tangent_thoughts/2015/10/06/azure-iaas-operations-guidance/" target="_blank">https://blogs.technet.microsoft.com/tangent_thoughts/2015/10/06/azure-iaas-operations-guidance/</a>
