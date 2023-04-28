import { defineConfig } from "tinacms";
import { new_post_Fields } from "./templates";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "main";

export default defineConfig({
  branch,
  clientId: "0861defe-27c3-43f8-aa1a-d4ce9370529b", // Get this from tina.io
  token: "ea14c92e7cd34ff2728b4ca00b1fabb8b19b72cd", // Get this from tina.io
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
