---
title: Release candidate testing
date: 2016-01-08 15:04:23
categories: [quality]
tags: [release candidate regression practices]

layout: page
---

Practice of testing a release build and compare results with a candidate build

For a given API in production (release) we compare (diff) against a candidate (staging, uat, etc) build in order to determine if the differences are breaking changes, accomply with an accepted treshold.

Even if the shape of the information is correct, is convenient to highlight the data diferences.


## Javascript implementation example

```js
import fs from "fs";
import hmtlTemplate from './html-template';
import * as jsondiffpatch from 'jsondiffpatch';

export function diff({
  release={},
  releaseUrl="",
  candidate={},
  candidateUrl="",
  title="",
  metadata={}
}) {
  const createdAt = new Date();
  const diff = jsondiffpatch.create({
    arrays: { detectMove: true, includeValueOnMove: false }
  });
  const delta = diff.diff(release, candidate);
  const content = jsondiffpatch.formatters.html.format(delta, release);
  const header = `
    <h1>${title}</h1>
    <table>
      <tr><td>${createdAt.toString()}</td></tr>
    <table>
    <table>
      <tr>${Object.keys(metadata).map(m => `<th>${m}</th>`).join('')}</tr>
      <tr>${Object.keys(metadata).map(m => `<td>${metadata[m]}</td>`).join('')}</tr>
    </table>
    <table>
      <tr>
        <th style="background: #ffbbbb;">Release</th>
        <th style="background: #bbffbb;">Candidate</th>
      </tr>
      <tr>
        <td><a href="${releaseUrl}">${releaseUrl}</a></td>
        <td><a href="${candidateUrl}">${candidateUrl}</a></td>
      </tr>
    </table>
  `;
  const filename = `${candidateUrl}`.replace(/[\W_]+/g,"-")+`-${createdAt.getTime()}.html`;
  fs.writeFile("reports/"+filename, hmtlTemplate(header, content), function(err) {
    if (err) {
      throw err;
    }
  });
}
```
