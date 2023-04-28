import { defineConfig } from "tinacms";
import { new_post_Fields } from "./templates";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "master";

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
      mediaRoot: "",
      publicFolder: "./",
    },
  },
  schema: {
    collections: [],
  },
});
