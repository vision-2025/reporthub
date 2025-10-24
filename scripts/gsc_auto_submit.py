import os, requests, json

SITEMAPS = [
  "https://us.newspreadnow.com/sitemap.xml", "https://uk.newspreadnow.com/sitemap.xml",
  "https://ca.newspreadnow.com/sitemap.xml", "https://au.newspreadnow.com/sitemap.xml",
  "https://de.newspreadnow.com/sitemap.xml", "https://ch.newspreadnow.com/sitemap.xml",
  "https://sg.newspreadnow.com/sitemap.xml", "https://no.newspreadnow.com/sitemap.xml",
  "https://se.newspreadnow.com/sitemap.xml", "https://nl.newspreadnow.com/sitemap.xml",
  "https://dk.newspreadnow.com/sitemap.xml", "https://jp.newspreadnow.com/sitemap.xml",
  "https://kr.newspreadnow.com/sitemap.xml", "https://fr.newspreadnow.com/sitemap.xml",
  "https://it.newspreadnow.com/sitemap.xml", "https://es.newspreadnow.com/sitemap.xml",
  "https://be.newspreadnow.com/sitemap.xml", "https://ae.newspreadnow.com/sitemap.xml",
  "https://nz.newspreadnow.com/sitemap.xml", "https://fi.newspreadnow.com/sitemap.xml",
  "https://br.newspreadnow.com/sitemap.xml", "https://pl.newspreadnow.com/sitemap.xml",
  "https://sa.newspreadnow.com/sitemap.xml", "https://mx.newspreadnow.com/sitemap.xml"
]

API_KEY = os.getenv("GSC_API_KEY")

for sitemap in SITEMAPS:
    endpoint = f"https://www.googleapis.com/webmasters/v3/sites/{sitemap}/sitemaps/{sitemap}?key={API_KEY}"
    res = requests.put(endpoint)
    print(f"[{'OK' if res.status_code==200 else 'ERROR'}] {sitemap} → {res.status_code}")
