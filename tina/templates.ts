import type { TinaField } from "tinacms";
export function new_post_Fields() {
  return [
    {
      type: "datetime",
      name: "date",
      label: "date",
    },
    {
      type: "string",
      name: "title",
      label: "title",
    },
    {
      type: "string",
      name: "author",
      label: "author",
    },
    {
      type: "string",
      name: "categories",
      label: "categories",
      list: true,
    },
    {
      type: "boolean",
      name: "toc",
      label: "toc",
    },
    {
      type: "object",
      name: "header",
      label: "header",
      fields: [
        {
          type: "image",
          name: "teaser",
          label: "teaser",
        },
      ],
    },
  ] as TinaField[];
}
