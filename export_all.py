import requests
import xml.etree.ElementTree as ET

def export_sitemap_urls(sitemap_urls, output_file):
    urls = []

    for sitemap_url in sitemap_urls:
        response = requests.get(sitemap_url)
        root = ET.fromstring(response.content)

        for child in root:
            url = child[0].text
            urls.append(url)

    with open(output_file, "w") as file:
        for url in urls:
            file.write(url + "\n")

    print("Os URLs foram exportados para o arquivo:", output_file)

# Exemplo de uso:
sitemap_urls = [
    "https://ecommerce-api.gazin.com.br/v1/publico/integracoes/sitemap/gazin-ecommerce"
]
output_file = "urls.txt"
export_sitemap_urls(sitemap_urls, output_file)
