import requests
from bs4 import BeautifulSoup
import time

# 入力ファイル（ファイル名は適宜変更してください。）
input_file = "pubmed_url.txt"
# 出力HTMLファイル（ファイル名は適宜変更してください。）
output_file = "DevelopmentSmallScaleSystemPRM.html"

def fetch_pubmed_metadata(url):
    """PubMed URLからメタデータを取得してHTML要素を返す"""
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # タイトル
    title_tag = soup.find("h1", class_="heading-title")
    title = title_tag.get_text(strip=True) if title_tag else "タイトル不明"

    # 著者
    authors = []
    author_tags = soup.select("div.authors-list span.authors-list-item > a")
    for a in author_tags:
        authors.append(a.get_text(strip=True))
    authors_str = "; ".join(authors) if authors else "著者情報不明"

    # ジャーナル情報
    journal_info_tag = soup.find("button", class_="journal-actions-trigger")
    journal_info = journal_info_tag.get_text(strip=True) if journal_info_tag else "ジャーナル情報不明"

    # DOI
    doi_tag = soup.find("span", class_="citation-doi")
    doi = doi_tag.get_text(strip=True) if doi_tag else ""

    # PMID
    pmid_tag = soup.find("strong", class_="current-id")
    pmid = pmid_tag.get_text(strip=True) if pmid_tag else ""

    # HTML断片を作成
    html_snippet = f"""
  <!-- ========================== -->
  <!-- {title} -->
  <!-- ========================== -->
  <meta name="citation_title" content="{title}">
  <meta name="citation_author" content="{authors_str}">
  <meta name="citation_journal_title" content="{journal_info}">
  <meta name="citation_pmid" content="{pmid}">
  <meta name="citation_doi" content="{doi}">

  <h2>{title}</h2>
  <p>著者: {authors_str}</p>
  <p>ジャーナル: {journal_info}</p>
  <p><a href="{url}" target="_blank">PubMedで論文を表示</a></p>
  <hr>
"""
    return html_snippet

def main():
    with open(input_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    # HTML全体のヘッダ
    html_header = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>PubMed Metadata Collection</title>
</head>
<body>
  <h1>PubMed Metadata Collection</h1>
"""
    html_footer = """
</body>
</html>"""

    contents = [html_header]

    for i, url in enumerate(urls, start=1):
        try:
            print(f"{i}. {url} のデータ取得中...")
            snippet = fetch_pubmed_metadata(url)
            contents.append(snippet)
            time.sleep(1)
        except Exception as e:
            print(f"{i}. {url} でエラー発生: {e}")
            contents.append(f"<p>{url} の取得に失敗しました。</p><hr>")

    contents.append(html_footer)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(contents)

    print("\n✅ すべてのメタデータをまとめて 'output.html' に保存しました。")

if __name__ == "__main__":
    main()