from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    """searches for linkedin or twitter profile page

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res[0]["url"]