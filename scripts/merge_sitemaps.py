
import os
from xml.etree import ElementTree as ET

sitemaps_dir = r"D:\limhansin\vision2025\reporthub\public\sitemaps"
merged_path = os.path.join(sitemaps_dir, "sitemap.xml")

root = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for file in os.listdir(sitemaps_dir):
    if file.startswith("sitemap-") and file.endswith(".xml") and file != "sitemap.xml":
        loc = f"https://newspreadnow.com/sitemaps/{file}"
        sm = ET.SubElement(root, "sitemap")
        loc_elem = ET.SubElement(sm, "loc")
        loc_elem.text = loc

tree = ET.ElementTree(root)
tree.write(merged_path, encoding="utf-8", xml_declaration=True)
print("[OK] sitemap.xml 병합 완료")
