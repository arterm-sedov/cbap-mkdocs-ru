# PDF Template Contract

The PDF cover page and running page footers use the neutral `extra.pdf` contract from the active MkDocs YAML configuration.

```yaml
extra:
  pdf:
    # Plain-text default for PDF right-side footers.
    copyright: © Comindware, 2009–2026
    frontpage:
      logo: assets/images/comindware_logo.svg
      headerRight: comindware.ru
      title: Comindware Platform 6.0
      subtitle: Руководство по использованию API
      footerLeft: Опубликовано 19.02.2026
      # footerRight defaults to pdf.copyright; set literal text to override.
    pageFooter:
      left: ''
      # right defaults to pdf.copyright; set literal text to override.
```

Use literal values only. Do not use `productName`, `productVersion`, `author`, `cover_subtitle`, or root `copyright` to drive PDF frontpage text.

The root MkDocs `copyright` value is HTML for the web footer. PDF footer fields must be plain text.

Default behavior:

- `frontpage.footerRight` is optional and defaults to `pdf.copyright`.
- `pageFooter.right` is optional and defaults to `pdf.copyright`.
- Explicit empty strings are respected, so `right: ''` suppresses the regular page right footer.
- Regular page center footer is always the page counter, for example `3 / 188`.

