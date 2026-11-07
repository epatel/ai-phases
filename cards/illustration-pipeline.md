# illustration-pipeline

How a phase illustration is made: SVG diagram first, then an ElevenLabs generation that "humanizes" it.

## Trigger

A phase's meaning changed, a label is wrong, or an illustration needs a fix.

## Steps

1. Edit the phase in `images/concept-2/diagrams/make_concept.py`, run `make diagrams previews`, and look at `build/previews/phase-N.png`. Get the author's OK on the diagram before spending credits.
2. `make refs` → `build/refs/phase-N.png` (1.6× render, ~50–150 KB).
3. Upload through the ElevenLabs MCP: `creative_create_asset_upload` (exact byte size, `image/png`), `PUT` the bytes to the returned URL, then `creative_finalize_asset_upload` with the flow ID → a reference `node_id`.
4. `creative_generate_image` with `model_id: gpt-image-2`, `generations_count: 1`, `flow_id`, and `connect_from: [<diagram node>, <style node>]`. Prompt template:

   ```
   Turn the FIRST reference image (a clean diagram) into a warm hand-drawn illustration.
   Keep its layout, structure, elements and text labels; spell every label exactly as in
   the diagram. Match the SECOND reference image exactly for drawing style, palette,
   lettering and the developer and robot character designs.
   STYLE: fine pen-and-ink lines, soft watercolour washes in muted dusty blue, lavender,
   sage green and mustard, off-white paper, neat handwritten lettering, thin hand-drawn
   arrows. No halftone dots, no comic caption boxes, no thick black outlines. 16:9.
   CONTENT (phase N): <heading, subtitle, then every element and label from the diagram>
   ```

5. Poll `creative_get_flow_run_status` until `all_completed`. Download `content_url` right away (signed, expires after 2 h) to a scratch folder, look at it, and check every label.
6. Move the old file to `images/concept-2/first-take/` (add a `-vN` suffix if a version is already there), copy the new one in, update the alt text in `blog-post.md`, `make check screenshot`.

## Cheaper route: edit the current illustration

For a small change (a label, one added chip), upload the current `images/concept-2/phase-N.png` as the only reference and prompt "Edit the reference image. Reproduce it EXACTLY … Change ONLY these things: …", listing every label to keep. One reference costs ~420 credits instead of ~655 and keeps the style closest. Used for phases 3 and 4 on 2026-11-07. Still update the SVG diagram so it matches.

## Fixed IDs

- Flow: (ID kept out of the repo)
- Style reference: node (ID kept out of the repo) — the concept-2 phase 2 illustration.
- Characters: developer with spiky brown hair, round glasses, dusty-blue hoodie; stakeholder with neat black hair, pink shirt, mustard tie; AI is a small lavender robot with an antenna.

## Cost

About 185 credits with no reference, 420 with one, 655 with two (2026-10-31 prices). Pass `estimate_only: true` to price a run first.

## Failure modes

- **Never call generate again to retry** — every call that starts is charged.
- "Free generations are busy" / daily free-tier limit: nothing is charged; wait or upgrade (the author upgraded on 2026-10-31).
- The model adds or duplicates elements (phase 4 drew the AI twice until the prompt said "EXACTLY ONE robot … do not add a separate AI badge") and drifts characters (phase 5 stakeholder gained glasses). Check before swapping in, and name the element count explicitly in the prompt.
- Long labels can be misspelled; check each one against the diagram.
