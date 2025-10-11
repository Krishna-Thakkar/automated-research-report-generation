import importlib.metadata
packages = [
    "langchain",
    "ipykernel",
    "langchain_groq",
    "langchain_google_genai",
    "langchain-community",
    "langchain-core",
    "langgraph",
    "tavily-python",
    "wikipedia",
    "structlog"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")