# AVB Academy English–German Translation Guidelines

## 1. Purpose
These guidelines ensure consistency, clarity, and technical accuracy in translations from English to German for AVB Academy content.
They are written in English to provide a clear reference for translators and technical reviewers.

## 2. Structure
The markdown files can be found in the `content` folder. Each file follows the `<filename>.<language>.md` structure.

The currently used languages are English (`en`) and German (`de`) 

```
├── content
│   ├── 00_introduction-to-audio-networks
│   ├── 01_milan
│   ├── 02_user-guides
│   ├── 03_about
│   ├── 04_milan-myths
│   ├── _index.de.md
│   ├── _index.en.md
│   ├── blog
│   ├── glossary
│   ├── imprint.en.md
│   └── licensing.en.md
├── data
│   ├── global_references.yaml
│   └── glossary.yaml
```

## 3. General Principles

- Focus on **meaning over literal translation** — prioritize technical accuracy.
- Maintain **clarity and readability** for German-speaking technical audiences.
- Respect **AVB, TSN and IEEE terminology**, keeping standard terms in English when appropriate.
- Use Hugo **tooltips** (`{{< tooltip "Term">}}`) for glossary-linked terms whenever possible, especially on their **first occurrence**.
- Keep tone **educational, professional, and accessible**.

## 4. Terminology Rules

### 4.1. Terms That Should Not Be Translated
Do **not** translate official standards, acronyms, or protocol names. Keep them in English and apply a **tooltip** to ensure readers can access glossary definitions.

Examples (use tooltip on first mention in German text):
- `{{< tooltip "AVB">}}`
- `{{< tooltip "TSN">}}`
- `{{< tooltip "gPTP">}}`
- `{{< tooltip "SRP">}}`
- `{{< tooltip "MSRP">}}`
- ...

## 5. Style and Tone

- Write in **formal but approachable German**.
- Maintain an **educational and technical** tone: clear, direct, and informative.
- Prefer **active voice** where possible.
- Keep sentences **concise** and avoid unnecessary complexity.
- Mirror the structure of the English source where it helps clarity, but adapt idiomatically to natural German.
- Avoid repeatedly showing English and German forms; introduce once (with tooltip) and then use the chosen form consistently.

## 6. Hugo Tooltip Integration

### 6.1. When to Use Tooltips
- Use a tooltip on the **first occurrence** of any technical or AVB-specific term.
- Subsequent mentions can omit the tooltip unless the term reappears after a long section or would benefit from quick re-linking.
- Prefer tooltips for:
  - Acronyms and standards (AVB, TSN, ...)
  - Complex terms that have glossary entries

### 6.2. Syntax and Examples
Use the same shortcode style used on the site. Example (English source and the German translation):

English source:
```
Time-Sensitive Networking (TSN) is a set of {{< tooltip "IEEE">}} standards that extend standard Ethernet to support real-time, deterministic communication.
```

German translation:
```
Time-Sensitive Networking (TSN) ist eine Sammlung aus {{< tooltip "IEEE">}} Spezifikationen um Standard Ethernet für Echtzeit- und deterministische Kommunikation zu erweitern.
```

When a tooltiped English term is combined into a German compound, hyphenate for readability:
Example:
`{{< tooltip "AVB">}}-Streams“ or „{{< tooltip "Milan">}}-Netzwerk`

### 6.3. Nested or Repeated Terms
- Avoid excessive tooltip clutter in sentences with many technical terms; prioritize the most important or least obvious terms.
- If a sentence contains multiple tooltip candidates, ensure readability—use tooltips for the terms that benefit most from a glossary link and omit for very common terms already defined earlier.

## 7. Formatting Conventions

- Introduce English technical terms in the German text with a tooltip on first mention:
  Example: `{{< tooltip "SRP">}} (Stream Reservation Protocol)`
- When joining English terms into German compounds, prefer hyphenation:
  Example: `{{< tooltip "AVB">}}-Stream`, `{{< tooltip "Milan">}}-Netzwerk`
- Use sentence case for headings unless the site style requires otherwise.
- Use code fences for command line snippets or config examples; do not apply tooltips inside code blocks (tooltips belong in prose).
- Keep inline code (e.g., `IEEE 802.1AS`) unaltered.
- Maintain consistent punctuation and spacing around shortcodes (follow site conventions; examples above use `{{< tooltip "Term">}}`).
- The glossary source file is `data/glossary.yaml`.

## 8. Consistency
- Keep a shared **termbase** (see Termbase Template below) and reuse approved translations.
- When in doubt, consult a technical reviewer familiar with AVB/TSN.
- Record new approved terms in the central termbase and update glossary entries accordingly.

## 9. Example Translations

**English Source:**  
`{{< tooltip "AVB">}} ensures precise time synchronization across all devices in a network.`

**German Translation:**  
`{{< tooltip "AVB">}} gewährleistet eine präzise Taktsynchronisation aller Geräte im Netzwerk.`

---

**English Source:**  
`The Stream Reservation Protocol (SRP) manages bandwidth allocation for AVB streams.`

**German Translation:**  
`Das Stream Reservation Protocol (SRP) verwaltet die Bandbreitenzuweisung für {{< tooltip "AVB">}}-Streams.`


## 10. Review Process

- Each translation should be **peer-reviewed** by a native German speaker with technical knowledge of AVB/TSN.
- Reviewers should confirm:
  - Technical accuracy
  - Correct tooltip usage and glossary linkage
  - Stylistic consistency and tone
- After approval, update the termbase with any new or changed translations.

## 11. Summary / Quick Checklist

- ✅ Guidelines written in English for translators and reviewers.  
- ✅ Use tooltips `{{< tooltip "Term">}}` on first mention of technical, brand, and standard terms.  
- ✅ Keep standards and acronyms in English; provide short German explanations if helpful.  
- ✅ Use standard German technical vocabulary where appropriate.  
- ✅ Hyphenate English terms when forming German compounds (e.g., `{{< tooltip "AVB">}}-Streams`).  
- ✅ Peer-review every translation and update the shared termbase.

## 12. Termbase
Please refer to the [Termbase-English-German](data/termbase.yaml) for the complete termbase. In case you need to update the termbase, please include it in your PR. The general idea is to use the `{{< termbase "TERM">}}` shortcode to have consistent translation between languages.

Use standard German technical vocabulary for general networking or AV terms; where industry usage prefers the English word, prefer that.

| English Term            | Preferred German         | Notes |
|-------------------------|--------------------------|-------|
| Stream                  | Stream                   | Commonly used as-is |
| Network                 | Netzwerk                 | Standard translation |
| Latency                 | Latenz                   | Standard technical term |
| Bandwidth               | Bandbreite               | Translate |
| Clock synchronization   | Taktsynchronisation      | Translate |
| Packet                  | Paket                    | Translate |
| Port                    | Port                     | Kept in English |
| Bridge                  | Bridge                   | Keep in AVB context |
| Audio stream            | Audiostream              | Compound word |
| Video stream            | Videostream              | Compound word |
