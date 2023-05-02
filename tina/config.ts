import { defineConfig } from "tinacms";
import { new_post_Fields } from "./templates";

// Your hosting provider likely exposes this as an environment variable
const branch =
  process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "master";

export default defineConfig({
  branch,
  clientId: "5abfd70b-e8cf-44a8-8376-f24439935163", // Get this from tina.io
  token: "7880906cadaf177cb2431fb058964d9113094537", // Get this from tina.io
  client: { skip: true },
  build: {
    outputFolder: "admin",
    publicFolder: "./",
  },
  media: {
    tina: {
      mediaRoot: "images/posts",
      publicFolder: "./",
    },
  },
  schema: {
    collections: [
      {
        name: "post",
        label: "Posts",
        path: "_posts",
        format: "md",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "author",
            label: "Author",
            options: ["Luke"],
          },

          {
            type: "string",
            name: "categories",
            label: "Categories",
            options: [
              "Windows",
              "Misc",
              "Azure",
              "Mac OSX",
              "PowerShell",
              "Mobile",
              "Linux",
              "Android",
              "iOS",
              "Service Management",
              "M365",
              "Windows Phone",
            ],
          },
          {
            type: "string",
            name: "description",
            label: "Description",
          },
          {
            type: "image",
            name: "Header",
            label: "Header",
          },
          {
            type: "datetime",
            name: "date",
            label: "Publish Date",
            ui: {
              dateFormat: "YYYY MM DD",
            },
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
        ],
      },
      {
        name: "drfts",
        label: "drafts",
        path: "_drafts",
        format: "md",
        fields: [
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "author",
            label: "Author",
            options: ["Luke"],
          },

          {
            type: "string",
            name: "categories",
            label: "Categories",
            options: [
              "Windows",
              "Misc",
              "Azure",
              "Mac OSX",
              "PowerShell",
              "Mobile",
              "Linux",
              "Android",
              "iOS",
              "Service Management",
              "M365",
              "Windows Phone",
            ],
          },
          {
            type: "string",
            name: "description",
            label: "Description",
          },
          {
            type: "image",
            name: "Header",
            label: "Header",
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
        ],
      },
    ],
  },
});
