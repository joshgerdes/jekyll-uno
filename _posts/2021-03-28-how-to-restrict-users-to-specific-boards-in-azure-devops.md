---
date: 2021-03-28 00:00:00 +1300
title: How to restrict users to specific boards in Azure DevOps
author: Luke
categories:
- Azure
- Misc
toc: false

---
Do you ever want to add external Azure Active Directory or other users to specific boards in a project, but not want to give them access to the entire Azure DevOps Project?

Using the steps below, we can restrict users to a specific board.

1. Invite external users to DevOps org with Stakeholder access.
2. In the project, create a new Team and do not add it to the existing security group to inherit permissions.
![Azure DevOps - Boards](/uploads/azdevopsboard1.jpg)
3. Add external users to created Team.
4. Set permission for created Team properly. In this case, it’s to set View project-level information to Allow.
![Azure DevOps - Boards](/uploads/azdevopsboard2.jpg)
5. Create a new area path and set the permission for the created Team in Security
![Azure DevOps - Boards](/uploads/azdevopsboard3.jpg)
6. Assign the area path to the newly created Team.
