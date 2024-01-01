// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "luke.geek.nz",
  tagline:
    "Microsoft MVP - Microsoft Azure ☁, Technical Consultant, Azure Solutions Architect Expert, Technologist and a drinker of coffee.detect",
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: "https://lukemurraynzdev.github.io",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/lukemurraynzdev/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "lukemurraynz", // Usually your GitHub org/user name.
  projectName: "lukemurraynzdev", // Usually your repo name.
  deploymentBranch: "gh-pages",
  trailingSlash: true,
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },
  themes: ["@docusaurus/theme-mermaid"],
  markdown: {
    mermaid: true,
    format: "detect",
  },

  plugins: ["plugin-image-zoom"],

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: false, // Optional: disable the docs plugin
        blog: {
          routeBasePath: "/", // Serve the blog at the site's root
          showReadingTime: true,
          blogTitle: "Lukes Tech Blog - Unleashing the power of the cloud and other technologies!",
          blogDescription: "Embark on a tech journey with Luke, a Microsoft Azure MVP, as he delves into the cutting-edge realm of Microsoft and Azure Cloud technologies. Explore, learn, and stay ahead in the dynamic world of cloud computing!",
          postsPerPage: 5,
          blogSidebarTitle: "Recent posts",
          blogSidebarCount: 5,
          feedOptions: {
            type: "all",
            copyright: `Copyright © ${new Date().getFullYear()} luke.geek.nz.`,
          },
        },

        theme: {
          customCss: "./src/css/custom.css",
        },
        gtag: {
          trackingID: "G-0QDLBY7NNN",
          anonymizeIP: true,
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      announcementBar: {
        id: "gfe-1", // Increment on change,
        backgroundColor: "#D3D3D3",
        content: `Happy New Year! This is a redesign of my website, hopefully you like it!`,
        isCloseable: true,
      },

      colorMode: {
        defaultMode: "dark",
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      // Replace with your project's social card
      image: "img/social-card.png",
      navbar: {
        title: "luke.geek.nz",
        logo: {
          alt: "luke.geek.nz",
          src: "img/logo.png",
        },
        hideOnScroll: true,
        items: [
          {
            label: "Tags",
            href: "/Tags/",
            position: "left",
          },
          {
            label: "Blog Archive",
            href: "/Archive/",
            position: "left",
          },
          {
            href: "https://twitter.com/lukemurraynz",
            position: "right",
            className: "navbar-icon",
            "aria-label": "X",
            html: `<svg height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 8.586l4.293-4.293a1 1 0 011.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 011.414-1.414L10 8.586z" clip-rule="evenodd" />
          </svg>`,
          },
          {
            href: "https://www.linkedin.com/in/ljmurray/",
            position: "right",
            className: "navbar-icon",
            "aria-label": "LinkedIn",
            html: `<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16" height="20" width="20" xmlns="http://www.w3.org/2000/svg"><path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"></path></svg>`,
          },
        ],
      },
      footer: {
        style: "dark",
        copyright: `Copyright © ${new Date().getFullYear()} luke.geek.nz. Powered by a lot of coffee and hamsters on wheels!`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: [
          "powershell",
          "bash",
          "python",
          "bicep",
          "yaml",
          "log",
          "hcl",
        ],
      },

    
    }),
};

export default config;
