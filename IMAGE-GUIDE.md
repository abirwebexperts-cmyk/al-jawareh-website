# Image guide

Every photo the site can use, with the **exact filename** and a **recommended size**. Drop files at the paths below, then rebuild (`python3 build.py`) and redeploy.

The site never breaks without these — until a file exists, that spot shows a clean, branded placeholder. Add them whenever you're ready, in any order.

**Format tips**

- Photos: JPG, optimised for web (aim for under ~300 KB each). Shoot or crop to the ratio shown.
- Logos: SVG is best (crisp at any size). A transparent PNG works too.
- Keep the filenames **exactly** as written — the site looks for these names.

---

## Brand logos  ·  `assets/images/brands/`

Shown on each brand page in the logo slot. Transparent background. Only upload logos you're licensed to use — until then the brand name shows as text.

| File | Recommended |
|------|-------------|
| `range-rover-logo.svg` | SVG, or PNG ~400×120, transparent |
| `land-rover-logo.svg` | SVG, or PNG ~400×120, transparent |
| `jaguar-logo.svg` | SVG, or PNG ~400×120, transparent |
| `mercedes-benz-logo.svg` | SVG, or PNG ~400×120, transparent |
| `bmw-logo.svg` | SVG, or PNG ~400×120, transparent |
| `audi-logo.svg` | SVG, or PNG ~400×120, transparent |
| `volkswagen-logo.svg` | SVG, or PNG ~400×120, transparent |
| `porsche-logo.svg` | SVG, or PNG ~400×120, transparent |
| `gmc-logo.svg` | SVG, or PNG ~400×120, transparent |

## Brand photos  ·  `assets/images/brands/`

The hero image on each brand page. A clean shot of the car or a relevant part works well.

| File | Recommended |
|------|-------------|
| `range-rover-hero.jpg` | 1200×900 (4:3) |
| `land-rover-hero.jpg` | 1200×900 (4:3) |
| `jaguar-hero.jpg` | 1200×900 (4:3) |
| `mercedes-benz-hero.jpg` | 1200×900 (4:3) |
| `bmw-hero.jpg` | 1200×900 (4:3) |
| `audi-hero.jpg` | 1200×900 (4:3) |
| `volkswagen-hero.jpg` | 1200×900 (4:3) |
| `porsche-hero.jpg` | 1200×900 (4:3) |
| `gmc-hero.jpg` | 1200×900 (4:3) |

## Part-category photos  ·  `assets/images/categories/`

Used on the brand×category pages (e.g. *Range Rover Brakes*). One good photo per category.

| File | Recommended |
|------|-------------|
| `engine-parts.jpg` | 1200×900 (4:3) |
| `suspension-air-struts.jpg` | 1200×900 (4:3) |
| `brakes.jpg` | 1200×900 (4:3) |
| `filters-service-parts.jpg` | 1200×900 (4:3) |
| `electrical-sensors.jpg` | 1200×900 (4:3) |
| `body-panels-lights.jpg` | 1200×900 (4:3) |
| `transmission-drivetrain.jpg` | 1200×900 (4:3) |
| `cooling-ac.jpg` | 1200×900 (4:3) |
| `steering.jpg` | 1200×900 (4:3) |

## Blog images  ·  `assets/images/blog/`

The header image for each guide (also used on cards and social shares).

| File | Recommended |
|------|-------------|
| `find-the-right-part-using-vin-chassis-number.jpg` | 1600×900 (16:9) |
| `genuine-vs-oem-vs-aftermarket-parts.jpg` | 1600×900 (16:9) |
| `range-rover-air-suspension-problems-guide.jpg` | 1600×900 (16:9) |
| `how-to-order-car-parts-on-whatsapp-uae.jpg` | 1600×900 (16:9) |
| `mercedes-benz-service-parts-when-to-replace.jpg` | 1600×900 (16:9) |
| `bmw-common-parts-to-replace-after-100000-km.jpg` | 1600×900 (16:9) |

## Site images  ·  `assets/images/site/`

| File | Recommended | Notes |
|------|-------------|-------|
| `favicon.svg` | vector | Already shipped. The browser-tab icon. |
| `favicon.ico` | 16/32/48 px | Auto-generated if Pillow is installed. |
| `apple-touch-icon.png` | 180×180 | Auto-generated. Home-screen icon on iPhone/iPad. |
| `logo.png` | 512×512 | Auto-generated. Used in structured data. |
| `og-default.jpg` | 1200×630 | Auto-generated share image. Replace with a branded photo if you like. |

> The four auto-generated files appear only if you have Pillow (`pip install Pillow`) when you run the build. Otherwise add them by hand — the vector `favicon.svg` already covers the tab icon.

---

### After adding images

```bash
python3 build.py     # copies assets into dist/
git add -A && git commit -m "Add images" && git push
# then in cPanel: Update from Remote → Deploy HEAD Commit
```
