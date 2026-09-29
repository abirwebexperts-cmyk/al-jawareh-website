# -*- coding: utf-8 -*-
"""
data.py — All site content lives here.
Edit this file to change copy, add brands/categories/locations/blog posts.
build.py reads from this module and generates the static site into dist/.
"""

# ---------------------------------------------------------------------------
# GLOBAL SITE CONFIG
# ---------------------------------------------------------------------------
SITE = {
    "name": "Al Jawareh Auto Spare Parts",
    "short_name": "Al Jawareh",
    "legal_name": "Al Jawareh Auto Spare Parts",
    "domain": "jawarehautoparts.ae",
    "base_url": "https://www.jawarehautoparts.ae",   # canonical host (https + www)
    "tagline": "Genuine & OEM Spare Parts for Premium European & American Vehicles",
    "phone_display": "050 149 4916",
    "phone_intl": "+971 50 149 4916",
    "phone_href": "971501494916",        # tel: value (no +, no spaces)
    "whatsapp": "971501494916",          # wa.me value
    "email": "sales@jawarehautoparts.ae",  # placeholder — confirm real inbox
    "address": {
        "line1": "Shop #4, Sheikh Khalifa Bin Zayed Al Nahyan Rd",
        "line2": "Industrial Area 12",
        "city": "Sharjah",
        "region": "Sharjah",
        "country": "United Arab Emirates",
        "country_code": "AE",
        "postal": "",
    },
    # Approximate coordinates for Industrial Area 12, Sharjah.
    # Replace with the exact pin from Google Maps for perfect accuracy.
    "geo": {"lat": "25.3126", "lng": "55.4370"},
    "maps_query": "Al Jawareh Auto Spare Parts, Industrial Area 12, Sharjah",
    # Opening hours — split shift with an afternoon break, Sat–Thu. Closed Fridays.
    "hours_display": [
        ("Sat – Thu morning", "8:00 AM – 1:00 PM"),
        ("Afternoon break", "1:00 PM – 4:00 PM"),
        ("Sat – Thu evening", "4:00 PM – 9:00 PM"),
        ("Friday", "Closed"),
    ],
    # Structured hours for schema.org (24h, ISO weekday names). Two windows, Sat–Thu.
    "hours_schema": [
        {"days": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "08:00", "closes": "13:00"},
        {"days": ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "16:00", "closes": "21:00"},
    ],
    "founded": "2016",
    "price_range": "$$",
    # Social links — leave blank; fill when available (used in footer + JSON-LD sameAs).
    "social": {
        "facebook": "",
        "instagram": "",
        "tiktok": "",
        "youtube": "",
        "google_business": "",
    },
    "og_image": "/assets/images/site/og-default.jpg",
}

# ---------------------------------------------------------------------------
# BRANDS (marques we stock) — one page each + brand×category pages
# ---------------------------------------------------------------------------
BRANDS = [
    {
        "slug": "range-rover",
        "name": "Range Rover",
        "origin": "British luxury SUV",
        "tagline": "Air suspension, driveline & electronics — sorted.",
        "card": "Genuine & OEM Range Rover parts — air struts, EAS compressors, brakes and more, VIN-matched.",
        "intro": ("Range Rover ownership in the UAE is brilliant until an air suspension fault or a "
                  "timing issue lands on the dash. We keep the parts these SUVs actually need — air "
                  "struts, EAS compressors, timing components, brakes and electronics — and we match "
                  "everything to your VIN so it fits the first time."),
        "models": ["Range Rover Vogue", "Range Rover Sport", "Range Rover Velar",
                   "Range Rover Evoque", "Range Rover (L405 / L460)"],
        "popular": ["Front & rear air struts", "EAS air suspension compressor",
                    "Timing chain kits (5.0 V8)", "Brake pads & discs",
                    "Suspension height sensors", "Water pumps & thermostats"],
        "note": ("Air suspension and timing parts are our highest-turnover Range Rover lines, so "
                 "there's a strong chance yours is in stock or a day away."),
    },
    {
        "slug": "land-rover",
        "name": "Land Rover",
        "origin": "British 4x4 & SUV",
        "tagline": "Defender, Discovery & Freelander — built for the terrain.",
        "card": "OEM Land Rover parts for Discovery, Defender and Freelander — drivetrain, suspension, service parts.",
        "intro": ("From the old-school Defender to the latest Discovery, Land Rovers work hard in UAE "
                  "conditions. We stock the drivetrain, suspension, cooling and service parts that keep "
                  "them going — genuine and quality OEM, matched to your chassis number."),
        "models": ["Land Rover Discovery", "Land Rover Discovery Sport",
                   "Land Rover Defender", "Land Rover Freelander", "Land Rover LR3 / LR4"],
        "popular": ["Air suspension components", "Timing kits & tensioners",
                    "Radiators & cooling parts", "Brake kits", "Control arms & bushings",
                    "Oil, air & fuel filters"],
        "note": ("Tell us your model year and we'll confirm the exact part — Land Rover part numbers "
                 "change often between facelifts."),
    },
    {
        "slug": "jaguar",
        "name": "Jaguar",
        "origin": "British performance & luxury",
        "tagline": "Supercharged V6/V8, precision electronics.",
        "card": "Jaguar spare parts for XE, XF, XJ, F-Pace and F-Type — timing, brakes, electronics.",
        "intro": ("Jaguar shares a lot of DNA with Land Rover, and we source for both. Whether it's a "
                  "supercharged F-Type or a daily XF, we supply timing components, brakes, cooling and "
                  "the electronic modules these cars rely on."),
        "models": ["Jaguar XE", "Jaguar XF", "Jaguar XJ", "Jaguar F-Pace", "Jaguar F-Type", "Jaguar E-Pace"],
        "popular": ["Timing chain kits", "Supercharger components", "Brake pads & discs",
                    "Water pumps & thermostats", "Ignition coils", "Suspension arms"],
        "note": "Send your VIN — Jaguar engines vary a lot by market and we want to get it right.",
    },
    {
        "slug": "mercedes-benz",
        "name": "Mercedes-Benz",
        "origin": "German luxury & performance",
        "tagline": "AIRMATIC, sensors & service parts in stock.",
        "card": "Genuine & OEM Mercedes-Benz parts — AIRMATIC, brakes, filters, sensors for C, E, S, GLC, GLE, G-Class.",
        "intro": ("Mercedes owners want parts that behave exactly like factory — and that's what we "
                  "supply. AIRMATIC struts, brake kits, filters, sensors and electronics for the full "
                  "range, from a C-Class to a G-Wagon, all matched to your chassis number."),
        "models": ["Mercedes-Benz C-Class", "Mercedes-Benz E-Class", "Mercedes-Benz S-Class",
                   "Mercedes-Benz GLC / GLE / GLS", "Mercedes-Benz G-Class", "Mercedes-Benz A-Class / CLA"],
        "popular": ["AIRMATIC air struts", "Brake pads, discs & sensors", "Oil & air filters",
                    "Ignition coils & plugs", "Water pumps", "ABS / wheel speed sensors"],
        "note": "Genuine and premium OEM (Bosch, Mahle, Sachs, ATE) available side by side — your call.",
    },
    {
        "slug": "bmw",
        "name": "BMW",
        "origin": "German performance",
        "tagline": "Cooling, VANOS & electronics — the usual suspects.",
        "card": "BMW spare parts for 3, 5, 7 Series and X models — cooling, VANOS, brakes, electronics.",
        "intro": ("BMWs are precise and they let you know when a part is due. We stock the parts these "
                  "cars are known for — cooling system components, VANOS parts, brakes and electronics — "
                  "across the Series and X ranges, genuine or OEM."),
        "models": ["BMW 3 Series", "BMW 5 Series", "BMW 7 Series",
                   "BMW X1 / X3 / X5 / X7", "BMW M models"],
        "popular": ["Water pumps & thermostats", "Cooling hoses & expansion tanks",
                    "VANOS solenoids & seals", "Brake pads, discs & sensors",
                    "Ignition coils", "Oil filter housings & gaskets"],
        "note": "Cooling parts are the BMW line we move most — often in stock for same-day collection.",
    },
    {
        "slug": "audi",
        "name": "Audi",
        "origin": "German premium",
        "tagline": "quattro drivetrain, DSG & timing.",
        "card": "Audi parts for A3–A8 and Q3–Q8 — timing, DSG, air suspension, brakes and service parts.",
        "intro": ("Audi's quattro drivetrain and TFSI engines need the right parts to stay sharp. We "
                  "supply timing components, DSG parts, air suspension (Q7/Q8), brakes and service items "
                  "for the A and Q ranges, matched to your VIN."),
        "models": ["Audi A3 / A4 / A6 / A8", "Audi Q3 / Q5 / Q7 / Q8", "Audi RS & S models"],
        "popular": ["Timing chain & tensioner kits", "DSG clutches & mechatronics",
                    "Air suspension struts (Q7/Q8)", "Brake kits", "Water pumps",
                    "Ignition coils & carbon-cleaning kits"],
        "note": "For DSG and mechatronic parts, your gearbox code helps us pin the exact unit.",
    },
    {
        "slug": "volkswagen",
        "name": "Volkswagen",
        "origin": "German everyday & SUV",
        "tagline": "TSI/TDI service parts & DSG.",
        "card": "Volkswagen parts for Golf, Passat, Tiguan, Touareg and Teramont — service parts, timing, DSG.",
        "intro": ("Volkswagens are everywhere in the UAE and we keep them running for less. Timing "
                  "components, DSG parts, filters, brakes and the service items these engines need — "
                  "genuine or quality OEM, whatever fits your budget."),
        "models": ["VW Golf / GTI", "VW Passat", "VW Tiguan", "VW Touareg", "VW Teramont"],
        "popular": ["Timing chain kits", "DSG service parts", "Oil, air & fuel filters",
                    "Water pumps & thermostats", "Brake pads & discs", "Ignition coils"],
        "note": "Shared parts with Audi mean fast availability and sharp pricing on most lines.",
    },
    {
        "slug": "porsche",
        "name": "Porsche",
        "origin": "German sports & SUV",
        "tagline": "911, Cayenne & Macan — no compromise parts.",
        "card": "Porsche spare parts for 911, Cayenne, Macan and Panamera — brakes, cooling, suspension.",
        "intro": ("Porsche parts are not the place to cut corners, and we don't. Big-brake components, "
                  "coolant pipes, PASM suspension and service parts for the 911, Cayenne, Macan and "
                  "Panamera — genuine and top-tier OEM only."),
        "models": ["Porsche 911", "Porsche Cayenne", "Porsche Macan", "Porsche Panamera",
                   "Porsche Boxster / Cayman"],
        "popular": ["Brake pads, discs & sensors", "Coolant pipes & water pumps",
                    "PASM suspension components", "Ignition coils & plugs",
                    "Air suspension parts (Cayenne)", "Filters & service kits"],
        "note": "We prioritise genuine and OEM-grade parts for Porsche — quality is non-negotiable here.",
    },
    {
        "slug": "gmc",
        "name": "GMC",
        "origin": "American SUV & pickup",
        "tagline": "Yukon, Sierra & Denali — heavy-duty ready.",
        "card": "GMC parts for Yukon, Sierra, Acadia and Denali — suspension, brakes, electrical, service.",
        "intro": ("For the American side, we stock GMC. Big SUVs and pickups take a beating on UAE "
                  "roads and job sites, so we keep suspension, brakes, electrical and service parts for "
                  "the Yukon, Sierra, Acadia and Denali ready to go."),
        "models": ["GMC Yukon", "GMC Sierra", "GMC Acadia", "GMC Terrain", "GMC Denali"],
        "popular": ["Shocks & suspension parts", "Brake pads & rotors",
                    "Alternators & starters", "Oil & air filters",
                    "Water pumps & radiators", "Ignition & sensors"],
        "note": "American parts source differently — give us the model year and we'll confirm quickly.",
    },
]

# ---------------------------------------------------------------------------
# PART CATEGORIES — one page each + brand×category pages
# ---------------------------------------------------------------------------
CATEGORIES = [
    {
        "slug": "engine-parts",
        "name": "Engine Parts",
        "short": "Engine",
        "icon": "engine",
        "card": "Timing kits, gaskets, water pumps, pistons and everything that keeps the heart running.",
        "intro": ("The engine is where most expensive faults live — and where the right part matters "
                  "most. We supply genuine and OEM engine components matched to your exact VIN, from "
                  "timing kits to complete gasket sets."),
        "items": ["Cylinder heads & gasket sets", "Timing chains, tensioners & guides",
                  "Water pumps & thermostats", "Pistons, rings & bearings",
                  "Belts, pulleys & tensioners", "Oil pumps & sumps",
                  "Turbochargers & superchargers", "Engine mounts"],
    },
    {
        "slug": "suspension-air-struts",
        "name": "Suspension & Air Struts",
        "short": "Suspension",
        "icon": "suspension",
        "card": "Air struts, EAS/AIRMATIC compressors, control arms and bushings — our specialty.",
        "intro": ("Air suspension is the number-one reason UAE owners of Range Rover, Mercedes and Audi "
                  "come to us. We stock air struts, compressors, height sensors and the full mechanical "
                  "suspension range — and we know these systems inside out."),
        "items": ["Front & rear air struts / springs", "EAS & AIRMATIC compressors",
                  "Suspension height / level sensors", "Shock absorbers & dampers",
                  "Control arms & wishbones", "Ball joints & tie rods",
                  "Bushings & mounts", "Anti-roll bar links"],
    },
    {
        "slug": "brakes",
        "name": "Brakes",
        "short": "Brakes",
        "icon": "brakes",
        "card": "Pads, discs, calipers, sensors and hoses — genuine friction that stops properly.",
        "intro": ("Brakes are not a place to gamble. We supply genuine and premium OEM brake components "
                  "— pads, discs, calipers, wear sensors and hoses — for every marque we stock, matched "
                  "to your vehicle."),
        "items": ["Brake pads (front & rear)", "Brake discs / rotors",
                  "Brake calipers & carriers", "Brake wear sensors",
                  "Brake hoses & lines", "Master cylinders", "ABS sensors", "Brake fluid"],
    },
    {
        "slug": "filters-service-parts",
        "name": "Filters & Service Parts",
        "short": "Filters & Service",
        "icon": "filter",
        "card": "Oil, air, fuel and cabin filters, plugs and fluids — everything for a proper service.",
        "intro": ("Regular servicing is the cheapest way to protect a European engine in the UAE heat. "
                  "We keep genuine and OEM filters, spark plugs, and fluids in stock so a full service "
                  "kit is one WhatsApp message away."),
        "items": ["Oil filters", "Air filters", "Fuel filters", "Cabin / AC pollen filters",
                  "Spark plugs & glow plugs", "Engine oil & fluids",
                  "Drain plugs & washers", "Service kits"],
    },
    {
        "slug": "electrical-sensors",
        "name": "Electrical & Sensors",
        "short": "Electrical",
        "icon": "electrical",
        "card": "Batteries, alternators, starters, coils, sensors and modules — diagnostics-matched.",
        "intro": ("Modern European cars are rolling computers, and electrical faults can be baffling. "
                  "We supply alternators, starters, ignition coils, sensors and control modules matched "
                  "to your VIN so the part talks to your car correctly."),
        "items": ["Batteries", "Alternators & starters", "Ignition coils & packs",
                  "ABS / wheel speed sensors", "Camshaft & crankshaft sensors",
                  "Oxygen (O2) sensors", "Control modules & relays", "Wiring & connectors"],
    },
    {
        "slug": "body-panels-lights",
        "name": "Body Panels & Lights",
        "short": "Body & Lights",
        "icon": "body",
        "card": "Bumpers, fenders, mirrors, grilles, headlights and taillights — OEM fit and finish.",
        "intro": ("After a knock, you want panels and lights that line up and look factory. We source "
                  "bumpers, fenders, mirrors, grilles and lighting for every marque we carry — genuine "
                  "or OEM, matched to your model and trim."),
        "items": ["Front & rear bumpers", "Fenders & wings", "Bonnets & doors",
                  "Side mirrors & glass", "Grilles & trims", "Headlights & modules",
                  "Tail lights", "Fog lights & DRLs"],
    },
    {
        "slug": "transmission-drivetrain",
        "name": "Transmission & Drivetrain",
        "short": "Transmission",
        "icon": "transmission",
        "card": "Gearboxes, DSG parts, clutches, driveshafts and differentials — power to the ground.",
        "intro": ("Whether it's a DSG, a torque-converter auto or a transfer case, drivetrain parts "
                  "have to be exact. We supply gearbox components, clutches, mechatronics, driveshafts "
                  "and differentials matched to your gearbox code and VIN."),
        "items": ["Gearboxes & transfer cases", "DSG clutches & mechatronics",
                  "Clutch kits & flywheels", "Driveshafts & CV joints",
                  "Differentials & mounts", "Transmission mounts",
                  "Gearbox oil & seals", "Prop shafts"],
    },
    {
        "slug": "cooling-ac",
        "name": "Cooling & AC",
        "short": "Cooling & AC",
        "icon": "cooling",
        "card": "Radiators, water pumps, condensers and AC compressors — vital in UAE heat.",
        "intro": ("In UAE temperatures, cooling and AC parts are safety and comfort items, not luxuries. "
                  "We stock radiators, water pumps, condensers, AC compressors and hoses for the full "
                  "range of marques we carry."),
        "items": ["Radiators", "Water pumps & thermostats", "Cooling fans & modules",
                  "Expansion tanks & caps", "Coolant hoses & pipes",
                  "AC compressors", "AC condensers", "AC expansion valves & driers"],
    },
    {
        "slug": "steering",
        "name": "Steering",
        "short": "Steering",
        "icon": "steering",
        "card": "Racks, pumps, tie rods and linkages — precise steering, restored.",
        "intro": ("Vague or heavy steering usually means a worn rack, pump or linkage. We supply "
                  "steering racks, power steering pumps, tie rods and linkages matched to your vehicle "
                  "so the wheel feels right again."),
        "items": ["Steering racks & boxes", "Power steering pumps",
                  "Electric power steering motors", "Tie rods & rod ends",
                  "Steering linkages & couplings", "Steering pump hoses",
                  "Idler & pitman arms", "Steering fluid"],
    },
]

# ---------------------------------------------------------------------------
# LOCATIONS — UAE areas for local SEO
# ---------------------------------------------------------------------------
LOCATIONS = [
    {
        "slug": "sharjah",
        "name": "Sharjah",
        "is_home": True,
        "intro": ("We're based in Industrial Area 12, Sharjah — right where the trade lives. Walk in, "
                  "collect the same day, or send us the part on WhatsApp and we'll have it ready."),
        "detail": ("Sharjah is home turf. Our shop on Sheikh Khalifa Bin Zayed Al Nahyan Road carries "
                   "the fast-moving parts for Range Rover, Mercedes, BMW, Audi and more in stock, with "
                   "same-day collection across the city."),
        "areas": ["Industrial Area", "Al Nahda", "Muwaileh", "Al Qasimia", "Al Taawun", "University City"],
        "delivery": "Same-day collection or delivery across Sharjah.",
    },
    {
        "slug": "dubai",
        "name": "Dubai",
        "is_home": False,
        "intro": ("Dubai owners get the same parts and pricing as Sharjah, delivered. We're a short "
                  "hop up the road and we deliver across the city daily."),
        "detail": ("From Deira to Downtown to the Marina, we deliver genuine and OEM parts across Dubai. "
                   "Send your VIN and part on WhatsApp and we'll quote, confirm and dispatch — no need "
                   "to drive to Sharjah."),
        "areas": ["Deira", "Bur Dubai", "Al Quoz", "Business Bay", "Dubai Marina", "Ras Al Khor"],
        "delivery": "Daily delivery to Dubai; typically same or next day.",
    },
    {
        "slug": "ajman",
        "name": "Ajman",
        "is_home": False,
        "intro": ("Ajman is minutes from our Sharjah shop, so parts arrive fast — often the same day."),
        "detail": ("We serve Ajman daily with genuine and OEM parts for European and American vehicles. "
                   "Being right next door in Sharjah means quick delivery and easy collection."),
        "areas": ["Al Jerf", "Al Nuaimiya", "Al Rashidiya", "Al Mowaihat", "Ajman Industrial Area"],
        "delivery": "Fast same-day / next-day delivery to Ajman.",
    },
    {
        "slug": "abu-dhabi",
        "name": "Abu Dhabi",
        "is_home": False,
        "intro": ("Abu Dhabi is well within our delivery network — send the details and we'll get your "
                  "part to the capital."),
        "detail": ("We deliver genuine and OEM spare parts across Abu Dhabi and the surrounding areas. "
                   "For harder-to-find European parts, we're worth the message — we source what local "
                   "shops often can't."),
        "areas": ["Abu Dhabi City", "Musaffah", "Khalifa City", "Mussafah Industrial", "Al Reem Island"],
        "delivery": "Delivery to Abu Dhabi; usually next day.",
    },
    {
        "slug": "ras-al-khaimah",
        "name": "Ras Al Khaimah",
        "is_home": False,
        "intro": ("RAK owners can order any part we stock and have it delivered north."),
        "detail": ("We supply Ras Al Khaimah with genuine and OEM parts for Range Rover, Mercedes, BMW, "
                   "Audi, Porsche and more. Message us the part and we'll arrange delivery to RAK."),
        "areas": ["Al Nakheel", "Al Hamra", "Al Dhait", "RAK Industrial Area", "Julphar"],
        "delivery": "Delivery to Ras Al Khaimah, usually next day.",
    },
    {
        "slug": "umm-al-quwain",
        "name": "Umm Al Quwain",
        "is_home": False,
        "intro": ("UAQ is on our northern delivery route — order and we'll bring it to you."),
        "detail": ("Umm Al Quwain customers get the same genuine and OEM parts and pricing, delivered. "
                   "Send your vehicle details and part on WhatsApp for a quick quote."),
        "areas": ["UAQ City", "Al Salamah", "Al Raas", "UAQ Industrial Area"],
        "delivery": "Delivery to Umm Al Quwain, usually next day.",
    },
    {
        "slug": "fujairah",
        "name": "Fujairah",
        "is_home": False,
        "intro": ("Fujairah on the east coast is covered by our delivery network."),
        "detail": ("We deliver genuine and OEM spare parts to Fujairah for European and American "
                   "vehicles. For parts the local market rarely stocks, we're the shortcut — message us."),
        "areas": ["Fujairah City", "Dibba", "Al Faseel", "Fujairah Industrial Area"],
        "delivery": "Delivery to Fujairah; allow one to two days.",
    },
    {
        "slug": "al-ain",
        "name": "Al Ain",
        "is_home": False,
        "intro": ("Al Ain owners can order the full range and have it delivered inland."),
        "detail": ("We supply Al Ain with genuine and OEM parts across all the marques we carry. Send "
                   "your VIN and part on WhatsApp and we'll quote and dispatch."),
        "areas": ["Al Ain City", "Al Jimi", "Al Muwaiji", "Al Ain Industrial Area", "Al Hili"],
        "delivery": "Delivery to Al Ain; usually next day.",
    },
]

# ---------------------------------------------------------------------------
# GLOBAL FAQs — used on /faq/ and home (subset)
# ---------------------------------------------------------------------------
FAQS = [
    ("Do you sell genuine or aftermarket parts?",
     "Both. We stock genuine (OEM manufacturer) parts and premium OEM-supplier equivalents from names "
     "like Bosch, Mahle, ATE and Sachs. Tell us your budget and we'll show you the best options for "
     "your car — no pressure, no surprises."),
    ("How do I order a part?",
     "The fastest way is WhatsApp. Send us your vehicle (make, model, year), your VIN or chassis number "
     "if you have it, and the part you need. We'll confirm the exact part, quote you, and once you "
     "approve, we deliver or hold it for collection."),
    ("Can you find a part from my VIN or chassis number?",
     "Yes — that's the best way to get it right. Your VIN tells us the exact specification of your car, "
     "so we can match the correct part number the first time and avoid returns."),
    ("Do you deliver across the UAE?",
     "Yes. We're in Sharjah and deliver to Dubai, Ajman, Abu Dhabi, Ras Al Khaimah, Umm Al Quwain, "
     "Fujairah and Al Ain. Nearby emirates are often same or next day."),
    ("Do you offer a warranty on parts?",
     "Warranty depends on the part and whether it's genuine or OEM — many carry a manufacturer or "
     "supplier warranty. We'll tell you the exact terms before you buy so there are no grey areas."),
    ("What payment methods do you accept?",
     "Cash, card and bank transfer are all fine. For deliveries we'll confirm the payment method when "
     "we quote you."),
    ("Can you supply a part you don't have in stock?",
     "Almost always. If it's not on the shelf, we source it through our supplier network — genuine or "
     "OEM — and give you a realistic timeline before you commit."),
    ("Do you ship internationally?",
     "We focus on the UAE, but for larger or bulk orders we can arrange export shipping. Message us "
     "the details and we'll let you know what's possible."),
    ("What are your opening hours?",
     "Saturday to Thursday, 9:00 AM to 9:00 PM, and Friday from 2:00 PM to 9:00 PM. WhatsApp messages "
     "are welcome any time and we'll reply during working hours."),
    ("Where are you located?",
     "Shop #4, Sheikh Khalifa Bin Zayed Al Nahyan Road, Industrial Area 12, Sharjah, UAE. There's a "
     "map on our contact page."),
]

# ---------------------------------------------------------------------------
# BLOG POSTS — unique buying / fitment guides
# ---------------------------------------------------------------------------
POSTS = [
    {
        "slug": "find-the-right-part-using-vin-chassis-number",
        "title": "How to Find the Right Car Part Using Your VIN or Chassis Number",
        "excerpt": ("Your VIN is the single most useful thing you can send us. Here's what it is, where "
                    "to find it, and why it stops you buying the wrong part."),
        "date": "2026-08-28",
        "category": "Buying Guide",
        "read_time": "5 min read",
        "body": [
            ("p", "Ordering the wrong part is the most common — and most frustrating — mistake in car "
                  "repairs. The fix is simple: send your VIN. Here's why it matters and how to find it."),
            ("h2", "What is a VIN?"),
            ("p", "The VIN (Vehicle Identification Number) is a 17-character code unique to your car. "
                  "It encodes the exact model, engine, transmission, market and build specification. Two "
                  "cars that look identical can take different parts — the VIN is how we tell them apart."),
            ("h2", "Where to find your VIN or chassis number"),
            ("ul", ["On the registration (Mulkiya) card", "At the base of the windscreen on the "
                    "driver's side", "On a sticker inside the driver's door jamb",
                    "Stamped on the chassis in the engine bay (on many models)"]),
            ("h2", "Why we ask for it"),
            ("p", "European cars in particular change part numbers between facelifts and even within a "
                  "single model year. A brake sensor, a water pump or an air strut may have three or four "
                  "variants. Your VIN lets us match the exact one, so it fits the first time and you "
                  "don't waste days on a return."),
            ("h2", "What to send us"),
            ("p", "For the quickest quote, message us your make, model and year, your VIN or chassis "
                  "number, and the part you need. A photo of the old part or the fault code also helps."),
        ],
    },
    {
        "slug": "genuine-vs-oem-vs-aftermarket-parts",
        "title": "Genuine vs OEM vs Aftermarket Parts: What's the Difference?",
        "excerpt": ("Three words that confuse everyone — and quietly decide how much you pay and how "
                    "long the part lasts. Here's the plain-English version."),
        "date": "2026-08-20",
        "category": "Buying Guide",
        "read_time": "6 min read",
        "body": [
            ("p", "\"Is it genuine?\" is the first question most customers ask. But there are really "
                  "three categories, and understanding them saves you money without gambling on quality."),
            ("h2", "Genuine (OEM-branded) parts"),
            ("p", "These carry the car manufacturer's own branding and box — a Mercedes part in a "
                  "Mercedes box. They're made to exact factory spec and usually carry the longest "
                  "warranty. They're also the most expensive."),
            ("h2", "OEM (original equipment manufacturer) parts"),
            ("p", "Here's the part most people don't know: many \"genuine\" parts are actually made by "
                  "specialist suppliers like Bosch, Mahle, ATE, Sachs or ZF — the same companies the "
                  "car maker uses on the production line. Bought under the supplier's own brand, an OEM "
                  "part is often the identical component for noticeably less money."),
            ("h2", "Aftermarket parts"),
            ("p", "Made by third parties, aftermarket parts range from excellent to poor. For some "
                  "items they're a smart budget choice; for others — brakes, suspension, anything "
                  "safety-related — we'd steer you toward genuine or OEM."),
            ("h2", "So which should you buy?"),
            ("ul", ["Safety-critical parts (brakes, steering, suspension): genuine or top OEM",
                    "Service items (filters, plugs): quality OEM is usually the sweet spot",
                    "Older or higher-mileage cars: OEM keeps costs sensible without cutting quality"]),
            ("p", "We stock all three where it makes sense and we'll always tell you which is which. "
                  "Message us your car and part and we'll lay out the options honestly."),
        ],
    },
    {
        "slug": "range-rover-air-suspension-problems-guide",
        "title": "Range Rover Air Suspension Problems & Replacement Guide",
        "excerpt": ("Sitting low in the morning? A warning on the dash? Air suspension is the classic "
                    "Range Rover fault. Here's what fails and what it costs to fix properly."),
        "date": "2026-08-12",
        "category": "Fitment Guide",
        "read_time": "7 min read",
        "body": [
            ("p", "If you own a Range Rover in the UAE, air suspension is the system most likely to need "
                  "attention — and the one owners ask us about most. Here's how it fails and how to fix "
                  "it without overspending."),
            ("h2", "Common symptoms"),
            ("ul", ["The car sits low on one corner or drops overnight",
                    "A \"suspension fault\" or \"vehicle too low\" message",
                    "Harsh ride or the car refusing to raise",
                    "The compressor running longer and louder than usual"]),
            ("h2", "What actually fails"),
            ("p", "Three parts cause most air suspension problems. Air struts (bags) perish and leak "
                  "with age and heat — UAE conditions are hard on them. The EAS compressor wears out, "
                  "often because it's been overworking to keep up with a leaking strut. And height "
                  "sensors or valve blocks can send bad signals that confuse the system."),
            ("h2", "Fix it once, properly"),
            ("p", "The mistake we see most is replacing one leaking strut and ignoring a tired "
                  "compressor — which then fails weeks later. If your car has covered serious mileage, "
                  "it's often smarter to replace struts in pairs and check the compressor at the same "
                  "time. We can advise based on your mileage and symptoms."),
            ("h2", "Parts we keep in stock"),
            ("p", "Front and rear air struts, EAS compressors, height sensors and valve blocks are "
                  "among our fastest-moving Range Rover lines — genuine and quality OEM. Send us your "
                  "VIN and symptoms and we'll tell you exactly what you need."),
        ],
    },
    {
        "slug": "how-to-order-car-parts-on-whatsapp-uae",
        "title": "How to Order Car Parts on WhatsApp in the UAE",
        "excerpt": ("No forms, no phone tag. Here's the fastest way to get a part quoted and delivered "
                    "anywhere in the UAE."),
        "date": "2026-08-05",
        "category": "How-To",
        "read_time": "4 min read",
        "body": [
            ("p", "Ordering parts should take two minutes, not two phone calls. WhatsApp is the fastest "
                  "way to reach us — here's how to make it quick and accurate."),
            ("h2", "Step 1 — Send your vehicle details"),
            ("p", "Make, model and year to start. If you have your VIN or chassis number, send that too "
                  "— it lets us match the exact part and skip the guesswork."),
            ("h2", "Step 2 — Tell us the part"),
            ("p", "Name the part, or just describe the problem — \"front brakes squealing\" or \"car "
                  "sitting low on the left\" is enough for us to point you right. A photo of the old "
                  "part or a fault code helps even more."),
            ("h2", "Step 3 — Get your quote"),
            ("p", "We confirm the correct part, tell you whether it's genuine or OEM, and quote you. "
                  "No obligation — you decide."),
            ("h2", "Step 4 — Delivery or collection"),
            ("p", "Once you approve, we deliver anywhere in the UAE or hold it for collection at our "
                  "Sharjah shop. Nearby emirates are often same or next day."),
            ("p", "Use the \"Request a part\" button anywhere on this site — it opens WhatsApp with the "
                  "details already filled in for you."),
        ],
    },
    {
        "slug": "mercedes-benz-service-parts-when-to-replace",
        "title": "Mercedes-Benz Service Parts: When to Replace Filters, Brakes & Fluids",
        "excerpt": ("A simple maintenance rhythm keeps a Mercedes reliable in UAE heat. Here's what to "
                    "replace and roughly when."),
        "date": "2026-07-29",
        "category": "Maintenance",
        "read_time": "6 min read",
        "body": [
            ("p", "Mercedes engineering is superb, but UAE heat and dust are demanding. Staying ahead of "
                  "servicing is the cheapest way to keep a Mercedes trouble-free. Here's a practical "
                  "guide to the main service parts."),
            ("h2", "Oil & oil filter"),
            ("p", "In this climate, don't stretch oil changes. Fresh oil and a genuine or OEM oil "
                  "filter at the recommended interval protect the engine from heat stress far better "
                  "than pushing the mileage."),
            ("h2", "Air & cabin filters"),
            ("p", "Dust clogs air filters faster here than in cooler climates — a restricted filter "
                  "hurts performance and economy. The cabin filter matters too: replace it to keep the "
                  "AC blowing clean, cold air."),
            ("h2", "Brakes"),
            ("p", "Stop-start city driving wears pads quickly. Replace pads when they're low and check "
                  "discs at the same time — and don't ignore the wear sensor warning, it's there for a "
                  "reason."),
            ("h2", "Fluids"),
            ("ul", ["Coolant — critical in UAE heat; check level and condition",
                    "Brake fluid — absorbs moisture over time and should be refreshed periodically",
                    "Transmission fluid — many owners forget it; fresh fluid protects the gearbox"]),
            ("p", "We keep genuine and OEM Mercedes service parts in stock — filters, pads, plugs and "
                  "fluids. Message us your model and we'll build you a service kit."),
        ],
    },
    {
        "slug": "bmw-common-parts-to-replace-after-100000-km",
        "title": "BMW Common Parts to Replace After 100,000 km",
        "excerpt": ("Past 100k, certain BMW parts become predictable. Knowing them lets you plan repairs "
                    "instead of being ambushed by them."),
        "date": "2026-07-22",
        "category": "Fitment Guide",
        "read_time": "6 min read",
        "body": [
            ("p", "BMWs are rewarding to drive and, past 100,000 km, fairly predictable to maintain — "
                  "if you know what tends to go. Here are the parts we supply most for higher-mileage "
                  "BMWs in the UAE."),
            ("h2", "Cooling system"),
            ("p", "The BMW cooling system is the classic weak point, especially in UAE heat. Water "
                  "pumps, thermostats, expansion tanks and hoses become brittle and fail with age. "
                  "Replacing them proactively is far cheaper than an overheating event."),
            ("h2", "Oil filter housing gasket & valve cover"),
            ("p", "Oil leaks from the filter housing gasket and valve cover gasket are extremely common "
                  "past 100k. They're not disasters, but left alone they make a mess and can drip onto "
                  "belts and sensors."),
            ("h2", "VANOS & ignition"),
            ("p", "VANOS solenoids and seals can cause rough running and codes with age. Ignition coils "
                  "also have a service life — a misfire past 100k is often a tired coil."),
            ("h2", "Suspension & brakes"),
            ("ul", ["Control arm bushings — worn bushings cause vague steering and uneven tyre wear",
                    "Brake pads, discs and sensors — routine but due more often with spirited driving"]),
            ("p", "We stock these BMW lines genuine and OEM. Send your model, year and mileage and we'll "
                  "tell you what's worth doing now versus later."),
        ],
    },
]
