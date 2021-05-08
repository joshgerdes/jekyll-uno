---
date: 2021-05-08 00:00:00 +1200
title: Full end to end encryption on an Azure WebApp using Cloudflare
author: Luke
categories:
- Azure
toc: true
header:
  teaser: "/uploads/cloudflare_azure_e2e_cert.png"

---
Cloudflare offers many capabilities; one of the capabilities it offers is SSL offloading.

When setting up an Azure Web App using default settings, it is set up using HTTP, not HTTPS, so we will set the WebApp to your custom domain, then use Cloudflare to protect traffic from your user's browsers to Cloudflare, then encrypt traffic from Cloudflare to your website.

We will go through both setups, with the result being full end-to-end encryption and security of your Azure WebApp using Cloudflare.

**Using Cloudflare without a backend Certificate** ![Using Cloudflare without a backend Certificate](/uploads/cloudflare_azure_brokensslchain.png "Using Cloudflare without a backend Certificate")

**Using Cloudflare with a backend Certificate** ![Using Cloudflare with a backend Certificate](/uploads/cloudflare_azure_e2e_cert.png "Using Cloudflare with a backend Certificate")

By default, Azure WebApps have a wildcard cert for the following domains:

* *.azurewebsites.net
* With Subject alternative names for:
* *.scm.azurewebsites.net
* *.azure-mobile.net
* *.scm.azure-mobile.net
* *.sso.azurewebsites.net

![badasscloud - azurewebsites.net secure](/uploads/badasscloudazurewebsitessl.png "badasscloud - azurewebsites.net secure")

This certificate allows you to use HTTPS using the default azurewebsites URL, which gets created when you create your Azure WebApp and is completely managed by Microsoft and the Azure ecosystem. Still, if you want to use your own Custom Domain, then these certificates won't work.

## Prerequisites

* Azure WebApp (supports Custom Domain SSL support, Custom Domains/SSL support are available from ‘B1’ plans and upwards.)
* [Cloudflare](https://www.cloudflare.com/en-gb/ "Cloudflare") account (can be free)
* Domain (an actual custom domain to use for your website that is already setup to use Cloudflare nameservers)
* [PfxCreator](https://github.com/georg-jung/PfxCreator "PFXCreator GitHub Repository")

## Add a Custom Domain to your Azure WebApp using Cloudflare.

 1. Login into the [Azure Portal](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites "Azure Portal - App Services")
 2. Navigate to your App Service.
 3. Underneath Settings on the left-hand side blade of the App Settings, look for Custom Domains and select it.
 4. Click on ‘Add Custom Domain’.
 5. type in your custom domain (in my example, I am using a domain I own called: badasscloud.com)
 6. Select Validate; you will have a similar seen to me below; select CNAME. ![Azure - Add Custom Domain](/uploads/AzureAppService_AddCustomDomain.png "Azure - Add Custom Domain")
 7. Now we need to validate that you are the one who owns the domains and can use it for your WebApp, so we will need to create some records to verify that you own the domain and redirect the website to the Azure Websites.
 8. Login to Cloudflare
 9. Select SSL/TLS and make sure that ‘Flexible’ SSL has been selected.
10. Select DNS _Note: You may need to remove any A records for ‘www’ or the root domain ‘@’ you have set; please make sure you have a reference to them in case you need to roll back any changes because we will be redirecting the main URL to an Azure DNS alias, we will be using Cloudflare CNAME flattening at the root level, so anyone going to ‘badasscloud.com’ will be redirected to the Azure WebApp._
11. You can also use the txt record to validate the domain and do some reconfiguration without changing the domain and redirecting traffic ahead of your change to avoid downtime.
12. Add in the records to Cloudflare (please note that verification will fail if Cloudflare proxy is turned on, so make sure that the proxy status is set to DNS only) ![](/uploads/badassclouddns_azureverification.png)
13. Navigate back to the Azure Portal.
14. Click on Validate again and select CNAME.
15. Verify that Hostname availability and Domain ownership is both Green, then press Add Custom Domain.
    ![Azure - Add Custom Domain](/uploads/AzureAppService_AddCustomDomain_VerificationComplete.png "Azure - Add Custom Domain")
16. If they are still Red, wait a few minutes for Cloudflare to replicate the changes across its Networks and Azure to clear any server-side caching, verification can fail if you try to verify straight away.
17. Now that Domain verification has been completed navigate Cloudflare and enable the Cloudflare proxy for your root domain and www record. ![](/uploads/badassclouddns_postazureverification.png)
18. Navigate and test your website. Now that the domain has been added to the Azure WebApp and Cloudflare proxy has been enabled, your website will now have a certificate supplied by Cloudflare. You have now set up Flexible SSL traffic to your website, so traffic between users’ browsers to Cloudflare is now encrypted. ![badasscloud.com - Cloudflare Certificate](/uploads/badasscloud_Azure_Cloudflarefront.png "badasscloud.com - Cloudflare Certificate")

## **Update your WebApp to support ‘Full’ end-to-end using Cloudflare origin certificate**

Adding your domain to Cloudflare was only the first part of the puzzle; although traffic between the browser and Cloudflare is now encrypted, traffic between Cloudflare and your WebApp is not; to encrypt this traffic, we are going to use the Cloudflare origin certificate.

Cloudflare Origin Certificates are free SSL certificates issued by Cloudflare for installation on your origin server to facilitate end-to-end encryption for your visitors using HTTPS. Once deployed, they are [compatible with the Strict SSL mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes#strict). By default, newly generated certificates are valid for 15 years, but you can change this to 7 days.

 1. Log in to Cloudflare
 2. Click on SSL/TLS
 3. Click on Origin Server
 4. Click on Create Certificate ![Cloudflare - Origin Certificate](/uploads/Cloudflare_OriginCert1.png "Cloudflare - Origin Certificate")
 5. Verify that the Private Key Type is RSA (2048)
 6. Make sure that the Hostnames you want to be covered under the origin cert is covered.
 7. Verify certificate validity, in my example, and I am going with 15 years; remember to keep this certificate validated and updated. ![Cloudflare - Origin Certificate](/uploads/Cloudflare_OriginCert2.png "Cloudflare - Origin Certificate")
 8. Click Create
 9. Cloudflare will now generate your Origin certificate and Private key (save these somewhere secure, the private key will not be shown again).
10. Now we need to create a certificate PFX file to upload to the Azure WebApp, run PfxCreator.exe (see Prerequisites for download link)
11. Paste the Origin Certificate into the: Certificate (PEM)
12. Paste the Private Key into the Private Key (PEM) ![PfxCreator](/uploads/PfxCreator.png "PfxCreator")
13. Type in a password for the certificate
14. Click Save PFX… and save your certificate.
15. Login into the Azure Portal
16. Navigate to your App Service.
17. Underneath Settings on the left-hand side blade of the App Settings, look for Custom Domains and select it.
18. You should see the SSL state of your domain as ‘Not Secure’, and under SSL Binding, you will have an option to Add Binding, click on Add Binding.
19. Select your Custom Domain and click Upload PFX Certificate
20. Click File and browse for your certificate.
21. Type in the password you entered PFXCreator earlier. ![Azure Portal - Add Private Certificate](/uploads/AzureWebApp-Cloudflare_OriginCert_AddBinding1.png.png "Azure Portal - Add Private Certificate")
22. Click on Upload.
23. Once uploaded, select your Custom Domain.
24. Select the Cloudflare Origin Certificate
25. Make sure the TLS/SSL type is: SNI SSL and click Add Binding. ![Azure Portal - Add Private Certificate](/uploads/AzureWebApp-Cloudflare_OriginCert_AddBinding3.png.png "Azure Portal - Add Private Certificate")
26. The SSL State of your Custom Domain should now have been changed to Secure.
27. Click on HTTPS Only
    _Note: You may see constant redirect issues with your website until the following Cloudflare changes have been made._ ![Azure Portal - Enable HTTPS](/uploads/AzureWebApp-Cloudflare_OriginCert_AddBinding4.png "Azure Portal - Enable HTTPS")
28. Login to Cloudflare
29. Select SSL/TLS and make sure that ‘Full (Strict)’ has been selected.
30. Give it 30 seconds to a minute to take effect, and you have now successfully encrypted traffic end-to-end on your website, from the browser to Cloudflare and from Cloudflare to your Azure WebApp.

\#ProTip - If you want to be more secure, you can look into blocking access to your website from Cloudflare and a few select IPs for testing only to avoid traffic from bypassing Cloudflare and going to the azure websites URL.