import requests
import xml.etree.ElementTree as ET

def export_sitemap_urls(sitemap_urls):
    for index, sitemap_url in enumerate(sitemap_urls, start=1):
        response = requests.get(sitemap_url)
        root = ET.fromstring(response.content)

        urls = []
        for child in root:
            url = child[0].text
            urls.append(url)

        output_file = f"sitemap{index}_urls.txt"
        with open(output_file, "w") as file:
            for url in urls:
                file.write(url + "\n")

        print("Os URLs foram exportados para o arquivo:", output_file)

# Exemplo de uso:
sitemap_urls = [
    "https://www.pensefarma.com.br/sitemap/brand-0.xml",
    "https://www.pensefarma.com.br/sitemap/category-0.xml",
    "https://www.pensefarma.com.br/sitemap/subcategory-0.xml",
    "https://www.pensefarma.com.br/sitemap/userRoute-0.xml",
    "https://www.pensefarma.com.br/sitemap/department-0.xml",
    "https://www.pensefarma.com.br/sitemap/product-0.xml",
    "https://www.pensefarma.com.br/sitemap/product-1.xml",
    "https://www.pensefarma.com.br/sitemap/product-2.xml",
    "https://www.pensefarma.com.br/sitemap/categories-sitemap.xml",
]
export_sitemap_urls(sitemap_urls)
