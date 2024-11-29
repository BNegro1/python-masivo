import httpx
from langchain_postgres import PGVector
from db_config import (
    db_user, db_password, db_database,
    db_host, db_port
)
from typing import List, Dict, Any
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
async def get_embedding(text: str) -> List[float]:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "http://tormenta.ing.puc.cl/api/embed",
            json={
                "model": "nomic-embed-text",
                "input": text
            }
        )
        response.raise_for_status()
        return response.json()["embeddings"][0]

connection = f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}"
collection_name = "movie_scripts"

vectorstore = PGVector(
    embeddings=get_embedding,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)

async def search_movies(query: str, k: int = 5):
    try:
        results = await vectorstore.asimilarity_search(
            query, 
            k=k,
            search_distance=0.3
        )
        
        
        total_tokens = 0
        filtered_results = []
        for doc in results:
            
            token_count = len(doc.page_content.split())
            if total_tokens + token_count <= 1500:  
                filtered_results.append(doc)
                total_tokens += token_count
            else:
                break
                
        return filtered_results
    except Exception as e:
        raise ValueError(f"Error en búsqueda vectorial: {str(e)}")
