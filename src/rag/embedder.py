import bs4
from langchain_community.document_loaders import RecursiveUrlLoader

# The root URL of the documentation to start crawling from.
# Using the base URL is better for a comprehensive crawl.
url = "https://docs.manim.community/en/stable/"

# Instantiate the loader
# This will start at the root URL and recursively follow links
# as long as they are under the same domain.
loader = RecursiveUrlLoader(
    url=url,
    max_depth=8,  # How many clicks deep to go from the starting page. Adjust as needed.
    prevent_outside=True, # Prevents the crawler from leaving the documentation site.
    use_async=True, # Uses asynchronous fetching for speed.
    timeout=600, # Long timeout for potentially slow pages.
    # This is the crucial part. It tells the loader to only extract text
    # from the <main id="main-content"> HTML tag, which contains the
    # core documentation on each page.
    extractor=lambda html: bs4.BeautifulSoup(html, "lxml").find("main", {"id": "main-content"}).get_text(),
    # Exclude common, less useful pages from being scraped.
    exclude_dirs=[
        "https://docs.manim.community/en/stable/_sources",
        "https://docs.manim.community/en/stable/genindex.html",
        "https://docs.manim.community/en/stable/search.html",
    ]
)

# Load the documents
print("Starting to scrape the documentation... This may take a few minutes.")
docs = loader.load()
print("Scraping complete!")
print(f"Loaded {len(docs)} documents.")
print("\n--- Sample content from the first document: ---")
print(docs[0].page_content[:800]) # Print the first 800 characters of the first page.